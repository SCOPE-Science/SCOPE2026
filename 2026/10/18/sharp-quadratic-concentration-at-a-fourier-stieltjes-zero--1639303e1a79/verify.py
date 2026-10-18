#!/usr/bin/env python3
"""Reproducibility checks for the sharp Fourier-zero concentration inequality.
Numerical checks supplement the analytic proof; they do not prove positivity on an unbounded interval.
"""
import math

PI=math.pi
B=PI/2
C=4/PI-1
ALPHA=2-4/PI
BETA=4-PI

def certificate(x):
    x=abs(x)
    return x*x+PI*math.cos(x)-B*B-C*(x-B)**2

def derivative(x):
    return 2*ALPHA*x+BETA-PI*math.sin(x)

def second_derivative(x):
    return 2*ALPHA-PI*math.cos(x)

assert abs(certificate(0.)) < 1e-13
assert abs(certificate(B)) < 1e-13
assert abs(derivative(B)) < 1e-13
assert derivative(0.) > 0
assert second_derivative(0.) < 0
assert second_derivative(B) > 0
assert 2*PI-4 > 0
for k in range(1,100001):
    x=40*k/100000
    assert certificate(x) >= -3e-13, (k,x,certificate(x))
# Symmetric three-point zeros and asymptotically optimal ratios.
prev=1.0
for p in (0.04,0.01,0.002,0.0002,0.00001):
    theta=math.acos(-p/(1-p))
    zero=p+(1-p)*math.cos(theta)
    assert abs(zero)<1e-13
    variance=(1-p)*theta**2
    radial=p*B**2+(1-p)*(theta-B)**2
    deficit=variance-B**2
    assert deficit + 1e-12 >= C*radial
    ratio=deficit/radial
    assert ratio > C-1e-10
    assert ratio < prev
    prev=ratio
assert abs(prev-C) < 0.0001
print('PASS: contact/derivative identities, 100000 sampled nonnegativities, five exact Fourier-zero families, asymptotic sharpness.')
print('Sharp coefficient:', C, 'last ratio:', prev)
