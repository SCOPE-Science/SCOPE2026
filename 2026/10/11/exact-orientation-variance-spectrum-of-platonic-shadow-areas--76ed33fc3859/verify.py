#!/usr/bin/env python3
"""Reproducible exact facet-normal enumeration and rational interval certificate.

Python standard library only.  This checks a finite, explicitly listed set of
Platonic normal configurations; no external mathematical tables are consumed.
"""
from fractions import Fraction as Q
from dataclasses import dataclass
from collections import Counter
from itertools import product
from math import isqrt, sqrt
import math, random

@dataclass(frozen=True)
class F5:
    a: Q = Q(0)
    b: Q = Q(0)
    def __post_init__(self):
        object.__setattr__(self,'a',Q(self.a))
        object.__setattr__(self,'b',Q(self.b))
    def __add__(self,o):
        o=as5(o); return F5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return F5(-self.a,-self.b)
    def __sub__(self,o):return self+(-as5(o))
    def __rsub__(self,o):return as5(o)-self
    def __mul__(self,o):
        o=as5(o);return F5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as5(o);den=o.a*o.a-5*o.b*o.b
        assert den!=0
        z=self*F5(o.a,-o.b)
        return F5(z.a/den,z.b/den)
    def sign(self):
        a,b=self.a,self.b
        if a==0 and b==0:return 0
        if a>=0 and b>=0:return 1
        if a<=0 and b<=0:return -1
        return (1 if a*a>5*b*b else -1) if a>0 else (1 if 5*b*b>a*a else -1)
    def __abs__(self):return self if self.sign()>=0 else -self
    def flt(self):return float(self.a)+float(self.b)*sqrt(5)

def as5(x):return x if isinstance(x,F5) else F5(x)

phi=F5(Q(1,2),Q(1,2))
psi=phi-1

def vec(a,b,c):return tuple(as5(x) for x in (a,b,c))
V={}
V['tetrahedron']=[vec(a,b,c) for a,b,c in product((-1,1),repeat=3) if a*b*c==1]
V['cube']=[vec(s,0,0) for s in (-1,1)]+[vec(0,s,0) for s in (-1,1)]+[vec(0,0,s) for s in (-1,1)]
V['octahedron']=[vec(a,b,c) for a,b,c in product((-1,1),repeat=3)]
V['dodecahedron']=([vec(0,a,b*phi) for a,b in product((-1,1),repeat=2)]+
  [vec(a,b*phi,0) for a,b in product((-1,1),repeat=2)]+
  [vec(a*phi,0,b) for a,b in product((-1,1),repeat=2)])
V['icosahedron']=([vec(a,b,c) for a,b,c in product((-1,1),repeat=3)]+
  [vec(0,a*psi,b*phi) for a,b in product((-1,1),repeat=2)]+
  [vec(a*psi,b*phi,0) for a,b in product((-1,1),repeat=2)]+
  [vec(a*phi,0,b*psi) for a,b in product((-1,1),repeat=2)])

def dot(u,v):return sum((x*y for x,y in zip(u,v)),F5())

def abs_correlation_counts(vv):
    q=dot(vv[0],vv[0])
    assert q.sign()>0 and all(dot(v,v)==q for v in vv)
    assert len(vv)==len(set(vv))
    return Counter(abs(dot(u,v)/q) for u in vv for v in vv)

third=F5(Q(1,3)); root5_fifth=F5(0,Q(1,5));root5_third=F5(0,Q(1,3))
expected={
 'tetrahedron':{F5(1):4,third:12},
 'cube':{F5(1):12,F5(0):24},
 'octahedron':{F5(1):16,third:48},
 'dodecahedron':{F5(1):24,root5_fifth:120},
 'icosahedron':{F5(1):40,third:240,root5_third:120},
}
for name,vv in V.items():
    counts=abs_correlation_counts(vv)
    assert counts==expected[name], (name,counts)
    print('EXACT_PAIR_COUNTS',name,'faces',len(vv),'ordered_pairs',sum(counts.values()))

# The octahedral normal multiset equals the tetrahedral normal multiset
# with its negative adjoined, proving pointwise equality of normalized brightness.
assert set(V['octahedron'])==set(V['tetrahedron'])|set(tuple(-a for a in n) for n in V['tetrahedron'])

# A rational interval [lo,hi] is represented by a pair of Fractions.
def itv(a,b=None):return (Q(a),Q(a if b is None else b))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    z=[a*b for a in x for b in y]
    return (min(z),max(z))
def div(x,y):
    assert y[0]>0
    return mul(x,(Q(1)/y[1],Q(1)/y[0]))
def sqrtr(q,places=24):
    q=Q(q); assert q>0
    den=10**places
    n=isqrt((q.numerator*den*den)//q.denominator)
    lo,hi=Q(n,den),Q(n+1,den)
    assert lo*lo<=q<hi*hi
    return lo,hi

def atan_interval(x,terms=24):
    x=Q(x);assert 0<x<1
    s=Q(0)
    for k in range(terms):s+=(-1)**k*x**(2*k+1)/Q(2*k+1)
    err=x**(2*terms+1)/Q(2*terms+1)
    return (s,s+err) if terms%2==0 else (s-err,s)

def asin_interval(x,terms=90):
    assert 0<x[0]<=x[1]<1
    def partial(z):
        total=Q(0)
        from math import comb
        for k in range(terms):
            total+=Q(comb(2*k,k),4**k*(2*k+1))*z**(2*k+1)
        return total
    low=partial(x[0])
    hi=partial(x[1]) + x[1]**(2*terms+1)/(1-x[1]*x[1])
    return low,hi

pi=sub(mul(itv(16),atan_interval(Q(1,5))),mul(itv(4),atan_interval(Q(1,239))))
root2=sqrtr(2)
root5=sqrtr(5)
a13=asin_interval(itv(Q(1,3)))
a15=asin_interval(div(itv(1),root5))
a53=asin_interval(div(root5,itv(3)))

def f_interval(r):
    if r==F5(0):return itv(1)
    if r==F5(1):return div(pi,itv(2))
    if r==third:
        return add(mul(itv(Q(2,3)),root2),mul(itv(Q(1,3)),a13))
    if r==root5_fifth:
        return mul(div(itv(1),root5),add(itv(2),a15))
    if r==root5_third:
        return add(itv(Q(2,3)),mul(div(root5,itv(3)),a53))
    raise ValueError(r)

variance={}
for name,vv in V.items():
    m=len(vv)
    total=itv(0)
    for rho,count in expected[name].items():
        total=add(total,mul(itv(count),f_interval(rho)))
    var=sub(div(mul(itv(Q(8,3*m*m)),total),pi),itv(1))
    variance[name]=var
    assert var[0]>0
    print('CERTIFIED_RELATIVE_VARIANCE',name,
          ('%.12f'%float(var[0]),'%.12f'%float(var[1])),
          'width',float(var[1]-var[0]))
assert variance['tetrahedron']==variance['octahedron']
assert variance['cube'][0]>variance['tetrahedron'][1]
assert variance['tetrahedron'][0]>variance['dodecahedron'][1]
assert variance['dodecahedron'][0]>variance['icosahedron'][1]
print('CERTIFIED_STRICT_ORDER cube > tetrahedron = octahedron > dodecahedron > icosahedron')
# Exact sharp integer view counts for at most one-percent relative RMS error.
# RMS((4/k)*sum(brightness)/surface_area - 1) = sqrt(variance/k).
one_percent_counts={'cube':104,'tetrahedron':57,'octahedron':57,
                    'dodecahedron':16,'icosahedron':6}
for name,k in one_percent_counts.items():
    lower,upper=variance[name]
    assert Q(10000)*lower>k-1,(name,'k-1 sufficient')
    assert Q(10000)*upper<=k,(name,'k insufficient')
print('CERTIFIED_ONE_PERCENT_RMS_MIN_COUNTS', one_percent_counts)


# An independent random-orientation regression; not used in the proof.
rr=random.Random(987654321)
N=60000
normals={}
for name,vv in V.items():
    norm=math.sqrt(dot(vv[0],vv[0]).flt())
    normals[name]=[tuple(t.flt()/norm for t in v) for v in vv]
means={name:0.0 for name in V}; m2={name:0.0 for name in V}
for i in range(N):
    z=[rr.gauss(0,1) for _ in range(3)]
    z=[v/math.sqrt(sum(t*t for t in z)) for v in z]
    for name, vv in normals.items():
        # b/mean is (2/m) times the sum of facet-normal absolute cosines.
        yn=2/len(vv)*sum(abs(sum(a*b for a,b in zip(z,v))) for v in vv)
        means[name]+=yn; m2[name]+=yn*yn
for name in V:
    mu=means[name]/N
    empirical=m2[name]/N-mu*mu
    assert abs(mu-1)<0.002,(name,mu)
    assert abs(empirical-float(variance[name][0]))<0.00035,(name,empirical)
    print('SAMPLED',name,'mean',round(mu,8),'relative_variance',round(empirical,8))
print('VERIFY_OK')
