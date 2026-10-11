#!/usr/bin/env python3
"""Exact rational certificate for a Fourier-truncation fourth moment.

Run with Python 3 and no nonstandard modules.  A finite alternating-series
interval at t=1 certifies the strict fourth-moment inequality.  Polynomial
arithmetic independently checks the first nonzero small-parameter terms.
"""
from fractions import Fraction as F
from math import factorial


def bessel_partial(n, last):
    return sum((F((-1) ** k, 2 ** (2*k+n) * factorial(k) * factorial(k+n))
                for k in range(last+1)), F(0))


bounds = {n: (bessel_partial(n, 9), bessel_partial(n, 10))
          for n in range(3)}
for lo, hi in bounds.values():
    assert 0 < lo < hi  # Alternating decreasing terms, so exact enclosing bounds.
(a, A), (b, B), (c, C) = (bounds[n] for n in range(3))
assert b*b - A*C > 0
# Every summand is nonnegative, and the lower bounds preserve its sign.
certified_lower = (a*a+2*b*b+c*c)**2 + 4*b*b*c*c + 2*(b*b-A*C)**2
assert certified_lower > 1
print('Certified J0,J1,J2 intervals:',
      [(n, str(lo), str(hi)) for n,(lo,hi) in bounds.items()])
print('Exact rational lower bound for the fourth moment:', certified_lower)
print('Lower-bound margin:', float(certified_lower-1))

# Coefficient arithmetic truncated to degree 10 (all quantities are even).
D = 10

def mul(p, q):
    r = [F(0)]*(D+1)
    for i in range(D+1):
        for j in range(D+1-i):
            r[i+j] += p[i]*q[j]
    return r


def add(*ps):
    return [sum((p[i] for p in ps), F(0)) for i in range(D+1)]


def scale(a, p):
    return [a*x for x in p]


def series(n):
    out = [F(0)]*(D+1)
    for k in range((D-n)//2+1):
        out[n+2*k] = F((-1)**k, 2**(n+2*k)*factorial(k)*factorial(k+n))
    return out

A0, B1, C2 = [series(n) for n in range(3)]
W = add(mul(A0,A0),scale(2,mul(B1,B1)),mul(C2,C2))
Z = add(mul(B1,B1),scale(-1,mul(A0,C2)))
M = add(mul(W,W),scale(4,mul(mul(B1,B1),mul(C2,C2))),scale(2,mul(Z,Z)))
assert M[0]==1 and M[1]==M[2]==M[3]==M[4]==M[5]==0
assert M[6]==F(5,576) and M[7]==0 and M[8]==F(-11,2304)
assert M[9]==0 and M[10]==F(473,460800)
print('Exact expansion: 1 + (5/576)t^6 - (11/2304)t^8 + (473/460800)t^10 + O(t^12)')
print('VERIFY_OK')
