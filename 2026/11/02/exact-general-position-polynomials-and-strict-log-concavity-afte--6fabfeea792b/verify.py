#!/usr/bin/env python3
"""Exact checks for general-position polynomials of complements of degree-two graphs.
Run with Python 3.10+; no third-party dependencies.
"""
from functools import lru_cache
from itertools import combinations
from math import comb


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def path_ind(k):
    return [comb(k - i + 1, i) for i in range((k + 1) // 2 + 1)]


def cycle_ind(k):
    return [1] + [k * comb(k - i, i) // (k - i)
                  for i in range(1, k // 2 + 1)]


def component_types(n):
    return sorted([('P', k) for k in range(1, n + 1)] +
                  [('C', k) for k in range(3, n + 1)],
                  key=lambda item: (item[1], item[0]))


def component_multisets(n):
    types = component_types(n)
    @lru_cache(maxsize=None)
    def rec(remaining, start):
        if remaining == 0:
            return ((),)
        out = []
        for idx in range(start, len(types)):
            if types[idx][1] <= remaining:
                out.extend(((idx,) + tail)
                           for tail in rec(remaining - types[idx][1], idx))
        return tuple(out)
    for indices in rec(n, 0):
        yield tuple(types[i] for i in indices)


def formula(parts):
    b = [1]
    e = p = t = q = 0
    for kind, size in parts:
        b = multiply(b, path_ind(size) if kind == 'P' else cycle_ind(size))
        if kind == 'P':
            e += size - 1
            p += max(0, size - 2)
        else:
            e += size
            if size == 3:
                t += 1
            else:
                p += size
            if size == 4:
                q += 1
    a = b + [0] * max(0, 5 - len(b))
    a[2] += e
    a[3] += p + t
    a[4] += q
    while a[-1] == 0:
        a.pop()
    return a


def complement_adjacency(parts):
    n = sum(k for _, k in parts)
    h = [set() for _ in range(n)]
    offset = 0
    for kind, k in parts:
        for j in range(k - 1):
            u, v = offset + j, offset + j + 1
            h[u].add(v); h[v].add(u)
        if kind == 'C':
            u, v = offset, offset + k - 1
            h[u].add(v); h[v].add(u)
        offset += k
    g = [set(range(n)) - h[v] - {v} for v in range(n)]
    return g


def brute_general_position(g):
    n = len(g)
    distance = [[n + 1] * n for _ in range(n)]
    for src in range(n):
        distance[src][src] = 0
        frontier = [src]
        for v in frontier:
            for w in g[v]:
                if distance[src][w] > distance[src][v] + 1:
                    distance[src][w] = distance[src][v] + 1
                    frontier.append(w)
        assert max(distance[src]) < n + 1, 'complement disconnected'
    forbidden = []
    for i, j, k in combinations(range(n), 3):
        d = distance
        if (d[i][j] + d[j][k] == d[i][k] or
            d[i][k] + d[k][j] == d[i][j] or
            d[j][i] + d[i][k] == d[j][k]):
            forbidden.append((1 << i) | (1 << j) | (1 << k))
    out = [0] * (n + 1)
    for mask in range(1 << n):
        if not any(mask & pattern == pattern for pattern in forbidden):
            out[mask.bit_count()] += 1
    while out[-1] == 0:
        out.pop()
    return out


def strict_lc(a):
    assert a and all(x > 0 for x in a), f'internal gap: {a}'
    return all(a[j] ** 2 > a[j - 1] * a[j + 1]
               for j in range(1, len(a) - 1))


def main():
    totals = {}
    minimum_slack = {}
    brute_counts = {}
    for n in range(5, 14):
        cases = 0
        minimum = None
        brute = 0
        for parts in component_multisets(n):
            a = formula(parts)
            assert strict_lc(a), (n, parts, a)
            slack = min(a[j] ** 2 - a[j - 1] * a[j + 1]
                        for j in range(1, len(a) - 1))
            minimum = min(minimum, slack) if minimum is not None else slack
            cases += 1
            if n <= 9:
                actual = brute_general_position(complement_adjacency(parts))
                assert actual == a, (n, parts, actual, a)
                brute += 1
        totals[n] = cases
        minimum_slack[n] = minimum
        brute_counts[n] = brute
    print('Finite graph types by n:', totals)
    print('Minimum exact LC slacks:', minimum_slack)
    print('Independent geodesic enumerations by n:', brute_counts)
    for n in range(14, 101):
        # Adversarial extremal component profiles, without claiming exhaustive
        for parts in ((('P', n),), (('C', n),),
                      tuple([('C', 3)] * (n // 3) +
                            ([('P', n % 3)] if n % 3 else [])),
                      tuple([('C', 4)] * (n // 4) +
                            ([('P', n % 4)] if n % 4 else []))):
            assert sum(k for _, k in parts) == n
            assert strict_lc(formula(parts)), (n, parts)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
