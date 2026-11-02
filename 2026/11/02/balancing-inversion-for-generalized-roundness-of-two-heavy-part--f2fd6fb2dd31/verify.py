#!/usr/bin/env python3
"""Independent numerical and exact arithmetic checks of the multipartite balance theorem."""
from __future__ import annotations
from decimal import Decimal, getcontext
from fractions import Fraction
from math import log2, sqrt
import numpy as np

getcontext().prec=65

def mu_formula(r,u,a):
    b=u-a
    v=a*b
    T=(r-1)*u+2*v
    C=u+r-2
    disc=T*T-4*r*v*C
    if disc<0: raise AssertionError((r,u,a,disc))
    return (Decimal(T)-Decimal(disc).sqrt())/(Decimal(2*r*v))

def full_quadratic_maxeig(r,u,a,q):
    sizes=[a,u-a]+[1]*(r-2)
    labels=[]
    for i,n in enumerate(sizes): labels.extend([i]*n)
    N=len(labels)
    D=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if i!=j:D[i,j]=q if labels[i]==labels[j] else 1.0
    # Helmert orthonormal basis of the full zero-sum hyperplane
    B=np.zeros((N,N-1))
    for j in range(1,N):
        B[:j,j-1]=1/np.sqrt(j*(j+1))
        B[j,j-1]=-j/np.sqrt(j*(j+1))
    return np.linalg.eigvalsh(B.T@D@B)[-1]

cases=0; matrices=0;trichotomy=0;limits=0
for r in range(3,15):
    for u in range(3,22):
        seq=[mu_formula(r,u,a) for a in range(1,u//2+1)]
        # mu and the negative type exponent have same monotonicity
        for s,t in zip(seq,seq[1:]):
            if u>r: assert t<s,(r,u,s,t)
            elif u<r: assert t>s,(r,u,s,t)
            else: assert abs(t-s)<Decimal('1e-55'),(r,u,s,t)
            trichotomy+=1
        for a in range(1,u//2+1):
            mu=seq[a-1]
            b=u-a;v=a*b;T=(r-1)*u+2*v;C=u+r-2
            # direct quadratic residual using decimal root
            assert abs(Decimal(r*v)*mu**2-Decimal(T)*mu+Decimal(C))<Decimal('1e-50')
            if u!=r:
                assert (mu<Decimal(2)/Decimal(r)) == (u>r)
            else: assert abs(mu-Decimal(2)/Decimal(r))<Decimal('1e-55')
            cases+=1
            if 3<=u<=12 and r<=9 and (a==1 or a==u//2):
                q=float(1/(1-mu))
                eig0=full_quadratic_maxeig(r,u,a,q)
                eiglo=full_quadratic_maxeig(r,u,a,q*0.9995)
                eighi=full_quadratic_maxeig(r,u,a,q*1.0005)
                assert abs(eig0)<5e-11,(r,u,a,'edge',eig0)
                assert eiglo< -1e-9 and eighi>1e-9,(r,u,a,eiglo,eighi)
                matrices+=1

# Exact rational balance-reversal examples, independent of floating point
examples={
    (3,4,1):Fraction(5,9),
    (3,4,2):Fraction(1,2),
    (4,4,1):Fraction(1,2),
    (4,4,2):Fraction(1,2),
    (5,4,1):Fraction(7,15),
    (5,4,2):Fraction(1,2),
}
for (r,u,a),root in examples.items():
    v=a*(u-a); T=(r-1)*u+2*v; C=u+r-2
    assert r*v*root*root-T*root+C==0
    assert abs(float(root)-float(mu_formula(r,u,a)))<1e-14
    limits+=1
print('PASS: positive-parameter exact residual tests:',cases)
print('PASS: strict/flat balancing comparisons:',trichotomy)
print('PASS: direct full-distance-matrix spectral thresholds:',matrices)
print('PASS: independent exact-rational reversal exemplars:',limits)
