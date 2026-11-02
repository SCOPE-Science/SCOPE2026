#!/usr/bin/env python3
"""Exact-rational checks for the scalar recession pulse theorem.
No external dependencies.  Time-above-threshold is represented by an
exponential for f(q)=q and as a rational for f(q)=q^2.
"""
from fractions import Fraction as F
from itertools import permutations
import random

rng=random.Random(20261027)
C=0

def phi2(q,h):
    return F(0) if q<=h else 1/h-1/q

def flood2(pulses, gaps, h):
    q=F(0); total=F(0)
    for j,p in enumerate(pulses):
        q+=p
        if j<len(gaps):
            after=q/(1+q*gaps[j])
            total+=phi2(q,h)-phi2(after,h)
            q=after
    return total+phi2(q,h)

def floodexp_factor(pulses, factors, h):
    q=F(0); factor=F(1)
    for j,p in enumerate(pulses):
        q+=p
        if j<len(factors):
            after=q*factors[j]
            if q>h:
                factor*=q/max(h,after)
            q=after
    if q>h:
        factor*=q/h
    return factor

for n in range(2,8):
    for _ in range(1500):
        h=F(rng.randint(1,9),rng.randint(1,9))
        pulses=tuple(h+F(rng.randint(1,12),rng.randint(1,8)) for _ in range(n))
        gaps=tuple(F(rng.randint(1,30),rng.randint(1,8)) for _ in range(n-1))
        factors=tuple(F(rng.randint(1,9),rng.randint(10,20)) for _ in range(n-1))
        b2=phi2(max(pulses),h)+sum((phi2(h+p,h) for p in pulses),F(0))-phi2(h+max(pulses),h)
        # the unique optimal schedule places largest first and fires at every threshold return
        seq=(max(pulses),)+tuple(p for j,p in enumerate(pulses) if j!=pulses.index(max(pulses)))
        op_gaps=tuple(phi2(seq[j],h) if j==0 else phi2(h+seq[j],h) for j in range(n-1))
        assert flood2(seq,op_gaps,h)==b2
        assert flood2(pulses,gaps,h)<=b2
        be=max(pulses)/h
        excused=False
        for p in pulses:
            if p==max(pulses) and not excused:
                excused=True
                continue
            be*=(h+p)/h
        assert floodexp_factor(pulses,factors,h)<=be
        op_factors=[]
        for j in range(n-1):
            current=seq[j] if j==0 else h+seq[j]
            op_factors.append(h/current)
        assert floodexp_factor(seq,tuple(op_factors),h)==be
        C+=4

# all arrangements of a three-pulse exact example
h=F(1)
ps=(F(2),F(3),F(5))
for seq in permutations(ps):
    ex=seq[0]/h
    for p in seq[1:]: ex*=1+p/h
    assert ex<=60
    if seq[0]==5: assert ex==60
    C+=1
print('PASS exact-rational assertions:',C)
print('For h=1, f(q)=q, pulses (2,3,5), optimum duration log(60), all-coincident log(10).')
