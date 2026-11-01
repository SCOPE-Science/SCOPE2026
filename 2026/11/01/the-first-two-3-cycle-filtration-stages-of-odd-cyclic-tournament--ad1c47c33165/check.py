#!/usr/bin/env python3
"""Standalone finite checks for the first two 3-cycle filtration stages.
Uses only the Python standard library. It does not replace the all-order proof.
"""
from itertools import combinations
from math import comb


def rank_mod_two(columns):
    pivots = {}
    for column in columns:
        v = column
        while v:
            top = v.bit_length() - 1
            if top in pivots:
                v ^= pivots[top]
            else:
                pivots[top] = v
                break
    return len(pivots)


def oriented_cycle(u, v, w, n):
    """Whether the three clockwise cyclic gaps are at most (n-1)//2."""
    a, b, c = sorted((u, v, w))
    k = (n - 1) // 2
    return b - a <= k and c - b <= k and n - c + a <= k


def bounded_faces(n, threshold):
    triangles = [q for q in combinations(range(n), 3) if oriented_cycle(*q, n)]
    families = {}
    for size in range(1, n + 1):
        families[size - 1] = [q for q in combinations(range(n), size)
                              if sum(set(t).issubset(q) for t in triangles) <= threshold]
        if not families[size - 1]:
            del families[size - 1]
            break
    return families, triangles


def betti_mod_two(faces):
    max_dim = max(faces)
    ranks = {}
    for d in range(1, max_dim + 1):
        indices = {q: i for i, q in enumerate(faces[d - 1])}
        columns = []
        for s in faces[d]:
            columns.append(sum(1 << indices[f] for f in combinations(s, d)))
        ranks[d] = rank_mod_two(columns)
    return tuple(len(faces[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
                 for d in range(max_dim + 1))


def edge_short_step(u, v, n):
    d = (v-u) % n
    return d if d <= (n-1)//2 else d-n


def run():
    for n in (3, 5, 7, 9, 11):
        k = (n - 1)//2
        f0, triangles = bounded_faces(n, 0)
        f1, _ = bounded_faces(n, 1)
        f2, _ = bounded_faces(n, 2)
        c = n*(n*n-1)//24
        assert len(triangles) == c
        assert c == comb(n, 3) - n*comb(k, 2)
        assert f0[0] == f1[0] == f2[0]
        for j in range(3, n):
            assert f1.get(j, []) == f0.get(j, []), (n, j)
        assert len(f1.get(2, [])) - len(f0.get(2, [])) == c
        for tri in triangles:
            a, b, cc = tri
            assert (edge_short_step(a, b, n) + edge_short_step(b, cc, n)
                    + edge_short_step(cc, a, n)) == n
        if n >= 5:
            assert len(f2[3]) == comb(n,4)
        b0, b1, b2 = betti_mod_two(f0), betti_mod_two(f1), betti_mod_two(f2)
        assert b0[0] == 1 and b0[1] == 1 and all(v == 0 for v in b0[2:])
        assert b1[0] == 1 and b1[1] == 0
        assert (b1[2] if len(b1) >= 3 else 0) == c-1
        assert b2[0] == 1 and b2[1] == 0
        if len(b2)>2:
            assert b2[2] == 0
        print(f'n={n:2d} cycle_triples={c:3d} '
              f'beta(F0)={b0} beta(F1)={b1} beta(F2)={b2}')
    print('CYCLIC_TOURNAMENT_FIRST_TWO_DIRECTIONALITY_STAGES_OK')


if __name__ == '__main__':
    run()
