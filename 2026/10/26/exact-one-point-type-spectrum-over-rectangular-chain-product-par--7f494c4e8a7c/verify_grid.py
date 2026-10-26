#!/usr/bin/env python3
"""Independent finite checks for one-point extension spectra of rectangular posets.

Only Python standard library is required. The exhaustive checks do not prove
formulas for arbitrary dimensions; the written combinatorial proof does.
"""
from itertools import product
from math import comb


def formula(a, b):
    n = a + b
    return (n + 3) * comb(n, a) - comb(n + 1, a) - comb(n + 1, b)


def nonalgebraic_formula(a, b):
    return formula(a, b) - a * b


def summation(a, b):
    if not a or not b:
        return 1
    ans = comb(a + b, a)
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            ans += comb(i + j - 2, i - 1) * comb(a + b - i - j + 2, a - i + 1) - 1
    return ans


def points(a, b):
    return [(i, j) for i in range(1, a + 1) for j in range(1, b + 1)]


def bitset_count(a, b):
    """Independently enumerate all lower and upper subsets and test strict cross-order."""
    V = points(a, b)
    n = len(V)
    less = [(p, q) for p in range(n) for q in range(n)
            if p != q and V[p][0] <= V[q][0] and V[p][1] <= V[q][1]]
    low, high = [], []
    for mask in range(1 << n):
        if all(not(mask >> q & 1) or (mask >> p & 1) for p,q in less):
            low.append(mask)
        if all(not(mask >> p & 1) or (mask >> q & 1) for p,q in less):
            high.append(mask)
    rankle = [(p,q) for p,q in less]
    total=0
    for L in low:
        for U in high:
            if L & U: continue
            if all(not(L >> p & 1) or not(U >> q & 1) or (p,q) in rankle
                   for p in range(n) for q in range(n)):
                total+=1
    return total


def transitive_extension_count(a, b):
    """Directly test transitivity on every ternary extension; no ideal/filter theorem."""
    V=points(a,b)
    n=len(V)
    ordered_pairs=[(i,j) for i in range(n) for j in range(n) if i!=j
                    and V[i][0]<=V[j][0] and V[i][1]<=V[j][1]]
    ans=0
    for states in product((-1,0,1), repeat=n):
        # Build a strict relation on P union {x}, with x index n.
        edges=set(ordered_pairs)
        edges.update((i,n) for i,s in enumerate(states) if s==-1)
        edges.update((n,i) for i,s in enumerate(states) if s==1)
        if any(i==j for i,j in edges): continue
        # A strict finite poset must have transitive relation, with no new edges implied.
        if any((i,k) not in edges for i,j in edges for j2,k in edges if j==j2):
            continue
        ans+=1
    return ans


def main():
    s=0
    for a in range(0,17):
        for b in range(0,17):
            assert formula(a,b)-a*b == summation(a,b), (a,b)
            s+=1
    print('BINOMIAL_SUM_CHECK',s)
    cases1=[(a,b) for a in range(5) for b in range(5)] + [(2,5),(5,2),(3,4),(4,3)]
    for a,b in cases1:
        v=bitset_count(a,b)
        assert v==nonalgebraic_formula(a,b),(a,b,v,nonalgebraic_formula(a,b))
    print('INDEPENDENT_IDEAL_FILTER_CHECK',len(cases1))
    cases2=[(a,b) for a in range(5) for b in range(5) if a*b<=8]+[(3,3),(1,9),(9,1)]
    for a,b in cases2:
        v=transitive_extension_count(a,b)
        assert v==nonalgebraic_formula(a,b),(a,b,v,nonalgebraic_formula(a,b))
    print('DIRECT_TRANSITIVITY_CHECK',len(cases2))
    print('SQUARE_TOTALS',[(n,formula(n,n)) for n in range(1,9)])
    print('SQUARE_NONALGEBRAIC',[(n,nonalgebraic_formula(n,n)) for n in range(1,9)])
    print('ALL_TESTS_PASS')

if __name__=='__main__':main()
