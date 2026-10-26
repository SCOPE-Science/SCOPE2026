#!/usr/bin/env python3
"""Reproducible arithmetic and quadrature for a sharp Fejer contraction constant."""
from fractions import Fraction as F
from math import acos, cos, pi, sin, sqrt

def polynomial(c, u):
    return 2*((2*c-1)*u+1-c)*((2*c+1)*u+1+c)

def primitive(c, u):
    return F(2,3)*(4*c*c-1)*u**3+2*c*u*u+2*(1-c*c)*u

def pieces(c):
    r=-(1+c)/(1+2*c)
    if c <= F(2,3):
        return primitive(c,1)-primitive(c,-1)-2*(primitive(c,r)-primitive(c,-1))
    s=(1-c)/(1-2*c)
    lo=min(r,s); hi=max(r,s)
    return primitive(c,1)-primitive(c,-1)-2*(primitive(c,hi)-primitive(c,lo))

def I_first(c):
    return -4*(4*c**4-5*c**3-12*c*c-8*c-2)/(3*(2*c+1)**2)

def I_mid(c):
    return -4*(16*c**6-72*c**4+39*c*c-6)/(3*(2*c-1)**2*(2*c+1)**2)

def I_late(c):
    return 4*(48*c**6-24*c**4+9*c*c-2)/(3*(2*c-1)**2*(2*c+1)**2)

def bernstein_coeffs(power_coefs):
    from math import comb
    n=len(power_coefs)-1
    return [sum((power_coefs[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)),F(0)) for k in range(n+1)]

def bernstein_on_interval(coefs,a,b):
    from math import comb
    n=len(coefs)-1
    expansion=[]
    for j in range(n+1):
        expansion.append(sum((coefs[k]*F(comb(k,j))*a**(k-j)*(b-a)**j for k in range(j,n+1)), F(0)))
    return bernstein_coeffs(expansion)

cases=[
    ([F(-6),F(39),F(-72),F(16)],F(4,9),F(1,2),-1),
    ([F(-4),F(-7),F(100),F(-176),F(64)],F(4,9),F(1,2),-1),
    ([F(-2),F(9),F(-24),F(48)],F(1,2),F(1),1),
    ([F(-4),F(-9),F(124),F(-272),F(192)],F(1,2),F(1),1),
]
for coeff,a,b,sign in cases:
    weights=bernstein_on_interval(coeff,a,b)
    assert all(w*sign>0 for w in weights),(coeff,weights)

for c in [F(0),F(1,40),F(1,3),F(2,3),F(67,100),F(7,10),F(71,100),F(3,4),F(4,5),F(9,10),F(1)]:
    for u in [F(-1),F(-3,4),F(0),F(1,3),F(1)]:
        assert polynomial(c,u)==2*(4*c*c-1)*u*u+4*c*u+2*(1-c*c)
    computed=pieces(c)
    expected=(I_first(c) if c<=F(2,3) else I_mid(c) if c*c<=F(1,2) else I_late(c))
    assert computed==expected,(c,computed,expected)

def h(c):return 8*c**5-20*c**3-14*c*c+c+2
lo,hi=0.3,0.4
assert h(lo)>0>h(hi)
for _ in range(100):
    mid=(lo+hi)/2
    if h(mid)>0:lo=mid
    else:hi=mid
c=(lo+hi)/2
I=float(I_first(c)); delta=sqrt(1-c*c)*I/pi
assert abs(c-0.33810718533465588595)<1e-12
assert abs(delta-0.88388237782919685)<1e-12
assert abs(2*acos(c)-2.451782841069228)<1e-12
assert delta>8/(3*pi)

def k4(x):return 1+1.5*cos(x)+cos(2*x)+0.5*cos(3*x)
def quadrature(theta,steps=100000):
    step=2*pi/steps
    return 0.5*sum(abs(k4((j+0.5)*step)-k4((j+0.5)*step-theta)) for j in range(steps))/steps
for angle in [0.0,1.0,2.0,2*acos(c),pi]:
    # Midpoint integration supplies numerical corroboration, not an infinite proof.
    value=quadrature(angle)
    assert value<=delta+1e-7,(angle,value,delta)
assert abs(quadrature(2*acos(c))-delta)<2e-8
print('CHECK_OK c=%.15f angle=%.15f delta=%.15f' %(c,2*acos(c),delta))
