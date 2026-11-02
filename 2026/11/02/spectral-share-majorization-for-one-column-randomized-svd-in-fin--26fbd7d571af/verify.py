#!/usr/bin/env python3
"""Exact finite-dimensional checks for one-column spectral-share dominance.
No external dependencies. The infinite-rank theorem is established analytically,
not by the finite tests below.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from random import Random


def verify_distribution(lam, vectors, title):
    lam = tuple(map(Q, lam))
    n = len(lam)
    assert n >= 2 and all(lam[j] >= lam[j+1] > 0 for j in range(n-1))
    assert len(vectors) > 0
    S = sum(lam)
    probs = [Q(1, len(vectors))] * len(vectors)
    pbar = [Q(0)] * n
    r = [Q(0)] * n
    captured = Q(0)
    swapped_r_diff = {(i,j):Q(0) for i in range(n) for j in range(i+1,n)}
    for x,prob in zip(vectors, probs):
        x=tuple(map(Q,x)); assert len(x)==n and all(z>0 for z in x)
        T=sum(a*b for a,b in zip(lam,x))
        captured += prob * sum(a*a*b for a,b in zip(lam,x))/T
        for i in range(n):
            pbar[i] += prob*lam[i]*x[i]/T
            r[i] += prob*x[i]/T
        for i in range(n):
            for j in range(i+1,n):
                Tswap=T+(lam[i]-lam[j])*(x[j]-x[i])
                swapped_r_diff[(i,j)]+=prob*(x[i]-x[j])**2/(T*Tswap)
    assert sum(pbar)==1, (title,'mass')
    assert all(pbar[i]>=pbar[i+1] for i in range(n-1)), (title,'ordered share')
    assert all(r[i]<=r[i+1] for i in range(n-1)), (title,'ordered r')
    for k in range(1,n):
        assert sum(pbar[:k])<=sum(lam[:k])/S,(title,'prefix',k)
    gap = sum((lam[i]*lam[j]*(lam[i]-lam[j])**2 * swapped_r_diff[(i,j)])/(2*S)
              for i in range(n) for j in range(i+1,n))
    residual=S-captured
    rademacher_residual=S-sum(a*a for a in lam)/S
    assert residual-rademacher_residual==gap,(title,'pair-sum identity',gap,residual-rademacher_residual)
    for i in range(n):
        for j in range(i+1,n):
            assert r[j]-r[i] == (lam[i]-lam[j])*swapped_r_diff[(i,j)]/2,(title,'pairwise swap',i,j)
    return len(vectors), gap, pbar, residual


def main():
    rng=Random(20261031)
    checks=0
    for n in range(2,7):
        for rep in range(16):
            spectrum=sorted((rng.randint(1,12) for _ in range(n)), reverse=True)
            vectors=list(product([Q(1,4),Q(7,4)],repeat=n))
            num,gap,_,_=verify_distribution(spectrum,vectors,f'IID n={n} rep={rep}')
            checks += num
    # Equal spectra and common random amplitude should give equality.
    for n in range(2,7):
        vv=list(product([Q(1,4),Q(7,4)],repeat=n))
        _,gap,_,_=verify_distribution([3]*n,vv,'flat spectrum')
        assert gap==0
        vv=[tuple([Q(1,4)]*n),tuple([Q(7,4)]*n)]
        _,gap,_,_=verify_distribution(list(range(n,0,-1)),vv,'common amplitude')
        assert gap==0
    # Exchangeable but dependent distribution: sampling without replacement.
    vv=sorted(set(permutations([Q(1,2),Q(1,2),Q(3,2),Q(3,2)])))
    _,gap,_,_=verify_distribution([9,4,2,1],vv,'without replacement')
    assert gap>0
    example_lam=[Q(9),Q(4),Q(1)]
    _,gap,shares,residual=verify_distribution(example_lam,list(product([Q(1,4),Q(7,4)],repeat=3)),'worked example')
    assert shares == [Q(61375257,105826105),Q(67777909,211652210),Q(21123787,211652210)]
    assert gap==Q(12082203,30236030)
    assert residual==Q(223734413,30236030)
    print(f'PASS: {checks} exact-rational iid configurations plus dependent and boundary cases')
    print('Three-mode exact shares:',[str(s) for s in shares])
    print('Exact residual excess:',gap,'approximately',float(gap))
    print('Infinite-dimensional passage uses dominated convergence and absolute pair-sum convergence in the proof.')

if __name__=='__main__':
    main()
