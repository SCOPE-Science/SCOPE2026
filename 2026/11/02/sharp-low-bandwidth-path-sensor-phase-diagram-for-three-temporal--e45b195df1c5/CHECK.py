#!/usr/bin/env python3
"""Exact low-band identities and independent finite-matrix tests for path sampling."""
import math
import numpy as np
from sympy import Rational, sqrt, simplify, symbols, factor, diff
u=symbols('u', real=True)
P=8*u**3-10*u**2+3*u
assert factor(P-u*(2*u-1)*(4*u-3))==0
assert factor(diff(P,u)-(24*u*u-20*u+3))==0
assert simplify(P.subs(u,Rational(1,4))-Rational(1,4))==0
for z in [(2+sqrt(2))/4,(2-sqrt(2))/4]:
    assert simplify(P.subs(u,z)-Rational(1,4))==0
for z, expected in [((3+sqrt(5))/8,(1-sqrt(5))/16),((3-sqrt(5))/8,(1+sqrt(5))/16)]:
    assert simplify(P.subs(u,z)-expected)==0
assert simplify(P.subs(u,Rational(225,256))-Rational(1,3))>0
assert simplify((10+7*sqrt(7))/108 - Rational(1,3))<0

def expected(K,M):
    if K==2:
        if M<=2:return {0,M}
        if M==3:return set(range(M+1))
        return {1,M-1}
    if K==3:return {0,M} if M<=5 else {1,M-1}
    if M==3:return set(range(M+1))
    if M==6:return {0,2,4,6}
    if M==8:return {0,1,3,5,7,8}
    if M<=8:return {0,M}
    return {1,M-1}

checks=0
for M in range(1,80):
    xx=np.arange(M+1)
    for K in (2,3,4):
        if K>M+1:continue
        d=np.ones(M+1);d[1:M]=2
        cos=np.cos(np.pi*np.outer(np.arange(1,K),xx)/M)
        ratios=d**K * np.prod(cos*cos, axis=0)
        opt=set(np.flatnonzero(np.abs(ratios-ratios.max())<1e-8))
        assert opt==expected(K,M),(M,K,opt,expected(K,M),ratios)
        checks+=1
# Independent operator calculation for moderate path sizes and all positions.
for M in range(1,21):
    n=M+1
    a=np.zeros((n,n),float)
    deg=np.ones(n);deg[1:-1]=2
    for i in range(n-1):a[i,i+1]=a[i+1,i]=1/(deg[i]*deg[i+1])**.5
    lam,U=np.linalg.eigh(a);lam=lam[::-1];U=U[:,::-1]
    for K in (2,3,4):
        if K>n:continue
        V=np.vander(lam[:K],N=K,increasing=True).T
        c0=np.linalg.det(V)**2
        # Discriminant factors identical for every position.
        for x in range(n):
            O=V*U[x,:K]
            observed=float(abs(np.linalg.det(O))**2)
            predicted=c0*float(np.prod(U[x,:K]**2))
            assert abs(observed-predicted)<2e-11
            # Compare independent eigensystem with exact cosine eigenvectors.
            model=deg[x]/(2*M) if K==1 else deg[x]/M
            for k in range(K):
                model=deg[x]/(2*M) if k in (0,M) else deg[x]/M
                model*=math.cos(math.pi*k*x/M)**2
                assert abs(U[x,k]**2-model)<2e-11,(M,K,x,k,U[x,k],model)
            checks+=1
print('PASS',checks,'families/operator comparisons plus 7 symbolic identities')
