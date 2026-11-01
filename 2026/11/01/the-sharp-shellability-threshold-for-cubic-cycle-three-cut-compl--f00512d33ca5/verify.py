"""Standalone exhaustive finite certificates for cubic-cycle three-cut complexes.

Python 3 standard library only. Run from the directory containing the two CSVs.
The published general theorem, rather than this finite computation, covers n>=15.
"""
from itertools import combinations
from pathlib import Path
from collections import defaultdict


def disconnected_triple(n, triple):
    # Direct breadth-first search in the induced graph C_n^3[triple].
    nodes = set(triple)
    reached = {triple[0]}
    frontier = [triple[0]]
    while frontier:
        u = frontier.pop()
        for v in nodes - reached:
            if min((u-v) % n, (v-u) % n) <= 3:
                reached.add(v)
                frontier.append(v)
    return len(reached) != 3


def cut_triples(n):
    return {t for t in combinations(range(n), 3) if disconnected_triple(n, t)}


def bits(t):
    return sum(1 << x for x in t)


def shell_order(n):
    path = Path(__file__).with_name(f"shelling_{n}.csv")
    rows = path.read_text(encoding="utf-8").splitlines()
    assert rows and all(row and not row.startswith('#') for row in rows)
    order = [tuple(int(x) for x in row.split(',')) for row in rows]
    assert all(len(t) == 3 and tuple(sorted(t)) == t and len(set(t)) == 3
               and all(0 <= v < n for v in t) for t in order)
    assert len(order) == len(set(order))
    assert set(order) == cut_triples(n)  # complete facet census
    return order


def all_submasks(mask):
    sub = mask
    while sub:
        yield sub
        sub = (sub - 1) & mask


def verify_shelling(n, expected_spanning):
    order = shell_order(n)
    old_triples = []
    old_faces = set()
    fullmask = (1 << n) - 1
    spanning = []
    for j, t in enumerate(order):
        removed = set(t)
        facet = fullmask ^ bits(t)
        # Independent definition-level test: the intersection with the earlier
        # subcomplex must be pure of codimension one. Its maximal faces are
        # covered by the previously present codimension-one faces of facet.
        common = [s for s in all_submasks(facet) if s in old_faces]
        ridges = [facet ^ (1 << v) for v in range(n)
                  if (facet >> v) & 1 and facet ^ (1 << v) in old_faces]
        if j:
            assert ridges, (n, j, 'empty ridge set')
            assert all(any((s & ridge) == s for ridge in ridges)
                       for s in common), (n, j, 'nonpure intersection')
        if j and len(ridges) == n - 3:
            spanning.append(j)
        # Second, different check: the Björner shelling criterion in the
        # complementary triple representation.
        witnesses = set()
        for u in old_triples:
            if len(removed & set(u)) == 2:
                witnesses.update(set(u) - removed)
        if j:
            assert all(witnesses & (set(u) - removed) for u in old_triples)
        old_triples.append(t)
        old_faces.update(all_submasks(facet))
    assert len(spanning) == expected_spanning, (n, len(spanning))
    return len(order), len(old_faces), spanning


def binary_rank(columns):
    # Exact Gaussian elimination over F_2, no approximate numerics.
    basis = {}
    for value in columns:
        while value:
            pivot = value.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return len(basis)


def mod2_reduced_betti(n):
    # Enumerate the ENTIRE face poset, not an Euler characteristic shortcut.
    full = (1 << n) - 1
    face_masks = {0}
    for t in cut_triples(n):
        f = full ^ bits(t)
        face_masks.update(all_submasks(f))
    graded = defaultdict(list)
    for face in sorted(face_masks):
        graded[face.bit_count() - 1].append(face)
    maxdim = max(graded)
    rank = {0: 1}  # augmented boundary: every vertex maps to the empty face
    for d in range(1, maxdim + 1):
        idx = {s: i for i, s in enumerate(graded[d - 1])}
        cols = []
        for face in graded[d]:
            b = face
            boundary = 0
            while b:
                v = b & -b
                b ^= v
                boundary ^= 1 << idx[face ^ v]
            cols.append(boundary)
        rank[d] = binary_rank(cols)
    rank[maxdim + 1] = 0
    betti = {d:len(graded[d]) - rank[d] - rank[d+1]
             for d in range(maxdim + 1)}
    return betti, [len(graded[d]) for d in range(maxdim + 1)]


def main():
    for n in range(3, 9):
        assert not cut_triples(n)
    expected = {9:{3:1}, 10:{4:11}, 11:{5:1}, 12:{7:2}}
    for n, wanted in expected.items():
        got, fvec = mod2_reduced_betti(n)
        got = {d:v for d,v in got.items() if v}
        assert got == wanted, (n, got, wanted)
        print(f'NON_SHELLABLE_OK n={n} facets={len(cut_triples(n))} '
              f'nonzero_reduced_mod2_betti={got} fvec={fvec}')
    for n, expected_facets, expected_spanning in [(13,169,1),(14,238,8)]:
        count, faces, spanning = verify_shelling(n,expected_spanning)
        assert count == expected_facets
        assert expected_spanning == ((n-6)*(n-7)//2 - 20)
        print(f'SHELLING_OK n={n} facets={count} nonempty_faces={faces} '
              f'spanning={expected_spanning} indices={spanning}')
    print('VERIFY_OK: all complete finite cases and both explicit shellings')

if __name__ == '__main__':
    main()
