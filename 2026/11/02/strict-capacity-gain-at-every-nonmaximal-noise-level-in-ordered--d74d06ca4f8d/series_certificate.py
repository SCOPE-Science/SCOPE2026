#!/usr/bin/env python3
"""Exact rational Taylor-coefficient certificate for the high-noise limit.

Formal power-series arithmetic over Q is truncated at degree 11.
No floating-point arithmetic or third-party packages are used.
"""
from fractions import Fraction as F

N=12

def P(c=0):
    a=[F(0)]*N
    a[0]=F(c)
    return a

def add(a,b):
    return [x+y for x,y in zip(a,b)]

def neg(a):
    return [-x for x in a]

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    out=P()
    for i,x in enumerate(a):
        for j,y in enumerate(b[:N-i]):
            out[i+j]+=x*y
    return out

def scale(a,k):
    return [x*F(k) for x in a]

def power(a,k):
    v=P(1)
    for _ in range(k):
        v=mul(v,a)
    return v

def logone(a):
    assert a[0]==1
    x=sub(a,P(1))
    total=P()
    for k in range(1,N):
        total=add(total,scale(power(x,k),F((-1)**(k+1),k)))
    return total

t=P();t[1]=1
t2=power(t,2);t4=power(t,4);t6=power(t,6)
beta=add(sub(t2,scale(t4,3)),scale(t6,F(34,3)))
b=scale(sub(P(1),t2),F(1,4))
u0=scale(add(P(1),t2),F(1,4))
u=sub(u0,scale(mul(t2,beta),F(1,2)))
v=add(b,scale(mul(mul(t,add(P(1),t)),beta),F(1,2)))
w=sub(b,scale(mul(mul(t,sub(P(1),t)),beta),F(1,2)))
logu=logone(scale(u,4));logv=logone(scale(v,4));logw=logone(scale(w,4))
d=add(sub(mul(t2,logu),scale(mul(mul(t,add(P(1),t)),logv),F(1,2))),
      scale(mul(mul(t,sub(P(1),t)),logw),F(1,2)))
assert all(d[k]==0 for k in range(2,9))


def hprob(a):
    return neg(mul(a,logone(scale(a,4))))

gain=sub(add(add(scale(hprob(u),2),hprob(v)),hprob(w)),
         add(scale(hprob(u0),2),scale(hprob(b),2)))
assert gain[6]==1 and gain[8]==-3 and gain[10]==F(32,3)
assert all(gain[k]==0 for k in (0,1,2,3,4,5,7,9,11))
print('EXACT_STATIONARITY_COEFFICIENTS_2_TO_8_ZERO')
print('EXACT_GAIN_NATS=t^6-3t^8+(32/3)t^10+O(t^12)')
print('SERIES_CERTIFICATE_OK')
