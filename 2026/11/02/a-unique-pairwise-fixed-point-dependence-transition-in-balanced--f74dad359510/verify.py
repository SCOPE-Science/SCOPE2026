#!/usr/bin/env python3
"""Exact finite consistency checks for two-block weighted permutation fixed-point covariance."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial

def polyadd(a,b):
    n=max(len(a),len(b)); return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def polymul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c
def polydiff(a):return [i*a[i] for i in range(1,len(a))]
def poleval(a,q):return sum(F(v)*q**i for i,v in enumerate(a))
def Z(m):return [comb(m,k)**2 for k in range(m+1)]
def H(m):
    z=Z(m);p=polymul(z,polydiff(polydiff(z)));q=polymul(polydiff(z),polydiff(z))
    return polyadd([m*m*v for v in p],[-(m-1)**2*v for v in q])

checks=0
# Independent combinatorial enumeration, including each tagged event, for m=2,3,4.
for m in range(2,5):
    hist=defaultdict(lambda: [0,0,0,0]); i=m;j=m+1
    for perm in permutations(range(2*m)):
        k=sum(perm[r]<m for r in range(m)); one=int(perm[i]==i);other=int(perm[j]==j)
        v=hist[k];v[0]+=1;v[1]+=one;v[2]+=other;v[3]+=one*other
    assert sum(h[0] for h in hist.values())==factorial(2*m);checks+=1
    for k in range(m+1):
        total,first,second,both=hist[k]
        assert total==factorial(m)**2*comb(m,k)**2;checks+=1
        assert F(first,total)==F(k,m*m);checks+=1
        assert F(second,total)==F(k,m*m);checks+=1
        assert F(both,total)==F(k*(k-1),m*m*(m-1)**2);checks+=1
    for theta in (F(1,5),F(1,3),F(1,2),F(1),F(3)):
        norm=sum(theta**k*hist[k][0] for k in range(m+1))
        p1=sum(theta**k*hist[k][1] for k in range(m+1))/norm
        p2=sum(theta**k*hist[k][2] for k in range(m+1))/norm
        p12=sum(theta**k*hist[k][3] for k in range(m+1))/norm
        z=Z(m);zp=polydiff(z);zpp=polydiff(zp);zval=poleval(z,theta)
        assert p1==theta*poleval(zp,theta)/(m*m*zval);checks+=1
        assert p2==p1;checks+=1
        assert p12==theta**2*poleval(zpp,theta)/(m*m*(m-1)**2*zval);checks+=1
        exact=theta**2*poleval(H(m),theta)/(m**4*(m-1)**2*zval**2)
        assert p12-p1*p2==exact;checks+=1
        if theta==1:
            assert exact==F(1,4*m*m*(2*m-1));checks+=1
# Direct Legendre recurrence, independent of coefficient formula.
l0=[1];l1=[1,1]
for m in range(1,18):
    lhs=polyadd([(2*m+1)*v for v in polymul([1,1],l1)],[-m*v for v in polymul([1,-2,1],l0)])
    assert all(v%(m+1)==0 for v in lhs); checks+=1
    l2=[v//(m+1) for v in lhs]
    assert l2==Z(m+1);checks+=1
    l0,l1=l1,l2
for m in range(2,18):
    h=H(m)
    assert h[0]==-m**4*(m-1)**2//2;checks+=1
    assert h[-1]==m*m*(m-1);checks+=1
    assert poleval(h,F(1))>0;checks+=1
    assert h[0]<0;checks+=1
# Finite threshold brackets (not a proof of uniqueness, which follows from root monotonicity).
for m in range(2,14):
    h=H(m);lo=F(0);hi=F(1)
    for iteration in range(35):
        mid=(lo+hi)/2
        if poleval(h,mid)>0:hi=mid
        else:lo=mid
        assert poleval(h,lo)<=0<poleval(h,hi);checks+=1
    if m==2:
        assert F(4494,10000)<hi<F(4495,10000);checks+=1
print('passed',checks,'exact-integer/rational assertions')
