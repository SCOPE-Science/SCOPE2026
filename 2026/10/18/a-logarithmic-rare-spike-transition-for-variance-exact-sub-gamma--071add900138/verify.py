#!/usr/bin/env python3
"""Finite diagnostics for rare-spike sub-gamma asymptotics; not an infinite proof."""
import math
from fractions import Fraction

def beta_moment(n):
    return Fraction(2, (n+1)*(n+2))

def coeff(n):
    return Fraction(2, math.factorial(n+2))

def G(z):
    if abs(z)<0.05:
        return sum(float(coeff(n))*z**n for n in range(18))
    return 2*math.expm1(z)/z**2-2/z

def scaled_profile(B, h, s):
    q=math.exp(-h)
    V=1-q+q*B*B
    z=h-2*math.log(B/h)+s
    t=z/B
    w=q*B*B/V
    L=(1-w)*G(t)+w*G(z)
    return L,(h/B)*(1-1/L)/t

for n in range(45):
    assert coeff(n)==beta_moment(n)/math.factorial(n)
    if n<40:
        assert coeff(n+1)/coeff(n)==Fraction(1,n+3)
assert sum(coeff(i)*Fraction(1,3)**i for i in range(60))<Fraction(9,8)
for B in (1600.,10000.,40000.):
    h=B**0.5
    for s in (-1.,0.,1.):
        L,P=scaled_profile(B,h,s)
        assert math.isfinite(L) and math.isfinite(P)
        assert L>=1 and 0<P<1.1
    # A boundary-layer comparison in the deep regime, not an asymptotic proof.
    if B>=10000.:
        L,P=scaled_profile(B,h,0.)
        assert abs(L-3)<0.7 and abs(P-2/3)<0.25
for B in (1000.,5000.):
    h=math.sqrt(B)
    q=math.exp(-h)
    E2=1-q+q*B**2
    E3=1-q+q*B**3
    E4=1-q+q*B**4
    deriv=E4/(12*E2)-(E3/(3*E2))**2
    assert deriv<0
print('VERIFY_OK: exact beta coefficients, finite transition profile, local curvature')
