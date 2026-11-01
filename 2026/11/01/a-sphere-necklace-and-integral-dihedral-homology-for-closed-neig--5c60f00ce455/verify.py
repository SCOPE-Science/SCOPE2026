#!/usr/bin/env python3
"""Finite cross-checks for the Möbius-ladder closed-neighborhood theorem.

Usage: python3 verify.py. Python standard library only.
The proof for all n is combinatorial; these checks test its local identities.
"""
from collections import Counter
from itertools import combinations


def faces(facets):
    return {tuple(t) for facet in facets for k in range(1, len(facet)+1)
            for t in combinations(sorted(facet), k)}


def sign_of_reordering(seq, target):
    p = [target.index(x) for x in seq]
    return (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))


def mod2_betti(F):
    layers = {k: sorted(f for f in F if len(f) == k+1) for k in range(4)}
    ranks = {}
    for k in (1, 2, 3):
        lower = {f: j for j, f in enumerate(layers[k-1])}
        pivots = {}
        for f in layers[k]:
            bits = 0
            for j in range(len(f)):
                bits ^= 1 << lower[f[:j] + f[j+1:]]
            while bits:
                pivot = bits.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot] = bits
                    break
                bits ^= pivots[pivot]
        ranks[k] = len(pivots)
    return tuple(len(layers[k]) - ranks.get(k, 0) - ranks.get(k+1, 0)
                 - (k == 0) for k in range(4))


def check(n):
    N = 2*n
    neighbors = lambda i: {(i-1)%N, (i+1)%N, (i+n)%N}
    neighborhoods = [neighbors(i) | {i} for i in range(N)]
    F = faces(neighborhoods)
    assert Counter(len(f)-1 for f in F) == {0:2*n, 1:7*n, 2:8*n, 3:2*n}
    if n <= 16:
        assert mod2_betti(F) == (0, 1, n, 0)

    for v in range(N):
        low, high = tuple(sorted(neighbors(v))), tuple(sorted(neighborhoods[v]))
        assert high in F and low in F
        assert sum(1 for t in F if len(t) == 4 and set(low).issubset(t)) == 1
        F.remove(low)
        F.remove(high)
    for v in range(N):
        tri = tuple(sorted({(v-1)%N,v,(v+1)%N}))
        edge = tuple(sorted({(v-1)%N,(v+1)%N}))
        assert tri in F and edge in F
        assert sum(1 for t in F if len(t) == 3 and set(edge).issubset(t)) == 1
        F.remove(tri)
        F.remove(edge)

    squares = [{i,(i+1)%N,(i+n)%N,(i+n+1)%N} for i in range(n)]
    sphere_faces = [faces(combinations(sorted(sq), 3)) for sq in squares]
    assert F == set().union(*sphere_faces)
    assert Counter(len(f)-1 for f in F) == {0:2*n, 1:5*n, 2:4*n}
    for i in range(n):
        for j in range(i+1,n):
            common = sphere_faces[i] & sphere_faces[j]
            if j == i+1 or (i == 0 and j == n-1):
                rung = {(i+1)%n, (i+1)%n+n} if j == i+1 else {0,n}
                assert common == faces([rung]), (n,i,j,common)
            else:
                assert not common, (n,i,j,common)

    Fgraph = faces([{i, (i+n)%N} for i in range(n)] +
                   [{i, i+1} for i in range(n)])
    assert Counter(len(f)-1 for f in Fgraph) == {0:2*n, 1:2*n}
    for sphere in sphere_faces:
        assert Counter(len(f)-1 for f in (sphere & Fgraph)) == {0:4,1:3}

    ordered = lambda i: [i,(i+n)%N,(i+1)%N,(i+n+1)%N]
    for op in (lambda v:(v+1)%N, lambda v:(-v)%N, lambda v:(v+n)%N):
        for i in range(n):
            mapped = [op(v) for v in ordered(i)]
            j = next(j for j in range(n) if set(mapped) == squares[j])
            assert sign_of_reordering(mapped, ordered(j)) == 1
    return True


def main():
    for n in range(4, 101):
        assert check(n)
    print('ALL_VERIFY_OK: n=4..100; complete free-face removals, sphere necklace, dihedral integral orientations; mod-2 chains n<=16')

if __name__ == '__main__':
    main()
