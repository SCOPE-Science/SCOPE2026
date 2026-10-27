#!/usr/bin/env python3
"""Reproduce the low-seat distinctive-representation boundary examples.
Only standard-library Python and exact finite integer calculations are used.
"""
from itertools import combinations, product

def props(ballots, m, k):
    n = len(ballots); q = (n+k-1)//k
    degrees = [sum(c in b for b in ballots) for c in range(m)]
    cs = tuple(combinations(range(m), k))
    good = set()
    feasible = []
    for W in cs:
        covered = {i for i,b in enumerate(ballots) if any(c in b for c in W)}
        if all(sum(c in ballots[i] for i in range(n) if i not in covered) < q
               for c in range(m)):
            good.add(W)
            if all(degrees[c] == q for c in W): feasible.append(W)
    if not feasible:
        return None
    for W in good:
        if all(degrees[c] == q for c in W): continue
        has_improving = False
        for c in W:
            for d in range(m):
                if d in W: continue
                if abs(degrees[c]-q) <= abs(degrees[d]-q): continue
                if degrees[c]*k >= n and degrees[d]*k < n: continue
                X = tuple(sorted((set(W)-{c})|{d}))
                if X in good:
                    has_improving=True
                    break
            if has_improving: break
        if not has_improving:
            return (W, feasible[0], tuple(degrees))
    return None

def run():
    count=0
    for n in range(1,5):
        for m in range(2,5):
            for ballot in product(range(1 << m), repeat=n):
                profile = tuple(frozenset(c for c in range(m) if mask>>c & 1) for mask in ballot)
                for k in (1,2):
                    assert props(profile,m,k) is None, (n,m,k,profile)
                    count += 1
    print('Low-seat small-profile instances checked:',count)
    # Smallest number of candidates possible for a three-seat trap is five.
    for n in range(1,5):
        for ballot in product(range(1<<4),repeat=n):
            profile = tuple(frozenset(c for c in range(4) if mask>>c & 1) for mask in ballot)
            assert props(profile,4,3) is None,(n,profile)
    print('Three-seat four-candidate finite profiles checked.')
    V=(frozenset((0,1)),frozenset((1,2)),frozenset((3,4)))
    m=5;k=3;q=1
    W=(1,3,4); D=(0,2,3)
    assert props(V,m,k)[0] == W
    assert all(sum(c in b for b in V)==q for c in D)
    assert all(any(c in b for c in D) for b in V)
    assert all(any(c in b for c in W) for b in V)
    assert all(sum(c in b for b in V)==q for c in D)
    print('Witness: approvals',V,'local non-DR',W,'DR',D)
    print('EXACT VERIFICATION PASSED')

if __name__=='__main__': run()
