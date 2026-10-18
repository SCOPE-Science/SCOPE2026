#!/usr/bin/env python3
"""Independent finite checks for square-rich order-three de Bruijn cycles.
Run with Python 3.9+; no third-party packages required.
Finite tests supplement, but do not replace, the mathematical proof.
"""
from collections import Counter
from math import factorial, comb
from itertools import product


def build_tour(q, choose_second_mask=0):
    """Construct an Euler tour with one oriented alternating square per symbol pair."""
    pairs = [(a, b) for a in range(q) for b in range(a + 1, q)]
    graph = {(a, b): [] for a in range(q) for b in range(q)}
    for a, b, c in product(range(q), repeat=3):
        if a == c and a != b:
            continue
        graph[(a, b)].append(((b, c), ((a, b, c),)))
    for k, (a, b) in enumerate(pairs):
        u, v = (b, a) if ((choose_second_mask >> k) & 1) else (a, b)
        graph[(u, v)].append(((u, v), ((u, v, u), (v, u, v))))
    for edges in graph.values():
        edges.reverse()
    vstack = [(0, 0)]
    estack = []
    reverse = []
    while vstack:
        node = vstack[-1]
        if graph[node]:
            nxt, expanded = graph[node].pop()
            vstack.append(nxt)
            estack.append(expanded)
        else:
            vstack.pop()
            if estack:
                reverse.append(estack.pop())
    expanded = [e for block in reversed(reverse) for e in block]
    assert len(expanded) == q ** 3
    assert len(set(expanded)) == q ** 3
    for i, e in enumerate(expanded):
        nxt = expanded[(i + 1) % len(expanded)]
        assert e[1:] == nxt[:2]
    sequence = tuple(e[0] for e in expanded)
    squares = [(sequence[i], sequence[(i + 1) % len(sequence)])
               for i in range(len(sequence))
               if sequence[i] == sequence[(i + 2) % len(sequence)]
               and sequence[(i + 1) % len(sequence)] == sequence[(i + 3) % len(sequence)]]
    expected = [(b, a) if (choose_second_mask >> k) & 1 else (a, b)
                for k, (a, b) in enumerate(pairs)]
    assert set(squares) == set(expected) and len(squares) == len(expected)
    return sequence


def rooted_tree_count(q):
    """Exact directed in-arborescence count of the nonalternating core."""
    vertices = [(a, b) for a in range(q) for b in range(q)]
    index = {v: i for i, v in enumerate(vertices)}
    n = q * q
    lap = [[0] * (n - 1) for _ in range(n - 1)]
    for a, b, c in product(range(q), repeat=3):
        if a == c and a != b:
            continue
        u = index[(a, b)]
        v = index[(b, c)]
        if u != v:
            if u < n - 1:
                lap[u][u] += 1
                if v < n - 1:
                    lap[u][v] -= 1
    # Fraction-free Bareiss determinant (pivoting allowed).
    m = n - 1
    prev = 1
    sign = 1
    for k in range(m - 1):
        if lap[k][k] == 0:
            t = next((r for r in range(k + 1, m) if lap[r][k]), None)
            assert t is not None
            lap[k], lap[t] = lap[t], lap[k]
            sign *= -1
        piv = lap[k][k]
        for i in range(k + 1, m):
            for j in range(k + 1, m):
                numerator = piv * lap[i][j] - lap[i][k] * lap[k][j]
                assert numerator % prev == 0
                lap[i][j] = numerator // prev
            lap[i][k] = 0
        prev = piv
    return sign * lap[-1][-1]


def census(q):
    """Exhaustively enumerate tours rooted at the unique 000 edge (q=2,3)."""
    total = q ** 3
    powers = (q ** 2, q)
    hist = Counter()
    masks = Counter()
    pairs = {(a, b): k for k, (a, b) in enumerate(
        (a, b) for a in range(q) for b in range(a + 1, q))}
    path = [0] * total
    # Triple 000 is the fixed first edge.
    def dfs(node, used, depth, square_count, signs):
        if depth == total:
            if node:
                return
            last = path[-1]
            a, b, c = last // powers[0], last // q % q, last % q
            d = path[0] % q
            if a == c and b == d:
                square_count += 1
                if a != b:
                    k = pairs[min(a,b), max(a,b)]
                    signs |= (1 if a < b else 2) << (2 * k)
            hist[square_count] += 1
            if square_count == comb(q,2):
                mask = sum((((signs >> (2*k)) & 3) == 2) << k
                           for k in range(comb(q,2)))
                masks[mask] += 1
            return
        for x in range(q):
            e = node * q + x
            if (used >> e) & 1:
                continue
            prev = path[depth - 1]
            a, b, c = prev // powers[0], prev // q % q, prev % q
            new_count = square_count
            new_signs = signs
            if a == c and b == x:
                new_count += 1
                if a != b:
                    k = pairs[min(a,b), max(a,b)]
                    new_signs |= (1 if a < b else 2) << (2*k)
            path[depth] = e
            dfs((node % q) * q + x, used | (1 << e), depth + 1,
                new_count, new_signs)
    dfs(0, 1, 1, 0, 0)
    return hist, masks


def main():
    expected_t = {2: 1, 3: 108, 4: 3538944}
    for q, expected in expected_t.items():
        got = rooted_tree_count(q)
        assert got == expected, (q, got, expected)
    for q in range(2, 8):
        m = comb(q, 2)
        masks = {0, (1 << m) - 1, sum(1 << k for k in range(0, m, 2))}
        if m <= 6:
            masks = set(range(1 << m))
        for mask in masks:
            build_tour(q, mask)
    exp = {2: {1: 2}, 3: {0: 27648, 1: 124416,
                         2: 165888, 3: 55296}}
    for q in (2, 3):
        hist, orientations = census(q)
        assert dict(hist) == exp[q], (q, hist)
        m = comb(q, 2)
        t = expected_t[q]
        per_orientation = (t * factorial(q - 1) ** (q + m)
                           * factorial(q - 2) ** m)
        assert len(orientations) == (1 << m)
        assert set(orientations.values()) == {per_orientation}
    print('SQUARE_RICH_DEBRUIJN_CHECKS_PASSED')
    print('CENSUS_Q2', exp[2], 'CENSUS_Q3', exp[3])
    print('TREES', expected_t)

if __name__ == '__main__':
    main()
