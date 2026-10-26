#!/usr/bin/env python3
"""Exact rational cross-checks for a radial exponential spectral quadratic.

Finite tests corroborate identities; the general theorem is proved analytically.
No external modules are required.
"""
from fractions import Fraction as F


def q(d, a, b, u):
    return (1-a) + (d+1)*(a-3*b)*u + (d+1)*(d+3)*b*u*u


def thresholds(d):
    return -F(1,d*(d+1)), F(4*(d+3),9*(d+1))


def vertex(d, a, b):
    if b <= 0:
        raise ValueError('vertex in this proof is used only for b>0')
    return (3*b-a)/(2*(d+3)*b)


def q_from_derivatives(d, a, b, u):
    # After factoring the positive spectral weight (1+rho^2)^(-(d+1)/2),
    # the scale-parameter derivatives have factors:
    # -f'(1)/weight = (d+1)*u - 1
    #  f''(1)/weight = -3*(d+1)*u+(d+1)*(d+3)*u**2
    return 1 + a*((d+1)*u-1) + b*(-3*(d+1)*u+(d+1)*(d+3)*u*u)


for d in (1,2,3,4,8,30):
    lo,hi=thresholds(d)
    assert q(d,0,lo,F(1))==0
    assert q(d,0,hi,vertex(d,0,hi))==0
    assert vertex(d,0,hi)==F(3,2*(d+3))
    for a,b in ((F(0),F(0)),(F(1,4),F(1,6)),(F(-3,5),F(-1,40))):
        for u in (F(0),F(1,10),F(1,3),F(1)):
            assert q(d,a,b,u)==q_from_derivatives(d,a,b,u)
    assert q(d,0,lo-F(1,1000),F(1))<0
    assert q(d,0,hi+F(1,1000),F(3,2*(d+3)))<0
print('Exact rational coefficient and boundary checks passed.')
