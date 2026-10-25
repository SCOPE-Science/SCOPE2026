#!/usr/bin/env python3
"""Reproducible independent finite checks for fixed-parameter GADI identities."""
import math
import numpy as np

def check(F,C,alpha,omega,steps):
    n=F.shape[0]
    I=np.eye(n)
    H=np.linalg.inv(alpha*I+F)
    T=2*alpha*H.T-I
    c=omega/2
    b=1-c
    E=np.sqrt(2*alpha*b)*H.T@C.T
    Q=C.T@C
    X=np.zeros((n,n))
    prev=[]
    for k in range(1,steps+1):
        half=np.linalg.solve(alpha*I+F.T, X@(alpha*I-F)+Q)
        dense=(X@(F-(1-omega)*alpha*I)+(2-omega)*alpha*half)@H
        convex=c*X+b*T@X@T.T+E@E.T
        assert np.allclose(dense,convex,atol=2e-11,rtol=2e-10)
        w=[b**j*sum(math.comb(r,j)*c**(r-j) for r in range(j,k)) for j in range(k)]
        if k>1:
            rec=[1+c*prev[0]] + [c*prev[j]+b*prev[j-1] for j in range(1,k-1)] + [b*prev[-1]]
            assert np.allclose(w,rec,atol=1e-13,rtol=1e-13)
        else: assert w==[1]
        prev=w
        blocks=[np.sqrt(w[j])*np.linalg.matrix_power(T,j)@E for j in range(k)]
        Z=np.column_stack(blocks)
        assert np.allclose(dense,Z@Z.T,atol=2e-10,rtol=2e-10), (omega,k,np.max(np.abs(dense-Z@Z.T)))
        assert np.allclose(dense,dense.T,atol=2e-11)
        assert np.linalg.eigvalsh((dense+dense.T)/2).min()>=-2e-10
        assert Z.shape[1]==k*C.shape[0]
        X=dense

rng=np.random.default_rng(20261020)
count=0
for n in [3,5,8]:
    for p in [1,2]:
        for omega in [0.,0.1,0.6,1.25,1.9]:
            for alpha in [.5,1.5]:
                A=rng.standard_normal((n,n))
                F=A.T@A+0.3*np.eye(n)+0.12*rng.standard_normal((n,n))
                C=rng.standard_normal((p,n))
                check(F,C,alpha,omega,4)
                count+=1
for k in range(1,7):
    n=8;F=np.diag(np.arange(1,n+1,dtype=float));C=np.ones((1,n));a=.7
    H=np.linalg.inv(a*np.eye(n)+F);T=2*a*H.T-np.eye(n);E=H.T@C.T
    Z=np.column_stack([np.linalg.matrix_power(T,j)@E for j in range(k)])
    assert np.linalg.matrix_rank(Z,tol=1e-11)==k,(k,np.linalg.svd(Z)[1])
    count+=1
print('VERIFY_OK tests',count)
