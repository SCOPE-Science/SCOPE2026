"""Exact checks for fixed-point counts of random maps conditional on indegrees.

Run: python verification_fixedpoints.py.  Uses the Python standard library only.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def elementary(degrees):
    values = [0] * (len(degrees) + 1)
    values[0] = 1
    for d in degrees:
        for r in range(len(degrees), 0, -1):
            values[r] += d * values[r - 1]
    return values


def falling(n, r):
    return factorial(n) // factorial(n-r)


def predicted_distribution(degrees):
    n = len(degrees)
    e = elementary(degrees)
    coeff = [Fraction(e[r], falling(n, r)) for r in range(n+1)]
    return [sum(((-1)**(r-k) * comb(r, k) * coeff[r]
                  for r in range(k, n+1)), Fraction(0))
            for k in range(n+1)]


def exhaustive_check():
    profiles = 0
    mappings = 0
    for n in range(1, 7):
        counts = defaultdict(lambda: [0] * (n + 1))
        for images in product(range(n), repeat=n):
            deg = [0] * n
            fixed = 0
            for i, j in enumerate(images):
                deg[j] += 1
                fixed += (i == j)
            counts[tuple(deg)][fixed] += 1
            mappings += 1
        for deg, hist in counts.items():
            predicted = predicted_distribution(deg)
            observed = [Fraction(c, sum(hist)) for c in hist]
            assert observed == predicted, (n, deg, observed, predicted)
            assert sum(hist) == factorial(n) // __import__('math').prod(factorial(a) for a in deg)
            assert sum(k * p for k, p in enumerate(predicted)) == 1
            if n > 1:
                var = sum((k-1)**2 * p for k, p in enumerate(predicted))
                formula = Fraction(n*n-sum(a*a for a in deg), n*(n-1))
                assert var == formula
            for r in range(n+1):
                fact_moment = sum(falling(k, r) * predicted[k] for k in range(r, n+1))
                assert fact_moment == Fraction(factorial(r)*elementary(deg)[r], falling(n, r))
                assert fact_moment <= 1
            profiles += 1
    return profiles, mappings


def limiting_moments():
    examples = [
        ([1] * 600, [], 1.0),
        ([300] + [1] * 300 + [0] * 299, [0.5], 0.5),
        ([240, 180] + [1] * 180 + [0] * 418, [0.4, 0.3], 0.3),
        ([600] + [0] * 599, [1.0], 0.0),
    ]
    for d, masses, residual in examples:
        n = len(d)
        assert sum(d) == n
        e = elementary(d)
        for r in range(1, 5):
            empirical_factorial = float(Fraction(factorial(r)*e[r], falling(n, r)))
            # Coefficients of exp(residual*z)*product(1+p*z).
            poly = [1.0] + [0.0] * r
            for p in masses:
                for j in range(r, 0, -1):
                    poly[j] += p * poly[j-1]
            target = 0.0
            for j in range(r+1):
                target += poly[j] * residual**(r-j) / factorial(r-j)
            target *= factorial(r)
            assert abs(empirical_factorial-target) < 0.07, (masses, r, empirical_factorial, target)
    return len(examples)


if __name__ == '__main__':
    a, b = exhaustive_check()
    c = limiting_moments()
    print(f'PASS: {b} mappings across {a} exact degree profiles; {c} illustrative limiting profiles.')
