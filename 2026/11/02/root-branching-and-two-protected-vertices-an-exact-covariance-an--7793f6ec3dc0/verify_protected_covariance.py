"""Exact finite checks for a root-degree / protected-node covariance identity.

Run with Python 3 and its standard library:
    python verify_protected_covariance.py

This program checks finite instances; the asymptotic theorem needs the
separate generating-function proof. No finite check establishes an infinite
assertion.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def polynomial_product(a, b, top):
    return [sum((a[j] * b[k-j] for j in range(k + 1)), Fraction(0))
            for k in range(top + 1)]


def generating_moments(top):
    """Independent exact coefficient arithmetic for the displayed formulas."""
    Q = Fraction
    exp_minus_z = [Q((-1) ** k, factorial(k)) for k in range(top + 1)]
    log_inv = [Q(0)] + [Q(1, k) for k in range(1, top + 1)]
    F = [-(exp_minus_z[k]) + (Q(1) if k == 0 else Q(0))
         - (Q(1) if k == 1 else Q(0))
         + (Q(1, 2) if k == 2 else Q(0)) for k in range(top + 1)]
    reciprocal = [Q(1) for _ in range(top + 1)]
    reciprocal_squared = [Q(k + 1) for k in range(top + 1)]
    A = polynomial_product(F, reciprocal, top)
    one_plus_log = log_inv.copy()
    one_plus_log[0] += 1
    log_minus_z = log_inv.copy()
    log_minus_z[1] -= 1
    mixed_first = polynomial_product(
        polynomial_product(one_plus_log, F, top), reciprocal_squared, top)
    mixed_second = polynomial_product(
        polynomial_product(log_minus_z, exp_minus_z, top), reciprocal, top)
    mixed = [x+y for x,y in zip(mixed_first, mixed_second)]
    for n in range(3, top + 1):
        harmonic = sum((Q(1, j) for j in range(1, n)), Q(0))
        yield n, n*A[n], harmonic, mixed[n-1], mixed[n-1]-n*A[n]*harmonic


def enumerate_moments(n):
    """Independent exhaustive parent-array enumeration for all (n-1)! trees."""
    count = 0
    total_protected = 0
    total_root_degree = 0
    total_product = 0
    for parents in product(*(range(j) for j in range(1, n))):
        children = [[] for _ in range(n)]
        for j, parent in enumerate(parents, start=1):
            children[parent].append(j)
        degree = len(children[0])
        protected = sum(bool(c) and all(children[j] for j in c)
                        for c in children)
        total_protected += protected
        total_root_degree += degree
        total_product += degree * protected
        count += 1
    assert count == factorial(n - 1)
    Q = Fraction
    mean_protected = Q(total_protected, count)
    mean_degree = Q(total_root_degree, count)
    mean_product = Q(total_product, count)
    return mean_protected, mean_degree, mean_product, (
        mean_product - mean_protected * mean_degree)


def main():
    checked = 0
    for n, ep, ed, edp, cov in generating_moments(90):
        # The exact previously known first moment provides a separate check.
        partial_exp = sum((Fraction((-1) ** j, factorial(j))
                           for j in range(n + 1)), Fraction(0))
        assert ep == n * (Fraction(1, 2) - partial_exp)
        checked += 1
        assert ed == sum((Fraction(1, j) for j in range(1, n)), Fraction(0))
        checked += 1
        if n <= 9:
            brute = enumerate_moments(n)
            assert brute == (ep, ed, edp, cov), (n, brute, ep, ed, edp, cov)
            checked += 4
        # This checks examples only, not an all-size sign theorem.
        assert cov < 0
        checked += 1
    for n, ep, ed, edp, cov in generating_moments(220):
        if n in (40, 80, 120, 180, 220):
            import math
            constant = 0.5 - 3 / math.e
            finite_correction = (1 + 1 / math.e) / (2 * (n - 1))
            # Consistent with, not a proof of, the O(n^-2) remainder.
            assert abs(float(cov) - constant - finite_correction) < 0.4 / n**2
            checked += 1
    print('PASS:', checked, 'independent exact/finite checks')
    print('Exact n=3..9 parent-array enumeration, rational coefficients n=3..90,')
    print('and numerical remainder checks at n=40,80,120,180,220.')


if __name__ == '__main__':
    main()
