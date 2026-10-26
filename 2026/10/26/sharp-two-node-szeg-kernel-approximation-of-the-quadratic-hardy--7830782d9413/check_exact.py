#!/usr/bin/env python3
"""Standalone checks of exact identities for a two-Szego-kernel Hardy approximation."""
from fractions import Fraction as F
import random
import cmath

# Exact polynomial check using coefficient dictionaries over Q.
def add(*poly):
    out={}
    for p in poly:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def mul(a,b):
    out={}
    for i,v in a.items():
        for j,w in b.items():out[i+j]=out.get(i+j,F(0))+v*w
    return {k:v for k,v in out.items() if v}
def const(v):return {0:F(v)} if v else {}
def lin(a,b):return {0:F(a),1:F(b)}
x=lin(0,1);one=const(1);xm=lin(1,-1); A=lin(1,0) # overwritten below
# E_min(x) = x^2+(1-x)^2*(x+3/4).
h=add(mul(x,x),mul(mul(xm,xm),lin(F(3,4),1)))
assert add(h,const(-F(9,16)))==mul(mul(lin(-1,2),lin(-1,2)),lin(F(3,16),F(1,4)))

# For Gaussian rationals each complex coefficient is represented as (real,imag).
def cadd(a,b):return (a[0]+b[0],a[1]+b[1])
def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def cab2(a):return a[0]*a[0]+a[1]*a[1]
a=(F(1,2),F(1,2));b=(F(1,2),F(-1,2))
s=cadd(a,b);p=cmul(a,b)
t=cadd((-s[0],-s[1]),cmul(p,conj(s)))
c2=cadd((F(1)-cab2(p),F(0)),cmul(conj(s),t))
assert p==(F(1,2),F(0))
assert t==(F(-1,2),F(0))
assert c2==(F(1,4),F(0))
assert cab2(p)+cab2(t)+cab2(c2)==F(9,16)

# Independent direct Gram-matrix computation with exact Gaussian rationals.
def reciprocal(x):
    d=cab2(x);return (x[0]/d,-x[1]/d)
def cdiv(x,y):return cmul(x,reciprocal(y))
def neg(x):return (-x[0],-x[1])
K11=reciprocal((F(1)-cab2(a),F(0)))
K22=reciprocal((F(1)-cab2(b),F(0)))
K12=reciprocal(cadd((F(1),F(0)),neg(cmul(a,conj(b)))))
K21=conj(K12)
det=cadd(cmul(K11,K22),neg(cmul(K12,K21)))
v1=cmul(a,a);v2=cmul(b,b)
w1=cdiv(cadd(cmul(K22,v1),neg(cmul(K12,v2))),det)
w2=cdiv(cadd(neg(cmul(K21,v1)),cmul(K11,v2)),det)
energy=cadd(cmul(conj(v1),w1),cmul(conj(v2),w2))
assert energy==(F(7,16),F(0)),energy

# Finite stress test (not a proof), avoiding nearly coincident poles.
rng=random.Random(51234)
checks=0
for i in range(600):
    a0=(rng.random()**0.5)*0.97*cmath.exp(2j*cmath.pi*rng.random())
    b0=(rng.random()**0.5)*0.97*cmath.exp(2j*cmath.pi*rng.random())
    pp=a0*b0;ss=a0+b0;tt=-ss+pp*ss.conjugate()
    cc=1-abs(pp)**2+ss.conjugate()*tt
    err=abs(pp)**2+abs(tt)**2+abs(cc)**2
    assert err>=F(9,16)-1e-12,(a0,b0,err)
    assert err<=1+1e-11,(a0,b0,err)
    checks+=2
print('PASS: 1 polynomial identity, 4 exact Blaschke checks, 1 exact Gram check,',checks,'finite numerical inequalities')
