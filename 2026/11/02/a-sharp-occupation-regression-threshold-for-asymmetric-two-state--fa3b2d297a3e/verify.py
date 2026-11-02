#!/usr/bin/env python3
"""Finite numerical reproducibility checks for the conditional two-state bridge law."""
import math
from fractions import Fraction

def mean(k, delta, substeps=3200):
    if k == 0:
        return 1.0
    assert substeps % 2 == 0
    def integrand(u):
        if u == 1.0 and k == 1:
            return math.exp(math.log(2)-delta)
        if not (0 < u < 1):
            return 0.0
        # Center the log-density to prevent underflow at moderate k.
        return math.exp(k*math.log(2*u)+(k-1)*math.log(2*(1-u))-delta*u)
    h = 1/substeps
    sums=[0.0,0.0]
    for j in range(substeps+1):
        u=j*h
        w=1 if j in (0,substeps) else (4 if j%2 else 2)
        p=w*integrand(u)
        sums[0]+=p
        sums[1]+=p*u
    return sums[1]/sums[0]

tests=0
for k in range(1,21):
    exact=Fraction(k+1,2*k+1)
    assert abs(mean(k,0)-float(exact))<2e-8,(k,exact)
    tests+=1
for delta in (-5,-1,0,1,1.9,2):
    vals=[mean(k,delta) for k in range(20)]
    for a,b in zip(vals,vals[1:]):
        assert a>b,(delta,a,b)
        tests+=1
for delta in (2.5,4,8,20):
    vals=[mean(k,delta) for k in range(1,51)]
    assert vals[0]<1
    assert any(b>a+1e-9 for a,b in zip(vals,vals[1:])),delta
    tests+=1
# The sharp asymptotic sign, not its convergence rate, is tested here.
for delta in (1,2.1,8):
    k=90
    val=mean(k,delta)
    assert (val-0.5)*(2-delta)>0,(delta,val)
    tests+=1
print('PASS: %d deterministic numerical/exact checks' % tests)
