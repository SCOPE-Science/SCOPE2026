#!/usr/bin/env python3
"""Exact arithmetic checks for a two-compartment MPRK density-ratio bound.
Uses only Python's standard library. Proof of inequalities is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

ZERO = {}
def const(c): return {(0,0,0):F(c)} if c else {}
def monomial(axis):
    k=[0,0,0];k[axis]=1
    return {tuple(k):F(1)}
def add(*polys):
    out={}
    for poly in polys:
        for k,v in poly.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def mul(p,q):
    out={}
    for a,x in p.items():
        for b,y in q.items():
            k=tuple(a[i]+b[i] for i in range(3));out[k]=out.get(k,F(0))+x*y
    return {k:v for k,v in out.items() if v}
def neg(p):return {k:-v for k,v in p.items()}
def sub(a,b):return add(a,neg(b))
def power(p,n):
    out=const(1)
    for _ in range(n):out=mul(out,p)
    return out
def diff(p,axis=2):
    out={}
    for k,v in p.items():
        if k[axis]:
            l=list(k);l[axis]-=1;out[tuple(l)]=v*k[axis]
    return out
B,E,t=monomial(0),monomial(1),monomial(2)
Fpart=add(E,mul(B,t))
Num=add(mul(const(2),Fpart),mul(t,mul(add(const(1),t),sub(const(2),t))))
Den=add(mul(add(power(t,2),mul(const(2),t),const(2)),Fpart),mul(t,mul(add(const(1),t),add(t,const(2)))))
J=sub(mul(diff(Num),Den),mul(Num,diff(Den)))
Expected=neg(add(
 mul(add(mul(const(3),B),E,const(4)),power(t,4)),
 mul(add(mul(const(4),power(B,2)),mul(const(12),B),mul(const(4),E),const(8)),power(t,3)),
 mul(add(mul(const(4),power(B,2)),mul(const(8),mul(B,E)),mul(const(8),B),mul(const(12),E),const(4)),power(t,2)),
 mul(add(mul(const(8),mul(B,E)),mul(const(4),power(E,2)),mul(const(8),E)),t),
 mul(const(4),power(E,2))))
assert J==Expected, 'Derivative identity fails'
print('Exact polynomial derivative identity: PASS',len(J),'terms')

def run(p,u,s):
    q=1-p;delta=u-p
    y1=p+delta/(1+s);y2=1-y1
    w1=1+u/y1;w2=1+(1-u)/y2
    z1=(u+(s/2)*p*w2)/(1+(s/2)*(q*w1+p*w2))
    z2=1-z1
    Bv=1+(q-p)*delta/(p*q)
    Ev=u*(1-u)/(p*q)
    part=Ev+Bv*s
    numer=2*part+s*(1+s)*(2-s)
    denom=(s*s+2*s+2)*part+s*(1+s)*(s+2)
    r=numer/denom
    assert z1-p==delta*r
    assert Ev>0 and Bv>=Ev and denom>0
    return z1,z2,r

checks=0
for p in [F(j,40) for j in range(2,39)]:
    for u in [F(k,41) for k in range(1,41)]:
        for s in (F(1,9),F(2),F(13),F(100)):
            z1,z2,r=run(p,u,s)
            assert z1>0 and z2>0 and z1+z2==1
            if F(2,5)<=p<=F(3,5):
                assert max(z1/p,z2/(1-p))<=max(u/p,(1-u)/(1-p))
            checks+=1
p,u,s=F(3,4),F(9,10),F(10)
z1,z2,r=run(p,u,s)
assert z1==F(15134,21985) and z2==F(6851,21985)
assert z2/(1-p)>max(u/p,(1-u)/(1-p))
print('Independent exact-rational recurrence and invariant-range tests: PASS',checks)
print('Exact interior witness: PASS',z1,z2)
