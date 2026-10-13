#!/usr/bin/env python3
"""Reproduce exact arithmetic absorption formulas for finite uniform spider networks.

Requires Python 3, NumPy. Each test reconstructs the Hermitian adjacency matrix
and numerically diagonalizes it independently of the number-theory formulas.
Finite tests corroborate but do not replace the analytical proof.
"""
from math import gcd, lcm, pi, sin
from itertools import combinations_with_replacement
import numpy as np


def totient(q):
    return sum(gcd(a, q) == 1 for a in range(1, q))


def ramanujan(q, s):
    return sum(np.cos(2*pi*a*s/q) for a in range(1, q) if gcd(a,q)==1)


def build(arms):
    N = 1+sum(arms)
    A = np.zeros((N,N), dtype=float)
    sites = [None]
    idx = 1
    for length in arms:
        for s in range(1,length+1):
            A[idx,0 if s==1 else idx-1] = 1.0
            A[0 if s==1 else idx-1,idx] = 1.0
            sites.append((len(sites),s))
            idx += 1
    return A


def formula(arms):
    N = 1 + sum(arms)
    n = [l+1 for l in arms]
    d=0
    for q in range(2,1+max(n)):
        k=sum(v%q==0 for v in n)
        if k>1: d+=totient(q)*(k-1)
    out = [0.0]
    for i,L in enumerate(arms):
        for s in range(1,L+1):
            z=0.0
            for q in range(2,n[i]+1):
                if n[i]%q:continue
                W=sum(1.0/v for v in n if v%q==0)
                z+=(1/(n[i]))*(1-1/n[i]/W)*(totient(q)-ramanujan(q,s))
            out.append(z)
    return d,np.array(out)


def exact_dark_projection(A):
    eig,U=np.linalg.eigh(A)
    N=len(eig)
    D=np.zeros((N,N))
    i=0
    while i<N:
        j=i+1
        while j<N and abs(eig[j]-eig[i])<1e-8:j+=1
        block=U[:,i:j]
        P=block@block.T
        v=P[:,0]
        w=P[0,0]
        if w>1e-9:P=P-np.outer(v,v)/w
        D+=P
        i=j
    return D

cases=0
states=0
for k in [3,4]:
    for arms in combinations_with_replacement(range(1,7),k):
        A=build(arms)
        d,z=formula(arms)
        P=exact_dark_projection(A)
        numeric=np.diag(P)
        assert np.max(abs(numeric-z))<3e-9,(arms,z,numeric)
        assert abs(np.trace(P)-d)<3e-9,(arms,d,np.trace(P))
        # Sum-over-sites consistency and zero-survival characterization.
        assert abs(sum(z)-d)<1e-8,(arms,d,sum(z))
        n=[L+1 for L in arms]
        idx=1
        for i,L in enumerate(arms):
            h=lcm(*(gcd(n[i],n[j]) for j in range(k) if j!=i))
            for s in range(1,L+1):
                assert (z[idx]<1e-9)==(s%h==0),(arms,i,s,h,z[idx])
                idx+=1
        cases+=1
        states+=len(z)
print(f'VERIFY_OK uniform_spider_tuples={cases} sitewise_dark_probabilities={states} rank_and_zero_sites=passed')
