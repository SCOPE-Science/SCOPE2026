#!/usr/bin/env python3
"""Reproducible numerical checks for odd regular bipyramid shadow theorem.

Python standard library only. All tolerances are stated in code. Numerical
sampling corroborates but does not establish the universal theorem.
"""
import math
import random

PI = math.pi

def probability(n, h):
    assert n >= 3 and n % 2 == 1 and h > 0
    a = PI/n
    q = h / math.hypot(h, math.cos(a))
    return (2/a)*(2*math.asin(q*math.sin(a)) - math.asin(q*math.sin(a/2)) - math.asin(q*math.sin(3*a/2)))

def derivative(n, q):
    a=PI/n
    A=math.sin(a)
    B=math.sin(a/2)
    D=math.sin(3*a/2)
    return 2*A/math.sqrt(1-(A*q)**2) - B/math.sqrt(1-(B*q)**2) - D/math.sqrt(1-(D*q)**2)

def optimum(n):
    lo=0.0; hi=1.0-1e-15
    assert derivative(n,lo)>0 and derivative(n,hi)<0
    for _ in range(85):
        mid=(lo+hi)/2
        if derivative(n,mid)>0: lo=mid
        else: hi=mid
    q=(lo+hi)/2
    return math.cos(PI/n)*q/math.sqrt(1-q*q),q

def hull_count(points):
    points=sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]
    for p in points:
        while len(low)>1 and cross(low[-2],low[-1],p)<=0: low.pop()
        low.append(p)
    up=[]
    for p in reversed(points):
        while len(up)>1 and cross(up[-2],up[-1],p)<=0: up.pop()
        up.append(p)
    return len(low)+len(up)-2

def hull_max(n,h,phi,c):
    pts=[(math.sin(phi+2*PI*j/n), c*math.cos(phi+2*PI*j/n)) for j in range(n)]
    T=h*math.sqrt(1-c*c)
    pts.extend([(0,T),(0,-T)])
    return hull_count(pts)==n+2

def inequality_max(n,h,phi,c):
    # A projected apex must cross exactly one upper and one lower base facet.
    C=math.cos(PI/n)
    k=h*math.sqrt(1-c*c)/c
    ds=[math.cos(phi+2*PI*(j+0.5)/n) for j in range(n)]
    p=sorted((x for x in ds if x>0),reverse=True)
    m=sorted((-x for x in ds if x<0),reverse=True)
    l=max(C/p[0],C/m[0])
    r=min(C/p[1] if len(p)>1 else float('inf'),C/m[1] if len(m)>1 else float('inf'))
    return l<k<r

rng=random.Random(20261018)
for n in (3,5,7,9,13):
    for h in (.18,.53,1.0,2.5):
        N=2000
        count=0
        for _ in range(N):
            phi=2*PI*rng.random()/n
            c=0.000001+0.999998*rng.random()
            direct=hull_max(n,h,phi,c)
            reduced=inequality_max(n,h,phi,c)
            assert direct==reduced,(n,h,phi,c)
            count+=direct
        predicted=probability(n,h)
        observed=count/N
        assert abs(observed-predicted)<.055,(n,h,observed,predicted)
print('INDEPENDENT_MONOTONE_CHAIN_SHADOWS_AND_FACET_TESTS_OK 40000')
for n in (3,5,7,9,15,31,101):
    h,q=optimum(n)
    assert derivative(n,max(0,q-0.0001))>0 and derivative(n,min(.9999999,q+.0001))<0
    assert probability(n,h)>probability(n,.95*h) and probability(n,h)>probability(n,1.05*h)
    if n==3: assert abs(h-.9407876671881886)<1e-7
print('UNIQUE_STATIONARY_MAXIMUM_AND_OPTIMUM_CHECKS_OK')
for n in (101,301,1001):
    h,q=optimum(n)
    v=n*n*probability(n,h)
    limit=PI*PI/(3*math.sqrt(3))
    assert abs(h-1/math.sqrt(2))<.001
    assert abs(v-limit)<.003,(n,v,limit)
print('SHARP_ODD_PARITY_ASYMPTOTIC_CHECKS_OK')
print('ALL_ODD_BIPYRAMID_CHECKS_OK')
