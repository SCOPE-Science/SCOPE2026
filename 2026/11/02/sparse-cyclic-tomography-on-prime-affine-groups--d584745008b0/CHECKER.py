#!/usr/bin/env python3
"""Independent finite-incidence check of sparse cyclic coset tomography.

Public mathematics only; uses exact modular row reduction of 0/1 matrices.
This is a finite diagnostic, not the proof for all primes.
"""
from itertools import combinations
from math import gcd
import random

MOD=1000003

def rank_mod(A,p=MOD):
    if not A:return 0
    a=[list(map(lambda z:z%p,row)) for row in A]
    n=len(a[0]); m=len(a); rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,m) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        z=pow(a[rank][col],p-2,p)
        a[rank][col:]=[(v*z)%p for v in a[rank][col:]]
        for i in range(rank+1,m):
            if (v:=a[i][col]):
                a[i][col:]=[(u-v*w)%p for u,w in zip(a[i][col:],a[rank][col:])]
        rank+=1
        if rank==m:break
    return rank

def order_mod(r,p):
    t=1;a=r%p
    while a!=1:a=a*r%p;t+=1
    return t

def inc_matrix(p,q,r,A,include_P):
    assert order_mod(r,p)==q
    index={(x,t):t*p+x for t in range(q) for x in range(p)}
    out=[]
    if include_P:
        for t in range(q):
            row=[0]*(p*q)
            for x in range(p):row[index[x,t]]=1
            out.append(row)
    for a in A:
        for x in range(p):
            row=[0]*(p*q)
            for t in range(q):
                y=(x+a*(1-pow(r,t,p)))%p
                row[index[y,t]]=1
            out.append(row)
    return out

def expected(p,q,m,with_P):
    return (p-1)*max(q-m,0)+(0 if with_P else (q-1 if m else q))

def run():
    tests=0; small_exhaustive=0
    # Different cyclic complement orders, including composite orders.
    cases=[(3,2,2),(5,2,4),(7,3,2),(11,5,3),(13,3,3),(13,4,5),(13,6,4),(13,12,2),(19,3,7),(19,9,4)]
    rng=random.Random(1709)
    for p,q,r in cases:
        assert order_mod(r,p)==q,(p,q,r)
        choices=[]
        if p<=7:
            choices=[a for m in range(p+1) for a in combinations(range(p),m)]
            small_exhaustive+=len(choices)
        else:
            for m in sorted({0,1,2,max(0,q-1),q,min(q+1,p),p}):
                if m>p:continue
                choices.append(tuple(range(m)))
                for j in range(3):choices.append(tuple(sorted(rng.sample(range(p),m))))
        choices=list(dict.fromkeys(choices))
        for A in choices:
            for with_P in (False,True):
                R=inc_matrix(p,q,r,A,with_P)
                rank=rank_mod(R)
                nullity=p*q-rank
                predicted=expected(p,q,len(A),with_P)
                assert nullity==predicted,(p,q,r,A,with_P,nullity,predicted)
                tests+=1
        print(f'OK p={p:2} q={q:2} r={r:2}: {len(choices)} subsets (x2 flags)')
    print(f'PASS {tests} exact modular incidence-rank checks; {small_exhaustive} exhaustive small-prime subset choices.')

if __name__=='__main__':run()

def spectral_checks():
    import numpy as np
    tested=0
    for p,q,r in [(3,2,2),(5,2,4),(7,3,2),(11,5,3),(13,4,5),(13,6,4)]:
        for A in [tuple(range(q)),tuple(range(min(p,q+1))),tuple(range(max(1,q-1)))]:
            z=np.exp(2j*np.pi/p)
            R=np.asarray(inc_matrix(p,q,r,A,True),dtype=float)
            actual=np.linalg.eigvalsh(R.T@R)
            m=len(A)
            k0=np.linalg.eigvalsh(p*np.eye(q)+m*np.ones((q,q)))
            blocks=[k0]
            for k in range(1,p):
                M=np.asarray([[z**(k*a*(1-pow(r,t,p))) for t in range(q)] for a in A])
                blocks.append(np.linalg.eigvalsh(M.conj().T@M))
            predicted=np.sort(np.concatenate(blocks))
            err=np.max(np.abs(np.sort(actual)-predicted))
            assert err<2e-8,(p,q,r,A,err)
            tested+=1
    # Full affine groups: p-1 is the complement order.  Exact 3-level law.
    for p,r in [(5,2),(7,3),(11,2),(13,2)]:
        q=p-1
        assert order_mod(r,p)==q
        A=tuple(range(p-1))
        R=np.asarray(inc_matrix(p,q,r,A,True),dtype=float)
        ev=np.linalg.eigvalsh(R.T@R)
        want=np.sort(np.array([1.]*(p-1)+[float(p)]*(p*(p-2))+[float(p+(p-1)**2)]))
        assert np.max(np.abs(np.sort(ev)-want))<1e-8,(p,ev,want)
        tested+=1
    print(f'PASS {tested} full complex Fourier-block / full-affine spectral comparisons.')

if __name__=='__main__':spectral_checks()
