#!/usr/bin/env python3
"""Standalone calculations for a two-method false-alarm ecological-survey interchange law."""
from fractions import Fraction as Q
from math import exp, log, isclose
from random import Random

def labor(order, prior, methods):
    total=0.0
    for state, prob in ((0,1-prior),(1,prior)):
        survived=1.0
        for name in order:
            rate,cost,duration=methods[name][state]
            u=exp(-rate*duration)
            total+=prob*survived*cost*(1-u)/rate
            survived*=u
    return total

def delta(order_prefix, prior, methods, first='A', second='B'):
    total=0.0
    for state,prob in ((0,1-prior),(1,prior)):
        S=1.0
        for name in order_prefix:
            lam,c,t=methods[name][state]
            S*=exp(-lam*t)
        a,ca,ta=methods[first][state]
        b,cb,tb=methods[second][state]
        total+=prob*S*(1-exp(-a*ta))*(1-exp(-b*tb))*(ca/a-cb/b)
    return total

# Exact-rational example. Both sensing methods have larger alarm intensity
# when the target species is present than when absent. Durations are log 2.
# State 0: A rate 1, B rate 2; state 1: A rate 4, B rate 3.
def exact_prefix_cost(order, pi):
    rates={'A':(1,4),'B':(2,3),'C':(1,3)}
    out=Q(0)
    for state,prob in ((0,1-pi),(1,pi)):
        survival=Q(1)
        for name in order:
            rate=rates[name][state]
            u=Q(1,2**rate)
            out+=prob*survival*(1-u)/rate
            survival*=u
    return out

D0=(1-Q(1,2))*(1-Q(1,4))*(Q(1)-Q(1,2))
D1=(1-Q(1,16))*(1-Q(1,8))*(Q(1,4)-Q(1,3))
assert D0==Q(3,16) and D1==-Q(35,512)
critical=D0/(D0-D1)
assert critical==Q(96,131)
assert exact_prefix_cost(['A','B'],Q(1,2))-exact_prefix_cost(['B','A'],Q(1,2))==Q(61,1024)>0
assert exact_prefix_cost(['A','B'],Q(9,10))-exact_prefix_cost(['B','A'],Q(9,10))==-Q(219,5120)<0
# Fixed informative prefix with conditional nonalarm posterior 9/13.
pi=Q(9,10)
posterior=(pi*Q(1,8))/(pi*Q(1,8)+(1-pi)*Q(1,2))
assert posterior==Q(9,13)<critical<pi
assert exact_prefix_cost(['C','A','B'],pi)-exact_prefix_cost(['C','B','A'],pi)>0
# The difference becomes positive after C, changing preferred A/B order.

rng=Random(20261026)
checks=0
for k in range(2500):
    prior=rng.uniform(.01,.99)
    npre=k%4
    keys=['A','B']+['P'+str(j) for j in range(npre)]
    methods={}
    for name in keys:
        duration=rng.uniform(.04,4)
        cost=rng.uniform(.05,3)
        l0=rng.uniform(.05,5)
        l1=rng.uniform(l0+.01,l0+5) # both types of alarm informative
        methods[name]={0:(l0,cost,duration),1:(l1,cost,duration)}
    prefix=keys[2:]
    direct=labor(prefix+['A','B'],prior,methods)-labor(prefix+['B','A'],prior,methods)
    predicted=delta(prefix,prior,methods)
    assert isclose(direct,predicted,abs_tol=2e-12,rel_tol=1e-9),(k,direct,predicted)
    checks+=1

# Every later block has an order-independent probability of being reached,
# and state-dependent alarm and missed-detection charges are order-invariant.
for k in range(200):
    pi=rng.uniform(.01,.99)
    a=rng.uniform(.1,5);b=rng.uniform(.1,5)
    t1=rng.uniform(.1,2);t2=rng.uniform(.1,2)
    # probability of no alarm in either modality is invariant under permutation
    s12=exp(-a*t1)*exp(-b*t2)
    s21=exp(-b*t2)*exp(-a*t1)
    assert isclose(s12,s21,rel_tol=1e-14)
    checks+=1

print('PASS',checks,'randomized direct-vs-interchange and reachability checks, plus exact-rational prevalence reversal and posterior flip')
