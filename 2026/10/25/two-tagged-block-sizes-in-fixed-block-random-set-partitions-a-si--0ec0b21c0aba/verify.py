"""Exact independent checks for tagged-block sizes in fixed-block uniform set partitions.

Run: python verify.py
Uses Python standard library only; comparisons use integer arithmetic.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def stirling(n):
    s = [[0] * (n + 1) for _ in range(n + 1)]
    s[0][0] = 1
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            s[i][k] = s[i - 1][k - 1] + k * s[i - 1][k]
    return s


def partitions(n):
    """Generate all partitions of [n] in restricted-growth-string representation."""
    def rec(a, maximum):
        if len(a) == n:
            yield tuple(a)
        else:
            for j in range(maximum + 2):
                a.append(j)
                yield from rec(a, max(j, maximum))
                a.pop()
    yield from rec([0], 0)


def joint_count(n, k, x, y, same, s):
    if same:
        if x != y or not (2 <= x <= n):
            return 0
        return comb(n - 2, x - 2) * s[n - x][k - 1]
    if x < 1 or y < 1 or x + y > n:
        return 0
    return comb(n - 2, x - 1) * comb(n - x - 1, y - 1) * s[n - x - y][k - 2]


def covariance_formula(n, k, s):
    z = s[n][k]
    a = Fraction(s[n - 1][k], z)
    t = Fraction(s[n - 2][k], z)
    return a + n * (n - 2) * t - (n - 1)**2 * a*a


def main():
    assertions = 0
    s = stirling(150)
    for n in range(2, 10):
        observed = {k: Counter() for k in range(1, n + 1)}
        for p in partitions(n):
            k = max(p) + 1
            x = sum(v == p[0] for v in p)
            y = sum(v == p[1] for v in p)
            observed[k][(x, y, p[0] == p[1])] += 1
        for k, counts in observed.items():
            assert sum(counts.values()) == s[n][k]
            assertions += 1
            for x in range(1, n + 1):
                for y in range(1, n + 1):
                    for same in (False, True):
                        expected = joint_count(n, k, x, y, same, s)
                        assert counts.get((x, y, same), 0) == expected, (n,k,x,y,same,expected)
                        assertions += 1
            denom = s[n][k]
            ex = sum(x*c for (x,y,same), c in counts.items())
            ey = sum(y*c for (x,y,same), c in counts.items())
            exy = sum(x*y*c for (x,y,same), c in counts.items())
            cov = Fraction(exy, denom) - Fraction(ex, denom)*Fraction(ey, denom)
            assert cov == covariance_formula(n, k, s), (n,k,cov,covariance_formula(n,k,s))
            assertions += 1
    for n in range(3, 150):
        d = 2 ** (n - 1) - 1
        two = Fraction(2**(n-3) * (2**(n-1)-n*(n-2)-2), d*d)
        assert covariance_formula(n, 2, s) == two
        assert (two > 0) == (n >= 6)
        assert (two < 0) == (n <= 5)
        onepair = Fraction(-2*(n-2), n*n*(n-1))
        assert covariance_formula(n, n-1, s) == onepair
        assertions += 4
    for k in range(2, 8):
        for n in (k, k+1, k+5, 50, 100):
            if n < k: continue
            # The conditioning error tends to zero exponentially for fixed k;
            # the exact finite expression is checked against a generous proved bound.
            v = covariance_formula(n, k, s)
            u = Fraction(k-1, k*k)
            p_fail_bound = Fraction(k*(k-1)**n, k**n)
            if p_fail_bound < 1:
                bound = Fraction(6*n*n) * p_fail_bound / (1-p_fail_bound)
                assert abs(v-u) <= bound, (n,k,v,u,bound)
                assertions += 1
    print('PASS: exact independent assertions:', assertions)


if __name__ == '__main__':
    main()
