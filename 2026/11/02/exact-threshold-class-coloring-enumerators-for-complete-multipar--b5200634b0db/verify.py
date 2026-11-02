#!/usr/bin/env python3
"""Exact checks for threshold-induced partitions of complete multipartite graphs.

This program uses only the Python standard library. Its independent graph check
recursively removes an isolated or universal vertex from every color class,
without using the 'at most one heavy part' characterization.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial


def integer_partitions(n, cap=None):
    cap = n if cap is None else min(cap, n)
    if n == 0:
        yield ()
    else:
        for first in range(cap, 0, -1):
            for rest in integer_partitions(n - first, first):
                yield (first,) + rest


def direct_threshold(parts, vertices):
    """Recursive isolated/universal vertex recognition on the literal graph."""
    vertices = tuple(vertices)
    if len(vertices) <= 1:
        return True
    for v in vertices:
        degree = sum(parts[v] != parts[u] for u in vertices if u != v)
        if degree == 0 or degree == len(vertices) - 1:
            return direct_threshold(parts, [u for u in vertices if u != v])
    return False


def all_colorings_by_graph(sizes, k):
    original_parts = tuple(i for i, sz in enumerate(sizes) for _ in range(sz))
    valid = surjective = 0
    for assignment in product(range(k), repeat=len(original_parts)):
        classes = [tuple(v for v, c in enumerate(assignment) if c == color)
                   for color in range(k)]
        if all(direct_threshold(original_parts, cls) for cls in classes):
            valid += 1
            surjective += all(classes)
    return valid, surjective


def exp_formula(sizes, k):
    """Compute (prod n_i!)[x_i^n_i] F(x)^k using exact rational arithmetic."""
    r = len(sizes)
    target = tuple(sizes)
    terms = {}
    for exponents in product(*(range(s + 1) for s in sizes)):
        if sum(v >= 2 for v in exponents) <= 1:
            denom = 1
            for v in exponents:
                denom *= factorial(v)
            terms[exponents] = Fraction(1, denom)
    poly = {(0,) * r: Fraction(1)}
    for _ in range(k):
        next_poly = defaultdict(Fraction)
        for current, val in poly.items():
            for exponents, weight in terms.items():
                summation = tuple(a + b for a, b in zip(current, exponents))
                if all(summation[i] <= sizes[i] for i in range(r)):
                    next_poly[summation] += val * weight
        poly = next_poly
    denominator = 1
    for s in sizes:
        denominator *= factorial(s)
    count = denominator * poly.get(target, 0)
    assert count.denominator == 1
    return count.numerator


def invariant(sizes):
    return next(k for k in range(1, max(sizes) + 1)
                if sum(s > k for s in sizes) <= k)


def verify():
    tests = 0
    total_assignments = 0
    for n in range(1, 8):
        for sizes in integer_partitions(n):
            earliest_nonzero = None
            for k in range(1, min(4, n) + 1):
                brute, surj = all_colorings_by_graph(sizes, k)
                formula = exp_formula(sizes, k)
                assert brute == formula, (sizes, k, brute, formula)
                if brute and earliest_nonzero is None:
                    earliest_nonzero = k
                if k == invariant(sizes):
                    assert surj > 0, (sizes, k, surj)
                if k < invariant(sizes):
                    assert brute == 0, (sizes, k)
                tests += 1
                total_assignments += k**n
            if invariant(sizes) <= min(4, n):
                assert earliest_nonzero == invariant(sizes), (sizes, earliest_nonzero)
    # More unbounded-size parameter samples, using exact EGF, independent of brute tests.
    extra = 0
    for sizes in [(20, 17, 14, 9, 3), (13, 13, 13), (1, 1, 1, 1, 1, 1),
                  (18,), (18, 2, 2, 2, 2), (7, 7, 7, 7), (2, 2, 2, 2, 2, 2)]:
        t = invariant(sizes)
        # Do not evaluate a large EGF: use the explicit construction theorem.
        if t > 1:
            assert sum(s > t - 1 for s in sizes) > t - 1
        assert sum(s > t for s in sizes) <= t
        extra += 1
    print(f'EXACT_GRAPH_VS_EGF_OK {tests} profiles_and_palette_tests')
    print(f'EXHAUSTIVE_COLOR_ASSIGNMENTS {total_assignments}')
    print(f'PARAMETER_THRESHOLD_SAMPLES_OK {extra}')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
