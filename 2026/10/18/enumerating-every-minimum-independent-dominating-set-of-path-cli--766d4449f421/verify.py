"""Reproduce independent-domination counts in path--clique tensor products.

Pure Python 3; no external packages required. Uses direct graph tests on small
instances and a separate finite-state row calculation on larger instances.
"""
from itertools import combinations
from collections import defaultdict
from math import comb


def predicted(n, q):
    if n < 2 or q < 2:
        raise ValueError('requires n,q >= 2')
    if q == 2:
        k = (n + 2) // 3
        return 2 * k, comb(k + 1, 3 * k - n) ** 2
    r = (n + 1) // 3
    t = n - 3 * r + 1
    minimum = n - r + 1
    multiplicity = comb(r + t - 1, t) * q * (q - 1) ** (r - 1)
    if n == q == 3:
        multiplicity += 1
    return minimum, multiplicity


def graph_direct(n, q):
    size = n * q
    neighbor = []
    for i in range(n):
        for a in range(q):
            mask = 0
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    for b in range(q):
                        if a != b:
                            mask |= 1 << (j * q + b)
            neighbor.append(mask)
    optimum, expected = predicted(n, q)
    # For small cases, prove there is no smaller independent dominating set.
    counts = {}
    for k in range(optimum + 1):
        good = 0
        for chosen in combinations(range(size), k):
            bits = sum(1 << v for v in chosen)
            if any(neighbor[v] & bits for v in chosen):
                continue
            covered = bits
            for v in chosen:
                covered |= neighbor[v]
            good += covered == (1 << size) - 1
        counts[k] = good
    assert counts[optimum] == expected, (n, q, counts, expected)
    assert all(counts[t] == 0 for t in range(optimum))


def row_dp(n, q):
    """Exhaustive valid row words over empty, full, and q singleton symbols."""
    E, F = -1, -2
    symbols = [E, F] + list(range(q))

    def independent(a, b):
        return a == E or b == E or (a >= 0 and a == b)

    def center_dominated(a, b, c):
        if b == F:
            return a == E and c == E
        if b >= 0:
            return a == b or c == b
        return a == F or c == F or (a >= 0 and c >= 0 and a != c)

    def cost(x):
        return q if x == F else int(x >= 0)

    dp = {(None, None): (0, 1)}
    for i in range(n):
        new = {}
        for (a, b), (weight, count) in dp.items():
            for c in symbols:
                if b is not None:
                    if not independent(b, c):
                        continue
                    if i == 1 and b == E and c != F:
                        continue
                    if i == 1 and b >= 0 and c != b:
                        continue
                    if i >= 2 and not center_dominated(a, b, c):
                        continue
                key = (b, c)
                nw = weight + cost(c)
                if key not in new or nw < new[key][0]:
                    new[key] = (nw, count)
                elif nw == new[key][0]:
                    old = new[key]
                    new[key] = (nw, old[1] + count)
        dp = new
    final = []
    for (a, b), (weight, count) in dp.items():
        if b == E and a != F:
            continue
        if b == F and a != E:
            continue
        if b >= 0 and a != b:
            continue
        final.append((weight, count))
    minimum = min(x for x, _ in final)
    return minimum, sum(y for x, y in final if x == minimum)


def main():
    direct_cases = [(2, n) for n in range(2, 11)]
    direct_cases += [(3, n) for n in range(2, 10)]
    direct_cases += [(4, n) for n in range(2, 8)]
    direct_cases += [(5, n) for n in range(2, 6)]
    for q, n in direct_cases:
        graph_direct(n, q)
    for q in range(2, 9):
        for n in range(2, 81):
            got = row_dp(n, q)
            expected = predicted(n, q)
            assert got == expected, (n, q, got, expected)
    print('VERIFIED: direct independent/dominating set checks,',
          len(direct_cases), 'small cases; finite-state checks,',
          7 * 79, 'additional parameter pairs')


if __name__ == '__main__':
    main()
