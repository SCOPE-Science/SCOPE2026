"""Exact rational tests for two-coordinate actuation of a damped directed ring.

This finite checker supplements, and does not replace, the analytical proof.
Run: python3 check.py
"""
from fractions import Fraction
from math import prod


def gramian_diagonal(n, t, a, cycles=None):
    """Sum coordinate contributions independently; cycles=None means infinity."""
    F = Fraction(1, 1) / (1 - t**n) if cycles is None else sum(t**(ell*n) for ell in range(cycles))
    return [F * (t**((j-0) % n) + t**((j-a) % n)) for j in range(n)]


def formulas(n, t, a, cycles=None):
    b = n - a
    F = Fraction(1, 1) / (1 - t**n) if cycles is None else sum(t**(ell*n) for ell in range(cycles))
    top = F * (1 + t**min(a,b))
    bottom = F * t**(max(a,b)-1) * (1 + t**min(a,b))
    determinant = (F**n * t**((a*(a-1) + b*(b-1)) // 2)
                   * (1 + t**b)**a * (1 + t**a)**b)
    trace_inverse = (1/F) * (sum(t**(-j) for j in range(a))/(1+t**b)
                             + sum(t**(-j) for j in range(b))/(1+t**a))
    condition = t**(-(max(a,b)-1))
    return bottom, top, determinant, trace_inverse, condition


def run():
    checks = 0
    for n in range(3, 13):
        for t in [Fraction(1, 9), Fraction(1, 4), Fraction(4, 9), Fraction(9, 16)]:
            for cycles in [1, 2, 3, None]:
                records = []
                for a in range(1, n):
                    D = gramian_diagonal(n, t, a, cycles)
                    actual = min(D), max(D), prod(D), sum(1/z for z in D), max(D)/min(D)
                    expected = formulas(n, t, a, cycles)
                    assert actual == expected, (n, t, a, cycles, actual, expected)
                    checks += 1
                    records.append(actual)
                target = records[n//2-1]
                for a, m in enumerate(records, start=1):
                    balanced = min(a, n-a) == n//2
                    comparisons = [m[0] <= target[0], m[2] <= target[2],
                                   m[3] >= target[3], m[4] >= target[4]]
                    assert all(comparisons), (n, t, a, cycles, 'optimization', comparisons)
                    if not balanced:
                        assert m[0] < target[0] and m[2] < target[2]
                        assert m[3] > target[3] and m[4] > target[4]
                        checks += 1
                assert sum(D) == 2 * (sum(t**j for j in range(n*cycles)) if cycles is not None
                                       else 1/(1-t))
                checks += 1
    # Exact finite-horizon Gramian construction from time steps (not merely residue formulas).
    for n in range(3, 10):
        for a in range(1, n):
            for t in [Fraction(1, 4), Fraction(4, 9)]:
                for cycles in [1, 2, 3]:
                    actual = [sum(t**k for k in range(n*cycles) if (k % n) == ((j-s) % n))
                              for j in range(n) for s in [0, a]]
                    merged = [actual[2*j] + actual[2*j+1] for j in range(n)]
                    assert merged == gramian_diagonal(n, t, a, cycles)
                    checks += 1
    # An 8-node ring: balancing reduces condition number from 4096 to 64.
    assert formulas(8, Fraction(1, 4), 1)[-1] == 4096
    assert formulas(8, Fraction(1, 4), 4)[-1] == 64
    print('VERIFY_OK', checks, 'exact rational comparisons and finite-time direct sums')


if __name__ == '__main__':
    run()
