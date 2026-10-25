"""Exact arithmetic certificate for complete-bipartite polar edge-polytope Ehrhart data.

Usage: python3 verify.py
Only the Python standard library is required.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import product


def count_by_range(p, q, n):
    """Proven range decomposition of integer edge-Lipschitz potentials."""
    assert p >= 1 and q >= 1 and n >= 0
    h = 2 * n
    return (h + 1) ** q + sum(
        ((r + 1) ** p - 2 * r ** p + (r - 1) ** p) * (h + 1 - r) ** q
        for r in range(1, h + 1)
    )


def interpolate_coefficients(p, q):
    """Monomial coefficients, from exact Newton differences on d+1 samples."""
    d = p + q - 1
    values = [count_by_range(p, q, n) for n in range(d + 1)]
    differences = values[:]
    polynomial = [Fraction(0) for _ in range(d + 1)]
    falling_binomial = [Fraction(1)]
    for k in range(d + 1):
        delta_k = differences[0]
        for j, coefficient in enumerate(falling_binomial):
            polynomial[j] += delta_k * coefficient
        differences = [differences[j + 1] - differences[j]
                       for j in range(len(differences) - 1)]
        if k < d:
            shifted = [Fraction(0)] * (len(falling_binomial) + 1)
            for j, coefficient in enumerate(falling_binomial):
                shifted[j] -= Fraction(k) * coefficient
                shifted[j + 1] += coefficient
            falling_binomial = [c / (k + 1) for c in shifted]
    return polynomial


def count_by_direct_enumeration(p, q, n):
    """Independent lattice count; loops over actual first-part potentials."""
    total = 0
    for free_x in product(range(-2 * n, 2 * n + 1), repeat=p - 1):
        x = (0,) + free_x
        lo = max(x) - n
        hi = min(x) + n
        if lo <= hi:
            total += (hi - lo + 1) ** q
    return total


def check():
    classes = 0
    first_failure = []
    strict_positive_lower = 0
    header = 'p,q,dimension,coefficients_constant_to_leading'
    rows = [header]
    for d in range(1, 14):
        for p in range(1, (d + 1) // 2 + 1):
            q = d + 1 - p
            coefficients = interpolate_coefficients(p, q)
            assert len(coefficients) == d + 1
            assert coefficients[0] == 1
            assert coefficients[d] == Fraction(2**d * factorial(p) * factorial(q), factorial(d))
            negative = [(j, coefficients[j]) for j in range(1, d + 1)
                        if coefficients[j] <= 0]
            if d < 13:
                assert not negative, (d, p, q, negative)
                strict_positive_lower += 1
            elif negative:
                first_failure.append((p, q, negative))
            # Ehrhart-Macdonald reciprocity: Q is a reflexive lattice polytope.
            # Hence L(-n-1) = (-1)^d L(n) for this family.
            for n in (0, 1):
                lhs = sum(c * (-n - 1)**j for j, c in enumerate(coefficients))
                assert lhs == (-1)**d * count_by_range(p, q, n)
            rows.append(f'{p},{q},{d},"{';'.join(map(str,coefficients))}"')
            classes += 1
    assert classes == 49
    assert strict_positive_lower == 42
    assert first_failure == [(7, 7, [(1, Fraction(-7184, 715))])]
    # Independent low-dimensional enumeration using actual vertex-potentials.
    tests = 0
    for p in range(1, 5):
        for q in range(1, 5):
            for n in (0, 1, 2):
                assert count_by_direct_enumeration(p, q, n) == count_by_range(p, q, n)
                tests += 1
    c = interpolate_coefficients(7, 7)
    assert c[1] == -Fraction(7184, 715)
    assert all(x > 0 for x in c[2:])
    print('EXACT_OK classes=49 strict_positive_d_le_12=42 first_failures=1',
          'exception=K_7_7 c1=-7184/715 direct_counts=', tests)
    return rows


if __name__ == '__main__':
    check()
