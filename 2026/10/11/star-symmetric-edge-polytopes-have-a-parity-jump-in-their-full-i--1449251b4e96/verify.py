#!/usr/bin/env python3
"""Finite reproducibility checks for the star symmetric-edge Euclidean ball formulas."""
import itertools
import math
import numpy as np
from scipy.optimize import linprog

for m in range(1,12):
    n=m+1
    facets=[]
    for eps in itertools.product((-1,1),repeat=m):
        S=sum(eps)
        f=np.array([S/n]+[S/n-t for t in eps],dtype=float)
        assert abs(sum(f))<1e-10
        assert all(abs(f[0]-f[i+1]-eps[i])<1e-10 for i in range(m))
        norm2=float(np.dot(f,f))
        assert abs(norm2-(m-S*S/n))<1e-10
        facets.append((eps,S,f,norm2))
    delta=m%2
    M2=m-delta/n
    radius=1/math.sqrt(M2)
    extremal=[(eps,S,f) for eps,S,f,norm2 in facets if abs(norm2-M2)<1e-9]
    expected=(math.comb(m,m//2) if m%2==0 else 2*math.comb(m,(m-1)//2))
    assert len(extremal)==expected
    # Each normal is intrinsically zero-sum, so dropping its central coordinate
    # preserves the rank of its span inside the zero-sum hyperplane.
    rank=np.linalg.matrix_rank(np.array([f[1:] for eps,S,f in extremal]),tol=1e-9)
    assert rank==(m-1 if m%2==0 else m)
    if m%2==0:
        ustar=(1-math.sqrt(1-4/(m*n)))/2
        trial=(-ustar,0.,ustar)
    else:
        ustar=0.
        trial=(0.,)
    for u in trial:
        center=np.r_[-m*u,np.full(m,u)]
        assert all(np.dot(f,center)+radius*math.sqrt(norm2)<=1+1e-10
                   for eps,S,f,norm2 in facets)
    # Full inradius LP, with arbitrary center in R^(m+1) subject to sum(c)=0.
    A=np.array([np.r_[f,math.sqrt(norm2)] for eps,S,f,norm2 in facets])
    obj=np.r_[np.zeros(n),-1.]
    res=linprog(obj,A_ub=A,b_ub=np.ones(len(facets)),
                A_eq=np.array([np.r_[np.ones(n),0.]]),b_eq=[0.],
                bounds=[(None,None)]*(n+1),method='highs')
    assert res.success
    assert abs(res.x[-1]-radius)<1e-8
    # All maximum-radius feasible centers, not merely the symmetric candidate.
    Ac=np.array([f for eps,S,f,norm2 in facets])
    bc=np.array([1-radius*math.sqrt(norm2) for eps,S,f,norm2 in facets])
    leafmean=np.r_[0.,np.full(m,1/m)]
    eq=np.ones((1,n))
    resmax=linprog(-leafmean,A_ub=Ac,b_ub=bc,A_eq=eq,b_eq=[0.],
                   bounds=[(None,None)]*n,method='highs')
    resmin=linprog(leafmean,A_ub=Ac,b_ub=bc,A_eq=eq,b_eq=[0.],
                   bounds=[(None,None)]*n,method='highs')
    assert resmax.success and resmin.success
    assert abs(-resmax.fun-ustar)<1e-7
    assert abs(resmin.fun+ustar)<1e-7
    if m%2==0:
        for u in (-ustar,ustar):
            c=np.r_[-m*u,np.full(m,u)]
            contacts=[(eps,S) for eps,S,f,norm2 in facets
                      if abs(np.dot(f,c)+radius*math.sqrt(norm2)-1)<1e-8]
            assert len(contacts)==math.comb(m,m//2)+math.comb(m,m//2-1)
    # Each outer vertex +/- (e_0-e_i) has squared norm exactly two.
    for i in range(1,n):
        v=np.zeros(n);v[0]=1;v[i]=-1
        assert abs(v@v-2.)<1e-12
print('VERIFY_OK star-incenter m=1..11 all_facets=yes full_LP=yes parity_rank=yes segment_contacts=yes outer_sphere=yes')
