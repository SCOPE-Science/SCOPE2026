#!/usr/bin/env python3
"""Reproducibility checks for pinned damped-Jordan D-optimal timing.
Exact Cauchy--Binet identities plus finite numerical diagnostics;
these finite checks do not replace the analytic uniqueness proof.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, isclose

count=0
# Cross-product identity in exact rational arithmetic for arbitrary nonnegative
# row weights and rational observation times; not a floating-point test.
for b in (F(1,3),F(1,1),F(3,2),F(4,1)):
    for k in range(13):
        t=b*F(k,12)
        for weights in product((F(1,2), F(1), F(2)),repeat=3):
            w0,w1,w2=weights
            g00=w0+w1+w2
            g01=w1*t+w2*b
            g11=w1*t*t+w2*b*b
            d=g00*g11-g01*g01
            rhs=w0*w1*t*t+w0*w2*b*b+w1*w2*(b-t)**2
            assert d==rhs
            count+=1

def phi(b,u):
    return u*u*exp(-2*u)+b*b*exp(-2*b)+(b-u)**2*exp(-2*(u+b))

def slope(b,u):
    return 2*exp(-2*u)*(u*(1-u)-exp(-2*b)*(b-u)*(1+b-u))

def roots(b,steps=3000):
    rr=[]
    old=0.0
    v_old=slope(b,old)
    for j in range(1,steps+1):
        new=b*j/steps; v=slope(b,new)
        if v_old*v<0:
            lo,hi=old,new
            for _ in range(75):
                mid=(lo+hi)/2
                if slope(b,lo)*slope(b,mid)<=0:hi=mid
                else:lo=mid
            rr.append((lo+hi)/2)
        old,v_old=new,v
    return rr

for b in (.04,.1,.25,.5,.8,.99,1.0,1.001,1.01,1.1,1.5,2.0,3.0,5.0,8.0,12.0):
    rr=roots(b)
    if b<=1:
        assert len(rr)==1,(b,rr)
        assert all(phi(b,b*j/1200)<=phi(b,0)+2e-13 for j in range(1201)),b
        assert isclose(phi(b,0),phi(b,b),rel_tol=2e-14)
    else:
        assert len(rr)==2,(b,rr)
        r=rr[1]
        assert 0<rr[0]<r<1
        assert phi(b,r)>phi(b,0)
        assert all(phi(b,b*j/1200)<phi(b,r)+2e-13 for j in range(1201)),b
        assert abs(slope(b,r))<2e-12
    count+=1205

# Double asymptotic checks: critical transition and strong damping.
for eps in (1e-3,5e-4,1e-4):
    b=1+eps
    u=roots(b)[1]
    approx=(b-u)/eps
    assert abs(approx-1/(1-exp(-2)))<.004
    gain=(phi(b,u)-phi(b,0))/eps**2
    assert abs(gain-exp(-2)/(1-exp(-2)))<.005
    count+=2
for b in (5.,6.,8.,10.):
    u=roots(b)[1]
    rel=(1-u)/(b*(b-1)*exp(-2*b))
    assert abs(rel-1)<.025,(b,rel)
    ratio=phi(b,u)/phi(b,0)
    ratio_asym=exp(2*b-2)/(2*b*b)
    assert abs(ratio/ratio_asym-1)<.03
    count+=2

# Balanced endpoint replication changes only an additive constant and a
# positive scale, leaving the free-time maximizer unchanged.
for b in (.5,1.0,1.8,3.0):
    uu=[b*j/29 for j in range(30)]
    base=[phi(b,u) for u in uu]
    for m in (1,2,3,7):
        via_rep=[m*m*b*b*exp(-2*b)+m*(u*u*exp(-2*u)+(b-u)**2*exp(-2*(u+b))) for u in uu]
        assert base.index(max(base))==via_rep.index(max(via_rep))
        count+=1
print(f'PASS {count} exact-rational and numerical diagnostic assertions')
