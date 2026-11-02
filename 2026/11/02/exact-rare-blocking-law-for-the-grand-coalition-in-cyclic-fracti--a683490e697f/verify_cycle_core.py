"""Exact checks for the cycle coalition-blocking count.

Requires Python 3.9+ standard library only. The finite checks test identities
and boundary conventions; the infinite-size asymptotic follows separately
from the proof in RESULT.md.
"""
from math import comb, exp, log, pi, sqrt


def count_runs(n):
    """Enumerate circular runs combinatorially using exact integers."""
    total = 0
    for s in range(2, (n - 1) // 2 + 1):
        for r in range(1, min(s // 2, n - s) + 1):
            numerator = n * comb(s - r - 1, r - 1) * comb(n - s - 1, r - 1)
            assert numerator % r == 0
            total += numerator // r
    return total


def count_direct(n):
    """Directly compare every member's coalition payoff, not a run proxy."""
    total = 0
    for mask in range(1, 1 << n):
        size = mask.bit_count()
        if all(
            n * (((mask >> ((i - 1) % n)) & 1) +
                 ((mask >> ((i + 1) % n)) & 1)) > 2 * size
            for i in range(n) if (mask >> i) & 1
        ):
            total += 1
    return total


def count_matrix(n):
    """Trace of transfer matrix via its characteristic recurrence."""
    polynomials = [[3], [1, 1], [1, 0, 1]]
    for _ in range(3, n + 1):
        a, b, c = polynomials[-1], polynomials[-2], polynomials[-3]
        p = [0] * (max(len(a) + 1, len(b) + 1, len(c) + 2))
        for j, x in enumerate(a):
            p[j] += x
            p[j + 1] += x
        for j, x in enumerate(b):
            p[j + 1] -= x
        for j, x in enumerate(c):
            p[j + 2] += x
        assert all(x >= 0 for x in p)
        polynomials.append(p)
    return sum(polynomials[n][:((n - 1) // 2) + 1]) - 1


def asymptotic_log(n):
    delta = 1 if n % 2 == 0 else 0.5
    return (0.5 * n * log(3) + log(4) + delta * log(3 / 4)
            + 0.5 * log(3 / (2 * pi * n)))


def main():
    exact_direct = 0
    for n in range(3, 19):
        a, b, c = count_direct(n), count_runs(n), count_matrix(n)
        assert a == b == c, (n, a, b, c)
        exact_direct += 1
    exact_matrix = 0
    for n in range(3, 151):
        assert count_runs(n) == count_matrix(n), n
        exact_matrix += 1
    for n in (400, 401, 1000, 1001):
        actual = count_matrix(n)
        ratio = exp(log(actual) - asymptotic_log(n))
        print('finite asymptotic illustration:', n, round(ratio, 8))
        assert 0.85 < ratio < 1.1
    print('PASS: %d direct-payoff and %d matrix-versus-run exact cases'
          % (exact_direct, exact_matrix))


if __name__ == '__main__':
    main()
