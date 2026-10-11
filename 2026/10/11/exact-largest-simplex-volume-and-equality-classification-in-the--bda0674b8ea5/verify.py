#!/usr/bin/env python3
"""Exact vertex-simplex census for the root D4 regular 24-cell.

All arithmetic is integral. The ambient vertex count is 24, and the
exhaustive search ranges over all 42,504 unordered five-vertex sets.
"""
import itertools
from collections import Counter
from math import comb, prod


def roots():
    return tuple(sorted({tuple(a if k == i else b if k == j else 0
                              for k in range(4))
                         for i, j in itertools.combinations(range(4), 2)
                         for a, b in itertools.product((-1, 1), repeat=2)}))


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def det_cofactor(m):
    return sum((-1)**j * m[0][j] * det3(
        tuple(tuple(m[i][k] for k in range(4) if k != j)
              for i in range(1, 4))) for j in range(4))


def det_permutation(m):
    total = 0
    for p in itertools.permutations(range(4)):
        inversion_parity = sum(p[i] > p[j] for i in range(4)
                               for j in range(i + 1, 4)) % 2
        total += (-1)**inversion_parity * prod(m[i][p[i]] for i in range(4))
    return total


def squared_distance(u, v):
    return sum((a - b)**2 for a, b in zip(u, v))


def main():
    vertices = roots()
    assert len(vertices) == 24
    assert len(set(vertices)) == 24
    assert all(sum(x*x for x in v) == 2 for v in vertices)
    assert all(sum(v) % 2 == 0 for v in vertices)
    expected = {0: 12168, 2: 11328, 4: 13776, 6: 3936,
                8: 1152, 10: 96, 12: 48}
    histogram = Counter()
    maximizers = set()
    scanned = 0
    for inds in itertools.combinations(range(24), 5):
        p = [vertices[i] for i in inds]
        rows = tuple(tuple(p[j+1][i] - p[0][i] for i in range(4))
                     for j in range(4))
        det1 = det_cofactor(rows)
        det2 = det_permutation(rows)
        assert det1 == det2
        modulus = abs(det1)
        histogram[modulus] += 1
        scanned += 1
        if modulus == 12:
            maximizers.add(inds)
    assert scanned == comb(24, 5) == 42504
    assert histogram == expected, histogram
    assert len(maximizers) == 48

    # No two maximizing simplices share a tetrahedral (four-vertex) face.
    four_sets = Counter(tuple(sorted(set(inds) - {i}))
                        for inds in maximizers for i in inds)
    assert len(four_sets) == 5 * 48
    assert max(four_sets.values()) == 1

    example = ((-1, -1, 0, 0), (-1, 1, 0, 0),
               (0, 0, -1, -1), (0, 0, -1, 1), (1, 0, 1, 0))
    i_example = tuple(sorted(vertices.index(v) for v in example))
    assert i_example in maximizers
    distances = Counter(squared_distance(vertices[i], vertices[j])
                        for i, j in itertools.combinations(i_example, 2))
    assert distances == {4: 6, 6: 4}
    for ids in maximizers:
        profile = Counter(squared_distance(vertices[i], vertices[j])
                          for i, j in itertools.combinations(ids, 2))
        assert profile == distances

    # The signed-coordinate-permutation group is transitive on all 48.
    vertex_index = {v: i for i, v in enumerate(vertices)}
    orbit = set()
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product((-1, 1), repeat=4):
            transformed = tuple(sorted(vertex_index[tuple(
                signs[k] * vertices[i][perm[k]] for k in range(4))]
                for i in i_example))
            orbit.add(transformed)
    assert len(orbit) == 48
    assert orbit == maximizers
    print("VERIFY_OK D4_24cell vertex_sets=42504 max_det=12 "
          "maximizers=48 B4_orbit=48 shared_four=0")


if __name__ == "__main__":
    main()
