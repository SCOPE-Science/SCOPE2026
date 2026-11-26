"""Check two exact cellular certificates for a Petersen torsion cup product."""

from collections import Counter
from itertools import combinations


def main():
    labels = tuple(map(frozenset, combinations(range(5), 2)))
    vertices = list(combinations(range(len(labels)), 2))
    edges = [(i, j) for i, j in vertices if labels[i].isdisjoint(labels[j])]
    ones = [(i, k) for i, e in enumerate(edges) for k in range(10) if k not in e]
    twos = [(i, j) for i, j in combinations(range(len(edges)), 2)
            if set(edges[i]).isdisjoint(edges[j])]
    assert (len(vertices), len(ones), len(twos)) == (45, 120, 75)

    tree = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    seen = {0}
    while True:
        after = seen.union(v for i in tree if seen.intersection(edges[i])
                           for v in edges[i])
        if after == seen:
            break
        seen = after
    assert len(tree) == 9 and len(seen) == 10

    idx = {cell: k for k, cell in enumerate(ones)}
    boundaries = []
    for i, j in twos:
        a, b = edges[i]
        d, f = edges[j]
        boundaries.append({idx[j, b]: 1, idx[j, a]: -1,
                           idx[i, f]: -1, idx[i, d]: 1})

    # Two degree-one motion cochains; the product on each square is a 2x2 determinant.
    left = {8: 1, 10: 1}
    right = {14: 1, 10: -1}
    cup = [left.get(i, 0) * right.get(j, 0) - left.get(j, 0) * right.get(i, 0)
           for i, j in twos]
    assert {twos[i]: x for i, x in enumerate(cup) if x} == {
        (8, 10): -1, (8, 14): 1, (10, 14): 1}

    witness = {k: val for val, ids in (
        (-2, (5,)),
        (-1, (1, 2, 4, 6, 9, 25, 33, 34, 37, 58, 61)),
        (1, (16, 24, 30, 32, 36, 38, 50, 51, 52, 53, 54, 60, 62, 76, 77)),
        (2, (68, 69, 84)),
    ) for k in ids}
    assert [sum(witness.get(k, 0) * s for k, s in b.items())
            for b in boundaries] == [2 * x for x in cup]

    binary_cycle = (0, 1, 3, 4, 6, 7, 10, 11, 16, 17, 19, 22, 23, 25, 27, 29,
                    31, 32, 36, 37, 38, 39, 41, 44, 45, 47, 49, 51, 55, 57,
                    58, 62, 63, 65, 67, 69)
    assert all(n % 2 == 0 for n in Counter(k for i in binary_cycle
                                           for k in boundaries[i]).values())
    assert sum(cup[i] for i in binary_cycle) % 2 == 1
    print('PRODUCT_ORDER_TWO_OK integral_double_boundary=True mod2_cycle_pairing=1')


if __name__ == '__main__':
    main()
