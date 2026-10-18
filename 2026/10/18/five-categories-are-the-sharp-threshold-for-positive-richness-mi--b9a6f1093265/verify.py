#!/usr/bin/env python3
"""Exact checks for sample-richness / unseen-mass threshold theorem.
Run with Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import product

checks=0

def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for i in range(1,n-k+2):
            for xs in compositions(n-i,k-1):
                yield (i,)+xs

def sums(p):
    q2=sum(x*x for x in p)
    q3=sum(x*x*x for x in p)
    return q2,q3

def covariance_closed(p):
    a,b=sums(p)
    return (1+a)*b-2*a*a

def covariance_direct(p):
    m=len(p)
    terms=[]
    for i,j in product(range(m),repeat=2):
        prob=p[i]*p[j]
        richness=1 if i==j else 2
        missing=1-sum(p[k] for k in {i,j})
        terms.append((prob,richness,missing))
    ek=sum(w*k for w,k,u in terms)
    em=sum(w*u for w,k,u in terms)
    ekm=sum(w*k*u for w,k,u in terms)
    return ekm-ek*em

for d in range(1,7):
    for den in range(d,16):
        for counts in compositions(den,d):
            p=tuple(F(x,den) for x in counts)
            a=covariance_closed(p)
            b=covariance_direct(p)
            assert a==b,(p,a,b)
            if d==1: assert a==0
            elif d<=4: assert a<0,(d,counts,a)
            checks+=1

p=(F(4,5),)+ (F(1,20),)*4
assert covariance_closed(p)==F(1,1600)
checks+=1
for d in range(6,21):
    e=F(1,100000)
    p=tuple((1-e)*x for x in ((F(4,5),)+(F(1,20),)*4)) + (e/F(d-5),)*(d-5)
    assert sum(p)==1 and all(x>0 for x in p) and covariance_closed(p)>0
    checks+=1
for d in range(2,51):
    p=(F(1,d),)*d
    assert covariance_closed(p)==-F(d-1,d**3)
    checks+=1
# Explicit one-heavy polynomial-factor identities, checked independently on a rich rational grid.
for d in (2,3,4,5):
    for den in range(d,35):
        for a in range(1,den//d+1):
            t=F(a,den)
            p=(1-(d-1)*t,)+(t,)*(d-1)
            c=covariance_closed(p)
            if d==2: rhs=-2*t*t*(t-1)**2
            elif d==3: rhs=-2*t*t*(18*t**3-12*t*t+1)
            elif d==4: rhs=-6*t**3*(48*t*t-30*t+5)
            else: rhs=-4*t*t*(300*t**3-160*t*t+26*t-1)
            assert c==rhs
            checks+=1
print('PASS exact checks:',checks)
print('Five-species witness:',covariance_closed((F(4,5),)+(F(1,20),)*4))
