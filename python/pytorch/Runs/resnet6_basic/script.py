# This example supposes that the events file contains summaries with a
# summary value tag 'loss'.  These could have been added by calling
# `add_summary()`, passing the output of a scalar summary op created with
# with: `tf.scalar_summary(['loss'], loss_tensor)`.
#import tensorflow as tf
#for e in tf.train.summary_iterator("events.out.tfevents.1568899349.64c2838c3715"):
#    print("********************************************")
    #if e.summary.value[0]=="Test/AngleError":
    #    print(e)
#    print(e.summary.value[0])
    #for v in e.summary.value:
    #    print("***")
    #    print(v)
    #    pass
        #if v.tag == 'loss' or v.tag == 'accuracy':
        #    print(v.simple_value)
    
# In [1]: from tensorflow.python.summary import event_accumulator  # deprecated
from tensorboard.backend.event_processing import event_accumulator
ea = event_accumulator.EventAccumulator('events.out.tfevents.x.ip-x-x-x-x',
     size_guidance={ # see below regarding this argument
         event_accumulator.COMPRESSED_HISTOGRAMS: 500,
         event_accumulator.IMAGES: 4,
         event_accumulator.AUDIO: 4,
         event_accumulator.SCALARS: 0,
         event_accumulator.HISTOGRAMS: 1,
          })