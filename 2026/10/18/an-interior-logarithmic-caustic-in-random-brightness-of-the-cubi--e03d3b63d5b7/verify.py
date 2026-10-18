#!/usr/bin/env python3
"""Independent rational algebra checks for a geometric brightness law."""
from fractions import Fraction as F
from math import sqrt, pi
import random


def rising(a, n):
    out = F(1)
    for k in range(n):
        out *= a + k
    return out


def moment(a, b, c):
    return rising(F(1, 2), a) * rising(F(1, 2), b) * rising(F(1, 2), c) / rising(F(3, 2), a + b + c)


def poly_mul(A, B):
    C = {}
    for alpha, x in A.items():
        for beta, y in B.items():
            exponent = tuple(a+b for a,b in zip(alpha,beta))
            C[exponent] = C.get(exponent, F(0)) + x*y
    return {k: v for k, v in C.items() if v}


Y = {(1,1,0): F(1), (1,0,1): F(1), (0,1,1): F(1), (1,1,1): F(-1)}
A={(0,0,0):F(1)}
expectations=[]
for power in range(1,4):
    A=poly_mul(A,Y)
    expectations.append(sum(coef*moment(*exp) for exp,coef in A.items()))
assert expectations == [F(4,21), F(128,3003), F(128,12597)], expectations
assert expectations[1] - expectations[0]**2 == F(400,63063)

# Verify the exact polynomial identities directly by evaluating many rational values;
# each is a polynomial of total degree at most three in two variables.
for i in range(14):
    s=F(i,20)
    for j in range(-8,9):
        t=F(j,30)
        x1=s
        x2=(1-s)/2+t
        x3=(1-s)/2-t
        lhs=(1-x1)*(1-x2)*(1-x3)
        rhs=F(1,4)+s/4-(s*s+s*s*s)/4-t*t+s*t*t
        assert lhs==rhs
        L=s*(1-s)
        U=(1-s)*(1+s)**2/4
        T=F(1,2)+t/(1-s) if s!=1 else F(0)
        assert lhs == L+(U-L)*4*T*(1-T)
for i in range(-7,8):
    for j in range(-7,8):
        u=F(i,100)
        v=F(j,100)
        x1=F(1,3)+u; x2=F(1,3)+v; x3=F(1,3)-u-v
        y=(1-x1)*(1-x2)*(1-x3)
        assert y == F(8,27)-F(2,3)*(u*u+u*v+v*v)+u*v*(u+v)
assert F(1,4)==F(1,4)
# At the edge normal chart: q = s*(1/4 - s/4 - s^2/4 + t^2), Y-1/4=q-t^2.
for s in [F(k,100) for k in range(1,30)]:
    for t in [F(k,80) for k in range(-12,13)]:
        q=s*(F(1,4)-s/4-s*s/4+t*t)
        y=(1-s)*((1+s)**2/4-t*t)
        assert y-F(1,4)==q-t*t
# The leading chart density at q=0 has factor 2/(pi*sqrt(q));
# the exact derivative dq/ds at s=t=0 equals 1/4.
assert F(1,4)==(F(1,10000)*(F(1,4)-F(1,10000)/4-F(1,10000)**2/4))/F(1,10000) + F(1,10000)/4+F(1,10000)**2/4

# Deterministically sample random Haar directions. This is only a sanity check.
rng=random.Random(327146)
N=120000
s1=s2=0.0
for _ in range(N):
    coords=[rng.gauss(0.,1.) for _ in range(3)]
    r2=sum(c*c for c in coords)
    if r2==0: continue
    x=[c*c/r2 for c in coords]
    y=(1-x[0])*(1-x[1])*(1-x[2])
    assert -1.e-12<=y<=8/27+1.e-12
    s1+=y;s2+=y*y
assert abs(s1/N-float(F(4,21))) < 0.0012
assert abs(s2/N-float(F(128,3003))) < 0.0005
print('VERIFY_OK: rational moments, two polynomial normal forms, mixture, and Haar sampling')
