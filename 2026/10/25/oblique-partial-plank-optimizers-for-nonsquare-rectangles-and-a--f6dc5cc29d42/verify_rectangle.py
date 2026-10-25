#!/usr/bin/env python3
"""Deterministic checks for the rectangular fixed-width central-slab theorem.
This is a computational cross-check, not a substitute for the analytic proof.
Run: python3 verify_rectangle.py
"""
from fractions import Fraction
from math import atan, cos, sin, sqrt, pi, isclose
from random import Random

def stationary(t, alpha):
    assert 1 <= t and 0 < alpha < 1
    def F(q):
        return q-t-alpha*(q*q-1)/sqrt(1+q*q)
    lo = t
    hi = max(2*t, 2.0)
    while F(hi) <= 0:
        hi *= 2
    for _ in range(95):
        mid = (lo+hi)/2
        if F(mid) > 0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2

def strip_area(a,b,w,theta):
    u,v=abs(cos(theta)),abs(sin(theta))
    if u < 1e-14: return 4*a*w
    if v < 1e-14: return 4*b*w
    U,V=a*u,b*v
    support=U+V
    if w>=support: return 4*a*b
    if w<=abs(U-V):
        return 4*w*min(a/v,b/u)
    return 4*a*b-(support-w)**2/(u*v)

def formula(a,b,w):
    q=stationary(a/b,w/b)
    area=4*a*b-(a+b*q-w*sqrt(1+q*q))**2/q
    return q,area

# An exact quadratic-surds certificate: (a,b,q,w)=(2,1,3,sqrt(10)/8).
w_times_sqrt10=Fraction(10,8)
assert Fraction(8) - (Fraction(5)-w_times_sqrt10)**2 / 3 == Fraction(53,16)
assert Fraction(3-2) == Fraction(8,8)  # stationarity after cancellation sqrt(10)

# Directly test the formula against independently evaluated two-tail/plateau slices.
rng=Random(190728)
worst=0.0
for j in range(500):
    b=0.3+4*rng.random()
    a=b*(1.00001+6*rng.random())
    w=b*(0.0001+0.9998*rng.random())
    q,area=formula(a,b,w)
    assert q>a/b
    theta=atan(q)
    assert abs(area-strip_area(a,b,w,theta)) < 2e-9*max(1,a*b)
    assert abs((q-a/b)*sqrt(1+q*q)-(w/b)*(q*q-1)) < 1e-8*max(1,q*q)
    # Independent 1600-angle grid, covering all orientations modulo half-turn.
    samples=[strip_area(a,b,w,k*pi/3200) for k in range(3200)]
    diff=area-max(samples)
    assert diff > -2e-8*max(1,a*b),(j,diff,a,b,w,q)
    worst=max(worst,abs(diff)/max(1,a*b))
    assert area > max(2*a*(2*w), 2*b*(2*w))
print('PASS: 500 analytic-vs-grid tests, max relative grid gap:',worst)

# At the critical width of the square, the nonsquare optimum obeys a cube-root law.
for delta in (1e-4,1e-6,1e-8):
    q=stationary(1+delta,1/sqrt(2))
    ratio=(q-1)/delta**(1/3)
    assert 1.8 < ratio < 2.2,(delta,ratio)
print('PASS: critical cube-root limit checks')
print('PASS: exact 53/16 example')
