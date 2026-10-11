"""Exact finite tests of anchored graph cubical cellular homology over F_2.

The accompanying integral theorem relies on a topological homotopy and an
integral chain decomposition; these finite tests do not prove torsion-freeness.
"""
from collections import defaultdict
from itertools import product, combinations
from math import comb, factorial


def expected_betti(vertex_count, edges, anchors, n):
    r = len(anchors)
    assert r >= 1 and n >= r
    b = len(edges) - vertex_count + 1
    assert b >= 0
    d = n - r
    if not d:
        return [factorial(r)]

    def tree_rank(t):
        if r == 1:
            return 0
        return sum((-1) ** k * comb(r, k) * (r - k - 1) ** t
                   for k in range(r))

    result = [comb(n, i) * b ** i for i in range(d)]
    top = (sum(comb(n, j) * b ** j * tree_rank(n - j)
               for j in range(d))
           + comb(n, d) * b ** d * factorial(r))
    return result + [top]


def cubical_betti_mod_two(vertex_count, edges, anchors, n):
    symbols = range(vertex_count + len(edges))
    dims = defaultdict(list)
    for cell in product(symbols, repeat=n):
        if all(anchor in cell for anchor in anchors):
            dims[sum(s >= vertex_count for s in cell)].append(cell)
    assert dims
    max_dim = max(dims)
    ranks = {}
    for d in range(1, max_dim + 1):
        target = {cell: i for i, cell in enumerate(dims[d - 1])}
        basis = {}
        for cell in dims[d]:
            boundary = 0
            for i, symbol in enumerate(cell):
                if symbol >= vertex_count:
                    for vertex in edges[symbol - vertex_count]:
                        face = cell[:i] + (vertex,) + cell[i + 1:]
                        assert face in target
                        boundary ^= 1 << target[face]
            while boundary:
                pivot = boundary.bit_length() - 1
                if pivot in basis:
                    boundary ^= basis[pivot]
                else:
                    basis[pivot] = boundary
                    break
        ranks[d] = len(basis)
    return [len(dims[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
            for d in range(n - len(anchors) + 1)]


def run():
    cases = [
        ('single-vertex', 1, (), (0,), 2),
        ('single-edge-one-anchor', 2, ((0, 1),), (0,), 3),
        ('single-edge-two-anchors', 2, ((0, 1),), (0, 1), 3),
        ('path-three', 3, ((0, 1), (1, 2)), (0, 2), 4),
        ('path-four', 4, ((0, 1), (1, 2), (2, 3)), (0, 3), 4),
        ('triangle-one-anchor', 3, ((0, 1), (1, 2), (0, 2)), (0,), 3),
        ('triangle-two-anchors', 3, ((0, 1), (1, 2), (0, 2)), (0, 1), 4),
        ('triangle-all-anchors', 3, ((0, 1), (1, 2), (0, 2)), (0, 1, 2), 4),
        ('cycle-four', 4, ((0, 1), (1, 2), (2, 3), (0, 3)), (0, 2), 4),
        ('cycle-and-tail', 4, ((0, 1), (1, 2), (0, 2), (2, 3)), (0, 3), 4),
        ('complete-four', 4, tuple(combinations(range(4), 2)), (0, 1), 4),
        ('complete-four-three-anchors', 4, tuple(combinations(range(4), 2)), (0, 1, 2), 4),
        ('complete-four-four-anchors', 4, tuple(combinations(range(4), 2)), (0, 1, 2, 3), 4),
        ('two-cycle-wedge', 5, ((0, 1), (1, 2), (0, 2), (0, 3), (3, 4), (0, 4)), (1, 3), 4),
    ]
    for name, vertices, edges, anchors, n in cases:
        expected = expected_betti(vertices, edges, anchors, n)
        actual = cubical_betti_mod_two(vertices, edges, anchors, n)
        if actual != expected:
            raise AssertionError(f'{name}: {actual} != {expected}')
        print(f'PASS {name}: Betti={actual}')
    print('VERIFY_OK', len(cases), 'exact cubical boundary-rank comparisons')


if __name__ == '__main__':
    run()
