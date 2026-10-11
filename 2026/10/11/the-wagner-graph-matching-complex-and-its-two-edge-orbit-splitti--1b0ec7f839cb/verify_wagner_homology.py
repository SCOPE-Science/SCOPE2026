#!/usr/bin/env python3
"""Independent exact simplicial-chain enumeration and finite-field rank checks.
Constructs the Möbius ladder by vertex distance rather than the other verifier's
bitmask face generator; tests all five graph cases. Standard library only.
"""
from collections import Counter
from itertools import combinations

V = range(8)
E = tuple((a, b) for a, b in combinations(V, 2)
          if (b - a) % 8 in (1, 4, 7))
assert len(E) == 12

def build_cases():
    for name, forbidden_edges, forbidden_vertices in (
        ('whole', (), ()),
        ('cycle_delete', ((0, 1),), ()),
        ('cycle_link', (), (0, 1)),
        ('rung_delete', ((0, 4),), ()),
        ('rung_link', (), (0, 4)),
    ):
        yield name, [e for e in E if e not in forbidden_edges and
                     all(v not in forbidden_vertices for v in e)]

def simplices(edges):
    result = {}
    for k in range(1, min(4, len(edges)) + 1):
        faces = [c for c in combinations(range(len(edges)), k)
                 if len(set(v for j in c for v in edges[j])) == 2 * k]
        if faces:
            result[k - 1] = faces
    return result

def column_rank(columns, p):
    pivots = {}
    for vector in columns:
        c = dict(vector)
        while c:
            row = min(c)
            a = c[row] % p
            if not a:
                del c[row]
                continue
            if row not in pivots:
                ai = pow(a, -1, p)
                pivots[row] = {r: v * ai % p for r, v in c.items() if v % p}
                break
            b = pivots[row]
            for r, v in b.items():
                c[r] = (c.get(r, 0) - a * v) % p
                if not c[r]:
                    del c[r]
    return len(pivots)

def boundary_ranks(faces, prime):
    maps = {d: {f: i for i, f in enumerate(faces[d])} for d in faces}
    rank = {}
    for d in faces:
        if d == 0:
            rank[d] = 0
            continue
        columns = []
        for face in faces[d]:
            col = {}
            for i in range(d + 1):
                row_face = face[:i] + face[i + 1:]
                col[maps[d - 1][row_face]] = (1 if i % 2 == 0 else -1) % prime
            columns.append(col)
        rank[d] = column_rank(columns, prime)
    return rank

EXPECTED = {
    'whole': ((12, 42, 44, 7), {2: 6}),
    'cycle_delete': ((11, 35, 33, 5), {2: 3}),
    'cycle_link': ((7, 11, 2), {1: 3}),
    'rung_delete': ((11, 35, 33, 4), {2: 4}),
    'rung_link': ((7, 11, 3), {1: 2}),
}

if __name__ == '__main__':
    for name, edges in build_cases():
        f = simplices(edges)
        fvec = tuple(len(f[d]) for d in sorted(f))
        assert fvec == EXPECTED[name][0], (name, fvec)
        for prime in (2, 3, 5, 101):
            ranks = boundary_ranks(f, prime)
            # Non-augmented first boundary vanishes, so beta_0 is reduced by one.
            betti = {d: len(f[d]) - ranks[d] - ranks.get(d + 1, 0)
                     - (d == 0) for d in f}
            assert {d: b for d, b in betti.items() if b} == EXPECTED[name][1], \
                (name, prime, betti)
        print(name, 'f_vector=', fvec, 'reduced_betti=', EXPECTED[name][1],
              'checked_characteristics=(2,3,5,101)')
    print('VERIFY_OK: independent all-simplex chain computations')
