#!/usr/bin/env python3
from itertools import combinations
from math import comb


def integer_partitions(n, max_part=None):
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(max_part, n), 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def graph_data(part_sizes):
    part_of = []
    for i, size in enumerate(part_sizes):
        part_of.extend([i] * size)
    n = len(part_of)
    dist = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u == v:
                dist[u][v] = 0
            elif part_of[u] == part_of[v]:
                dist[u][v] = 2
            else:
                dist[u][v] = 1
    return part_of, dist


def is_distance_equalizer_direct(part_sizes, mask):
    part_of, dist = graph_data(part_sizes)
    n = len(part_of)
    selected = [v for v in range(n) if (mask >> v) & 1]
    outside = [v for v in range(n) if not ((mask >> v) & 1)]
    for x, y in combinations(outside, 2):
        if not any(dist[w][x] == dist[w][y] for w in selected):
            return False
    return True


def is_distance_equalizer_classification(part_sizes, mask):
    part_of, _ = graph_data(part_sizes)
    counts = [0] * len(part_sizes)
    for v, p in enumerate(part_of):
        if (mask >> v) & 1:
            counts[p] += 1
    contains_part = any(counts[i] == part_sizes[i] for i in range(len(part_sizes)))
    support_size = sum(c > 0 for c in counts)
    return contains_part or support_size >= 3


def padd(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def psub(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] -= x
    return out


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def proper_nonempty_poly(size):
    out = [comb(size, k) for k in range(size + 1)]
    out[0] -= 1
    out[-1] -= 1
    return out


def formula_polynomial(part_sizes):
    n = sum(part_sizes)
    total = [comb(n, k) for k in range(n + 1)]
    bad = [1]
    blocks = [proper_nonempty_poly(s) for s in part_sizes]
    for block in blocks:
        bad = padd(bad, block)
    for i, j in combinations(range(len(blocks)), 2):
        bad = padd(bad, pmul(blocks[i], blocks[j]))
    return psub(total, bad)


def direct_polynomial(part_sizes):
    n = sum(part_sizes)
    out = [0] * (n + 1)
    for mask in range(1 << n):
        if is_distance_equalizer_direct(part_sizes, mask):
            out[mask.bit_count()] += 1
    return out


def predicted_basis_data(part_sizes):
    r = len(part_sizes)
    m = min(part_sizes)
    if r == 2:
        return m, sum(size == m for size in part_sizes)
    if m == 1:
        return 1, sum(size == 1 for size in part_sizes)
    if m == 2:
        return 2, sum(size == 2 for size in part_sizes)
    count = sum(size == 3 for size in part_sizes)
    for i, j, k in combinations(range(r), 3):
        count += part_sizes[i] * part_sizes[j] * part_sizes[k]
    return 3, count


def main():
    types = []
    for n in range(2, 9):
        for p in integer_partitions(n):
            if len(p) >= 2:
                types.append(p)

    subset_checks = 0
    polynomial_checks = 0
    basis_checks = 0
    for part_sizes in types:
        n = sum(part_sizes)
        for mask in range(1 << n):
            direct = is_distance_equalizer_direct(part_sizes, mask)
            classified = is_distance_equalizer_classification(part_sizes, mask)
            if direct != classified:
                raise AssertionError((part_sizes, mask, direct, classified))
            subset_checks += 1

        direct_poly = direct_polynomial(part_sizes)
        formula_poly = formula_polynomial(part_sizes)
        if direct_poly != formula_poly:
            raise AssertionError((part_sizes, direct_poly, formula_poly))
        polynomial_checks += 1

        min_size = next(k for k, c in enumerate(direct_poly) if c)
        min_count = direct_poly[min_size]
        predicted = predicted_basis_data(part_sizes)
        if (min_size, min_count) != predicted:
            raise AssertionError((part_sizes, (min_size, min_count), predicted))
        basis_checks += 1

    print(f"isomorphism_types={len(types)}")
    print(f"subset_classification_checks={subset_checks}")
    print(f"polynomial_checks={polynomial_checks}")
    print(f"minimum_basis_checks={basis_checks}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
