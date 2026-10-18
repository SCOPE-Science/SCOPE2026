"""Standalone exact checks for recursive-tree early-leaf point-process identities.
Run with: python3 verify.py
No external dependencies or random sampling.
"""
from fractions import Fraction
from itertools import product, combinations
from math import factorial, isqrt


def predicted(n, subset):
    ordered = sorted(subset)
    if any(i < 2 or i > n for i in ordered):
        raise ValueError('Leaf labels must be in 2..n')
    numerator = 1
    denominator = 1
    for j, i in enumerate(ordered, 1):
        numerator *= (i-j)
        denominator *= (n-j)
    return Fraction(numerator, denominator)


def independent_attachment_product(n, subset):
    answer = Fraction(1)
    for t in range(2, n+1):
        forbidden = sum(i < t for i in subset)
        answer *= Fraction(t-1-forbidden, t-1)
    return answer


def leaf_set(n, parents):
    used = set(parents)
    return set(range(2, n+1)) - used


def exhaustive(n):
    counts = {}
    total = 0
    for parents in product(*(range(1, j) for j in range(2, n+1))):
        total += 1
        leaves = leaf_set(n, parents)
        for k in range(len(leaves)+1):
            for subset in combinations(sorted(leaves), k):
                counts[subset] = counts.get(subset, 0) + 1
    assert total == factorial(n-1)
    tests = 0
    for r in range(n):
        for subset in combinations(range(2, n+1), r):
            actual = Fraction(counts.get(subset, 0), total)
            assert actual == predicted(n, subset), (n, subset, actual, predicted(n, subset))
            assert actual == independent_attachment_product(n, subset)
            marginal_product = Fraction(1)
            for i in subset:
                marginal_product *= predicted(n, (i,))
            assert actual <= marginal_product
            tests += 1
    return tests


def bounded_distinct_factorial_moments(n, cutoff, order):
    labels = range(2, min(cutoff, n)+1)
    ans = Fraction(0)
    for subset in combinations(labels, order):
        ans += predicted(n, subset)
    return factorial(order)*ans


def main():
    checks = 0
    for n in range(2, 9):
        checks += exhaustive(n)
    for n in (15, 25, 45):
        labels = range(2, n+1)
        for r in (1, 2, 3):
            for subset in combinations(labels, r):
                assert predicted(n, subset) == independent_attachment_product(n, subset)
                checks += 1
    for n in (1000, 4000, 16000):
        m = isqrt(n-1)
        mean = bounded_distinct_factorial_moments(n, m+1, 1)
        assert abs(float(mean) - 0.5) < 0.035
        second = bounded_distinct_factorial_moments(n, m+1, 2)
        assert abs(float(second) - 0.25) < 0.040
        checks += 2
    print('PASS:',checks,'exact/computational consistency assertions')
    print('Finite-n identities are exact. The infinite Poisson convergence is proved analytically, not by these tests.')

if __name__ == '__main__':
    main()
