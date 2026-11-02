#!/usr/bin/env python3
"""Independent finite-dimensional checks for two-choice cyclic averaging.

Run: python CHECK.py
Needs numpy and sympy (see requirements.txt). Finite checks are not
substitutes for the all-order proof in RESULT.md.
"""
import itertools
import math
from fractions import Fraction

import numpy as np
import sympy as sp

checks = 0

def verify(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def jmat(n, b):
    a = 1.0-b
    z = np.zeros((n, n))
    z[0,0] = 1.0+b*b
    z[-1,-1] = a*a
    for k in range(1,n-1):
        z[k,k] = a*a+b*b
    for k in range(n-1):
        z[k,k+1] = z[k+1,k] = a*b
    return z


def selector(n, b, bits):
    a=1.0-b
    M=np.zeros((n,n))
    for i,flag in enumerate(bits):
        if flag:
            M[i,i]=a
            M[i,(i-1)%n]+=b
        else:
            M[i,i]=1.0
    return M


def recurrence_poly(n, b):
    X=sp.symbols('X')
    a=1-b; t=a*b; c=a*a+b*b
    d0=sp.Integer(1)
    d1=X-(1+b*b)
    if n==2: return sp.expand((X-a*a)*d1-t*t*d0)
    u,v=d0,d1
    for k in range(2,n):
        u,v=v,sp.expand((X-c)*v-t*t*u)
    return sp.expand((X-a*a)*v-t*t*u)

for b in [0.15,0.5,0.73]:
    a=1-b; r=a/(2-b); top=2/(2-b)
    C=b*(3-2*b)**2/(2*(2-b)**2*a*a)
    for n in range(2,8):
        J=jmat(n,b)
        ev=np.linalg.eigvalsh(J)
        lam=ev[-1]
        verify(1<lam<top+1.e-10,('bounds',n,b))
        verify((ev[:-1]<1+1.e-10).all(),('unique_above_one',n,b))
        flags=[]; vmax=-1.
        for bits in itertools.product([0,1],repeat=n):
            B=selector(n,b,bits)
            value=np.linalg.eigvalsh(B.T@B)[-1]
            if value>vmax+2.e-12:
                flags=[bits];vmax=value
            elif abs(value-vmax)<2.e-12:
                flags.append(bits)
        verify(abs(vmax-lam)<2.e-10,('all_masks',n,b))
        verify(len(flags)==n and all(sum(x)==n-1 for x in flags),('single_hole',n,b))
        if n<=6:
            v=np.linalg.eigh(J)[1][:,-1]
            verify(np.max(v)*np.min(v)>0,('positive_eigenvector',n,b))
            z=(lam-(a*a+b*b)-math.sqrt((lam-(a*a+b*b))**2-4*(a*b)**2))/(2*a*b)
            H=(2-b)/a;K=b/a
            F=(H*z-1)*(1+K*z)-z**(2*n)*(H-z)*(z+K)
            verify(abs(F)<5.e-8,('secular',n,b))
    for n in [4,5,6]:
        lam=np.linalg.eigvalsh(jmat(n,b))[-1]
        ratio=(top-lam)/r**(2*n)
        verify(abs(ratio/C-1)<0.05,('asymptotic',n,b))

x=sp.symbols('x', positive=True)
a=1-x;t=a*x;r=a/(2-x);H=1/r;K=x/a
coef=sp.factor(t*(1/r**2-1)*(H-r)*(r+K)/(H*(1+K*r)))
verify(sp.simplify(coef-x*(3-2*x)**2/(2*(2-x)**2*(1-x)**2))==0,'asymptotic_coefficient_identity')
for b in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)]:
    for n in range(2,9):
        J=sp.zeros(n,n)
        a=1-b
        J[0,0]=1+b*b
        J[n-1,n-1]=a*a
        for k in range(1,n-1): J[k,k]=a*a+b*b
        for k in range(n-1): J[k,k+1]=J[k+1,k]=a*b
        X=sp.symbols('X')
        verify(sp.expand(J.charpoly(X).as_expr()-recurrence_poly(n,b))==0,('exact_characteristic',n,b))
print('CHECK_OK assertions='+str(checks))
