#!/usr/bin/env python3
"""Exact finite checks for the root-count law of quadratic congruences."""
from collections import Counter


def prediction(p):
    assert p >= 2
    s0 = p * (p - 1)**2 // 2 + (p - 1)
    s1 = 2 * p * (p - 1)
    s2 = p * (p - 1)**2 // 2
    counts = Counter()
    counts[0] += (p**3 + 1) * s0 + p**3 * (p - 1)**2
    counts[1] += p**4 * (p - 1)
    counts[2] += p**3 * s2
    counts[p] += p**3 * (p - 1) + s1
    counts[2 * p] += s2
    counts[p * p] += 1
    assert sum(counts.values()) == p**6
    return counts


def enumerate_polynomials(p):
    m = p * p
    counts = Counter()
    for a in range(m):
        for b in range(m):
            for c in range(m):
                roots = sum((a * x * x + b * x + c) % m == 0 for x in range(m))
                counts[roots] += 1
    return counts


def check(p):
    all_coefficients = enumerate_polynomials(p)
    predicted = prediction(p)
    assert all_coefficients == predicted, (p, all_coefficients, predicted)
    assert sum(k * n for k, n in all_coefficients.items()) == p**6
    assert p * sum(k*k*n for k, n in all_coefficients.items()) == (3*p - 2) * p**6
    nonzero = all_coefficients.copy()
    nonzero[p*p] -= 1
    if not nonzero[p*p]:
        del nonzero[p*p]
    assert sum(nonzero.values()) == p**6-1
    assert sum(k * n for k, n in nonzero.items()) == p**6-p*p
    assert p * sum(k*k*n for k, n in nonzero.items()) == (3*p - 2)*p**6 - p**5
    return sum(all_coefficients.values())

if __name__ == '__main__':
    tests = (2, 3, 5, 7)
    tested = sum(check(p) for p in tests)
    print('VERIFY_OK primes=%d coefficient_vectors=%d full_root_enumeration=yes' % (len(tests), tested))
