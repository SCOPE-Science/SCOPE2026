#!/usr/bin/env python3
"""Independent finite-dimensional numerical and combinatorial spot checks.

Requires Python 3.9+ and numpy. The mathematical inequalities for arbitrary n
are proved in RESULT.md; this finite checker is not an infinite certificate.
"""
import itertools
import math
import random
import numpy as np


def adjacency(n, edges):
    A = np.ones((2*n, 2*n), dtype=float) - np.eye(2*n)
    A[:n, n:] = 0
    A[n:, :n] = 0
    for i, j in edges:
        A[i, n+j] = A[n+j, i] = 1
    return A


def radius(n, edges):
    return float(np.linalg.eigvalsh(adjacency(n, edges))[-1])


def rho_match(n, k):
    return (n-1 + math.sqrt((n-1)**2+4*k))/2


def star_equation(n, k, lam):
    z = lam-n+1
    return ((lam+1)*z)**2-k*(z+1)*(z+k)


def rho_star(n, k):
    lo = n-1.0
    hi = n+k+2.0
    assert star_equation(n,k,lo) < 0
    assert star_equation(n,k,hi) > 0
    for _ in range(110):
        m=(lo+hi)/2
        if star_equation(n,k,m)>0:hi=m
        else:lo=m
    return (lo+hi)/2


def incidence_squares(n, edges):
    dl=[0]*n; dr=[0]*n
    for i,j in edges:dl[i]+=1;dr[j]+=1
    return sum(t*t for t in dl)+sum(t*t for t in dr)


def check_family(n, k, edge_lists):
    lower=rho_match(n,k)
    upper=rho_star(n,k)
    if k == 1: assert abs(lower-upper)<1e-10
    count=0
    for edges in edge_lists:
        lam=radius(n,edges)
        assert lower-2e-11<=lam<=upper+2e-11, (n,k,edges,lam,lower,upper)
        s2=incidence_squares(n,edges)
        assert 2*k<=s2<=k*k+k
        is_match=(len({e[0] for e in edges})==k and len({e[1] for e in edges})==k)
        is_star=(len({e[0] for e in edges})==1 or len({e[1] for e in edges})==1)
        assert (abs(lam-lower)<2e-9)==is_match, ('minimum',n,k,edges)
        assert (abs(lam-upper)<2e-9)==is_star, ('maximum',n,k,edges)
        count+=1
    return count


def run():
    tested=0
    for n in (2,3,4):
        all_edges=list(itertools.product(range(n),repeat=2))
        for k in range(1,n+1):
            tested += check_family(n,k,itertools.combinations(all_edges,k))
    rng=random.Random(20261013)
    for n in (5,7,9,12):
        all_edges=list(itertools.product(range(n),repeat=2))
        for k in range(1,n+1):
            trials=120 if n <=7 else 60
            patterns=[rng.sample(all_edges,k) for _ in range(trials)]
            patterns += [[(i,i) for i in range(k)],[(0,j) for j in range(k)]]
            tested+=check_family(n,k,patterns)
    # Large-clique critical-window limit for two nontrivial bridge densities.
    for theta in (.25,.5,1.):
        expected=theta*(theta+math.sqrt(theta*theta+4))/2
        for n in (500, 2000, 8000):
            k=int(round(theta*n))
            observed=rho_star(n,k)-(n-1)
            assert abs(observed-expected)<.04, (theta,n,observed,expected)
            dm=rho_match(n,k)-(n-1)
            assert abs(dm-theta)<.01
    print('PASS: %d spectral, equality, and degree-square configurations; 9 large-size comparisons' % tested)
    print('n=4,k=3 matching %.12f star %.12f'%(rho_match(4,3),rho_star(4,3)))

if __name__=='__main__':run()
