#!/usr/bin/env python3
"""Finite-dimensional spectral checks for absorbing Hamming-one shells."""
from math import comb
import numpy as np
from scipy.linalg import eigh

def expected(n,d):
    q=(1+(n-1)*(0<d<n))/comb(n,d)
    if n%2==0 and d%2==0:
        q -= (comb(n,n//2)/2**n)*(comb(n//2,d//2)/comb(n,d))**2
    return q

def full_rank_and_probs(n, detectors):
    N=1<<n; H=np.zeros((N,N),dtype=float)
    for x in range(N):
        for i in range(n): H[x,x^(1<<i)]=1
    lam,U=eigh(H)
    B=np.zeros((N,N));rank=0
    for k in range(n+1):
        ind=np.flatnonzero(abs(lam-(n-2*k))<1e-8)
        Z=U[np.ix_(detectors,ind)]
        _,s,vt=np.linalg.svd(Z,full_matrices=True)
        r=np.count_nonzero(s>1e-8)
        rank+=r
        B+= U[:,ind]@vt[:r].T@vt[:r]@U[:,ind].T
    return rank,np.diag(B)

if __name__=='__main__':
    tested=0
    for n in range(2,8):
        S=[1<<i for i in range(n)]
        rank,probs=full_rank_and_probs(n,S)
        R=n*n-n+2-(n%2==0)
        assert rank==R,(n,rank,R)
        for x,p in enumerate(probs):
            d=x.bit_count()
            assert abs(p-expected(n,d))<5e-9,(n,x,p,expected(n,d))
            tested+=1
        if n<=6:
            rank0,_=full_rank_and_probs(n,S+[0])
            assert rank0==R+(n%2==0),(n,rank0)
            opposite=[((1<<n)-1)^(1<<i) for i in range(n)]
            rankopp,_=full_rank_and_probs(n,S+opposite)
            assert rankopp==R,(n,rankopp)
        print('n',n,'rank',rank,'pred',R,'Pcenter',round(probs[0],9),'P_d2',round(probs[3],9),flush=True)
    print(f'VERIFY_OK_shell_probabilities={tested}_dimensions=6_auxiliary=10')
