#!/usr/bin/env python3
"""Direct finite-sector spectral check for two particle-statistics conventions."""
import itertools, math
import numpy as np
from collections import Counter
from scipy.linalg import eigh

def make_h(N,k,fermion):
    basis=list(itertools.combinations(range(N),k))
    lookup={s:i for i,s in enumerate(basis)}
    H=np.zeros((len(basis),len(basis)),dtype=np.float64)
    for c,S in enumerate(basis):
        occupied=set(S)
        for i in S:
            for j in range(N):
                if j in occupied: continue
                T=tuple(sorted((occupied-{i})|{j}))
                s=(-1)**sum(min(i,j)<l<max(i,j) for l in S) if fermion else 1
                H[lookup[T],c]=s
    assert np.all(H==H.T)
    P=np.array([idx for idx,S in enumerate(basis) if 0 in S],dtype=int)
    return H,P

def rank_from_eigenprojections(H,P):
    eig,V=eigh(H,check_finite=False,driver='evr')
    cl=[]
    for j,x in enumerate(eig):
        if not cl or abs(x-cl[-1][-1][0])>1.e-6:cl.append([])
        cl[-1].append((x,j))
    dark=0
    for group in cl:
        Vg=V[:,[j for _,j in group]]
        if P.size:
            sv=np.linalg.svd(Vg[P,:],compute_uv=False)
            r=sum(sv>1e-7)
        else:r=0
        dark+=len(group)-r
    return dark,len(cl)

tests=0
for N in range(4,10):
    for k in range(1,N):
        M=math.comb(N,k)
        for f in (False,True):
            H,P=make_h(N,k,f)
            dark,ng=rank_from_eigenprojections(H,P)
            expected=(math.comb(N-2,k) if k<=N-2 else 0) if f else max(0,math.comb(N-1,k)-math.comb(N-1,k-1))
            assert dark==expected,(N,k,f,dark,expected,ng)
            predicted=(1-(N-k)*(N-k-1)/(N*(N-1))) if f else min(2*k/N,1)
            assert abs(1-dark/M-predicted)<1e-12
            tests+=1
print('PASS: checked',tests,'independently constructed sector Hamiltonians by spectral-projection ranks')
print('N  k  HC-capture  F-capture')
for N,k in ((4,2),(6,2),(6,3),(8,3),(8,4),(10,5)):
 print(N,k,f'{min(2*k/N,1):.8f}',f'{1-(N-k)*(N-k-1)/(N*(N-1)):.8f}')
from scipy.linalg import expm
check_dyn=0
worst=0.0
for N in (4,5,6,7):
    for k in range(1,min(N,4)):
        for f in (False,True):
            H,P=make_h(N,k,f)
            M=H.shape[0]
            dark=(math.comb(N-2,k) if k<=N-2 else 0) if f else max(0,math.comb(N-1,k)-math.comb(N-1,k-1))
            loss=np.zeros(M)
            loss[P]=1
            for kap in (0.7,2.1):
                E=expm((-1j*H-0.5*kap*np.diag(loss))*600.0)
                surv=float(np.linalg.norm(E,'fro')**2/M)
                err=abs(surv-dark/M)
                worst=max(worst,err)
                assert err < 5.e-6,(N,k,f,kap,surv,dark/M)
                check_dyn+=1
print('PASS:',check_dyn,'no-jump finite-time matrix exponentials at t=600, two rates; worst survival residual',f'{worst:.3g}')
