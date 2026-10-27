"""Monte Carlo cross-check of exponential uncovered-gap universality.

Reproduce with: python reproduce_gap_law.py
Requires numpy. Exact geometry is maintained through sorted union intervals.
These tests support, but do not replace, the continuum proof.
"""
from bisect import bisect_left
import math
import numpy as np


def simulate(seed, length=160., padding=15., horizon=2., intensity=1., p_right=.3,
             lengths=(.17,1.7), probs=(.56,.44), inhomogeneous=False):
    rng=np.random.default_rng(seed)
    lo,hi=-padding,length+padding
    cumulative=intensity*horizon if not inhomogeneous else intensity*horizon*horizon
    number=rng.poisson((hi-lo)*cumulative)
    heads=rng.uniform(lo,hi,number)
    lengths_sampled=rng.choice(lengths,size=number,p=probs)
    orientations=rng.random(number)<p_right
    if inhomogeneous:
        event_times=horizon*np.sqrt(rng.random(number))
    else:
        event_times=horizon*rng.random(number)
    attempts=sorted(zip(event_times,heads,lengths_sampled,orientations))
    intervals=[]
    for _,head,extent,right in attempts:
        k=bisect_left(intervals,(head,-math.inf))
        if (k and intervals[k-1][1]>=head) or (k<len(intervals) and
           intervals[k][0]<=head<=intervals[k][1]):
            continue
        left,right_end=(head,head+extent) if right else (head-extent,head)
        k=bisect_left(intervals,(left,-math.inf))
        if k and intervals[k-1][1]>=left:k-=1
        j=k
        while j<len(intervals) and intervals[j][0]<=right_end:
            left=min(left,intervals[j][0])
            right_end=max(right_end,intervals[j][1]);j+=1
        intervals[k:j]=[(left,right_end)]
    gaps=[]
    edge=0.
    for left,right in intervals:
        if left>=length:break
        if right<=0:continue
        if left>edge:gaps.append(left-edge)
        edge=max(edge,right)
    if edge<length:gaps.append(length-edge)
    return gaps


def check(name, t, rate, pright, lengths, probs, inhomogeneous=False):
    sampled=[]
    for seed in range(360):
        sampled.extend(simulate(seed+100000*int(inhomogeneous),horizon=t,
                                intensity=rate,p_right=pright,
                                lengths=lengths,probs=probs,inhomogeneous=inhomogeneous))
    gaps=np.array(sampled)
    cumulative=rate*t*t if inhomogeneous else rate*t
    observed_mean=float(gaps.mean())
    predicted_mean=1/cumulative
    assert abs(observed_mean-predicted_mean)<.028
    print(name,'count',len(gaps),'mean',observed_mean,'expected',predicted_mean)
    for threshold in (.1,.3,.6,1.):
        observed=float(np.maximum(gaps-threshold,0).sum()/gaps.sum())
        expected=math.exp(-cumulative*threshold)
        print('  x',threshold,'observed',round(observed,6),'expected',round(expected,6))
        assert abs(observed-expected)<.025


if __name__=='__main__':
    check('mixed lengths, biased directions',2.,1.,.3,(.17,1.7),(.56,.44))
    check('time-variable rate and reversed bias',1.5,1.,.82,(.15,2.),(.25,.75),True)
    print('All reproducibility checks passed.')
