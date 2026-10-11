#!/usr/bin/env python3
"""Independent GF(2) elliptic-quadric model and face-count verification.
No external packages or data.
"""
from itertools import combinations


def quadratic(x):
    b = [(x >> k) & 1 for k in range(6)]
    return b[0] * b[1] ^ b[2] * b[3] ^ b[4] * b[5] ^ b[4] ^ b[5]


def main():
    vectors = [i for i in range(1, 64) if quadratic(i) == 0]
    assert len(vectors) == 27
    neighbors = [set() for _ in vectors]
    for i, j in combinations(range(27), 2):
        # Over GF(2), span(x,y) is a totally singular projective line
        # precisely when the third nonzero point x+y is singular.
        if quadratic(vectors[i] ^ vectors[j]) == 0:
            neighbors[i].add(j)
            neighbors[j].add(i)
    assert all(len(nbrs) == 10 for nbrs in neighbors)
    assert sum(map(len, neighbors)) // 2 == 135
    for i, j in combinations(range(27), 2):
        assert len(neighbors[i] & neighbors[j]) == (1 if j in neighbors[i] else 5)

    # Witness of isomorphism with the 27 exceptional-divisor labels ordered
    # as E_0,...,E_5; L_01,...,L_45; Q_0,...,Q_5.
    phi = [0, 1, 8, 11, 17, 23, 2, 6, 13, 19, 25, 7, 14, 20,
           26, 9, 15, 21, 22, 16, 10, 4, 3, 5, 12, 18, 24]
    assert sorted(phi) == list(range(27))
    classes = []
    for i in range(6):
        b = [0] * 6
        b[i] = 1
        classes.append((0, b))
    for i, j in combinations(range(6), 2):
        b = [0] * 6
        b[i] = b[j] = -1
        classes.append((1, b))
    for i in range(6):
        b = [-1] * 6
        b[i] = 0
        classes.append((2, b))
    for i, j in combinations(range(27), 2):
        a, b = classes[i]
        c, d = classes[j]
        divisor_edge = (a * c - sum(x * y for x, y in zip(b, d)) == 1)
        assert divisor_edge == (phi[j] in neighbors[phi[i]])

    # Alternate enumeration by combinations, not binary-mask subset stepping.
    by_cardinality = [set() for _ in range(11)]
    for nbrs in neighbors:
        nbrs = sorted(nbrs)
        for card in range(1, 11):
            by_cardinality[card].update(combinations(nbrs, card))
    f = tuple(len(by_cardinality[k]) for k in range(1, 11))
    assert f == (27, 351, 1800, 4590, 6588, 5670, 3240, 1215, 270, 27)
    assert sum(f) == 23778
    assert sum((-1)**d * n for d, n in enumerate(f)) == 72
    print('POLAR_CHECK_OK: Q-minus(5,2) points: 27; (27,10,1,5) collinearity')
    print('POLAR_CHECK_OK: explicit 27-label isomorphism to cubic line intersection')
    print('POLAR_CHECK_OK: face counts =', f, ', Euler = 72')


if __name__ == '__main__':
    main()
