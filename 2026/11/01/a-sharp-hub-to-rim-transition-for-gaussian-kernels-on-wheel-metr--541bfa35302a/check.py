#!/usr/bin/env python3
"""Exact-identity and numerical reproducibility tests for wheel metric Gaussian matrices."""
from fractions import Fraction as F
import math
import numpy as np
from scipy.optimize import brentq

def roots(n):
    c=1.0 if n%2==0 else math.cos(math.pi/n)
    f=lambda x:1-2*c*x+(2*c-1)*x**4
    a=brentq(f,0.01,0.95,xtol=1e-14)
    if n<=5:
        return a,None
    H=lambda x:1+3*x-(n-3)*x*x*(1+x)
    return a,brentq(H,1e-8,0.99,xtol=1e-14)

def K(n,x):
    W=np.eye(n+1)
    W[0,1:]=x
    W[1:,0]=x
    for i in range(n):
        for j in range(i+1,n):
            k=1+i;ell=1+j
            W[k,ell]=W[ell,k]=x if ((i-j)%n in (1,n-1)) else x**4
    return W

def f(n,x):
    c=1 if n%2==0 else math.cos(math.pi/n)
    return 1-2*c*x+(2*c-1)*x**4

def g(n,x): return 1+2*x+(n-3)*x**4-n*x**2

a=F(27,50);b=F(11,20);d=F(63,100)
assert 1-2*a+a**4>0
assert 1-2*b+b**4<0
assert g(8,b)>0
assert g(9,a)<0
assert g(7,d)>0
# c7 > 1 - (22/49)^2/2 > root threshold from f7(d)<0
c7lower=1-F(22,49)**2/2
assert c7lower > (1-d**4)/(2*(d-d**4))
assert 1-2*c7lower*d+(2*c7lower-1)*d**4<0
print('Exact rational interval certificates PASS')

checks=0
for n in range(4,121):
    rf,rh=roots(n)
    r=rf if n<=8 else rh
    assert r is not None
    if n<=8: assert rh is None or rf<rh, (n,rf,rh)
    else: assert rh<rf, (n,rf,rh)
    assert abs(f(n,rf))<1e-11
    if rh is not None: assert abs(g(n,rh))<1e-11
    for mult in (0.8,1,1.2):
        x=r*mult
        if x>=1: continue
        eig=np.linalg.eigvalsh(K(n,x))
        if mult<1: assert eig[0]>-3e-10,(n,mult,eig[0])
        if mult>1: assert eig[0]<-3e-10,(n,mult,eig[0])
        if mult==1:
            expected=2 if n in (5,7) else 1
            assert sum(abs(eig)<2e-10)==expected, (n, eig[:5],expected)
        checks+=1
for n in (1000,10000,100000):
    rh=roots(n)[1]
    pred=n**-.5+n**-1+n**-1.5
    assert abs(rh-pred)<20/n**2, (n,rh,pred)
print(f'{checks} direct matrix spectral checks (orders 4...120) PASS')
for n in (4,5,6,7,8,9,10,100,10000):
    rf,rh=roots(n)
    r=rf if n<=8 else rh
    print(f'n={n} rim={rf:.12f} hub={rh} threshold_t={-math.log(r):.12f} nullity={2 if n in (5,7) else 1}')
print('large-n root asymptotic PASS')
