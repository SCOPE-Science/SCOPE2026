#!/usr/bin/env python3
"""Exact-rational checks for a bounded nonlinear flux-correction interval.

This verifies finite algebraic test sets only; RESULT.md contains the proof
for all admissible parameters.
"""
from fractions import Fraction as F
from math import sqrt


def interval(s, t, p):
    assert 0 < s <= 1 and 0 <= t <= s and 0 < p <= 1
    return (max(F(0), (s-p)/(1-s/6)),
            min(F(1), (1+t-p)/(1+s/6)))


def algebraic(s, t, p):
    return (p >= F(7,6)*s - 1 and
            p >= (1+t+s)/2 - F(3,s)*(1+t-s))


def quadratic(s, t, p):
    r=t/s
    return (F(7,6)*s <= 1+p and
            (1+r)*s*s + (7-6*r-2*p)*s <= 6)


def test():
    checks=0
    for ns in range(1,41):
        s=F(ns,40)
        for nt in range(ns+1):
            t=F(nt,40)
            for np in range(1,41):
                p=F(np,40)
                lo,hi=interval(s,t,p)
                actual=(lo<=hi)
                assert actual==algebraic(s,t,p), (s,t,p,lo,hi)
                assert actual==quadratic(s,t,p), (s,t,p,lo,hi)
                checks+=1
    assert checks==34400
    s=F(6,7); r=F(1,6)
    assert (1+r)*s*s+(7-6*r)*s-6 == 0
    assert F(7,6)*s-1==0
    # Algebraic witnesses: above the high-contrast and uniform-step ceilings.
    assert interval(F(83,100),F(83,1000),F(1,10000))[0] > interval(F(83,100),F(83,1000),F(1,10000))[1]
    assert interval(F(43,50),F(43,250),F(1,10000))[0] > interval(F(43,50),F(43,250),F(1,10000))[1]
    def root(r):
        b=7-6*r
        return (sqrt(b*b+24*(1+r))-b)/(2*(1+r))
    for r in (0,1/20,1/10,1/6,1/2,1):
        print('speed ratio',r,'universal interval ceiling',min(6/7,root(r)))
    print(checks,'exact-rational parameter comparisons passed')

if __name__=='__main__':
    test()
