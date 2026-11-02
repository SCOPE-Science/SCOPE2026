"""Independent signed-run enumeration and rational identity for fan orientations.
Run: python run_transfer_check.py (stdlib only).
"""
from collections import Counter


def path_extremum_polynomial(length):
    # Directly orient the path edges; count sources from indegree zero.
    counts = Counter()
    for mask in range(1 << (length - 1)):
        indeg = [0] * length
        for i in range(length - 1):
            if (mask >> i) & 1:
                indeg[i + 1] += 1
            else:
                indeg[i] += 1
        counts[sum(x == 0 for x in indeg)] += 1
    return counts


def add_scaled(dst, src, offset, mult):
    for j, v in src.items():
        dst[j + offset] += mult * v


def compositions_weighted(n):
    # Two initial spoke signs, followed by arbitrary run composition;
    # independent of the proposed rational coefficient formula.
    run_poly = {}
    for ell in range(1, n + 1):
        run_poly[ell] = {j + ell - 1: c for j, c in path_extremum_polynomial(ell).items()}
    dp = [Counter() for _ in range(n + 1)]
    dp[0][0] = 1
    for k in range(1, n + 1):
        for ell in range(1, k + 1):
            for a, x in dp[k - ell].items():
                for b, y in run_poly[ell].items():
                    dp[k][a + b] += x * y
    return {degree: 2 * count for degree, count in dp[n].items()}


def rational_coefficient(n):
    # From 2tz/(1-3tz+(1-t)t^2 z^2), calculate the coefficients in z.
    prev2, prev1 = {}, {1: 2}
    if n == 1:
        return prev1
    for k in range(2, n + 1):
        nxt = Counter()
        for j, v in prev1.items():
            nxt[j + 1] += 3 * v
        for j, v in prev2.items():
            nxt[j + 2] -= v
            nxt[j + 3] += v
        prev2, prev1 = prev1, {j: v for j, v in nxt.items() if v}
    return prev1


def fib(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    for n in range(1, 12):
        d = compositions_weighted(n)
        r = rational_coefficient(n)
        assert d == r, (n, d, r)
        assert d.get(n) == 2 * fib(2 * n)
        assert sum(d.values()) == 2 * 3 ** (n - 1)
        print(n, 'number', sum(d.values()), 'simple', d[n], 'maxdegree', max(d))
    for n in range(12, 70):
        r = rational_coefficient(n)
        assert sum(r.values()) == 2 * 3 ** (n - 1)
        assert r[n] == 2 * fib(2 * n)
        assert max(r) == n + (n - 1) // 2
        assert r[max(r)] == (2 if n % 2 else 3 * n)
        assert all(v > 0 for v in r.values())
    print('SIGNED_RUN_RATIONAL_GENERATING_FUNCTION_PASS')
