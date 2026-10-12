#!/usr/bin/env python3
"""Finite exact cross-checks for affine Grassmann third-support extremizers.

Pure Python 3; independent of external algebra and optimization packages.
"""
from collections import Counter
from itertools import combinations, product


def field(q):
    assert q in (2, 3, 4)
    if q == 3:
        return lambda a, b: (a + b) % 3, lambda a, b: a * b % 3

    def mul(a, b):
        if q == 2:
            return a & b
        p = 0
        for i in range(2):
            for j in range(2):
                if (a >> i) & (b >> j) & 1:
                    p ^= 1 << (i + j)
        if p & 8:
            p ^= 0b1110  # x^3 = x(x^2+x+1)
        if p & 4:
            p ^= 0b111   # x^2 = x+1
        return p

    return lambda a, b: a ^ b, mul


def rref_subspaces(q, dimension, rank):
    """Produce each rank-space exactly once in canonical RREF over F_q."""
    for pivots in combinations(range(dimension), rank):
        pset = set(pivots)
        slots = [(i, j) for i, p in enumerate(pivots)
                 for j in range(p + 1, dimension) if j not in pset]
        for values in product(range(q), repeat=len(slots)):
            rows = [[0] * dimension for _ in range(rank)]
            for i, p in enumerate(pivots):
                rows[i][p] = 1
            for (i, j), v in zip(slots, values):
                rows[i][j] = v
            yield tuple(tuple(row) for row in rows)


def exhaustive_coding_count(q):
    add, mul = field(q)
    points = list(product(range(q), repeat=4))

    def determinant(m):
        a, b, c, d = m
        return add(mul(a, d), (q - mul(b, c)) % q if q == 3 else mul(b, c))

    evals = [(1, *m, determinant(m)) for m in points]
    zero_masks = {}
    for co in product(range(q), repeat=6):
        mask = 0
        for j, vec in enumerate(evals):
            value = 0
            for x, y in zip(co, vec):
                value = add(value, mul(x, y))
            if value == 0:
                mask |= 1 << j
        zero_masks[co] = mask
    dist = Counter()
    for rows in rref_subspaces(q, 6, 3):
        common = zero_masks[rows[0]] & zero_masks[rows[1]] & zero_masks[rows[2]]
        dist[common.bit_count()] += 1
    assert max(dist) == q * q, (q, dist)
    count = dist[q * q]
    assert count == (60 if q == 2 else 2 * q * q * (q + 1)), (q, count)
    assert sum(dist.values()) == {2: 1395, 3: 33880, 4: 376805}[q]
    return dist, determinant


def independent_geometric_count(q, det):
    add, mul = field(q)
    count = 0
    for u, v in rref_subspaces(q, 4, 2):
        valid = True
        for s, t in product(range(q), repeat=2):
            w = tuple(add(mul(s, x), mul(t, y)) for x, y in zip(u, v))
            predicted = add(mul(s, det(u)), mul(t, det(v)))
            if det(w) != predicted:
                valid = False
                break
        if valid:
            count += 1
    assert count == {2: 15, 3: 8, 4: 10}[q], (q, count)
    return count


def main():
    for q in (2, 3, 4):
        dist, det = exhaustive_coding_count(q)
        plane_directions = independent_geometric_count(q, det)
        assert dist[q * q] == q * q * plane_directions
        print("q={} subspaces={} largest_zero_set={} extremizers={} directions={}".format(
            q, sum(dist.values()), max(dist), dist[q * q], plane_directions))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
