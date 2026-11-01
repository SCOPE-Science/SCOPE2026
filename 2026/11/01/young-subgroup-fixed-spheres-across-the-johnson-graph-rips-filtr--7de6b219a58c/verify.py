#!/usr/bin/env python3
"""Self-contained finite checks of Johnson-graph orbit fixed-space models.

Run: python3 verify.py
Uses only the Python standard library. These tests supplement the all-parameter
mathematical proof; they do not constitute an exhaustive infinite verification.
"""
from itertools import combinations
from collections import defaultdict


def orbit_distance_checks(max_k=6):
    cases = 0
    comparisons = 0
    for k in range(1, max_k + 1):
        by_i = defaultdict(list)
        for xs in combinations(range(2*k), k):
            mask = sum(1 << x for x in xs)
            by_i[sum(x < k for x in xs)].append(mask)
        for i in range(k + 1):
            for j in range(i, k + 1):
                if i == j:
                    vals = (k - (a & b).bit_count()
                            for ix, a in enumerate(by_i[i])
                            for b in by_i[i][ix+1:])
                else:
                    vals = (k - (a & b).bit_count()
                            for a in by_i[i] for b in by_i[j])
                maximum = max(vals, default=0)
                predicted = k - abs(i + j - k)
                assert maximum == predicted, (k, i, j, maximum, predicted)
                comparisons += 1
        for r in range(k):
            t = k - r
            valid = [i for i in range(k+1) if abs(2*i-k) >= t]
            a = (k-t)//2
            assert valid == list(range(a+1)) + list(range(k-a,k+1))
            for i in valid:
                for j in valid:
                    if i == j: continue
                    direct = k - abs(i+j-k) <= r
                    if i <= a and j <= a or i >= k-a and j >= k-a:
                        assert direct
                    else:
                        low = i if i <= a else k-i
                        high = j if j <= a else k-j
                        assert direct == (abs(low-high) >= t)
            cases += 1
    return cases, comparisons


def fold_to_matching(m, t):
    """Execute the specific two-sided graph-fold sequence, checking every move."""
    assert m >= 1 and t >= 1
    L = [('L', i) for i in range(m)]
    H = [('H', i) for i in range(m)]
    adj = {u: set() for u in L+H}
    for i in range(m):
        for j in range(m):
            if abs(i-j) < t:
                adj[L[i]].add(H[j]); adj[H[j]].add(L[i])
    deletions = 0
    for start in range(0, m, t):
        end = min(start+t, m)
        for j in range(start+1, end):
            u, v = L[start], L[j]
            assert u in adj and v in adj and u not in adj[v]
            assert adj[u] <= adj[v], (m,t,u,v,'L')
            for w in adj[v]: adj[w].remove(v)
            del adj[v]; deletions += 1
        for j in range(start+1, end):
            u, v = H[start], H[j]
            assert u in adj and v in adj and u not in adj[v]
            assert adj[u] <= adj[v], (m,t,u,v,'H')
            for w in adj[v]: adj[w].remove(v)
            del adj[v]; deletions += 1
    retained = list(range(0,m,t))
    assert set(adj) == set(L[i] for i in retained) | set(H[i] for i in retained)
    for i in retained:
        assert adj[L[i]] == {H[i]}
        assert adj[H[i]] == {L[i]}
    assert len(retained) == (m-1)//t+1
    return deletions


def f2_rank(cols):
    pivots = {}
    for x in cols:
        while x:
            lead = x.bit_length()-1
            if lead in pivots: x ^= pivots[lead]
            else:
                pivots[lead] = x
                break
    return len(pivots)


def mod2_betti(m, t):
    """Independently enumerate all independent sets in the band conflict graph."""
    n = 2*m
    bad = set()
    for i in range(m):
        for j in range(m):
            if abs(i-j) < t:
                bad.add((i,m+j))
    F = defaultdict(list)
    for mask in range(1,1<<n):
        if all(not ((mask>>i)&1 and (mask>>j)&1) for i,j in bad):
            F[mask.bit_count()-1].append(mask)
    ranks = {}
    for d in sorted(F):
        if d==0:continue
        ix = {face:i for i,face in enumerate(F[d-1])}
        columns = []
        for face in F[d]:
            col = 0
            v = face
            while v:
                one = v & -v
                v -= one
                col ^= 1 << ix[face ^ one]
            columns.append(col)
        ranks[d] = f2_rank(columns)
    b = {d:len(faces)-ranks.get(d,0)-ranks.get(d+1,0)
         for d,faces in F.items()}
    b[0] -= 1
    return {d:rank for d,rank in b.items() if rank}


def main():
    cases, comparisons = orbit_distance_checks(6)
    moves = 0
    fold_cases = 0
    for m in range(1,61):
        for t in range(1,61):
            moves += fold_to_matching(m,t)
            fold_cases += 1
    homology_cases = 0
    for k in range(1,13):
        for r in range(k):
            t = k-r
            m = r//2+1
            dimension = r//(2*t)
            got = mod2_betti(m,t)
            assert got == {dimension:1}, (k,r,got,dimension)
            homology_cases += 1
    print('PASS: exact full-orbit distance extrema:',comparisons,
          'index pairs for',cases,'radii')
    print('PASS: explicit neighborhood folds:',moves,
          'deletions across',fold_cases,'band graphs')
    print('PASS: independent mod-2 chain-rank calculations:',homology_cases,
          'fixed-space complexes')

if __name__ == '__main__':
    main()
