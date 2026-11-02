#!/usr/bin/env python3
"""Exact rational Taylor/Fourier checks for the elliptic trace calculation.
Run: python3 ellipse_check.py (only Python standard library is required).
This checks finite algebraic identities, not the spectral perturbation theorem.
"""
from fractions import Fraction as F
from math import factorial

def add(a,b):
    d=dict(a)
    for k,v in b.items(): d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}

def mul(a,b,limit=3):
    d={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if i+k<=limit:
                key=(i+k,j+l)
                d[key]=d.get(key,F(0))+v*w
    return {k:v for k,v in d.items() if v}

def scale(a,c): return {k:c*v for k,v in a.items() if c*v}
def power(a,n):
    z={(0,0):F(1)}
    for _ in range(n): z=mul(z,a)
    return z

def binomial(q,n):
    r=F(1)
    for k in range(n):r*=F(q-k,k+1)
    return r

def series_one_plus(t,q):
    out={};p={(0,0):F(1)}
    for k in range(4):
        out=add(out,scale(p,binomial(q,k)))
        p=mul(p,t)
    return out

def trace_coeff(beta,s,i,j,order):
    """Fourier-zero coefficient of normalized geometric integrand.
    The overall factor 2*pi*r*(1-s)^beta*s^((|i|+|j|)/2) is omitted.
    """
    e={(1,2):F(1),(1,-2):F(1),(2,0):F(1)}
    radial=series_one_plus(scale(e,-s/(1-s)),beta)
    arc=series_one_plus({(1,2):F(-1),(1,-2):F(-1),(2,0):F(1)}, F(1,2))
    weight=mul(radial,arc)
    def basis(k):
        u={(0,1 if k>=0 else -1):F(1), (1,-1 if k>=0 else 1):F(1)}
        return power(u,abs(k))
    left=basis(i)
    right={(m,-f):v for (m,f),v in basis(j).items()}
    integrand=mul(mul(left,right),weight)
    return integrand.get((order,0),F(0))

def second_formula(beta):
    s=F(3)/(2*beta+3)
    x=s*s*(beta+2)*(beta+3)/6
    direct=trace_coeff(beta,s,1,1,2)
    coupling=trace_coeff(beta,s,1,3,1)
    assert coupling==1
    q=direct+x/(1-x)
    target=(beta-3)*(2*beta+3)/(4*beta*(5*beta+9))
    assert q==target,(beta,q,target)
    assert trace_coeff(beta,s,1,-1,1)==0
    assert trace_coeff(beta,s,1,-1,2)==0
    assert trace_coeff(beta,s,1,1,1)==0
    return q

checks=0
for beta in [F(1,3),F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(9,2),F(8)]:
    s=F(3)/(2*beta+3)
    assert F(1)/(beta+1) < s < F(2)/(beta+2)
    first=trace_coeff(beta,s,1,-1,1)
    assert first == 0
    q=second_formula(beta)
    print('beta=',beta, 's*=',s,'quadratic relative coefficient=',q)
    checks+=7

beta=F(3);s=F(1,3)
x=s*s*(beta+2)*(beta+3)/6
assert x==F(5,9)
assert trace_coeff(beta,s,1,3,1)==1
assert trace_coeff(beta,s,3,-1,2)==F(-5,8)
assert trace_coeff(beta,s,1,-1,3)==F(17,8)
assert trace_coeff(beta,s,1,1,3)==0
assert trace_coeff(beta,s,1,1,2)+x/(1-x)==0
cubic=trace_coeff(beta,s,1,-1,3)+2*x/(1-x)*trace_coeff(beta,s,1,3,1)*trace_coeff(beta,s,3,-1,2)
assert cubic==F(9,16),cubic
checks+=7
print('critical beta=3: x=5/9, third-order off-diagonal coefficient=',cubic)
print('PASS:',checks,'exact rational checks.')
