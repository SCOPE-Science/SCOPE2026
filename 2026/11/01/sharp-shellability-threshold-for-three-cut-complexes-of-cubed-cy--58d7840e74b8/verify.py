"""Exhaustive finite verification of shellings and subtop homology for third-power cycle three-cut complexes.
Run from the directory containing order13.txt and order14.txt: python3 verify.py.
Pure Python 3, standard library only; all arithmetic in homology checks is exact over F_2.
"""
from itertools import combinations
from collections import defaultdict
from pathlib import Path


def cut_facets(n):
    """Facets of ordinary 3-cut complex of the third power of C_n."""
    p = 3
    universe = (1 << n) - 1
    neighborhood = []
    for v in range(n):
        neighborhood.append(sum(1 << ((v + d) % n) for d in range(-p, p + 1) if d))
    facets = []
    for tri in combinations(range(n), 3):
        tri_mask = sum(1 << v for v in tri)
        # Exact breadth-first search of the induced three-vertex graph.
        seen, frontier = 1 << tri[0], [tri[0]]
        for u in frontier:
            rem = neighborhood[u] & tri_mask & ~seen
            while rem:
                w = rem & -rem
                rem ^= w
                seen |= w
                frontier.append(w.bit_length() - 1)
        if seen != tri_mask:
            facets.append(universe ^ tri_mask)
    return sorted(facets)


def all_faces(facets):
    faces = set()
    for top in facets:
        sub = top
        while sub:
            faces.add(sub)
            sub = (sub - 1) & top
    return faces


def rank_f2(columns):
    pivots = {}
    for vec in columns:
        while vec:
            pivot = vec.bit_length()
            if pivot in pivots:
                vec ^= pivots[pivot]
            else:
                pivots[pivot] = vec
                break
    return len(pivots)


def mod2_homology(facets):
    layers = defaultdict(list)
    for f in all_faces(facets):
        layers[f.bit_count() - 1].append(f)
    dim = max(layers)
    ranks = [0] * (dim + 2)
    for d in range(1, dim + 1):
        lower = {face: i for i, face in enumerate(layers[d - 1])}
        boundary = []
        for face in layers[d]:
            col = 0
            bits = face
            while bits:
                b = bits & -bits
                bits ^= b
                col ^= 1 << lower[face ^ b]
            boundary.append(col)
        ranks[d] = rank_f2(boundary)
    bettis = [len(layers[d]) - ranks[d] - ranks[d + 1] for d in range(dim + 1)]
    bettis[0] -= 1  # reduced H_0, connected cases
    fvec = tuple(len(layers[d]) for d in range(dim + 1))
    return bettis, fvec, ranks


def shell_certificate(n, path):
    expected = set(cut_facets(n))
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    order = []
    for row in lines:
        vv = [int(x) for x in row.split()]
        assert len(vv) == n - 3 and len(set(vv)) == len(vv) and all(0 <= x < n for x in vv)
        order.append(sum(1 << v for v in vv))
    assert len(order) == len(expected) and set(order) == expected and len(set(order)) == len(order), 'order is not a permutation of all facets'
    old = []
    betti_top = 0
    for j, facet in enumerate(order):
        if j:
            # All codimension-one faces already present earlier, encoded by
            # the vertices removed to obtain them.
            available = 0
            for prev in old:
                diff = facet & ~prev
                if diff.bit_count() == 1:
                    available |= diff
            assert available, (n, j, 'no old ridge')
            for prev in old:
                # Pure codim-one intersection iff every previous intersection
                # lies in an old ridge of the new facet.
                assert available & ~prev, (n, j, 'impure attachment')
            if available == facet:
                betti_top += 1
        old.append(facet)
    return len(order), betti_top


def main():
    expected_below = {9: (3, 1), 10: (4, 11), 11: (5, 1), 12: (7, 2)}
    expected_facets = {9: 9, 10: 30, 11: 66, 12: 112, 13: 169, 14: 238}
    for n in range(9, 13):
        facets = cut_facets(n)
        assert len(facets) == expected_facets[n]
        bettis, fvec, ranks = mod2_homology(facets)
        critical_degree, multiplicity = expected_below[n]
        assert len(bettis) == n-3
        assert bettis[critical_degree] == multiplicity
        assert all(v == 0 for d, v in enumerate(bettis) if d != critical_degree)
        assert critical_degree < n - 4
        assert sum(((-1) ** d) * f for d, f in enumerate(fvec)) == 1 + sum(((-1) ** d) * b for d, b in enumerate(bettis))
        print('SUBTOP_OK',n,'facets',len(facets),'faces',sum(fvec),'face_vector',fvec,'boundary_ranks',ranks[1:-1],'nonzero_reduced_H',critical_degree,multiplicity)
    for n, expected_hom in [(13, 1), (14, 8)]:
        count, spanning = shell_certificate(n, Path(__file__).with_name('order%d.txt' % n))
        assert count == expected_facets[n]
        assert spanning == expected_hom
        print('SHELLING_OK',n,'facets',count,'top_sphere_count',spanning)
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
