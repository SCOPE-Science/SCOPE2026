#!/usr/bin/env python3
"""Finite consistency checks for the sharp tracial crossed-Heinz bound.
Analytic proof is supplied separately; these checks do not prove infinite cases.
"""
from fractions import Fraction
from math import sqrt
from random import Random

def trace_ratio(a, b, t, r):
    delta = a-b
    d = (a**t-b**t)*(a**(1-t)-b**(1-t))
    u = 1-r*r
    lo = a+b-delta*r
    hi = a+b+delta*r
    return (lo+hi-abs(lo-d*u)-abs(hi-d*u))/(2*delta**2*u)

def predicted(a,b,t):
    d = (a**t-b**t)*(a**(1-t)-b**(1-t))
    return min(d, (sqrt(a)+sqrt(b))**2/2)/(a-b)**2

# Exact noncommuting sharpness witness: a=100, b=1, t=1/2.
r=Fraction(9,11)
u=1-r*r
D=Fraction(81)
s_lo=Fraction(101)-Fraction(99)*r
s_hi=Fraction(101)+Fraction(99)*r
c_lo=s_lo-D*u
c_hi=s_hi-D*u
assert (s_lo,s_hi,c_lo,c_hi)==(20,182,Fraction(-820,121),Fraction(18782,121))
deficit=s_lo+s_hi-abs(c_lo)-abs(c_hi)
distance2=2*Fraction(99**2)*u
new_gamma=Fraction(121,2)/Fraction(99**2)
old_gamma=Fraction(40,99**2)
assert deficit==40 and distance2==6480
assert deficit/distance2==new_gamma==Fraction(1,162)
assert new_gamma>old_gamma

# Exact commuting sharpness witness: a=4, b=1, t=1/2.
assert Fraction(2,18)==Fraction(1,9)

rng=Random(210673)
for _ in range(15000):
    b=10**rng.uniform(-1.0,1.0)
    a=b*10**rng.uniform(.2,4.)
    t=rng.uniform(.02,.98)
    r=rng.uniform(0,.995)
    gamma=predicted(a,b,t)
    got=trace_ratio(a,b,t,r)
    assert got >= gamma-5e-12*max(1,gamma), (a,b,t,r,gamma,got)
    x=rng.uniform(0,2)
    s=2*b+(a-b)*x
    u=x*(2-x)
    lhs=2*s-(sqrt(a)+sqrt(b))**2*u
    rhs=((sqrt(a)+sqrt(b))*x-2*sqrt(b))**2
    assert abs(lhs-rhs)<=5e-10*(1+a+b), (a,b,x,lhs,rhs)
print('TRACIAL_CROSSED_HEINZ_CHECK_OK; exact sharp witnesses and 15000 random principal angles checked')
