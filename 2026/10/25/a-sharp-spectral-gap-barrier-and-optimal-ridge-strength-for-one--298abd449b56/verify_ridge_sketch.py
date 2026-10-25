#!/usr/bin/env python3
"""Reproduce exact-algebra and angular probability checks for a planar ridge sketch.

Only Python's standard library is required. Tests support, but do not replace,
the analytical proof in RESULT.md.
"""
from fractions import Fraction as F
from math import acos, asin, cos, isclose, pi, sin, sqrt


def polynomial(r, ell, t):
    return (ell**2 * ((r - 1)**2 * t**2 - (r**2 - 6*r + 1))
            + ell * (-(r - 1)**3*t - r**3 + 5*r**2 + 5*r - 1)
            + 4*r**2)


def invariant_difference(r, ell, t):
    # Directly from trace and determinant of (C+ell I)^(-1)(D+ell I).
    d = r*(1+t) + (1-t)
    numerator = 2*ell**2 + ell*(r+1+d) + 2*r
    return numerator**2 - ell*(ell+d)*(r+1+2*ell)**2


def thresholds(r):
    delta = sqrt(r*r-6*r+1)
    return ((r*r-4*r-1-(r-1)*delta)/4,
            (r*r-4*r-1+(r-1)*delta)/4)


def probability(r, ell):
    if r <= 3+2*sqrt(2):
        return 0.0
    lo, hi = thresholds(r)
    if ell <= lo:
        return 0.0
    d = sqrt(r*r-6*r+1)
    tm = (r-1)/(2*ell) - (2*ell+r+1)*d/(2*ell*(r-1))
    tp = (r-1)/(2*ell) + (2*ell+r+1)*d/(2*ell*(r-1))
    return (asin(min(1.0,tp))-asin(max(-1.0,tm)))/pi


def check():
    checks = 0
    # Rational identities, including the isotropy-induced factor of 2.
    for r in (F(3), F(6), F(9), F(16), F(25)):
        for ell in (F(1,10), F(1), F(3,2), F(4), F(17), F(100)):
            for t in (F(-1), F(-3,4), F(-1,3), F(0), F(1,3), F(3,4), F(1)):
                assert polynomial(r,ell,t) == invariant_difference(r,ell,t)
                checks += 1
    # Independent matrix calculation using rational coordinates for A=diag(3,1).
    r = F(9)
    for u in (F(0), F(1,4), F(1,3), F(2,3), F(1), F(2), F(3)):
        x=(1-u*u)/(1+u*u); y=2*u/(1+u*u)
        t=x*x-y*y
        for ell in (F(1,2),F(1),F(2),F(5),F(19),F(100)):
            # H = ell I + 2(A z)(A z)^T (no explicit sqrt(2)).
            h11=ell+2*r*x*x; h22=ell+2*y*y; h12=2*F(3)*x*y
            detH=h11*h22-h12*h12
            assert detH == ell*(ell+2*r*x*x+2*y*y)
            # trace(H^-1 G) = (h22*(r+ell)+h11*(1+ell))/detH.
            tr=(h22*(r+ell)+h11*(1+ell))/detH
            determinant=(r+ell)*(1+ell)/detH
            base_trace_ratio=(r+1+2*ell)**2/((r+ell)*(1+ell))
            sign = tr*tr/determinant-base_trace_ratio
            pred = polynomial(r,ell,t)
            assert (sign > 0) == (pred > 0)
            assert (sign == 0) == (pred == 0)
            checks += 1
    # Condition-number improvement probability versus direct angular integration.
    for r in (6.0,7.0,10.0,20.0):
        lo,hi=thresholds(r)
        for ell in (lo/2, (lo+hi)/2, hi, 2*hi, 100*hi):
            n=20000
            count=sum(polynomial(r,ell,cos(2*pi*(k+0.5)/n))<0
                      for k in range(n))
            observed=count/n
            exact=probability(r,ell)
            assert abs(observed-exact) < 2/n + 1e-11, (r,ell,observed,exact)
            checks += 1
        peak=probability(r,hi)
        assert peak>probability(r,hi*.9) and peak>probability(r,hi*1.1)
        checks += 1
    print('VERIFY_OK',checks)

if __name__=='__main__':
    check()
