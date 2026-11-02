#!/usr/bin/env python3
"""Standalone checks for a spherical quadratic mean and its spectral moment identities."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, cos, sin, pi, sqrt
import random

checks=0

def eq(x,y):
    global checks
    assert x==y,(x,y)
    checks+=1

def close(x,y,eps=2e-7):
    global checks
    assert abs(x-y)<eps,(x,y,eps)
    checks+=1

def rising(q,k):
    t=F(1)
    for j in range(k): t*=q+j
    return t

def compositions(n,k):
    if n==1:
        yield (k,)
        return
    for j in range(k+1):
        for rest in compositions(n-1,k-j):
            yield (j,)+rest

def moment_X(lams,k):
    n=len(lams)
    num=F(0)
    for a in compositions(n,k):
        coeff=F(1)
        remaining=k
        for j in a:
            coeff*=comb(remaining,j)
            remaining-=j
        term=coeff
        for j,l in zip(a,lams): term*=l**j*rising(F(1,2),j)
        num+=term
    return F(n**k)*num/rising(F(n,2),k)

def moment_Y(lams,k):
    return sum(F((-1)**(k-j)*comb(k,j))*moment_X(lams,j) for j in range(k+1))

def spectral_moments(lams):
    n=len(lams)
    a=[x-F(1,n) for x in lams]
    aa={j:sum((z**j for z in a),F(0)) for j in (2,3,4)}
    v=F(2*n,n+2)*aa[2]
    m3=F(8*n*n,(n+2)*(n+4))*aa[3]
    m4=F(n**3,(n+2)*(n+4)*(n+6))*(12*aa[2]**2+48*aa[4])
    return v,m3,m4

random.seed(314159)
for n in range(2,8):
    for trial in range(30):
        wt=[random.randint(0,30) for _ in range(n)]
        if sum(wt)==0:wt[0]=1
        lams=[F(w,sum(wt)) for w in wt]
        v,m3,m4=spectral_moments(lams)
        eq(moment_X(lams,0),1)
        eq(moment_X(lams,1),1)
        eq(moment_Y(lams,1),0)
        eq(moment_Y(lams,2),v)
        eq(moment_Y(lams,3),m3)
        eq(moment_Y(lams,4),m4)
        assert m4<=15*v*v
        checks+=1
        assert m4>=0
        checks+=1

# Circle quadrature is independent of moment formulas, including rank-deficient endpoints.
N=16384
for t in range(0,17):
    p=t/16
    lams=[F(t,16),F(16-t,16)]
    v,m3,m4=spectral_moments(lams)
    theta=0.
    for j in range(N):
        a=2*pi*(j+0.5)/N
        x=2*(p*cos(a)**2+(1-p)*sin(a)**2)
        theta+=sqrt(x)/N
    deficit=1-theta
    base=float(v)/8-float(m3)/16
    assert -3e-7<=deficit-base<=5*float(m4)/16+3e-7
    checks+=1
    if t in (0,8,16):
        assert deficit>=-3e-7
        checks+=1

# Same purity but opposite cubic spectral skewness.
for n in (3,4,8):
    for d in (F(1,100*n),F(1,1000*n)):
        a=[F(1,n)+2*d,F(1,n)-d,F(1,n)-d]+[F(1,n)]*(n-3)
        b=[F(1,n)-2*d,F(1,n)+d,F(1,n)+d]+[F(1,n)]*(n-3)
        va,ta,_=spectral_moments(a)
        vb,tb,_=spectral_moments(b)
        eq(va,vb)
        eq(ta,-tb)
        assert ta>0
        checks+=1

print(f'PASS {checks} exact-rational and independent circle-quadrature assertions')
