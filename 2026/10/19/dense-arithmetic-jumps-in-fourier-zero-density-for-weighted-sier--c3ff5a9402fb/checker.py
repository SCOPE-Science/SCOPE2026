#!/usr/bin/env python3
"""Reproducible checks of weighted triangular self-similar Fourier-zero geometry.

All lattice memberships and finite set counts use exact fractions. Floating
point evaluations are supplementary and are not used for infinite claims.
"""
from fractions import Fraction as F
from math import cos, pi, sin
import cmath


def signed_period(u, v, cap=200):
    # The additive order of (u,v) in (Q/Z)^2 is odd iff a finite signed period exists.
    for h in range(1, cap+1):
        for sign in (+1, -1):
            if ((2**h-sign)*u).denominator == 1 and ((2**h-sign)*v).denominator == 1:
                return h,sign
    return None


def lattice_coset(k, u, v, R):
    ans=set()
    step=2**k
    bound=R//step+3
    for n in range(-bound,bound+1):
        x=step*(u+n)
        for m in range(-bound,bound+1):
            y=step*(v+m)
            if x*x+y*y<=R*R:
                ans.add((x,y))
    return ans


def weights(u,v):
    u,v=float(u),float(v)
    # 0 < u < 1/2 < v < u+1/2
    A=sin(2*pi*(v-u))
    B=sin(2*pi*(1-v))
    C=sin(2*pi*u)
    assert min(A,B,C)>0
    s=A+B+C
    return A/s,B/s,C/s


def mask(p,z):
    a,b,c=p
    x,y=z
    return a+b*cmath.exp(-2j*pi*x)+c*cmath.exp(-2j*pi*y)


def check(u,v,h,R=140):
    p=weights(u,v)
    assert abs(sum(p)-1)<1e-14 and max(p)<.5
    assert abs(mask(p,(float(u),float(v))))<1e-14
    h_test=signed_period(u,v)
    assert h_test and h_test[0]==h
    finite=set()
    for k in range(1,h+1):
        for sgn in (+1,-1):
            L=lattice_coset(k,sgn*u,sgn*v,R)
            assert L.isdisjoint(finite),('unexpected first period collision',k)
            finite|=L
    whole=set()
    for k in range(1,11):
        for sgn in (+1,-1):
            whole |= lattice_coset(k,sgn*u,sgn*v,R)
    assert whole==finite, 'finite level union differed from h-level union'
    target=float(F(2,3)*(1-F(1,4**h)))
    observed=len(whole)/(pi*R**2)
    assert abs(observed-target)<.015, (h,target,observed)
    # At the frequency 2^K * (u,v), count zero mask factors exactly.
    K=24
    zeros=0
    for k in range(1,K+1):
        w1,w2=2**(K-k)*u,2**(K-k)*v
        if (w1-u).denominator==1 and (w2-v).denominator==1 or \
           (w1+u).denominator==1 and (w2+v).denominator==1:
            zeros+=1
    assert zeros>=K//h-1, zeros
    print('resonance',u,v,'h=',h,'weights=',tuple(round(x,9) for x in p),
          'density=',round(target,9),'finite_ratio=',round(observed,9),
          'points=',len(whole),'order_at_scaled_node=',zeros)


for u,v,h in [(F(1,3),F(2,3),1), (F(1,5),F(3,5),2), (F(1,7),F(4,7),3)]:
    check(u,v,h)

# Boundary and supercritical masks: one torus root or no roots, by geometry.
for p in [(.5,.3,.2),(.3,.5,.2),(.3,.2,.5)]:
    vals=[abs(mask(p,(u/2,v/2))) for u in (0,1) for v in (0,1)]
    assert min(vals)<1e-13 and sum(z<1e-13 for z in vals)==1
assert abs(mask((.6,.2,.2),(.5,.5)))>.1

# One irrational coordinate gives a nonresonant root pair; check mask equality.
u=2**.5/8
v=.625
assert abs(mask(weights(u,v),(u,v)))<1e-14
print('nonresonant example: u=sqrt(2)/8, v=5/8, mask residual',abs(mask(weights(u,v),(u,v))))
print('all checks passed')
