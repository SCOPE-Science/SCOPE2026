#!/usr/bin/env python3
"""Exact rational consistency checks for sharp quadratic L4 point evaluation."""
from fractions import Fraction as F
from math import comb

def conv(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def Q(x):
    return 70*x**4-80*x**3+36*x*x-8*x+1

def derivative(x):return 8*(35*x**3-30*x*x+9*x-1)

for x in [F(-2),F(-1,3),F(0),F(1,10),F(1,3),F(3,8),F(1),F(2)]:
    a=[x,F(1)-2*x,x]
    p=conv(a,a)
    assert sum(v*v for v in p)==Q(x)

lo=F(373438841903251,10**15)
hi=F(373438841903252,10**15)
assert derivative(lo)<0<derivative(hi)
# Q''=840(x-2/7)^2+24/7 ensures strict global convexity.
x=F(3,8)
lower=Q(x)-derivative(x)**2/(2*F(24,7))
assert lower==F(44825,196608)
assert lower>F(1,5)
assert Q(lo)>lower and Q(hi)>lower
# Unique minimizing rho inside (lo,hi), so C_2,4 is strictly between 1/Q(lo) and 1/lower.
print('PASS: exact convolution, derivative root isolation, strong convexity, strictly positive contraction gap')
print('root bracket:',lo,hi,'Q lower bound:',lower)
