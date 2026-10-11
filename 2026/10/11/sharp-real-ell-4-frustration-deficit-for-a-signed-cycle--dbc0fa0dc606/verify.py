#!/usr/bin/env python3
"""Reproduce finite diagnostics for the real signed-cycle l4 theorem.
This program checks necessary polynomial identities over a rational grid;
the analytical compactness and recovery argument is in RESULT.md.
"""
from fractions import Fraction as F
from math import cos, pi, sqrt, copysign

def pair(a,b):
    a,b=F(a),F(b)
    m=(a+b)/2
    d=(b-a)/2
    E=6*m*m*d*d+d**4
    dg=b*abs(b)-a*abs(a)
    assert (a**4+b**4)/2 == m**4+E
    assert 4*E >= dg**2
    assert 4*E <= 7*dg**2
    if a*b>=0:
        assert 8*E >= 3*dg**2

for a in range(-9,10):
    for b in range(-9,10):
        pair(a,b)
print('exact integer-grid pair checks: 361 cases passed')

def trial(n):
    g=[sqrt(2)*cos(pi*j/n) for j in range(n)]
    x=[copysign(sqrt(abs(v)),v) if v else 0. for v in g]
    xx=sum(v**4 for v in x)
    by=[x[j]+(x[j+1] if j+1<n else -x[0]) for j in range(n)]
    val=(sum(v**4 for v in by)/xx)**.25
    assert abs(xx/n-1.)<5e-13
    return n*n*(2-val)

for n in (16,64,256,1024,2048):
    print('n = %4d, n^2 trial gap = %.12f' % (n,trial(n)))
print('proved target coefficient = %.12f' % (3*pi*pi/16))
