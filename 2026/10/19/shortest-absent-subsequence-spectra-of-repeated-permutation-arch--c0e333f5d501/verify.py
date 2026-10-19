#!/usr/bin/env python3
"""Exact finite checks for shortest absent subsequences of repeated permutation arches."""
from itertools import permutations, product
from math import comb

def polynomial_count(q, t, pi):
    pos = [0] * (q + 1)
    for i, v in enumerate(pi, 1):
        pos[v] = i
    return sum(comb(q - v + t, t) * pos[v] for v in range(1, q + 1))

def is_subsequence(u, w):
    it = iter(w)
    return all(any(ch == wanted for ch in it) for wanted in u)

def direct_count(q, t, pi):
    word = tuple(range(1, q + 1)) * t + pi
    return sum(not is_subsequence(u, word)
               for u in product(range(1, q + 1), repeat=t + 2))

# Independent direct subsequence test, not using the absent-triple criterion.
checked = 0
for q in range(1, 5):
    for t in range(1, 4):
        for p in permutations(range(1, q + 1)):
            a = polynomial_count(q, t, p)
            b = direct_count(q, t, p)
            assert a == b, (q, t, p, a, b)
            checked += 1

# All permutations, not random samples, for the complete length-four spectrum.
expected = {
    1: (1, 1, []),
    2: (5, 7, [6]),
    3: (15, 25, [16, 19, 20, 21, 24]),
}
for q in range(1, 8):
    values = {polynomial_count(q, 2, p)
              for p in permutations(range(1, q + 1))}
    lo = min(values); hi = max(values)
    gaps = sorted(set(range(lo, hi + 1)) - values)
    print('q', q, 'interval', lo, hi, 'support', len(values), 'gaps', gaps)
    if q in expected:
        assert (lo, hi, gaps) == expected[q]
    if q in (6, 7):
        assert gaps == [lo + 1, hi - 1]
    assert lo == comb(q + 3, 4)
    assert lo == polynomial_count(q, 2, tuple(range(1, q + 1)))
    assert hi == polynomial_count(q, 2, tuple(range(q, 0, -1)))

print('ALL_SAS_ARCH_SPECTRUM_CHECKS_PASSED independent_direct_cases', checked)
