#!/usr/bin/env python3
"""Exact-rational and deterministic checks for a two-level quadrature risk theorem.
Requires only the Python standard library. All universal claims are proved analytically.
"""
from fractions import Fraction as F
from math import atanh, sqrt
from random import Random

def moment(n,k):
    z=F(1)
    for i in range(k):
        z*=F(2*i+1,2*i+n)
    return z

def coefficient(n,j):
    m1=F(1,n);m2=moment(n,2)
    return (j-1)*(moment(n,j)-m2+2*m1*m1)-2*m1*sum((moment(n,k) for k in range(1,j)),F(0))

def increment(n,j):
    m=moment(n,j)
    g=F(n-2,n)-F(j*(n-1),2*j+n)
    return m*g+F(4-n,n*n*(n+2))

def gap_three(e):
    d=1-e
    a=atanh(sqrt(d))/sqrt(d)
    b=1/(2*e)+a/2
    target=(1+2*e)/(3*e)
    return b-2*target*a+target*target-F(4,45)*d*d/(e*e)

checks=0
for n in range(2,24):
    assert moment(n,1)==F(1,n);checks+=1
    assert moment(n,2)==F(3,n*(n+2));checks+=1
    assert coefficient(n,2)==0;checks+=1
    for j in range(2,65):
        assert coefficient(n,j+1)-coefficient(n,j)==increment(n,j);checks+=1
        if n>=4:
            assert increment(n,j)<0 and coefficient(n,j+1)<0;checks+=1
        if n==2 and j>=3:
            assert increment(n,j)>0 and coefficient(n,j+1)>0;checks+=1
assert increment(2,2)==0 and coefficient(2,3)==0;checks+=2
assert coefficient(3,3)<0 and coefficient(3,4)<0;checks+=2
for j in range(3,63):
    assert increment(3,j+1)>increment(3,j);checks+=1
assert increment(3,2)<0 and increment(3,62)>0;checks+=2
for j in range(65,200):
    assert increment(3,j)>0;checks+=1

rng=Random(20261018)
for n in range(2,13):
    for _ in range(450):
        v=[rng.randrange(-100,101) for i in range(n)]
        total=sum(x*x for x in v)
        if total==0: continue
        w=F(v[0]*v[0],total)
        eps=F(rng.choice([1,2,3,4,5,7,9]),rng.choice([11,13,17,19,23]))
        if eps>=1: continue
        lam=eps*w+1-w
        gauss=1/lam
        inter=1+(1-lam)/eps
        assert gauss==1/(1-(1-eps)*w);checks+=1
        assert inter==1+(1-eps)*w/eps;checks+=1
        assert inter>=gauss>=1;checks+=1

for e in (.01,.03,.05,.06,.1,.2,.6,.9):
    assert (gap_three(e)>0)==(e<.0503804097941479);checks+=1
lo,hi=.05038,.05039
assert gap_three(lo)>0 and gap_three(hi)<0;checks+=2
for _ in range(60):
    mid=(lo+hi)/2
    if gap_three(mid)>0:lo=mid
    else:hi=mid
assert abs((lo+hi)/2-.0503804097941479)<2e-14;checks+=1

# Positive-risk ratio in dimension 2, strictly bounded below by one.
for i in range(1,1000):
    e=i/1000
    ratio=2*(1+e)/(1+sqrt(e))**2
    assert ratio>1;checks+=1
print('PASS',checks,'deterministic exact-rational/numerical assertions')
