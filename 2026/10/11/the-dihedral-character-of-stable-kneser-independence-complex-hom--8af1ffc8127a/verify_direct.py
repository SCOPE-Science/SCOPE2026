#!/usr/bin/env python3
"""Exact simplex-level character check for Schrijver independence complexes.

No external dependencies. Exhaustively examines every simplex and every
rotation/reflection for polygon sizes 8 through 12. This corroborates,
but does not replace, the general proof.
"""
from itertools import combinations


def sign_of_perm(perm):
    inversions = sum(a > b for i, a in enumerate(perm) for b in perm[i + 1:])
    return -1 if inversions % 2 else 1


def predicted(m, typ, j):
    if typ == 'rotation':
        if j == 0:
            return (m**3 - 12*m*m + 35*m - 6)//6
        if m % 2 == 0 and j == m//2:
            return m//2 - 1
        if m % 3 == 0 and j in (m//3, 2*m//3):
            return m//3 - 1
        return -1
    if m % 2:
        return 1
    return 3 - m//2 if j % 2 == 0 else m//2 - 3


def run(m):
    chords = tuple((a, b) for a, b in combinations(range(m), 2)
                   if b-a not in (1, m-1))
    loc = {pair: i for i, pair in enumerate(chords)}
    simplices = set()
    for v in range(m):
        wheel = [i for i, edge in enumerate(chords) if v in edge]
        for size in range(1, len(wheel)+1):
            simplices.update(combinations(wheel, size))
    for triple in combinations(range(m), 3):
        edges = [tuple(sorted(edge)) for edge in combinations(triple, 2)]
        if all(e in loc for e in edges):
            simplices.add(tuple(sorted(loc[e] for e in edges)))

    def trace(typ, j):
        if typ == 'rotation':
            f = lambda x: (x+j) % m
        else:
            f = lambda x: (j-x) % m
        p = [loc[tuple(sorted((f(a), f(b))))] for a, b in chords]
        out = -1  # reduced Lefschetz number: subtract H_0 of connected K
        for face in simplices:
            image = [p[i] for i in face]
            if set(image) == set(face):
                inverse_order = {x: i for i, x in enumerate(face)}
                orientation = sign_of_perm([inverse_order[i] for i in image])
                out += (-1)**(len(face)-1) * orientation
        return out

    for typ in ('rotation', 'reflection'):
        for j in range(m):
            got = trace(typ, j)
            expected = predicted(m, typ, j)
            assert got == expected, (m, typ, j, got, expected)
    b = predicted(m, 'rotation', 0)
    print('m=%d vertices=%d nonempty_simplices=%d H2_dim=%d checked=%d'
          % (m, len(chords), len(simplices), b, 2*m))


if __name__ == '__main__':
    for size in range(8, 13):
        run(size)
    print('DIRECT SIMPLEX TRACE CHECKS PASS')
