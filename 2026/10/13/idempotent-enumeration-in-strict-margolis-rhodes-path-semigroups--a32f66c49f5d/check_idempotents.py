#!/usr/bin/env python3
from itertools import product
from math import factorial


def is_edge_subset(s, n):
    if len(s) != 2:
        return False
    a, b = sorted(s)
    return b == a + 1 and 0 <= a < n - 1


def is_simplex(s, n):
    return len(s) == 0 or len(s) == 1 or is_edge_subset(s, n)


def direct_rank_counts(n):
    """Enumerate every partial self-map of P_n and test the definitions."""
    counts = {}
    # -1 denotes undefined.
    for vals in product(range(-1, n), repeat=n):
        fibers = []
        ok = True
        for y in range(n):
            fib = {x for x, v in enumerate(vals) if v == y}
            if fib and not is_edge_subset(fib, n):
                ok = False
                break
            fibers.append(fib)
        if not ok:
            continue

        # Full inverse image of each target edge must be a simplex or empty.
        for y in range(n - 1):
            if not is_simplex(fibers[y] | fibers[y + 1], n):
                ok = False
                break
        if not ok:
            continue

        # Equality f^2=f as partial maps: every image point is defined and fixed.
        domain = {x for x, v in enumerate(vals) if v >= 0}
        for x in domain:
            y = vals[x]
            if y not in domain or vals[y] != y:
                ok = False
                break
        if not ok:
            continue

        rank = len({v for v in vals if v >= 0})
        counts[rank] = counts.get(rank, 0) + 1
    return counts


def closed_count(n, k):
    if k < 0 or 2 * k > n:
        return 0
    ans = 0
    for j in range(k // 2 + 1):
        ans += ((-1) ** j) * (2 ** (k - 2*j)) * factorial(n-k-j) // (
            factorial(n-2*k) * factorial(k-2*j) * factorial(j)
        )
    return ans


def polynomial_counts(N):
    polys = [[1], [1], [1, 2], [1, 4]]
    while len(polys) <= N:
        n = len(polys)
        deg = n // 2
        cur = [0] * (deg + 1)
        # I_{n-1}
        for k, c in enumerate(polys[n-1]):
            cur[k] += c
        # 2 y I_{n-2}
        for k, c in enumerate(polys[n-2]):
            if k + 1 < len(cur):
                cur[k+1] += 2*c
        # - y^2 I_{n-4}
        for k, c in enumerate(polys[n-4]):
            if k + 2 < len(cur):
                cur[k+2] -= c
        polys.append(cur)
    return polys[:N+1]


expected_direct = {
    1: {0: 1},
    2: {0: 1, 1: 2},
    3: {0: 1, 1: 4},
    4: {0: 1, 1: 6, 2: 3},
    5: {0: 1, 1: 8, 2: 10},
    6: {0: 1, 1: 10, 2: 21, 3: 4},
}
for n, expected in expected_direct.items():
    got = direct_rank_counts(n)
    assert got == expected, (n, got, expected)

polys = polynomial_counts(14)
for n in range(15):
    formula = [closed_count(n, k) for k in range(n//2 + 1)]
    assert polys[n] == formula, (n, polys[n], formula)

expected_totals = [1, 1, 3, 5, 10, 19, 36, 69, 131, 250, 476, 907, 1728]
assert [sum(polys[n]) for n in range(len(expected_totals))] == expected_totals

print('DIRECT_TOTALS', [sum(expected_direct[n].values()) for n in range(1, 7)])
print('RANKS_P6', [expected_direct[6].get(k, 0) for k in range(4)])
print('FORMULA_TOTALS', expected_totals)
print('CHECK_OK')
