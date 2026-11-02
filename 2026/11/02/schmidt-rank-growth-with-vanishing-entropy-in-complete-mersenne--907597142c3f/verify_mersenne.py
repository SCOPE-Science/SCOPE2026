#!/usr/bin/env python3
"""Reproducible finite-matrix and state checks for complete Mersenne-uniform hypergraph states."""
from math import comb
import numpy as np

def residue_prob(n,q):
    p=np.zeros(q,dtype=float)
    p[0]=1.0
    for _ in range(n):
        p=(p+np.roll(p,1))/2.0
    return p

def compressed_spectrum(m,b,q):
    a=residue_prob(m,q);c=residue_prob(b,q)
    F=np.ones((q,q),float)
    for r in range(q):
        F[r,q-1-r]=-1
    T=np.sqrt(a)[:,None]*F*np.sqrt(c)[None,:]
    return np.sort(np.linalg.svd(T,compute_uv=False)**2)[::-1]

def direct_spectrum(m,b,k):
    M=np.zeros((1<<m,1<<b),float)
    for i in range(1<<m):
        for j in range(1<<b):
            wt=i.bit_count()+j.bit_count()
            M[i,j]=(-1 if comb(wt,k)%2 else 1)*2**(-(m+b)/2)
    vals=np.linalg.svd(M,compute_uv=False)**2
    return np.sort(vals)[::-1]

def limit_spectrum(q):
    return np.sort(np.r_[[(1-2/q)**2],np.full(q-1,4/q**2)])[::-1]

def main():
    checks=0
    for j in (2,3,4):
        q=1<<j
        for m,b in ((q-1,q-1),(q,q+1),(q+3,q+7),(2*q+11,2*q+13)):
            vals=compressed_spectrum(m,b,q)
            assert len(vals)==q and vals[-1]>1e-14,(q,m,b,vals)
            assert abs(sum(vals)-1)<1e-10
            checks+=1
        for m,b in ((q-1,q-1),(q,q)) if q<=8 else ():
            if m+b<=14:
                actual=direct_spectrum(m,b,q-1)
                compressed=compressed_spectrum(m,b,q)
                assert np.allclose(actual[:q],compressed,rtol=1e-10,atol=1e-12)
                assert np.max(np.abs(actual[q:]))<1e-12
                checks+=1
        near=compressed_spectrum(5*q*q,5*q*q+3,q)
        target=limit_spectrum(q)
        assert np.max(abs(near-target))<1e-7,(q,near,target)
        purity=target@target
        exact=(1-2/q)**4+(q-1)*16/q**4
        assert abs(purity-exact)<1e-10
        entropy=-np.sum(target*np.log2(target))
        print('q',q,'limit_spectrum',target,'entropy_bits',entropy,'purity',purity)
        checks+=2
    print('PASS',checks,'independent spectral and rank comparisons')
if __name__=='__main__':main()
