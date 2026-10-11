#!/usr/bin/env python3
"""Exact checks for the uniform multiclique equivariant homology character."""
from itertools import combinations, permutations, product
from collections import Counter
from math import gcd, lcm, comb, factorial


def partitions(n, smallest=1):
    if n == 0:
        yield ()
    for p in range(smallest, n + 1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


def cycle_permutation(lengths):
    p = list(range(sum(lengths)))
    s = 0
    for length in lengths:
        for i in range(length):
            p[s + i] = s + ((i + 1) % length)
        s += length
    return tuple(p)


def fixed_colors(power, h):
    return sum(1 for color in range(len(h)) if iterate(h, color, power) == color)


def iterate(p, x, power):
    for _ in range(power):
        x = p[x]
    return x


def character(lengths, color_lengths):
    """Cycle-index formula, evaluated using only the two cycle partitions."""
    n = sum(lengths)
    h = cycle_permutation(color_lengths)
    val = 0
    for mask in range(1 << len(lengths)):
        active = [lengths[i] for i in range(len(lengths)) if mask & (1 << i)]
        ways = 1
        for a in active:
            ways *= fixed_colors(a, h) ** ((a - 1) // 2)
            if a % 2 == 0:
                ways *= fixed_colors(a // 2, h)
        for i, a in enumerate(active):
            for b in active[:i]:
                ways *= fixed_colors(lcm(a, b), h) ** gcd(a, b)
        val += (-1) ** len(active) * ways
    return (-1) ** n * val


def parity_of_restriction(p, vertices):
    images = [p[x] for x in vertices]
    return (-1) ** sum(images[i] > images[j]
                       for i in range(len(images))
                       for j in range(i + 1, len(images)))


def direct_trace(lengths, color_lengths):
    """Independent signed-cell fixed-point calculation by literal pair orbits."""
    g = cycle_permutation(lengths)
    h = cycle_permutation(color_lengths)
    n = len(g)
    reduced = -1
    for k in range(1, n + 1):
        for vertices in combinations(range(n), k):
            if {g[x] for x in vertices} != set(vertices):
                continue
            edges = set(combinations(vertices, 2))
            weight = 1
            while edges:
                start = edges.pop()
                orbit = [start]
                nxt = tuple(sorted((g[start[0]], g[start[1]])))
                while nxt != start:
                    assert nxt in edges
                    edges.remove(nxt)
                    orbit.append(nxt)
                    nxt = tuple(sorted((g[nxt[0]], g[nxt[1]])))
                weight *= fixed_colors(len(orbit), h)
            reduced += (-1) ** (k - 1) * parity_of_restriction(g, vertices) * weight
    return (-1) ** (n - 1) * reduced


def cells(n, q, size):
    for vertices in combinations(range(n), size):
        edges = tuple(combinations(vertices, 2))
        for colors in product(range(q), repeat=len(edges)):
            yield (vertices, colors)


def sparse_rank(columns):
    pivots = {}
    for column in columns:
        v = set(column)
        while v:
            p = max(v)
            if p in pivots:
                v.symmetric_difference_update(pivots[p])
            else:
                pivots[p] = v
                break
    return len(pivots)


def betti_mod2(n, q):
    all_cells = [list(cells(n, q, k)) for k in range(1, n + 1)]
    ranks = [0] * (n + 1)
    for k in range(2, n + 1):
        rows = {c: j for j, c in enumerate(all_cells[k - 2])}
        columns = []
        for vertices, colors in all_cells[k - 1]:
            colored_pairs = dict(zip(combinations(vertices, 2), colors))
            column = []
            for dropped in vertices:
                face = tuple(v for v in vertices if v != dropped)
                face_colors = tuple(colored_pairs[pair] for pair in combinations(face, 2))
                column.append(rows[(face, face_colors)])
            columns.append(column)
        ranks[k - 1] = sparse_rank(columns)
    return [len(all_cells[k]) - ranks[k] - ranks[k + 1] - (1 if k == 0 else 0)
            for k in range(n)]


def conjugacy_size(lengths):
    z = 1
    for k, c in Counter(lengths).items():
        z *= k ** c * factorial(c)
    return factorial(sum(lengths)) // z


def wedge3_character(lengths):
    coeff = [1, 0, 0, 0]
    for length in lengths:
        new = list(coeff)
        if length <= 3:
            for i in range(length, 4):
                new[i] += ((-1) ** (length - 1)) * coeff[i - length]
        coeff = new
    return coeff[3]


def run():
    group_checks = 0
    for n in range(2, 6):
        for q in range(2, 5):
            for lengths in partitions(n):
                for colors in partitions(q):
                    a = character(lengths, colors)
                    b = direct_trace(lengths, colors)
                    assert a == b, (n, q, lengths, colors, a, b)
                    group_checks += 1
    rank_checks = 0
    for n, q in [(2, 2), (2, 3), (3, 2), (3, 3), (3, 4),
                 (4, 2), (4, 3), (5, 2)]:
        bs = betti_mod2(n, q)
        predicted = character((1,) * n, (1,) * q)
        assert bs == [0] * (n - 1) + [predicted], (n, q, bs, predicted)
        rank_checks += 1
    exterior_checks = 0
    for q in range(3, 8):
        for colors in partitions(q):
            dimension = sum(conjugacy_size(lengths) * character(lengths, colors)
                            for lengths in partitions(3)) // factorial(3)
            assert dimension == wedge3_character(colors), (q, colors, dimension)
            exterior_checks += 1
    print('VERIFY_OK direct_signed_character_checks=', group_checks,
          'exact_mod2_homology_cases=', rank_checks,
          'exterior_cube_character_checks=', exterior_checks)


if __name__ == '__main__':
    run()
