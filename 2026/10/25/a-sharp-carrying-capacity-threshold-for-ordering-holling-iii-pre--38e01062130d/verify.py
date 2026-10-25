#!/usr/bin/env python3
"""Reproducible checks for a Holling-III two-intensity ordering theorem.

Run with Python 3.10+; no third-party packages are required.
The exhaustive assertions are exact algebraic finite checks; integrations are
illustrative numerical tests, not proofs of the parameter-uniform theorem.
"""
from fractions import Fraction as Q
from random import Random

def threshold_polynomial(B, y):
    return -1 + B*y*y*(1-2*y)

def prey_velocity(x, intensity, growth, capacity, saturation):
    return growth*x*(1-x/capacity)-intensity*x*x/(1+saturation*x*x)

def commutator_coefficient(x, low, high, growth, capacity, saturation):
    T=threshold_polynomial(saturation*capacity*capacity, x/capacity)
    return (high-low)*growth*x*x*T/(1+saturation*x*x)**2

def rk4(x, intensity, duration, growth, capacity, saturation, steps=512):
    h=duration/steps
    for _ in range(steps):
        v=lambda v: prey_velocity(v,intensity,growth,capacity,saturation)
        k1=v(x); k2=v(x+h*k1/2); k3=v(x+h*k2/2); k4=v(x+h*k3)
        x+=h*(k1+2*k2+2*k3+k4)/6
        assert x>0
    return x

def schedule(x, jobs, growth, capacity, saturation, steps=512):
    for intensity,duration in jobs:
        x=rk4(x,intensity,duration,growth,capacity,saturation,steps)
    return x

def run():
    # An exact above-threshold realization: two turning populations.
    B=Q(54)
    assert threshold_polynomial(B,Q(1,6))==0
    assert threshold_polynomial(B,Q(1,3))==1
    assert threshold_polynomial(B,Q(3,4))<0
    assert threshold_polynomial(Q(27),Q(1,3))==0
    assert threshold_polynomial(Q(27),Q(1,4))<0
    assert threshold_polynomial(Q(26),Q(1,3))<0
    # Exact local counterexample: both treatments initially shrink prey.
    x=Q(1,3); lo=Q(20); hi=Q(30)
    assert prey_velocity(x,lo,Q(1),Q(1),Q(54)) == Q(-2,21)
    assert prey_velocity(x,hi,Q(1),Q(1),Q(54)) == Q(-16,63)
    assert commutator_coefficient(x,lo,hi,Q(1),Q(1),Q(54))==Q(10,441)
    assert commutator_coefficient(Q(1,12),lo,hi,Q(1),Q(1),Q(54))<0
    assert commutator_coefficient(Q(3,4),lo,hi,Q(1),Q(1),Q(54))<0
    # Numerical replay of three local-order regimes, including step refinement.
    for density,sgn in [(1/12,-1),(1/3,+1),(3/4,-1)]:
        first=schedule(density,[(20,0.01),(30,0.01)],1,1,54)
        other=schedule(density,[(30,0.01),(20,0.01)],1,1,54)
        first2=schedule(density,[(20,0.01),(30,0.01)],1,1,54,1024)
        other2=schedule(density,[(30,0.01),(20,0.01)],1,1,54,1024)
        assert sgn*(first-other)>0
        assert abs((first-other)-(first2-other2))<1e-11
    rng=Random(450053)
    count=0
    # Two blocks: the low-then-high ordering is universally best below threshold.
    for _ in range(600):
        r=10**rng.uniform(-1,0.7)
        K=10**rng.uniform(-0.4,0.4)
        B=rng.uniform(0.05,27.0)
        b=B/K**2
        a=rng.uniform(0.0,8.0)
        A=a+rng.uniform(0.1,8.0)
        d1=rng.uniform(0.003,0.13)
        d2=rng.uniform(0.003,0.13)
        x=K*10**rng.uniform(-1,0.55)
        ascending=schedule(x,[(a,d1),(A,d2)],r,K,b)
        descending=schedule(x,[(A,d2),(a,d1)],r,K,b)
        assert ascending<=descending+1e-11, (r,K,B,a,A,d1,d2,x,ascending,descending)
        count+=1
    # Three jobs: exact result concerns arbitrary finite lists, not only pairs.
    from itertools import permutations
    for _ in range(60):
        r=1.;K=1.;b=rng.uniform(0.2,27.0)
        jobs=[(v,rng.uniform(.015,.13)) for v in (1.,3.,7.)]
        x=rng.uniform(.05,1.2)
        results=[(schedule(x,list(p),r,K,b),p) for p in permutations(jobs)]
        asc=schedule(x,jobs,r,K,b)
        desc=schedule(x,list(reversed(jobs)),r,K,b)
        assert asc<=min(q[0] for q in results)+2e-10
        assert desc>=max(q[0] for q in results)-2e-10
    print('PASS: 11 exact rational root/derivative/velocity checks;')
    print('PASS: 3 refined local reversal integrations;')
    print(f'PASS: {count} randomized two-block scenarios;')
    print('PASS: 60 independent three-treatment six-permutation comparisons.')
if __name__=='__main__': run()
