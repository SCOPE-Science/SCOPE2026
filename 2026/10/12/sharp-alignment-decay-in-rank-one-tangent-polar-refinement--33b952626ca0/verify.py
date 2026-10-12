#!/usr/bin/env python3
"""Finite exact/numerical checks of the rank-one tangent polar iteration theorem.
The analytic proof in RESULT.md supplies the infinite-parameter argument.
"""
from fractions import Fraction as F
from math import sqrt
import random
import numpy as np


def analytic_X(a,b,t):
    d=sqrt(a*a + (4**t)*b*b)
    return np.array([[a/d, (2**t)*b/d],[(2**t)*b/d,0.]])

def sign_matrix(A):
    U,s,Vh=np.linalg.svd(A,full_matrices=False)
    return U@Vh

def loop(a,b,t):
    G=np.array([[a,b],[b,0.]])
    X=G.copy()
    for _ in range(t):
        X=sign_matrix(X)
        X[1,1]=0.
    return X

# An exact-rational calculation after clearing the square-root denominator:
# X_t is N_t/sqrt(d_t), and I_t=(a^2+2^(t+1)b^2)/sqrt(d_t).
# Squaring the alignment quotient gives an entirely rational quantity.
checks=0
for a in range(1,19):
    for b in range(1,19):
        for t in range(1,11):
            k=2**t
            d=F(a*a+k*k*b*b)
            n=F(a*a+2*k*b*b)
            ratio_sq=n*n/(d*F(a*a+4*b*b))
            if t>1:
                assert ratio_sq <= 1
            if t==1:
                assert ratio_sq==1
            if t>=2:
                # R_t is positive and decreasing as t increases.
                previous_k=k//2
                prev_n=F(a*a+2*previous_k*b*b)
                prev_d=F(a*a+previous_k*previous_k*b*b)
                assert n*n*prev_d < prev_n*prev_n*d
            # AM-GM or 2x2 Cauchy supplies globally sharp lower bound.
            sharp_sq=F(8*k,(k+2)**2)
            assert ratio_sq>=sharp_sq
            checks+=1

# Equality for the sharp factor is realized at a^2=2k b^2.
for t in range(1,17):
    k=2**t
    a=sqrt(2*k)
    b=1.
    x=analytic_X(a,b,t)
    G=np.array([[a,b],[b,0.]])
    ratio=float(np.sum(G*x)/np.linalg.svd(G,compute_uv=False).sum())
    sharp=2*sqrt(2*k)/(k+2)
    assert abs(ratio-sharp)<5e-13,(t,ratio,sharp)

rng=random.Random(20261009)
numeric=0
for i in range(900):
    a=10**rng.uniform(-3,3)
    b=10**rng.uniform(-3,3)
    t=rng.randint(1,12)
    X=loop(a,b,t)
    target=analytic_X(a,b,t)
    assert np.max(np.abs(X-target))<5e-9,(a,b,t,X,target)
    assert abs(float(np.sum(X*np.array([[a,b],[b,0.]]))) - (a*a + (2**(t+1))*b*b)/sqrt(a*a+4**t*b*b))<1e-7
    numeric+=1

# Exact symbolic derivative of the squared ratio with y=(b/a)^2.
try:
    import sympy as s
    k,y=s.symbols('k y',positive=True)
    R2=(1+2*k*y)**2/((1+k*k*y)*(1+4*y))
    derivative=s.factor(s.diff(R2,y))
    certificate=(k-2)**2*(2*k*y-1)*(2*k*y+1)/((1+4*y)**2*(1+k*k*y)**2)
    assert s.simplify(derivative-certificate)==0
    assert s.simplify(R2.subs(y,1/(2*k)) - 8*k/(k+2)**2)==0
    print('SYMBOLIC_OK')
except ImportError:
    print('SYMBOLIC_SKIPPED sympy unavailable; analytic certificate in RESULT.md')

print(f'VERIFY_OK {checks} exact rational checks; {numeric} independent polar-SVD repetitions; equality for 16 horizons')
