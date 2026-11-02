#!/usr/bin/env python3
"""Exact checks for the inflection divisor of X^4+Y^4+XZ^3.
Scientific verification only; no external research infrastructure.
Requires Python 3 and SymPy for the integer-polynomial Hessian check.
"""
from itertools import product
import sympy as sp

X,Y,Z=sp.symbols('X Y Z')
F=X**4+Y**4+X*Z**3
H=sp.factor(sp.det(sp.hessian(F,(X,Y,Z))))
assert sp.expand(H-108*Y**2*Z*(8*X**3-Z**3))==0
assert sp.expand(F.subs({X:sp.Rational(1,2),Z:1})-(Y**4+sp.Rational(9,16)))==0

units=[1,5,7,11,13,17,19,23]
assert len(units)==8

def delta(a):
    return 12 if a%12 in (5,7) else 0

def action(a,j,e):
    return (a*j)%3,(a*e+delta(a))%24

q0={action(a,0,3) for a in units}
q1={action(a,1,5) for a in units}
q2={action(a,2,7) for a in units}
assert q0=={(0,e) for e in (3,9,15,21)}
assert q1==q2=={(1,e) for e in (5,11,17,23)}|{(2,e) for e in (1,7,13,19)}
for a in units:
    h=2+(2 if a%3==1 else 0)
    infinity=4 if a%8==1 else 0
    q0fix=sum(action(a,0,e)==(0,e) for e in (3,9,15,21))
    q12fix=sum(action(a,j,e)==(j,e) for j,es in ((1,(5,11,17,23)),(2,(1,7,13,19))) for e in es)
    expect=2+2*(a%3==1)+4*(a%8==1)+4*(a in (1,5))+8*(a==1)
    assert h+infinity+q0fix+q12fix==expect,(a,q0fix,q12fix)

# Point census on prime fields. The affine chart has Z=1, and
# the chart at infinity has Z=0,X=1; there are no points [0:1:0].
def prime_count(p):
    count=0
    for x in range(p):
      for y in range(p):
        if (x**4+y**4+x)%p==0 and (y*y*(8*x**3-1))%p==0:
            count+=1
    count+=sum((1+y**4)%p==0 for y in range(p))
    return count

for p in (5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97):
    r=p%24
    expected=2+2*(r%3==1)+4*(r%8==1)+4*(r in (1,5))+8*(r==1)
    assert prime_count(p)==expected,(p,prime_count(p),expected)

# Quadratic extension finite fields F_p[t]/(t^2-d), with nonsquare d.
class Quadratic:
    def __init__(self,p,d):
        self.p,self.d=p,d
        assert d%p!=0 and pow(d,(p-1)//2,p)==p-1
        self.E=list(product(range(p),repeat=2))
        self.zero=(0,0)
        self.one=(1,0)
    def add(self,a,b):
        p=self.p
        return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def mul(self,a,b):
        p,d=self.p,self.d
        return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def pw(self,a,n):
        out=self.one
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out
    def scale(self,a,n):return ((a[0]*n)%self.p,(a[1]*n)%self.p)
    def eq0(self,a):return a==self.zero

def quadratic_count(p,d):
    K=Quadratic(p,d)
    count=0
    for x in K.E:
        x3=K.pw(x,3)
        x4=K.mul(x,x3)
        hX=K.add(K.scale(x3,8),K.scale(K.one,-1))
        for y in K.E:
            f=K.add(K.add(x4,K.pw(y,4)),x)
            h=K.mul(K.pw(y,2),hX)
            if K.eq0(f) and K.eq0(h):count+=1
    count+=sum(K.eq0(K.add(K.one,K.pw(y,4))) for y in K.E)
    return count
for p,d in ((5,2),(7,3),(11,2)):
    assert quadratic_count(p,d)==20,(p,d,quadratic_count(p,d))
print('C48_FULL_HESSIAN_GALOIS_ORBITS_PRIME_AND_QUADRATIC_EXTENSION_COUNTS_PASS')
