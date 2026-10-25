#!/usr/bin/env python3
"""Exact integer checks for dyadic two-summand Zeckendorf congruence laws."""
from collections import Counter

BASE_C = tuple(
    3 if r % 4 == 1 else
    1 if r % 4 == 3 else
    2 if r % 8 == 0 else
    8 if r == 2 else 0
    for r in range(32)
)
BASE_D = tuple(sum(BASE_C[x] * BASE_C[(r - x) % 32]
                   for x in range(32)) for r in range(32))
EXPECTED_EVEN_D = {0: 64, 2: 112, 4: 112, 6: 80,
                   8: 64, 10: 112, 12: 48, 14: 80,
                   16: 64, 18: 112, 20: 48, 22: 80,
                   24: 64, 26: 112, 28: 48, 30: 80}
assert sum(BASE_C) == 48
assert sum(BASE_D) == 48**2
assert all(BASE_D[r] == 64 for r in range(1, 32, 2))
assert all(BASE_D[r] == value for r, value in EXPECTED_EVEN_D.items())
assert sum(BASE_D[r] for r in range(0, 32, 2)) * 9 == 5 * 48**2

def fib_mod_values(modulus, length):
    f, g = 0, 1
    vals = []
    for _ in range(length):
        vals.append(f)
        f, g = g, (f + g) % modulus
    return vals

pair_checks = 0
for exponent in range(5, 12):
    mod = 1 << exponent
    period = 3 << (exponent - 1)
    values = fib_mod_values(mod, period)
    f, g = values[-2], values[-1]
    # Verify full return of (F_period, F_period+1)=(0,1).
    a, b = 0, 1
    for _ in range(period):
        a, b = b, (a + b) % mod
    assert (a, b) == (0, 1)
    frequencies = Counter(values)
    assert all(frequencies[r] == BASE_C[r % 32]
               for r in range(mod)), exponent
    # Independent pair counting by period residue enumeration.
    pair_frequencies = Counter()
    for residue, multiplicity in frequencies.items():
        for residue2, multiplicity2 in frequencies.items():
            pair_frequencies[(residue + residue2) % mod] += multiplicity * multiplicity2
    assert all(pair_frequencies[r] == (1 << (exponent - 5)) * BASE_D[r % 32]
               for r in range(mod)), exponent
    assert sum(pair_frequencies.values()) == period**2
    pair_checks += mod

# For actual canonical two-term expansions, indices are >=2 and nonconsecutive.
# Compare independent direct integer enumeration with group-by-residue counting.
for exponent in range(5, 9):
    mod = 1 << exponent
    vals = fib_mod_values(mod, 243)
    for upper in (48, 96, 144, 242):
        # Independently rebuild the unbounded Fibonacci integers, rather than
        # deriving the direct residues from the periodic modular array.
        exact_fibs = [0, 1]
        for _ in range(2, upper + 1):
            exact_fibs.append(exact_fibs[-1] + exact_fibs[-2])
        direct = Counter()
        for i in range(2, upper + 1):
            for j in range(i + 2, upper + 1):
                number = exact_fibs[i] + exact_fibs[j]
                if number % 2 == 0:
                    direct[number % mod] += 1
        # Each matching pair is canonical and 2 divides the represented integer.
        grouped = Counter()
        for j in range(4, upper + 1):
            for i in range(2, j - 1):
                if (vals[i] + vals[j]) % 2 == 0:
                    grouped[(vals[i] + vals[j]) % mod] += 1
        assert direct == grouped
        assert all(direct[r] == 0 for r in range(1, mod, 2))
print('VERIFY_OK powers=5..11 residue_cells=%d mod32_pair_convolution=PASS exact_index_pairs=16 class_bias=PASS' % pair_checks)
