#!/usr/bin/env python3
"""Exact finite checks for loop / parallel-edge dependence in uniform pairings.

Run with Python 3.9+ (standard library only): python verify.py
This is a finite diagnostic; the all-size statements use the separate proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def matchings(points):
    if not points:
        yield ()
        return
    x = points[0]
    for j in range(1, len(points)):
        y = points[j]
        for tail in matchings(points[1:j] + points[j + 1:]):
            yield ((x, y),) + tail


def compositions(s, k):
    if k == 1:
        yield (s,)
    else:
        for a in range(s + 1):
            for rest in compositions(s - a, k - 1):
                yield (a,) + rest


def exact_matching_moments(degrees):
    owners = []
    for i, d in enumerate(degrees):
        owners.extend([i] * d)
    totals = [0, 0, 0]
    count = 0
    for matching in matchings(tuple(range(len(owners)))):
        loops = 0
        cross_counts = {}
        for x, y in matching:
            i, j = owners[x], owners[y]
            if i == j:
                loops += 1
            else:
                key = (min(i, j), max(i, j))
                cross_counts[key] = cross_counts.get(key, 0) + 1
        parallel_pairs = sum(c * (c - 1) // 2 for c in cross_counts.values())
        totals[0] += loops
        totals[1] += parallel_pairs
        totals[2] += loops * parallel_pairs
        count += 1
    return tuple(Fraction(x, count) for x in totals)


def formulas(degrees):
    q = sum(degrees)
    assert q >= 6 and q % 2 == 0
    a = [d * (d - 1) // 2 for d in degrees]
    s = sum(a)
    b = sum(2 * a[i] * a[j] for i in range(len(a)) for j in range(i + 1, len(a)))
    t = sum(2 * a[i] * a[j] * ((2 * degrees[i] - 3) + (2 * degrees[j] - 3))
            for i in range(len(a)) for j in range(i + 1, len(a)))
    return (Fraction(s, q - 1),
            Fraction(b, (q - 1) * (q - 3)),
            Fraction(b * s - t, (q - 1) * (q - 3) * (q - 5)))


def reg_cov(v, r):
    assert v >= 2 and r >= 2 and v * r >= 6 and (v * r) % 2 == 0
    q = v * r
    a = r * (r - 1) // 2
    return Fraction(2 * v * (v - 1) * a * a * (q * (2 - r) + (2 * r - 3)),
                    (q - 1) ** 2 * (q - 3) * (q - 5))


def run():
    tests = 0
    pairings_total = 0
    for q in (6, 8, 10):
        for num_vertices in (2, 3, 4):
            for degrees in compositions(q, num_vertices):
                obs = exact_matching_moments(degrees)
                expected = formulas(degrees)
                for actual, correct in zip(obs, expected):
                    assert actual == correct, (degrees, actual, correct)
                    tests += 1
                pairings_total += 1
    for v in range(2, 10):
        for r in range(2, 12):
            q = v * r
            if q < 6 or q % 2:
                continue
            actual = formulas([r] * v)
            cov = actual[2] - actual[0] * actual[1]
            assert cov == reg_cov(v, r)
            tests += 1
            if r == 2:
                assert cov > 0
                tests += 1
            else:
                assert cov < 0
                tests += 1
    # The unique minimal two-vertex, degree-two exception has just three pairings.
    small = exact_matching_moments((2, 2))
    cov_small = small[2] - small[0] * small[1]
    assert small == (Fraction(2, 3), Fraction(2, 3), Fraction(0))
    assert cov_small == Fraction(-4, 9)
    tests += 2
    print(f'PASS: {tests} exact moment/formula/sign assertions')
    print(f'Enumerated {pairings_total} degree profiles with six, eight, or ten half-edges')
    print('Boundary: degree 2 on 2 vertices has covariance -4/9')
    print('Unbounded theorem requires the combinatorial proof, not these tests')


if __name__ == '__main__':
    run()
