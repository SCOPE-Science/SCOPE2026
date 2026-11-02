#!/usr/bin/env python3
"""Exact finite-field verification of quartic harmonic sampling rank formulas.
Uses two prime fields; theorem itself is proved algebraically in RESULT.md.
"""
from itertools import combinations
from math import comb

def rank_mod(rows, cols, p):
    # Sparse modular row reduction, exact arithmetic in F_p.
    pivots = {}
    rank = 0
    for entries in rows:
        v = {c: a % p for c, a in entries if a % p}
        while v:
            c = min(v)
            if c not in pivots:
                z = pow(v[c], -1, p)
                v = {j: (a*z) % p for j,a in v.items() if a*z % p}
                pivots[c] = v
                rank += 1
                break
            z = v[c]
            w = pivots[c]
            for j,a in w.items():
                val = (v.get(j,0) - z*a) % p
                if val:
                    v[j] = val
                elif j in v:
                    del v[j]
    return rank

def measured(n,k,p):
    pairs=list(combinations(range(n),2))
    # Harmonic even basis: 6*x_i^2*x_j^2-x_i^4-x_j^4.
    # Multiply each sampled value by k^2, removing denominators.
    def even_rows():
        for sub in combinations(range(n),k):
            S=set(sub)
            yield [(c,6*(i in S)*(j in S)-(i in S)-(j in S)) for c,(i,j) in enumerate(pairs)]
    r0=rank_mod(even_rows(),len(pairs),p)
    # Pair parity: harmonic basis x_i*x_j*(x_i^2-x_j^2) evaluates to zero.
    # Remaining n-2 basis vectors indexed by outside coordinate l:
    # x_i*x_j*(x_i^2+x_j^2-6*x_l^2).
    # Divide by nonzero common x_i*x_j/k.
    m=n-2
    def pair_rows():
        for t in combinations(range(m),k-2):
            T=set(t)
            yield [(i,2-6*(i in T)) for i in range(m)]
    r2=rank_mod(pair_rows(),m,p)
    r4=comb(n,4) if k>=4 else 0
    total=r0+comb(n,2)*r2+r4
    return (r0,r2,r4,total)

def prediction(n,k):
    h=comb(n+3,4)-comb(n+1,2)
    null=comb(n,2)
    if k==3: null+=comb(n,4)
    if n==3*k-4: null+=comb(n,2)
    if n==3*k-2: null+=1
    if n==6*k-4: null+=n-1
    return h-null,null

def run():
    cases=[(8,3),(8,4),(9,4),(10,4),(11,5),(12,4),(13,5),(14,3),(14,6),(16,6),(20,4)]
    checks=0
    for n,k in cases:
        exp,null=prediction(n,k)
        for p in (1000003,1000033):
            r0,r2,r4,total=measured(n,k,p)
            assert total==exp,(n,k,p,(r0,r2,r4,total),exp)
            checks+=1
        print(f'n={n} k={k} harmonic_nullity={null} rank={exp} blocks=(even {r0}, pair {r2}, four {r4})')
    print(f'PASS: {checks} exact modular rank checks; all observed ranks match the proved formula.')

if __name__=='__main__':run()
