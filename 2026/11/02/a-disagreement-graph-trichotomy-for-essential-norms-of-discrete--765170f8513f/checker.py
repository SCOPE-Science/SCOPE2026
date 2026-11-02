#!/usr/bin/env python3
"""Exact finite tests for two-symbol weighted composition differences.

Finite tests assess row-tail identities and graph-cover mechanics, not an
infinite-dimensional compactness claim. Only the Python standard library is used.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from random import Random


def weighted_row(phi, psi, mu, nu, v, retained):
    """Conjugated matrix row of (C_phi-C_psi)(I-P_F)."""
    row = {}
    for w,sgn in ((phi[v],1), (psi[v],-1)):
        if w not in retained:
            row[w] = row.get(w,Q(0)) + sgn*nu[v]/mu[w]
    return {w:a for w,a in row.items() if a}


def signed_max(row, n):
    """Brute-force real infinity-to-infinity row norm."""
    return max((abs(sum(a*s[w] for w,a in row.items()))
                for s in product((-1,1), repeat=n)), default=Q(0))


def row_tail_formula(phi,psi,mu,nu,F):
    return max((sum(map(abs,weighted_row(phi,psi,mu,nu,v,F).values()))
                for v in range(len(phi))), default=Q(0))


def direct_sign_formula(phi,psi,mu,nu,F):
    n=len(phi)
    return max((max(abs(sum(a*s[w] for w,a in weighted_row(phi,psi,mu,nu,v,F).items()))
                    for v in range(n))
                for s in product((-1,1),repeat=n)),default=Q(0))


def greedy_matching_cover(edges):
    matching=[]
    endpoints=set()
    for a,b in edges:
        if a not in endpoints and b not in endpoints:
            matching.append((a,b));endpoints.update((a,b))
    return matching,endpoints


def main():
    checks=0
    rng=Random(2307)
    for n in range(2,8):
        for _ in range(24):
            phi=[rng.randrange(n) for _ in range(n)]
            psi=[rng.randrange(n) for _ in range(n)]
            mu=[Q(rng.randrange(1,8), rng.randrange(1,8)) for _ in range(n)]
            nu=[Q(rng.randrange(1,8), rng.randrange(1,8)) for _ in range(n)]
            for _ in range(5):
                F={j for j in range(n) if rng.randrange(2)}
                x=row_tail_formula(phi,psi,mu,nu,F)
                y=direct_sign_formula(phi,psi,mu,nu,F)
                assert x==y,(n,phi,psi,F,x,y)
                checks+=1
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            E=[e for i,e in enumerate(pairs) if mask>>i&1]
            matching,F=greedy_matching_cover(E)
            assert all(a in F or b in F for a,b in E)
            assert all(set(e).isdisjoint(set(f)) for i,e in enumerate(matching)
                       for f in matching[i+1:])
            checks+=1
    # Infinite-example finite-prefix analogues: any fixed hub set covers
    # arbitrarily many distinct star edges, while matching edges escape it.
    for n in range(2,41):
        star=[(0,j) for j in range(1,n+1)]
        matching=[(2*j,2*j+1) for j in range(n)]
        assert all(a==0 or b==0 for a,b in star)
        assert all(set(e).isdisjoint(set(f)) for i,e in enumerate(matching)
                   for f in matching[i+1:])
        checks+=1
    print(f'PASS: {checks} exact finite checks; no infinite conclusion inferred from enumeration')

if __name__=='__main__': main()
