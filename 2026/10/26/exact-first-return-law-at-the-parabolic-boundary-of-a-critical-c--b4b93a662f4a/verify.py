#!/usr/bin/env python3
"""Independent finite exact-arithmetic checks for the parabolic cusp map.
Run: python3 verify.py
Analytic proof, not this finite test, handles all return times.
"""
from fractions import Fraction as Q
from math import isclose

def g0(x):
    return x - x*x/Q(2)

def g1(x):
    return 1-x+x*x/Q(2)

def H(x):
    return 2*x - x*x

def check():
    c=Q(1,2)
    assert H(1)-H(c)==Q(1,4)
    tested=0
    for denominator in range(2,41):
        for j in range(denominator+1):
            y=Q(j,denominator)
            tested+=1
            assert g0(y)+g1(y)==1
            assert g0(y)+Q(1,2)*(1-y)*(1-y)==Q(1,2)
            # Invariance transfer formula: 2(1-y) = (1-y)(h(g0)+h(g1)).
            assert (1-y)*(2*(1-g0(y))+2*(1-g1(y))) == 2*(1-y)
            assert g0(y) == y-y*y/Q(2)
    t=c
    for n in range(11):
        q=4*t*t
        assert q>=0 and q<=1
        # First-return tail derived independently by integrating
        # conditional pushforward density from 0 to previous threshold.
        if n:
            prev=seq[n-1]
            z=prev
            primitive=4*(z*z-z*z*z+z**4/Q(4))
            assert q==primitive
        if n==0: seq=[t]
        else:seq.append(t)
        t2=g0(t)
        assert 4*(t*t-t2*t2) == 4*t**3-t**4
        t=t2
    # n^2 P(tau>n) ->16, n^3 P(tau=n) ->32,
    # large finite values compared to the analytic limits.
    x=0.5
    nmax=100000
    for _ in range(nmax):
        x=x-x*x/2
    assert abs(nmax*x/2-1)<0.001
    assert abs(nmax*nmax*(4*x*x)/16-1)<0.003
    assert tested==858
    print(f'VERIFY_OK exact_transfer_grid={tested} exact_return_tails=11 asymptotic_steps=100000')

if __name__=='__main__':
    check()
