"""Exact enumeration of phase-ordering coefficients for periodic dyadic holes.

Run: python verify.py
Uses only the Python standard library. All fractions exact.
"""
from itertools import permutations
from collections import Counter
from fractions import Fraction

EXPECT = {
    2: (Fraction(3, 2), 1),
    3: (Fraction(2), 1),
    4: (Fraction(9, 4), 4),
    5: (Fraction(5, 2), 10),
    6: (Fraction(11, 4), 12),
    7: (Fraction(23, 8), 144),
    8: (Fraction(3), 864),
}

def erosion(a):
    q = len(a)
    # Direct finite search, including an entire extra cycle as a check.
    return tuple(min(k + a[(s+k) % q] for k in range(2*q)) for s in range(q))

def erosion_iterative(a):
    q = len(a)
    b = list(a)
    while True:
        new = [min(a[s], 1 + b[(s+1) % q]) for s in range(q)]
        if new == b:
            return tuple(b)
        b = new

def all_coefficients(q):
    vals = Counter()
    for tail in permutations(range(1, q)):
        a = (0,) + tail # unique canonical cyclic representative
        b = erosion(a)
        assert b == erosion_iterative(a)
        val = sum((Fraction(1, 2**v) for v in b), Fraction(0))
        vals[val] += 1
    assert sum(vals.values()) == __import__('math').factorial(q-1)
    return vals

for q, (expect_max, expect_count) in EXPECT.items():
    spectrum = all_coefficients(q)
    min_sum = Fraction(2) * (1 - Fraction(1, 2**q))
    assert min(spectrum) == min_sum
    assert spectrum[min_sum] == 1
    assert max(spectrum) == expect_max
    assert spectrum[expect_max] == expect_count
    print(f'q={q}: min_sum={min_sum}; max_sum={max(spectrum)}; '
          f'maximizers={spectrum[max(spectrum)]}; distinct_values={len(spectrum)}')
print('VERIFY_OK')
