#!/usr/bin/env python3
"""Exact and sampled checks for complete-network signed-expression dynamics."""
from fractions import Fraction as Q
from itertools import product
from random import Random

def sign(x):
    return 1 if x >= 0 else -1

def update(x, amp):
    n=len(x)
    mean=sum(x)/n
    return [mean + sum(amp[j]*sign(x[j]) for j in range(n) if j != i)/n for i in range(n)]

def two_cycle_after_transient(x, s):
    amp=[s]*len(x)
    y=update(x, amp)
    z=update(y, amp)
    w=update(z, amp)
    return (y == w and min(y) < 0 < max(y) and min(z) < 0 < max(z)
            and all(v != 0 for v in y+z))

rational_cases=0
for n in range(2,9):
    s=Q(1,10)
    for sig in product((-1,1),repeat=n):
        if min(sig)==max(sig):
            continue
        imbalance=sum(sig)
        for k in range(-99,100):
            shift=Q(k,1000)
            x=[shift + s*Q(v,4) for v in sig]
            if tuple(sign(v) for v in x) != sig:
                continue
            mean=sum(x)/n
            expected=(imbalance == 0 and abs(mean)<s/n) if n%2==0 else (
                abs(imbalance)==1 and mean*imbalance<0 and abs(mean)<s*(n-1)/(n*n))
            # Cases where zero appears in first or second update are excluded by claim.
            y=update(x,[s]*n)
            z=update(y,[s]*n)
            if any(v==0 for v in y+z):
                continue
            assert two_cycle_after_transient(x,s)==expected,(n,sig,shift,mean,imbalance)
            rational_cases += 1
print('PASS exact deterministic parity-window cases:',rational_cases)

rng=Random(20261024)
paths=0
for n in (2,3,4,7,15):
    s=0.1
    worst=0
    max_gap=0.0
    max_mean_error=0.0
    for run in range(100):
        state=[rng.uniform(-s/2,s/2) for _ in range(n)]
        previous_expression=[v+s*rng.random()*sign(v) for v in state]
        hit=None
        for t in range(1,1200):
            amp=[s*rng.random() for _ in range(n)]
            expression=[v+a*sign(v) for v,a in zip(state,amp)]
            gap=max(abs(state[i]-previous_expression[j]) for i in range(n)
                    for j in range(n) if i!=j)
            assert gap <= 4*s+1e-12
            max_gap=max(max_gap,gap)
            next_state=update(state,amp)
            z=sum(a*sign(v) for a,v in zip(amp,state))
            mean_error=abs(sum(next_state)/n-sum(state)/n-(n-1)*z/(n*n))
            assert mean_error<1e-12
            max_mean_error=max(max_mean_error,mean_error)
            state=next_state
            previous_expression=expression
            if min(state)>0 or max(state)<0:
                hit=t
                break
        assert hit is not None
        paths += 1
        worst=max(worst,hit)
    print('PASS n=%d: 100 uniform sample paths; max hit=%d, max confidence gap=%.12g, mean-error=%.3g'
          %(n,worst,max_gap,max_mean_error))
print('PASS total sample paths:',paths)
