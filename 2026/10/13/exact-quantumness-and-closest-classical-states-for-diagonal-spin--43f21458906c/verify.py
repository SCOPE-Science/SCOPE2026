#!/usr/bin/env python3
from fractions import Fraction
import math
import cmath


def g(y, x, b):
    return 3.0*y**3 + (6.0*b-1.0)*y - 2.0*x


def root(x, b):
    lo, hi = -1.0, 1.0
    assert g(lo,x,b) < 0.0 < g(hi,x,b)
    for _ in range(100):
        mid=(lo+hi)/2.0
        if g(mid,x,b) > 0.0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2.0


def h(y):
    return (1.0-y*y)/2.0


def f2(x,b,y):
    return 0.5*(x-y)**2 + 1.5*(b-h(y))**2


def check_exact_classicality(a,b,c):
    x=a-c
    lhs=b*b <= 4*a*c
    rhs=x*x+2*b <= 1
    assert lhs == rhs
    assert b*b-4*a*c == x*x+2*b-1

# Exact rational identity checks.
for a,b,c in [
    (Fraction(1,3),Fraction(1,3),Fraction(1,3)),
    (Fraction(0),Fraction(1),Fraction(0)),
    (Fraction(11,20),Fraction(2,5),Fraction(1,20)),
    (Fraction(1,10),Fraction(7,10),Fraction(1,5)),
]:
    check_exact_classicality(a,b,c)

# Representative nonclassical states, including the previously known central ray
# and off-axis states. Each tuple is (a,b,c).
cases=[
    (0.0,1.0,0.0),
    (0.60,0.40,0.0),
    (0.55,0.40,0.05),
    (0.10,0.70,0.20),
    (0.02,0.55,0.43),
]

for a,b,c in cases:
    assert abs(a+b+c-1.0) < 1e-14
    x=a-c
    assert x*x+2*b > 1.0-1e-14
    y=root(x,b)
    assert -1.0 < y < 1.0
    assert abs(g(y,x,b)) < 1e-12

    # Cubic has one real root: monotonicity for b>=1/6, positive Cardano
    # discriminant in the remaining nonclassical regime.
    if b < 1.0/6.0:
        Delta=x*x/9.0-(1.0-6.0*b)**3/729.0
        assert Delta > 0.0

    # Stationarity identity and equivalent distance formulas.
    d=b-h(y)
    assert abs((x-y)-3.0*y*d) < 1e-11
    q1=f2(x,b,y)
    q2=1.5*(1.0+3.0*y*y)*d*d
    assert abs(q1-q2) < 1e-11

    # Equal three-phase coherent mixture reconstructs sigma_y.
    theta=math.acos(y)
    cp=math.cos(theta/2.0)
    sp=math.sin(theta/2.0)
    M=[[0j for _ in range(3)] for __ in range(3)]
    for k in range(3):
        phi=2.0*math.pi*k/3.0
        v=[cp*cp, math.sqrt(2.0)*cp*sp*cmath.exp(-1j*phi), sp*sp*cmath.exp(-2j*phi)]
        for i in range(3):
            for j in range(3):
                M[i][j]+=v[i]*v[j].conjugate()/3.0
    target=[(1+y)**2/4.0,(1-y*y)/2.0,(1-y)**2/4.0]
    for i in range(3):
        for j in range(3):
            expected=target[i] if i==j else 0.0
            assert abs(M[i][j]-expected) < 2e-14
    assert min(target) > 0.0

    # Dense scan of the complete diagonal classical region. For each horizontal
    # coordinate yy the best allowed vertical coordinate is the clamp of b to
    # [0,h(yy)]. The analytic minimizer must beat the sampled values.
    analytic=f2(x,b,y)
    best=float('inf')
    N=20000
    for k in range(N+1):
        yy=-1.0+2.0*k/N
        hh=h(yy)
        bp=min(max(b,0.0),hh)
        val=0.5*(x-yy)**2+1.5*(b-bp)**2
        if val<best:
            best=val
    assert analytic <= best + 2e-8

print('VERIFY_OK')
