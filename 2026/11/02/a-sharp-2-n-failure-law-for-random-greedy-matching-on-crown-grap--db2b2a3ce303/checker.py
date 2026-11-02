#!/usr/bin/env python3
"""Reproducibility checks for random-edge greedy matching on crown graphs.

Only the finite arithmetic tests are computational. The all-n bounds and
asymptotic conclusion follow from the proof in RESULT.md.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from math import factorial, log

assertions = 0

def check(condition, label):
    global assertions
    assert condition, label
    assertions += 1


def overlap_chain(n, exact=True, milestones=False):
    """Independent exact Markov chain for (k, overlap count)."""
    if exact:
        d = {n: Fraction(1)}
    else:
        d = {n: 1.0}
    stored = {}
    for k in range(n, 1, -1):
        if milestones and k in (n, n//2, 10, 4, 3, 2):
            stored[k] = d.copy()
        nd = {}
        for r, p in d.items():
            a = k-r
            denom = k*k-r
            check(denom > 0, ('positive rate', n,k,r))
            moves = [(r-2, r*(r-1)), (r-1, 2*r*a), (r, a*a)]
            check(sum(w for _, w in moves)==denom, ('transition sum',n,k,r))
            for nxt, weight in moves:
                if not weight:
                    continue
                check(0<=nxt<=k-1, ('transition state', n,k,r,nxt))
                q = p*Fraction(weight,denom) if exact else p*weight/denom
                nd[nxt] = nd.get(nxt,0)+q
        d = nd
        if exact:
            check(sum(d.values())==1, ('conservation',n,k))
    check(set(d).issubset({0,1}), ('last state', n))
    return d.get(1, 0), stored


def brute_mask(n):
    """Completely independent DP over unmatched vertex subsets."""
    full=(1<<n)-1
    @lru_cache(None)
    def dp(left,right):
        edges=[(i,j) for i in range(n) if left>>i&1
                         for j in range(n) if right>>j&1 if i!=j]
        if not edges:
            # A perfect matching uses all vertices; otherwise one diagonal pair remains.
            return Fraction(0 if left==0 else 1)
        return sum((dp(left^(1<<i),right^(1<<j)) for i,j in edges),Fraction(0))/len(edges)
    return dp(full,full), dp.cache_info().currsize


def brute_orders(n):
    """Enumerate all orderings of eligible edges for n=3 (6! possibilities)."""
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    failures=0
    for order in permutations(edges):
        left=set(range(n));right=set(range(n))
        for i,j in order:
            if i in left and j in right:
                left.remove(i);right.remove(j)
        failures += bool(left)
    return Fraction(failures, factorial(len(edges)))


def contraction_proof_check(k):
    # The polynomial below is the exactly factored difference of numerators
    # for the two sides of the factorial-moment contraction inequality.
    polynomial=4*k**3-11*k**2+8*k-2
    return polynomial >= 0 and Fraction((k-2)**2,k*k-2)<=Fraction((k-1)**4,k**4)


def run():
    known={2:Fraction(0),3:Fraction(1,3),4:Fraction(4,21),5:Fraction(4,21)}
    for n in range(2,11):
        p,_=overlap_chain(n)
        check(Fraction(0)<=p<=Fraction(1), ('prob',n))
        check(p<=Fraction(2,n+1), ('global inequality',n))
        check(Fraction(2,n+1)-p <= Fraction(16,n*n)*sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0)), ('finite bound',n))
        if n in known:
            check(p==known[n], ('known rational',n))
        if n<=6:
            q, states=brute_mask(n)
            check(p==q, ('independent bitmask',n,p,q,states))
    check(brute_orders(3)==Fraction(1,3), ('independent edge permutations',3))
    for k in range(2,201):
        check(contraction_proof_check(k), ('contraction inequality',k))
    for n in (30,100,500,2000):
        p,_=overlap_chain(n,exact=False)
        check(p>0 and n*p<2, ('positive finite approximation',n))
        print(f'n={n}: failure={p:.12g}; n*failure={n*p:.12g}')
    print(f'PASS {assertions} deterministic checks (exact arithmetic and numerical diagnostics)')

if __name__=='__main__':
    run()
