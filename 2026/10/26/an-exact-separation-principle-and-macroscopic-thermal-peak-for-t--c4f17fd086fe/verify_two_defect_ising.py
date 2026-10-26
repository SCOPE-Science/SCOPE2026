"""Independent finite-spin enumeration for a two-antiferromagnetic-bond Ising cycle.

Run: python verify_two_defect_ising.py
Python standard library only. Enumerations check finite instances, not the general proof.
"""
from fractions import Fraction
from itertools import product
from math import cosh, exp, tanh


def exact_formula(n, ell, t):
    assert n >= 4 and 1 <= ell < n and 0 <= t < 1
    return ((1 + t) * (1 - t ** n) / ((1 - t) * (1 + t ** n))
            - 8 * t * (1 - t ** ell) * (1 - t ** (n - ell)) /
            (n * (1 - t) ** 2 * (1 + t ** n)))


def exact_enumeration(n, ell, t):
    """Take exp(2 beta J)=(1+t)/(1-t), an integer for test parameters."""
    q = (1 + t) / (1 - t)
    assert q.denominator == 1
    q = int(q)
    signs = [1] * n
    signs[ell - 1] = -1
    signs[n - 1] = -1
    total = moment2 = 0
    for spins in product((-1, 1), repeat=n):
        matched = sum(signs[i] * spins[i] * spins[(i + 1) % n] == 1
                      for i in range(n))
        weight = q ** matched
        total += weight
        moment2 += weight * sum(spins) ** 2
    return Fraction(moment2, n * total)


def scaling_profile(x):
    return 2 * tanh(x / 2) / x - 8 * (1 - 1 / cosh(x / 2)) / x ** 2


def main():
    comparisons = 0
    for n in range(4, 13):
        for ell in range(1, n):
            for t in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
                calculated = exact_formula(n, ell, t)
                enumerated = exact_enumeration(n, ell, t)
                assert calculated == enumerated, (n, ell, t, calculated, enumerated)
                comparisons += 1
        vals = [exact_formula(n, ell, Fraction(1, 2))
                for ell in range(1, n // 2 + 1)]
        assert all(a > b for a, b in zip(vals, vals[1:]))
        for ell in range(1, n):
            assert exact_formula(n, ell, Fraction(1, 2)) == exact_formula(n, n - ell, Fraction(1, 2))
    for n in range(6, 24, 2):
        assert exact_formula(n, n // 2, Fraction(1, 100)) > 1
        assert exact_formula(n, n // 2, Fraction(0)) == 1
    x = 6.550654363681413
    target = scaling_profile(x)
    errors = []
    for n in (32, 64, 128, 256, 512, 1024):
        t = exp(-x / n)
        val = exact_formula(n, n // 2, t) / n
        errors.append(abs(val - target))
    assert all(a > b for a, b in zip(errors, errors[1:]))
    assert errors[-1] < 2e-6
    print(f"PASS: {comparisons} exact finite-state moment comparisons,"
          " cyclic separation inequalities, endpoint checks,"
          " and six convergent scaling comparisons")


if __name__ == '__main__':
    main()
