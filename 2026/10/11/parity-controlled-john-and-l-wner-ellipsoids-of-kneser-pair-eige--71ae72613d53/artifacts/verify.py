#!/usr/bin/env python3
"""Exact finite checks for the matching-polar calculation of Kneser pair eigenpolytopes.
Finite enumeration illustrates but does not establish the general theorem.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from collections import Counter
from functools import lru_cache


def edges(n):
    return tuple(combinations(range(n), 2))


def fractional_one_factors(n):
    """Enumerate independent-edge/odd-cycle covers, each once, for modest n."""
    ed = edges(n)
    idx = {e: i for i, e in enumerate(ed)}
    @lru_cache(None)
    def covers(rem):
        if not rem:
            return (((), 0),)
        a, tail = rem[0], rem[1:]
        out = []
        for b in tail:
            nxt = tuple(v for v in tail if v != b)
            for pieces, q in covers(nxt):
                out.append((((idx[(a,b)], F(1)),) + pieces, q))
        for ell in range(3, len(rem)+1, 2):
            for other in combinations(tail, ell-1):
                remaining = tuple(v for v in tail if v not in other)
                for order in permutations(other):
                    if order > order[::-1]:
                        continue
                    cyc = (a,) + order
                    ce = tuple((idx[tuple(sorted((cyc[j],cyc[(j+1)%ell])))],F(1,2)) for j in range(ell))
                    for pieces,q in covers(remaining):
                        out.append((ce+pieces, q+ell))
        return tuple(out)
    arr = covers(tuple(range(n)))
    seen = set()
    for pieces,q in arr:
        v = tuple(sorted(pieces))
        assert v not in seen
        seen.add(v)
        yield v, q


def check(n):
    ed = edges(n); N=len(ed); d=N-n
    maxsq = F(n*(n-1)*(n-2),2) if n%2==0 else F((n-1)*(n-3)*(2*n-1),4)
    counts = Counter(); maxcnt = 0
    for factor,q in fractional_one_factors(n):
        y = [F(0)]*N
        for i,w in factor: y[i] = w
        for a in range(n):
            assert sum((y[i] for i,e in enumerate(ed) if a in e),F(0)) == 1
        assert sum(y,F(0)) == F(n,2)
        h = [1-(n-1)*u for u in y]
        assert all(sum((h[i] for i,e in enumerate(ed) if a in e),F(0))==0 for a in range(n))
        normsq = sum((x*x for x in h),F(0))
        assert normsq == F(n*(n-1)*(n-2),2)-F((n-1)**2*q,4)
        assert normsq<=maxsq
        counts[q]+=1
        if normsq==maxsq: maxcnt+=1
    expect=1
    for j in range(n-1,0,-2):expect*=j
    if n%2==0:
        assert maxcnt==expect and sum(counts.values())>=maxcnt
        assert counts[0]==expect
    else:
        import math
        m=n-4
        oddmatch=1
        for j in range(m,0,-2):oddmatch*=j
        assert maxcnt==math.comb(n,3)*oddmatch
        assert counts[3]==maxcnt
    # Exact projector diagonal and projection identity in the ambient pair-coordinate realization.
    Jinvcoeff=F(1,(n-2)*(2*n-2));
    invdiag=F(1,n-2)
    P = [[(F(i==j) - invdiag*len(set(e)&set(f)) + 4*Jinvcoeff) for j,f in enumerate(ed)] for i,e in enumerate(ed)]
    assert all(P[i][i]==F(n-3,n-1) for i in range(N))
    for i in range(N):
        for j in range(N):
            assert sum((P[i][k]*P[k][j] for k in range(N)),F(0))==P[i][j]
    assert sum((P[i][i] for i in range(N)),F(0))==d
    return dict(n=n,dimension=d,vertices=N,fractional_matching_extremes=sum(counts.values()),odd_cycle_vertex_counts=dict(sorted(counts.items())),tangent_facets=maxcnt,inradius_squared=str(1/maxsq),circumradius_squared=str(F(n-3,n-1)))

if __name__=='__main__':
    for n in range(5,9):
        print(check(n))
    print('VERIFY_OK Kneser-pair-eigenpolytope n=5..8 exact_half_integral_vertices=yes projector_idempotent=yes parity_contact_counts=yes John_Lowner_radii=yes')
