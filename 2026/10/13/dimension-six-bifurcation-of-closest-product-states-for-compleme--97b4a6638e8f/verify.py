#!/usr/bin/env python3
"""Finite corroboration for a geometric overlap bifurcation in complementary Dicke superpositions.

Python 3 standard library. Analytic uniform-in-n arguments are in RESULT.md.
"""
import cmath
import math
from fractions import Fraction
from itertools import product


def overlap_squared(n, x, phase=0.0):
    c = math.sqrt(1-x)
    s = math.sqrt(x)
    a = math.sqrt(n / 2.0)
    return abs(a * (s*c**(n-1)*cmath.exp(-1j*phase)
                    + s**(n-1)*c*cmath.exp(-1j*(n-1)*phase)))**2


def stat(n, t):
    a = (n-2)/2
    return (n-2)*math.tanh(a*t)-n*math.tanh(t)


def solve(n):
    if n<=5:
        return .5
    lo=1e-9
    hi=8.0
    assert stat(n,lo)>0 and stat(n,hi)<0
    for _ in range(90):
        mid=(lo+hi)/2
        if stat(n,mid)>0:
            lo=mid
        else:
            hi=mid
    t=(lo+hi)/2
    return .5*(1+math.tanh(t))


def direct_tensor_overlap(n, x, phase):
    u0=math.sqrt(1-x)
    u1=math.sqrt(x)*cmath.exp(-1j*phase)
    amp=0j
    for bits in product((0,1),repeat=n):
        if sum(bits) in (1,n-1):
            term=math.sqrt(1/(2*n))
            for b in bits:
                term *= u1 if b else u0
            amp+=term
    return abs(amp)**2


def check():
    for n in range(4,17):
        x=solve(n)
        p=overlap_squared(n,x)
        for j in range(201):
            xx=j/200
            q=overlap_squared(n,xx)
            assert q <= p+1e-12, (n,xx,q,p)
        assert abs(p-overlap_squared(n,1-x))<1e-12
        if n<6:
            assert x==.5
            assert abs(p-n/(2**(n-1)))<1e-12
        else:
            assert .5 < x < 1
            assert p > overlap_squared(n,.5)+1e-14
            assert abs(stat(n,math.atanh(2*x-1)))<1e-9
    assert abs(overlap_squared(6,(1+1/math.sqrt(3))/2)-float(Fraction(2,9)))<1e-13
    for n in range(4,9):
        for x in (.12,.5,.71):
            for phi in (0.0,.19,1.12):
                assert abs(direct_tensor_overlap(n,x,phi)-overlap_squared(n,x,phi))<2e-14
    for n in (25,80,200):
        q=overlap_squared(n,solve(n))
        assert abs(q-1/(2*math.e))<(.04 if n==25 else .012 if n==80 else .006)
    print('VERIFY_OK direct_tensor_n=4..8 grid_n=4..16 special_n6=2/9 asymptotic_n=25,80,200')

if __name__=='__main__':
    check()
