#!/usr/bin/env python3
"""Exact rational Bernstein certificate and numerical spectral spot checks.
Requires Python standard library only. Run: python3 verify.py
"""
from fractions import Fraction as F
from math import comb, sqrt, log

class Poly:
    def __init__(self, terms=None):
        self.d = {k:F(v) for k,v in (terms or {}).items() if v}
    @classmethod
    def const(cls, v): return cls({(0,0):v})
    @classmethod
    def var(cls, ix): return cls({((1,0) if ix==0 else (0,1)):1})
    def __add__(self, other):
        if not isinstance(other,Poly): other=Poly.const(other)
        d=dict(self.d)
        for k,v in other.d.items(): d[k]=d.get(k,F(0))+v
        return Poly(d)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,other):return self+-other if isinstance(other,Poly) else self+(-F(other))
    def __rsub__(self,other):return -self+other
    def __mul__(self,other):
        if not isinstance(other,Poly):other=Poly.const(other)
        d={}
        for (i,j),v in self.d.items():
            for (k,l),w in other.d.items():
                a=(i+k,j+l)
                d[a]=d.get(a,F(0))+v*w
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        r=Poly.const(1);a=self
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r

A,t=Poly.var(0),Poly.var(1)
One=Poly.const(1)
base=(1-A*A*t)*(1-t)*(1+t*t+t**4)
cases={
    'zero':(1-A**4*t*t)*(1-A*A*t*t+A**4*t**4),
    'minus_sqrtq':(1-A**4*t*t)*(1-A*A*t*t)*(1+A*A*t*t-A*t),
    # 7/4 > sqrt(3), so this is a rigorous lower bound for the -sqrt(3q) sector.
    'minus_sqrt3q_lower':(1-A**4*t*t)*(1+A*A*t*t)*(1+A*A*t*t-F(7,4)*A*t),
}
expect={'zero':F(885,2048), 'minus_sqrtq':F(1677,10240),
        'minus_sqrt3q_lower':F(381,40960)}
for name,g in cases.items():
    diff=g-base
    assert all(j>=1 for (_,j) in diff.d)
    # diff/t, with A=(3/4)u and 0<=u<=1. This contains all A=1/sqrt(q), q>=2.
    d={(i,j-1):v*F(3,4)**i for (i,j),v in diff.d.items()}
    na=max(i for i,j in d); nt=max(j for i,j in d)
    assert (na,nt)==(8,5)
    b=[]
    for u in range(na+1):
        for v in range(nt+1):
            coeff=sum((d.get((i,j),F(0))*F(comb(u,i),comb(na,i))
                    *F(comb(v,j),comb(nt,j))
                      for i in range(u+1) for j in range(v+1)),F(0))
            b.append(coeff)
    assert len(b)==54 and min(b)==expect[name] and all(c>0 for c in b)
    print('BERNSTEIN_OK',name,'coefficients',len(b),'minimum',min(b))

# Spectral recurrence for the distance polynomials of a generalized hexagon.
def Ps(q,x):
    p=[1.0,x,x*x-q-1.0]
    for i in range(2,5): p.append(x*p[i]-q*p[i-1])
    p.append((x*p[5]-q*p[4])/(q+1))
    return p

def eigsum(q,x,p):
    vals=Ps(q,x)
    return sum(vals[i]*i**p for i in range(1,7))

for q in range(2,10):
    eig=[-q-1,-sqrt(3*q),-sqrt(q),0,sqrt(q),sqrt(3*q),q+1]
    for lam in eig:
        v=Ps(q,lam)
        assert abs(sum(v)) < 1e-6 if lam!=q+1 else True
        assert abs(lam*v[6]-q*v[5]) < 1e-5 * max(1,abs(q*v[5]))
    lo,hi=0.,1.
    for k in range(100):
        mid=(lo+hi)/2
        if eigsum(q,-q-1,mid)>0:hi=mid
        else:lo=mid
    alpha=(lo+hi)/2
    assert 0<alpha<1
    for lam in eig[1:-1]:
        assert eigsum(q,lam,alpha)<-0.01
    print('SPECTRAL_OK',q,'critical_exponent',format(alpha,'.15g'))
print('VERIFY_OK')
