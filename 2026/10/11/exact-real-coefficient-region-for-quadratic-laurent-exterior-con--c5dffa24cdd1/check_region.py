#!/usr/bin/env python3
"""Supplementary finite checks of the exact coefficient inequalities; not an infinite proof."""
from math import sqrt, cos, pi

def B(a):
    return (1+a)/4 if a <= 0 else (1-a)*sqrt(1+a)/4

def H(a):
    return (1-3*a) if a <= 0 else (1+a)**1.5

def g(a,x):
    return 4*x**3-3*(1+a)*x

parameters = [-1.,-0.95,-0.5,-0.1,0.,0.1,0.5,0.9,1.]
for a in parameters:
    t = B(a)
    assert abs(1-a*a-8*t*t-2*t*H(a)) < 2e-14
    candidate = min(3*a-1,-(1+a)**1.5)
    assert abs(candidate+H(a)) < 2e-14
    for j in range(8001):
        x = cos(pi*j/8000)
        assert g(a,x)>=candidate-2e-13
    if t>1e-8:
        above = t+0.001
        assert 1-a*a-8*above**2-2*above*H(a)<0
for i in range(81):
    a1=-1+2*i/80
    a2=-1+2*((31*i+17)%81)/80
    a=(a1+a2)/2
    assert (B(a1)+B(a2))/2 <= B(a)+1e-13
print('coefficient identities, cubic minima, sharpness and sampled concavity checks passed')
