"""Reproducible finite checks for the sharp first-jet Berezin envelope.

Finite arithmetic checks supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
import cmath
import math

checks=0
for ti in range(0,10):
    t=F(ti,10)
    for ci in range(0,11):
        c=F(ci,10)
        for ri in range(0,100):
            r=F(ri,100)
            u=r*(r+c)/(1+c*r)
            A=(t+u)/(1+t*u)
            Q=(1-r*r)/(1-r*A)
            phi=(t+r*(c+r)/(1+c*r))/(1+t*r*(c+r)/(1+c*r))
            B=(1-r*r)/(1-r*phi)
            assert B == Q
            assert Q<=1+t*r
            assert Q>=0
            checks+=3
        limit=2*(1+t)*(1+c)/((1+t)*(1+c)+2*(1-t))
        assert limit<=1+t
        assert (limit==1+t)==(c==1)
        checks+=2

# Independently check the angular-modulus bound on a grid of interior points.
for t in [0.12,0.49,0.87]:
    for c in [0.,0.3,0.8,1.]:
        for r in [0.,0.15,0.4,0.78,0.93]:
            u=r*(r+c)/(1+c*r)
            expected=(1-r*r)*(1+t*u)/(1+t*u-r*t-r*u)
            for k in range(19):
                z=r*cmath.exp(2j*math.pi*k/19)
                h=(c+z)/(1+c*z) if c<1 else 1
                psi=z*h
                phi=(t+psi)/(1+t*psi)
                val=(1-r*r)/(1-z.conjugate()*phi)
                assert abs(val)<=expected+1e-11
                checks+=1
print(f'PASS: {checks} exact-rational and complex sample assertions')
