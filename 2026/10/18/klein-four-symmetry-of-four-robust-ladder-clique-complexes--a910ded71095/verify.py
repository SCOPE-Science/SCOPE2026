#!/usr/bin/env python3
"""Exhaustive finite sanity checks for the ladder four-robust symmetry formula.
No external dependencies. The infinite-family argument is in RESULT.md.
"""
from itertools import combinations
from math import comb


def inv_orbits(n, mode):
    def transform(v):
        r, c = divmod(v, n)
        if mode in ('row', 'both'):
            r = 1-r
        if mode in ('end', 'both'):
            c = n-1-c
        return r*n+c
    unseen = set(range(2*n))
    pairs, fixed = [], []
    while unseen:
        v = min(unseen)
        w = transform(v)
        if v == w:
            fixed.append(v)
        else:
            pairs.append((v,w))
        unseen.discard(v)
        unseen.discard(w)
    return pairs, fixed


def graph_neighbors(n):
    adj = [0] * (2*n)
    for r in (0,1):
        for c in range(n):
            v = r*n+c
            adj[v] |= 1 << ((1-r)*n+c)
            for d in (c-1,c+1):
                if 0 <= d < n:
                    adj[v] |= 1 << (r*n+d)
    return adj


def no_four_independent(S, adj):
    if len(S) <= 3:
        return True
    for A in combinations(S, 4):
        if all(not (adj[u] & (1 << v)) for u,v in combinations(A,2)):
            return False
    return True


def signed_face_trace(n, mode):
    pairs, fixed = inv_orbits(n, mode)
    adj = graph_neighbors(n)
    counts = {}
    trace = 0
    for t in range(min(3,len(pairs))+1):
        for p_idx in combinations(range(len(pairs)), t):
            vpair = [v for i in p_idx for v in pairs[i]]
            for u in range(min(len(fixed),6-2*t)+1):
                for extra in combinations(fixed, u):
                    S = vpair + list(extra)
                    if no_four_independent(S, adj):
                        counts[(t,u)] = counts.get((t,u),0)+1
                        trace += (-1)**(t+u)
    return trace, counts


def gf2_betti_ladder(n):
    adj = graph_neighbors(n)
    faces = [[] for _ in range(7)]
    for k in range(1,7):
        for face in combinations(range(2*n),k):
            if no_four_independent(face, adj):
                faces[k].append(face)
    ranks = [0]*7
    for k in range(2,7):
        index = {f:i for i,f in enumerate(faces[k-1])}
        echelon = {}
        for f in faces[k]:
            col = sum((1 << index[f[:j]+f[j+1:]]) for j in range(k))
            while col:
                pivot = col.bit_length()-1
                if pivot not in echelon:
                    echelon[pivot] = col
                    break
                col ^= echelon[pivot]
        ranks[k] = len(echelon)
    # dimensions k-1 correspond to face size k.
    betti = {0:len(faces[1])-1-ranks[2]}
    for k in range(2,7):
        betti[k-1] = len(faces[k])-ranks[k]- (ranks[k+1] if k<6 else 0)
    return betti, sum(map(len,faces))


def main():
    tests = 0
    for n in range(4,37):
        N = comb(n-1,3)
        f = n//2-1 if n%2==0 else 0
        for mode, expected in [('row',-N),('end',-f),('both',f)]:
            actual, counts = signed_face_trace(n,mode)
            assert actual == expected, (n,mode, actual, expected, counts)
            tests += 1
        if n in (4,5,6,7,8):
            betti, size = gf2_betti_ladder(n)
            assert betti == {0:0,1:0,2:0,3:0,4:0,5:N}, (n, betti)
            print(f'n={n} vertices={2*n} faces={size} reduced_F2_betti={betti}; traces=(identity={N},row={-N},end={-f},both={f})')
    print(f'PASS: {tests} independent invariant-face Lefschetz checks for n=4..36')
    print('PASS: 5 independent exhaustive simplicial boundary-matrix checks for n=4..8')
    print('Note: finite checks support but do not prove the all-n statement.')

if __name__ == '__main__':
    main()
