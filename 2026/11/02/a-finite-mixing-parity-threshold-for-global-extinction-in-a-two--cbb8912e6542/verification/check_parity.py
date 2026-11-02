#!/usr/bin/env python3
"""Standalone algebraic and trajectory checks for a two-patch saturating map.
This is a finite consistency test, not a proof of all-parameter assertions.
"""
from fractions import Fraction as Q
from math import sqrt, log

def mult(a,b):
    return [[sum(a[i][h]*b[h][j] for h in (0,1)) for j in (0,1)] for i in (0,1)]

def power(m,k):
    a=[[Q(1),Q(0)],[Q(0),Q(1)]]
    for _ in range(k): a=mult(a,m)
    return a

def eigenvalue(r1,r2,p,k):
    s=(1-2*p)**k
    av=(r1+r2)/2
    return (av*(1+s)+sqrt((av*(1+s))**2-4*r1*r2*s))/2

def iterate(r1,r2,p,k,a1,a2,steps=30000):
    v=[0.6,0.4]
    s=(1-2*p)**k
    u=(1+s)/2; w=(1-s)/2
    for _ in range(steps):
        z1=u*v[0]+w*v[1];z2=w*v[0]+u*v[1]
        v=[r1*z1/(1+a1*z1),r2*z2/(1+a2*z2)]
    return v

count=0
for p in (Q(3,5),Q(4,5),Q(9,10),Q(19,20)):
    m=[[1-p,p],[p,1-p]]
    for k in range(1,18):
        s=(1-2*p)**k
        formula=[[Q(1,2)*(1+s),Q(1,2)*(1-s)],[Q(1,2)*(1-s),Q(1,2)*(1+s)]]
        assert power(m,k)==formula
        r1=Q(2);r2=Q(1,5)
        a=mult([[r1,Q(0)],[Q(0),r2]],formula)
        assert a[0][0]+a[1][1]==(r1+r2)*(1+s)/2
        assert a[0][0]*a[1][1]-a[0][1]*a[1][0]==r1*r2*s
        count+=1

r1=2.0;r2=0.2;p=.9;av=(r1+r2)/2;product=r1*r2
tau=(av-1)/(av-product)
assert abs(tau-1/7)<1.e-14
print('exact rational P^k and characteristic identity tests:',count)
cutoff=int(log(tau)/log(2*p-1))
last_odd=cutoff if cutoff%2 else cutoff-1
print('threshold tau=',tau,'; odd last extinct k=',last_odd)
print('k | eigenvalue | predicted | endpoints after 30000 steps')
for k in range(1,12):
    lam=eigenvalue(r1,r2,p,k)
    pred='extinction' if lam<=1 else 'endemic'
    v=iterate(r1,r2,p,k,r1,r2)
    assert (max(v)<1e-8 if lam<.995 else True)
    assert (min(v)>1e-4 if lam>1.005 else True)
    print('%2d | %.10f | %-10s | %.8f,%.8f'%(k,lam,pred,v[0],v[1]))

# The boundary rho=1 is exactly achieved for p=(1+tau)/2 at k=1.
p=(1+tau)/2
assert abs(eigenvalue(r1,r2,p,1)-1)<1e-13
v=iterate(r1,r2,p,1,r1,r2)
assert max(v)<.0001
print('critical-case k=1, p=',p,'; x(30000)=',v)
