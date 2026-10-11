#!/usr/bin/env python3
"""Exact-rational algebraic witnesses and numerical asymptotic checks."""
from fractions import Fraction as Q
from math import sqrt, isclose


def add(p, q):
    n=max(len(p),len(q)); return [(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(n)]
def mul(p, q):
    out=[Q(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j]+=x*y
    return out
def deriv(p): return [i*p[i] for i in range(1,len(p))]

def derivative_certificate(c,s,a2):
    assert c*c+s*s==1
    N=[c*c+a2,2*c*s,s*s]
    one=[Q(1),Q(0),Q(1)]
    # (1+z^2)^3 F'(z)/a^2 = (1+z^2)N'(z)-4zN(z).
    num=add(mul(deriv(N),one),mul([Q(0),-4],N))
    expect=[2*s*c,2*(1-3*c*c-2*a2),-6*s*c,-2*s*s]
    assert num==expect, (num,expect)

def g(z,c,s,a2):
    return s*c+(1-3*c*c-2*a2)*z-3*s*c*z*z-s*s*z*z*z

def root(c,a2):
    s=sqrt(1-c*c)
    lo,hi=0.0,1.0
    while g(hi,c,s,a2)>0: hi*=2.0
    for _ in range(120):
        m=(lo+hi)/2
        if g(m,c,s,a2)>0: lo=m
        else: hi=m
    return (lo+hi)/2

for c,s in [(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(15,17),Q(8,17)),(Q(0),Q(1))]:
    for a2 in [Q(1,9),Q(1,2),Q(18,25),Q(4,1)]:
        derivative_certificate(c,s,a2)

c,s,a2,z=Q(3,5),Q(4,5),Q(18,25),Q(1,4)
assert g(z,c,s,a2)==0
exact_dw2=a2*((c+s*z)**2+a2)/(1+z*z)**2
assert exact_dw2==Q(156672,180625)
nilpotent_a2=Q(3,8)
assert nilpotent_a2*(Q(1,4)+nilpotent_a2)/(Q(5,4)**2)==Q(3,20)
for a2 in [0.3,0.5,1.1]:
    for c in [1e-4,1e-6]:
        z=root(c,a2)
        if a2<0.5: assert abs(z-sqrt(1-2*a2))<0.005
        elif a2==0.5: assert abs(z/c**(1/3)-1)<0.005
        else: assert abs(z/c*(2*a2-1)-1)<0.005
for c in [1e-3,1e-6]:
    z=root(c,0.5);s=sqrt(1-c*c)
    dw=sqrt(0.5*((c+s*z)**2+0.5)/(1+z*z)**2)
    assert abs((dw-0.5)/c**(4/3)-0.75)<0.03
print('RANK_ONE_DW_CUBIC_AND_CUSP_CHECKS_OK')
