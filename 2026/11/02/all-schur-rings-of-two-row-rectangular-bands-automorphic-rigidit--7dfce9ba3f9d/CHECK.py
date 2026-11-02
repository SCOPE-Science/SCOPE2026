#!/usr/bin/env python3
"""Exact integer verification for Schur partitions of two-row rectangular bands."""
from math import comb
from collections import defaultdict


def partitions(n):
    """Restricted-growth strings, one for each set partition of n labeled points."""
    a = [0] * n
    def generate(pos, largest):
        if pos == n:
            yield tuple(a)
            return
        for v in range(largest + 2):
            a[pos] = v
            yield from generate(pos + 1, max(largest, v))
    if n == 0:
        yield ()
    else:
        yield from generate(1, 0)


def profiles(p, m):
    k = max(p) + 1
    rows = [[0, 0] for _ in range(k)]
    cols = [[0] * m for _ in range(k)]
    groups = [[] for _ in range(k)]
    for v, c in enumerate(p):
        i, j = divmod(v, m)
        rows[c][i] += 1
        cols[c][j] += 1
        groups[c].append((i, j))
    return rows, cols, groups


def schur_via_profiles(p, m):
    rows, cols, groups = profiles(p, m)
    k = len(groups)
    return all(
        all(rows[c][i] == rows[c][cells[0][0]] and
            cols[c][j] == cols[c][cells[0][1]]
            for i, j in cells for c in range(k))
        for cells in groups
    )


def schur_via_products(p, m):
    """Independently test all coefficients of all class-sum products."""
    rows, cols, groups = profiles(p, m)
    for X in range(len(groups)):
        for Y in range(len(groups)):
            for cells in groups:
                if len({rows[X][i] * cols[Y][j] for i, j in cells}) != 1:
                    return False
    return True


def component_weight(size):
    return 1 + (comb(size, size // 2) // 2 if size % 2 == 0 else 0)


def weighted_bell(n, weights):
    # Block containing 0 has k elements; recurse on the other n-k points.
    totals = [1]
    for j in range(1, n + 1):
        totals.append(sum(comb(j - 1, k - 1) * weights(k) * totals[j - k]
                          for k in range(1, j + 1)))
    return totals


def orbit_partition(generators, size):
    parent = list(range(size))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for sigma in generators:
        assert sorted(sigma) == list(range(size))
        for v in range(size):
            a, b = root(v), root(sigma[v])
            parent[a] = b
    parts = defaultdict(set)
    for v in range(size):
        parts[root(v)].add(v)
    return {frozenset(s) for s in parts.values()}


def automorphism_generators(p, m):
    """Construct permutations of rows/columns whose orbits are the classes."""
    rows, cols, groups = profiles(p, m)
    balanced = all(a == b for a, b in rows)
    column_groups = []
    tau = list(range(2 * m))
    if not balanced:
        assert all(a == 0 or b == 0 for a, b in rows)
        # Column groupings in either row must coincide.
        column_groups = [tuple(j for j in range(m) if p[j] == c)
                         for c in range(max(p) + 1) if rows[c][0]]
        for G in column_groups:
            assert len({p[m + j] for j in G}) == 1
        assert len({tuple(j for j in range(m) if p[m + j] == c)
                    for c in set(p[m:])}) == len(column_groups)
    else:
        by_pair = defaultdict(list)
        for j in range(m):
            by_pair[frozenset((p[j], p[m + j]))].append(j)
        for pair, C in by_pair.items():
            if len(pair) == 1:
                column_groups.append(tuple(C))
            else:
                a, b = sorted(pair)
                left = sorted(j for j in C if p[j] == a)
                right = sorted(j for j in C if p[j] == b)
                assert len(left) == len(right) and len(left) > 0
                column_groups.extend((tuple(left), tuple(right)))
                for u, v in zip(left, right):
                    tau[u] = v
                    tau[v] = u
        tau = [m + tau[j] if i == 0 else tau[j]
               for i in range(2) for j in range(m)]
    generators = []
    for C in column_groups:
        for x, y in zip(C, C[1:]):
            sigma = list(range(2 * m))
            for row in range(2):
                sigma[row * m + x], sigma[row * m + y] = (
                    row * m + y, row * m + x)
            generators.append(sigma)
    if balanced:
        generators.append(tau)
    expected = {frozenset(j for j, c in enumerate(p) if c == color)
                for color in set(p)}
    got = orbit_partition(generators, 2 * m)
    assert got == expected, (m, p, got, expected)
    # Every generator must be (row permutation, column permutation).
    for sigma in generators:
        image_row0 = {sigma[j] // m for j in range(m)}
        image_row1 = {sigma[m + j] // m for j in range(m)}
        assert len(image_row0) == len(image_row1) == 1
        assert image_row0 != image_row1
        assert all(sigma[j] % m == sigma[m + j] % m for j in range(m))
    return balanced


def main():
    B = weighted_bell(9, lambda _: 1)
    W = weighted_bell(9, component_weight)
    print('m  all  row-separated  row-balanced  formula')
    for m in range(1, 6):
        total = separate = balanced = 0
        for p in partitions(2 * m):
            valid = schur_via_profiles(p, m)
            if m <= 4:
                assert valid == schur_via_products(p, m)
            if valid:
                total += 1
                if automorphism_generators(p, m):
                    balanced += 1
                else:
                    separate += 1
        assert separate == B[m]
        assert balanced == W[m]
        assert total == B[m] + W[m]
        print(m, total, separate, balanced, B[m] + W[m])
    for m in range(6, 10):
        print(m, B[m] + W[m], B[m], W[m], B[m] + W[m])
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
