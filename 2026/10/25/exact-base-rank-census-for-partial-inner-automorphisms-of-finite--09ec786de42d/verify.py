#!/usr/bin/env python3
"""Independent exact checks for a rank census of finite partial-inner automorphisms.

Pure Python 3, no dependencies. Does not rely on any external files.
The general statement is proved mathematically in RESULT.md; the checks are finite.
"""
from collections import defaultdict, deque
from itertools import permutations, product
from math import comb, factorial


def stirling_rows(n):
    rows = [[1]]
    for a in range(1, n + 1):
        prev = rows[-1]
        row = [0] * (a + 1)
        for b in range(1, a + 1):
            row[b] = (prev[b - 1] if b - 1 < len(prev) else 0) + (b * prev[b] if b < len(prev) else 0)
        rows.append(row)
    return rows


def theoretical(n):
    if n == 1:
        return (0, 1)
    S = stirling_rows(n)
    ans = [1, n * n] + [0] * (n - 1)
    for k in range(2, n + 1):
        m = n - k
        contribution = 0
        for q in range(1, k + 1):
            if not S[k][q]:
                continue
            ext = []
            for t in range(m + 1):
                ext.append(sum(comb(m, j) * q ** (m - j) * S[j][t]
                               for j in range(t, m + 1)))
            contribution += S[k][q] * (sum(factorial(t) * u * u for t, u in enumerate(ext))
                                         - factorial(m))
        ans[k] = comb(n, k) ** 2 * factorial(k) * contribution
        if k == n:
            ans[k] += factorial(n)
    return tuple(ans)


def partitions(n):
    blocks = []
    def rec(i):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from rec(i + 1)
            blocks[j].pop()
        blocks.append([i])
        yield from rec(i + 1)
        blocks.pop()
    yield from rec(0)


def direct_paired_partition_census(n):
    """Enumerate every compatible ordered pair of partitions with a block bijection.

    Local coefficients enumerate matched marked subsets, independently of the
    formula using extensions of a fixed marked partition.
    """
    by_r = defaultdict(list)
    for P in partitions(n):
        by_r[len(P)].append(P)
    distribution = [0] * (n + 1)
    for group in by_r.values():
        r = len(group[0])
        for P in group:
            for Q in group:
                for beta in permutations(range(r)):
                    polynomial = [1]
                    for i, B in enumerate(P):
                        a, b = len(B), len(Q[beta[i]])
                        local = [comb(a, c) * comb(b, c) * factorial(c)
                                 for c in range(min(a, b) + 1)]
                        nxt = [0] * (len(polynomial) + len(local) - 1)
                        for j, x in enumerate(polynomial):
                            for h, y in enumerate(local):
                                nxt[j + h] += x * y
                        polynomial = nxt
                    for k in range(2, min(len(polynomial), n + 1)):
                        distribution[k] += polynomial[k]
    bell = [sum(1 for _ in partitions(k)) for k in range(n + 1)]
    for k in range(2, n + 1):
        distribution[k] -= comb(n, k) ** 2 * factorial(k) * bell[k] * factorial(n - k)
    distribution[n] += factorial(n)
    distribution[0] = 1 if n > 1 else 0
    distribution[1] = n * n
    return tuple(distribution)


def direct_semigroup_closure(n):
    """Enumerate generators on T_n and close them under composition (n=2,3)."""
    T = list(product(range(n), repeat=n))
    ids = {f: i for i, f in enumerate(T)}
    m = len(T)
    prod = [[ids[tuple(g[f[x]] for x in range(n))] for g in T] for f in T]
    generators = set()
    for g in range(m):
        for h in range(m):
            gh = prod[g][h]
            partial = [-1] * m
            for a in range(m):
                if prod[gh][a] == a and prod[a][gh] == a:
                    partial[a] = prod[prod[h][a]][g]
            generators.add(tuple(partial))
    known = set(generators)
    frontier = deque(generators)
    while frontier:
        f = frontier.popleft()
        for g in tuple(known):
            for a, b in [(f, g), (g, f)]:
                z = tuple(-1 if v < 0 else b[v] for v in a)
                if z not in known:
                    known.add(z)
                    frontier.append(z)
        assert len(known) < 10000, 'Unexpected blowup in small-n calculation'
    return len(known), len(generators)


def main():
    expected = {
        1: (0, 1),
        2: (1, 4, 2),
        3: (1, 9, 90, 6),
        4: (1, 16, 3672, 2112, 24),
        5: (1, 25, 141800, 157800, 59400, 120),
        6: (1, 36, 6202350, 10245600, 7635600, 2034720, 720),
    }
    for n, row in expected.items():
        assert theoretical(n) == row
        if n <= 5:
            assert direct_paired_partition_census(n) == row
    assert direct_semigroup_closure(2) == (7, 7)
    assert direct_semigroup_closure(3) == (106, 88)
    for n in range(3, 7):
        S = stirling_rows(n + 1)
        B = [sum(x) for x in S]
        assert theoretical(n)[n - 1] == n ** 2 * factorial(n - 1) * (B[n + 1] - 2 * B[n])
    print('VERIFY_OK formula_n=1..6 paired_partitions_n=1..5 raw_semigroup_n=2,3')
    for n in range(1, 7):
        print('n=%d ranks=%s total=%d' % (n, theoretical(n), sum(theoretical(n))))


if __name__ == '__main__':
    main()
