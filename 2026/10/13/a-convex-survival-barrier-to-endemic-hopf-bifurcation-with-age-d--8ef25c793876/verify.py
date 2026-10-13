#!/usr/bin/env python3
"""Reproducible finite checks for a convex-survival endemic spectral theorem.
The infinite-dimensional assertion is established by the proof, not these checks.
"""
import itertools
from fractions import Fraction as Q
import numpy as np

def hyperexp_jac(weights,rates,kappa,beta0):
    """Exact rational Jacobian of finite hyperexponential renewal reduction."""
    n = len(weights)
    assert len(rates)==n and sum(weights)==1
    mean=sum((w/r for w,r in zip(weights,rates)),Q(0))
    r0=beta0*sum((w/(r+kappa) for w,r in zip(weights,rates)),Q(0))
    assert r0>1
    bstar=(1-Q(1)/r0)/mean
    c=bstar*r0
    d=beta0/r0
    j=[[Q(0) for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n):
        for k in range(n):
            j[i][k]=-weights[i]*c
            j[n+i][k]=-weights[i]*c
            j[i][n+k]=weights[i]*d
            j[n+i][n+k]=weights[i]*d
        j[i][i]-=rates[i]
        j[n+i][n+i]-=rates[i]+kappa
    return j,r0,bstar

cases=0
min_gap=float('inf')
for n in (1,2,3,4):
    samples={
        1:[(Q(1),)],
        2:[(Q(1,2),Q(1,2)),(Q(1,3),Q(2,3))],
        3:[(Q(1,3),)*3,(Q(1,2),Q(1,3),Q(1,6))],
        4:[(Q(1,4),)*4,(Q(1,2),Q(1,4),Q(1,6),Q(1,12))],
    }[n]
    for weights in samples:
        for rates in (tuple(Q(i) for i in range(1,n+1)),
                      tuple(Q(1,3)+Q(2*i,3) for i in range(n))):
            for kap in (Q(0),Q(1,3),Q(2)):
                first=sum((w/(r+kap) for w,r in zip(weights,rates)),Q(0))
                for fac in (Q(6,5),Q(2),Q(8)):
                    beta0=fac/first
                    mat,r0,bstar=hyperexp_jac(weights,rates,kap,beta0)
                    assert all(isinstance(x,Q) for row in mat for x in row)
                    eig=np.linalg.eigvals(np.asarray(mat,dtype=float))
                    realmax=max(z.real for z in eig)
                    assert realmax < -1e-8,(weights,rates,kap,fac,realmax)
                    min_gap=min(min_gap,-realmax)
                    cases+=1

# Closed-form uniform-duration cosine transform: (1-cos(omega*T))/(T*omega^2).
# Its sign follows from the elementary nonnegativity of 1-cos(theta).
from math import cos
for T in (Q(1,3),Q(1),Q(3)):
    for om in (Q(1,5),Q(1),Q(5),Q(20)):
        val=(1-cos(float(om*T)))/(float(T)*float(om*om))
        assert val>=-1e-14

# For gamma shape 0<j<=1, d(log K)/da=(j-1)/a-rate is strictly negative.
for shape in (Q(1,5),Q(1,2),Q(1)):
    for age in (Q(1,10),Q(1),Q(10)):
        for rate in (Q(1,3),Q(3)):
            assert (shape-1)/age-rate<0

print('VERIFY_OK',cases,'exact-rational hyperexponential Jacobians with negative eigenvalues;',
      'uniform and gamma sign guards; smallest sampled spectral gap:',round(min_gap,7))
