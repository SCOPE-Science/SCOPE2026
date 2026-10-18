#!/usr/bin/env python3
"""Finite, independent checks for scale-two Manhattan Rips complexes of integer boxes.

Requires only the Python standard library. Full generality is proved in RESULT.md;
these finite checks test the normalization, clique combinatorics and homology.
"""
from collections import Counter, defaultdict
from itertools import product


def cliques(dims, scale=2):
    """Enumerate every nonempty simplex once, using increasing vertex indices."""
    pts = list(product(*(range(s + 1) for s in dims)))
    adj = [set() for _ in pts]
    for i, p in enumerate(pts):
        for j in range(i + 1, len(pts)):
            if sum(abs(x - y) for x, y in zip(p, pts[j])) <= scale:
                adj[i].add(j)
    def extend(face, options):
        for i, v in enumerate(options):
            sigma = face + (v,)
            yield sigma
            yield from extend(sigma, [x for x in options[i + 1:] if x in adj[v]])
    return pts, list(extend((), list(range(len(pts)))))


def homology_gf2(pts, faces):
    cells = defaultdict(list)
    for face in faces:
        cells[len(face) - 1].append(face)
    ranks = {}
    for degree in sorted(cells):
        if degree < 1:
            continue
        lookup = {f: i for i, f in enumerate(cells[degree - 1])}
        pivots = {}
        rank = 0
        for face in cells[degree]:
            column = 0
            for j in range(len(face)):
                column ^= 1 << lookup[face[:j] + face[j + 1:]]
            while column:
                bit = column.bit_length() - 1
                if bit in pivots:
                    column ^= pivots[bit]
                else:
                    pivots[bit] = column
                    rank += 1
                    break
        ranks[degree] = rank
    betti = {d: len(fs) - ranks.get(d, 0) - ranks.get(d + 1, 0)
             - (1 if d == 0 else 0) for d, fs in cells.items()}
    return {d: b for d, b in betti.items() if b}, {d: len(fs) for d, fs in cells.items()}


def chi(faces):
    return sum(1 if len(face) % 2 else -1 for face in faces)


def local_weights():
    pts, faces = cliques((2, 2, 2))
    weights = Counter()
    totals = Counter()
    for face in faces:
        points = [pts[i] for i in face]
        minimum = tuple(min(p[k] for p in points) for k in range(3))
        if minimum != (0, 0, 0):
            continue
        width = tuple(max(p[k] for p in points) for k in range(3))
        weights[width] += (1 if len(face) % 2 else -1)
        totals[width] += 1
    assert len(totals) == 27
    assert sum(totals.values()) == 117
    for w in product(range(3), repeat=3):
        if 2 in w:
            expected = 0
        else:
            expected = (1, -1, 1, -2)[sum(w)]
        assert weights[w] == expected, (w, weights[w], expected)
    print('LOCAL_WEIGHTS_PASS: all 27 span types; 117 anchored simplices')
    print('NONZERO_WEIGHTS: k unit-length coordinate spans have weights 1,-1,1,-2 for k=0,1,2,3')


def cube_projection_test():
    for a, b, c in [(2, 2, 2), (1, 2, 3)]:
        cubes = list(product(range(a), range(b), range(c)))
        for target in cubes:
            for source in cubes:
                img = {
                    tuple(min(max(u, t), t + 1) for u, t in zip(point, target))
                    for point in product(*(range(v, v + 2) for v in source))
                }
                if source == target:
                    assert len(img) == 8
                else:
                    assert any(len({p[j] for p in img}) == 1 for j in range(3))
                    assert len(img) <= 4
    print('CUBE_PROJECTIONS_PASS: distinct unit cubes project into simplex faces')


def cases():
    dims_list = [(0, 0, 0), (1, 0, 2), (1, 1, 1), (1, 1, 3),
                 (1, 2, 3), (2, 2, 2), (2, 3, 3), (3, 3, 3)]
    for dims in dims_list:
        pts, faces = cliques(dims)
        bh, fvector = homology_gf2(pts, faces)
        a, b, c = dims
        expected = ({3: a * b * c} if a * b * c else {})
        assert bh == expected, (dims, bh, expected)
        assert chi(faces) == 1 - a * b * c
        print('BOX_PASS:', dims, 'vertices', len(pts), 'simplices', len(faces),
              'chi', chi(faces), 'reduced_mod2_betti', bh)


def main():
    local_weights()
    cube_projection_test()
    cases()
    # The 3-cube itself is the boundary of the 4-dimensional cross-polytope.
    pts, faces = cliques((1, 1, 1))
    fvec = Counter(len(f) - 1 for f in faces)
    assert [fvec[k] for k in range(4)] == [8, 24, 32, 16]
    print('UNIT_CUBE_CROSS_POLYTOPE_PASS: f-vector (8,24,32,16)')
    print('ALL_FINITE_CHECKS_PASSED')

if __name__ == '__main__':
    main()
