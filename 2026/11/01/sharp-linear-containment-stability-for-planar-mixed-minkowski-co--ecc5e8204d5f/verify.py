#!/usr/bin/env python3
"""Exact-arithmetic checks for planar section/quotient stability."""
from fractions import Fraction as F
from random import Random

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    s=sorted(set(points))
    if len(s)<=1:return s
    lower=[]
    for p in s:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    upper=[]
    for p in s[::-1]:
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def area(poly):
    return abs(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(poly,poly[1:]+poly[:1])))/2

def x_center_chord(poly):
    xs=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        if p[1]==0:xs.append(p[0])
        if q[1]==0:xs.append(q[0])
        if (p[1]<0<q[1]) or (q[1]<0<p[1]):
            xs.append((q[1]*p[0]-p[1]*q[0])/(q[1]-p[1]))
    return max(xs)

def check(poly):
    A=area(poly)
    h=max(p[1] for p in poly)
    assert h>0
    top=next(p for p in poly if p[1]==h)
    b=top[0]
    a=x_center_chord(poly)
    assert a>0
    base=2*a*h
    eps=A/base-1
    assert eps>=0
    maxg=max(abs((p[0]-b*p[1]/h)/a)+abs(p[1]/h) for p in poly)
    assert maxg<=1+2*eps,(poly,a,h,A,eps,maxg)
    return eps,maxg

if __name__=='__main__':
    D=[(F(-1),F(0)),(F(0),F(-1)),(F(1),F(0)),(F(0),F(1))]
    count=0
    for den in [1,2,3,4,5,7,8,11,17,31]:
        for num in range(1,den+1):
            t=F(num,den)
            P=hull(D+[(F(1),t),(F(-1),-t)])
            e,g=check(P)
            assert area(P)==2+t
            assert e==t/2
            assert g==1+t==1+2*e
            count+=1
    rng=Random(20261031)
    for j in range(2500):
        ps=[(F(rng.randint(-20,20),rng.randint(1,13)),F(rng.randint(-20,20),rng.randint(1,13))) for k in range(rng.randint(3,12))]
        P=hull(ps+[(-x,-y) for x,y in ps]+D)
        check(P)
        count+=1
    print('PASS:',count,'exact rational polygon checks (including sharpness).')
