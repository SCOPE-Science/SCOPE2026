#!/usr/bin/env python3
"""Independent finite checks for the Markov-binomial zero-density formula.
Python 3 standard library only. Finite checks do not prove the asymptotic theorem.
"""
from fractions import Fraction as Q
from itertools import product
from math import acos, cos, sqrt, pi, log, exp


def mul_add(c, A, zB=None):
    return [c*x for x in A]


def recurrence(a,b,n):
    den=a+b; A=[Q(1)];B=[b/den,a/den];
    if n==0:return A
    if n==1:return B
    u=1-a; v=1-b; h=a+b-1
    for m in range(2,n+1):
        C=[Q(0)]*(m+1)
        for j,vj in enumerate(B):
            C[j]+=u*vj; C[j+1]+=v*vj
        for j,vj in enumerate(A): C[j+1]+=h*vj
        A,B=B,C
    return B


def enumerate_chain(a,b,n):
    den=a+b; result=[Q(0)]*(n+1)
    for xs in product((0,1),repeat=n):
        p=(a if xs[0] else b)/den
        for x,y in zip(xs,xs[1:]):
            p*=({(0,0):1-a,(0,1):a,(1,0):b,(1,1):1-b})[(x,y)]
        result[sum(xs)]+=p
    return result

finite=0
for a,b in product([Q(1,5),Q(2,5),Q(3,5),Q(4,5)],repeat=2):
    if a+b<=1:continue
    for n in range(1,9):
        c=recurrence(a,b,n)
        assert c==enumerate_chain(a,b,n)
        assert sum(c)==1 and all(z>0 for z in c)
        assert sum(j*c[j] for j in range(n+1))==n*a/(a+b)
        finite+=1


def scaled_eval(a,b,n,t):
    u=1-a;v=1-b;h=a+b-1
    s=max(1.0,abs(u-v*t),sqrt(h*t))
    f0=1.0; f1=(b-a*t)/(a+b)/s
    if n==1:return f1
    alpha=(u-v*t)/s;beta=h*t/s**2
    for i in range(2,n+1):
        f0,f1=f1,alpha*f1-beta*f0
    return f1


def bisect(a,b,n,lo,hi):
    y=scaled_eval(a,b,n,lo)
    for _ in range(48):
        md=(lo+hi)/2
        ym=scaled_eval(a,b,n,md)
        if (y<0)==(ym<0):lo=md;y=ym
        else:hi=md
    return (lo+hi)/2

checks=0
for a,b,n in [(.6,.7,20),(.8,.8,28),(.8,.3,30),(.99,.05,20),(.35,.9,35)]:
    u=1-a;v=1-b;h=a+b-1
    lo=((sqrt(a*b)-sqrt(h))/v)**2
    hi=((sqrt(a*b)+sqrt(h))/v)**2
    # Fine logarithmic mesh resolves oscillations on sampled intervals.
    mesh=[lo/100*exp(i*log(hi*100/(lo/100))/18000) for i in range(18001)]
    prev=scaled_eval(a,b,n,mesh[0]); roots=[]
    for i in range(1,len(mesh)):
        nextval=scaled_eval(a,b,n,mesh[i])
        if (nextval<0)!=(prev<0): roots.append(bisect(a,b,n,mesh[i-1],mesh[i]))
        prev=nextval
    assert len(roots)==n,(a,b,n,len(roots))
    assert all(t>0 for t in roots)
    for frac in (.15,.30,.50,.70,.85):
        theta=frac*pi
        # Invert cos(theta)=(u-vt)/(2sqrt(h*t)) numerically.
        z=(-sqrt(h)*cos(theta)+sqrt(h*cos(theta)**2+u*v))/v
        t=z*z
        empirical=sum(x<=t for x in roots)/n
        assert abs(empirical-frac) <= 2.0/n, (a,b,n,frac,empirical)
        checks+=1
print('PASS: exact rational distributions',finite,'; finite root/CDF checks',checks)
