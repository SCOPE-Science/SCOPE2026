#!/usr/bin/env python3
"""Definition-based finite checks of two-color rainbow independent domination on rook graphs.
All graph tests use the original adjacency rule, not the proof's forced-corner lemma.
Run: python3 verify.py
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, factorial


def falling(a, k):
    return factorial(a) // factorial(a-k)


def derangement(k):
    return sum((-1)**j * factorial(k) // factorial(j) for j in range(k+1))


def predicted(p, q):
    if p < q:
        s = sum((-1)**j * comb(p,j)*falling(q-j,p-j)
                for j in range(p+1))
        return {2*p: falling(q,p)*s}
    n = p
    d = {2*n-2: n*factorial(n)*(n-1)*derangement(n-2),
         2*n-1: 2*n*factorial(n)*derangement(n-1),
         2*n: factorial(n)*derangement(n)}
    return {w:c for w,c in d.items() if c}


def adj_masks(p,q):
    masks=[]
    for i in range(p):
        for j in range(q):
            masks.append(sum(1<<(a*q+b) for a in range(p)
                             for b in range(q) if (a,b)!=(i,j) and (a==i or b==j)))
    return masks


def admissible(red,blue,neighbors):
    if red & blue:
        return False
    # Exact original definition: each positive color class is independent.
    for mask in (red,blue):
        for v,N in enumerate(neighbors):
            if (mask>>v)&1 and mask & N:
                return False
    # Every zero-labeled vertex has an open neighbor of each color.
    for v,N in enumerate(neighbors):
        if not ((red|blue)>>v)&1 and (not (red&N) or not (blue&N)):
            return False
    return True


def independent_masks(p,q):
    masks=[0]
    for k in range(1,p+1):
        for rr in combinations(range(p),k):
            for cc in permutations(range(q),k):
                masks.append(sum(1<<(r*q+c) for r,c in zip(rr,cc)))
    return masks


def test_direct(p,q):
    neigh=adj_masks(p,q); counts=Counter()
    # Exhaust all ternary functions with no structural restrictions.
    for labels in product(range(3), repeat=p*q):
        r=b=0
        for v,t in enumerate(labels):
            if t==1:r|=1<<v
            if t==2:b|=1<<v
        if admissible(r,b,neigh):
            counts[(r|b).bit_count()]+=1
    want=predicted(p,q)
    assert dict(counts)==want,(p,q,dict(counts),want)
    return sum(counts.values())


def test_partial_matching(p,q):
    neigh=adj_masks(p,q); S=independent_masks(p,q); counts=Counter()
    allbits=(1<<(p*q))-1
    bad=[]
    for subset in S:
        neighbors=0
        for v,adj in enumerate(neigh):
            if (subset>>v)&1: neighbors|=adj
        bad.append(allbits & ~(subset|neighbors))
    for i,red in enumerate(S):
        for j,blue in enumerate(S):
            if red & blue: continue
            if (bad[i] & ~blue) or (bad[j] & ~red): continue
            # Check the unoptimized original definition on every actual solution.
            assert admissible(red,blue,neigh)
            counts[(red|blue).bit_count()]+=1
    want=predicted(p,q)
    assert dict(counts)==want,(p,q,dict(counts),want)
    return len(S),sum(counts.values())


def main():
    td=0
    small=[(2,q) for q in range(2,6)]+[(3,q) for q in range(3,5)]
    for p,q in small:
        c=test_direct(p,q); td+=3**(p*q)
        print('ALL_TERNARY',p,q,'valid',c)
    tp=0; valid=0
    big=[(p,q) for p in range(2,6) for q in range(p,7) if (p,q) not in small]
    for p,q in big:
        size,c=test_partial_matching(p,q); tp+=size*size;valid+=c
        print('INDEPENDENT_PAIRS',p,q,'patterns',size,'valid',c)
    print('PASS full_label_assignments_checked',td,
          'independent_pairs_checked',tp,'valid_in_independent_tests',valid)

if __name__=='__main__': main()
