#!/usr/bin/env python3
"""Finite diagnostics for centered graph-ball maximal averages on K_{m,n}.
The all-size theorem is proved analytically in RESULT.md; this code checks finite examples only.
"""
import itertools
import math
import numpy as np


def mode_lambda(m, n):
    tau = 1.0 + (m*n+1)/(m+1)**2
    return (tau + math.sqrt(tau*tau - 4/(m+1)**2))/2


def selector_matrix(m,n,choice):
    N=m+n
    mat=np.zeros((N,N), dtype=float)
    for i,r in enumerate(choice):
        if r==0:mat[i,i]=1.0
        if r==1:
            if i<m:
                mat[i,i]=1/(n+1)
                mat[i,m:]=1/(n+1)
            else:
                mat[i,i]=1/(m+1)
                mat[i,:m]=1/(m+1)
        if r==2:mat[i,:]=1/N
    return mat


def maxfn(m,n,f):
    f=np.abs(np.asarray(f,dtype=float))
    X=np.sum(f[:m]);Y=np.sum(f[m:]);U=(X+Y)/(m+n)
    A=np.maximum(np.maximum(f[:m],(f[:m]+Y)/(n+1)),U)
    B=np.maximum(np.maximum(f[m:],(f[m:]+X)/(m+1)),U)
    return np.r_[A,B]


def fractions(n):
    for a in range(n+1):
        for b in range(n-a+1):
            yield (a,b,n-a-b)


def quotient_norm(m,n,ac,bc):
    groups=[(side,typ,ct) for side,count in [(0,ac),(1,bc)]
            for typ,ct in enumerate(count) if ct]
    k=len(groups)
    S=np.zeros((k,k),dtype=float)
    for i,(side,typ,ct) in enumerate(groups):
        for j,(side2,typ2,ct2) in enumerate(groups):
            if typ==0:val=1.0 if i==j else 0.0
            elif typ==1:
                den=n+1 if side==0 else m+1
                val=(ct2 if side!=side2 else (1.0 if i==j else 0.0))/den
            else:val=ct2/(m+n)
            S[i,j]=val*math.sqrt(ct/ct2)
    # Perron top eigenvalue is attained on selector-class-constant vectors.
    return np.linalg.svd(S,compute_uv=False)[0]**2


def main():
    exact=0
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4)]:
        vals=[np.linalg.svd(selector_matrix(m,n,choice),compute_uv=False)[0]**2
              for choice in itertools.product((0,1,2),repeat=m+n)]
        assert abs(max(vals)-mode_lambda(m,n))<2e-11
        exact+=len(vals)
    print('ALL_BALL_SELECTOR_EXHAUSTIVE_CHECKS_OK',exact)
    compressed=0
    for m,n in [(2,10),(2,15),(3,10),(4,10),(5,8),(8,8)]:
        vmax=max(quotient_norm(m,n,ac,bc) for ac in fractions(m) for bc in fractions(n))
        assert abs(vmax-mode_lambda(m,n))<2e-11,(m,n,vmax)
        compressed+=sum(1 for _ in fractions(m))*sum(1 for _ in fractions(n))
    print('SELECTOR_CLASS_COMPRESSION_CHECKS_OK',compressed)
    witnesses=0
    for m in range(2,9):
        for n in range(m,17):
            lam=mode_lambda(m,n)
            c=m/((m+1)**2*lam-1)
            assert 0<c<1
            f=np.r_[np.ones(m),np.full(n,c)]
            T=selector_matrix(m,n,(0,)*m+(1,)*n)
            assert np.max(np.abs(maxfn(m,n,f)-T@f))<1e-12
            assert abs(np.linalg.norm(T@f)**2/np.linalg.norm(f)**2-lam)<2e-11
            witnesses+=1
    print('EXACT_MODE_WITNESS_DIAGNOSTICS_OK',witnesses)
    rng=np.random.default_rng(20261031)
    randomn=0
    for m,n in [(2,2),(2,7),(3,8),(4,5),(5,10)]:
        lam=mode_lambda(m,n)
        for k in range(500):
            f=rng.lognormal(size=m+n)
            assert np.linalg.norm(maxfn(m,n,f))**2 <= (lam+1e-9)*np.linalg.norm(f)**2
            randomn+=1
    print('NONNEGATIVE_RANDOM_INPUT_DIAGNOSTICS_OK',randomn)
    for m in [2,3,5,10]:
        for n in [100,1000,10000]:
            lam=mode_lambda(m,n)
            asym=m*n/(m+1)**2 +1+1/(m+1)**2-1/(m*n)
            assert abs(lam-asym)<5/n**2*max(1,(m+1)**3)
    print('TWO_TERM_LARGE_CLASS_ASYMPTOTIC_OK')
    print('ALL_EVENTUAL_BICLIQUE_MAXIMAL_CHECKS_OK')

if __name__=='__main__':main()
