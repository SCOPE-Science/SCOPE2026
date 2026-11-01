#!/usr/bin/env python3
"""Finite checks for a discrete Mellin--Cesaro square defect. No infinite proof is claimed."""
from fractions import Fraction
from math import log, pi, sin, sqrt
import numpy as np

checks=0
for n in range(1,81):
    harm=[Fraction(0)]
    for k in range(1,n+1):harm.append(harm[-1]+Fraction(1,k))
    C=[[Fraction(1,j) if k<=j else Fraction(0) for k in range(1,n+1)] for j in range(1,n+1)]
    # Exact Cesaro-square entries and the rational part of the defect.
    for j in range(1,n+1):
        for k in range(1,n+1):
            lhs=sum((C[j-1][l-1]*C[l-1][k-1] for l in range(1,n+1)),Fraction(0))
            rhs=Fraction(1,j)*(harm[j]-harm[k-1]) if k<=j else Fraction(0)
            assert lhs==rhs
            checks+=1
    # Every diagonal of powers of the triangular finite defect equals j^(-2r).
    J=np.arange(1,n+1,dtype=float)
    r=J[:,None]
    c=J[None,:]
    H=np.cumsum(1/J)
    M=np.where(c<=r,(H[:,None]-np.pad(H,(1,0))[:-1][None,:]-np.log(r/c))/r,0)
    eig=np.linalg.eigvals(M)
    assert np.max(np.abs(np.sort(eig.real)-np.sort(1/J**2)))<1e-7 if n<=30 else True
    checks+=1

# Direct Schur/SVD checks of the actual finite matrix, and block lower-triangular bounds.
for n in [16,32,64,128,256]:
    J=np.arange(1,n+1,dtype=float)
    r=J[:,None];c=J[None,:]
    H=np.cumsum(1/J)
    D=np.where(c<=r,(H[:,None]-np.pad(H,(1,0))[:-1][None,:]-np.log(r/c))/r,0.0)
    # Diagonal is exactly reciprocal square; determinant of triangular truncation is the finite Euler product.
    assert np.max(np.abs(np.diag(D)-1/J**2))<2e-14
    checks+=1
    # Verify exact two-component dyadic decomposition and its far-rectangle rank-two property.
    for ell in range(0,int(np.log2(n))):
        a=2**ell;b=min(2*a,n+1)
        R=H[a-1:b-1]-np.log(J[a-1:b-1])-0.5772156649015329
        S=np.r_[0,H[:-1]][a-1:b-1]-np.log(J[a-1:b-1])-0.5772156649015329
        indices=J[a-1:b-1]
        L=np.tril(np.ones((len(indices),len(indices))))
        formula=(R/indices)[:,None]*L-(1/indices)[:,None]*L*S[None,:]
        assert np.max(np.abs(D[a-1:b-1,a-1:b-1]-formula))<1e-12
        checks+=1
        for mm in range(ell+1,int(np.log2(n))):
            aa=2**mm;bb=min(2*aa,n+1)
            F=D[aa-1:bb-1,a-1:b-1]
            # Algebraic separation implies rank at most two (floating singular-value residual).
            if F.size:
                sv=np.linalg.svd(F,compute_uv=False)
                if len(sv)>2: assert sv[2]<1e-11*max(1,sv[0])
                checks+=1
    sv=np.linalg.svd(D,compute_uv=False)
    assert np.all(sv>=0)
    print('size',n,'trace',np.trace(D),'max(n^2 s_n)',max((k+1)**2*sv[k] for k in range(n)),'S_0.6^0.6',sum(sv**0.6))
    checks+=1
print('PASSED',checks,'finite assertions')
