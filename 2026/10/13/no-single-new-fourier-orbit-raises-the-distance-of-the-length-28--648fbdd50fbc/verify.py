#!/usr/bin/env python3
"""Exact finite-field witnesses for a distance-four abelian-code extension obstruction."""
from itertools import combinations

MOD = 0x11D
EXP = []
LOG = {}
x = 1
for k in range(255):
    assert x not in LOG
    EXP.append(x)
    LOG[x] = k
    x <<= 1
    if x & 0x100:
        x ^= MOD
assert x == 1 and len(LOG) == 255


def mult(a, b):
    return EXP[(LOG[a] + LOG[b]) % 255] if a and b else 0


def divide(a, b):
    assert b
    return EXP[(LOG[a] - LOG[b]) % 255] if a else 0


def power_unit(i):
    return EXP[(15 * i) % 255]


ZETA = EXP[17]
SUBFIELD = []
for k in range(16):
    r = 0
    for b in range(4):
        if (k >> b) & 1:
            r ^= EXP[17 * b]
    SUBFIELD.append(r)
assert len(set(SUBFIELD)) == 16
assert all(mult(a, a) in SUBFIELD for a in SUBFIELD)
assert all(EXP[17 * i] in SUBFIELD for i in range(15))

UNIT_CIRCLE = [power_unit(i) for i in range(17)]
assert len(set(UNIT_CIRCLE)) == 17

# For each exponent w, count four-subsets where the divided difference vanishes.
zero_counts = [0] * 17
sets_checked = 0
for z in combinations(UNIT_CIRCLE, 4):
    sets_checked += 1
    reciprocal_denominators = []
    for a in z:
        denominator = 1
        for b in z:
            if a != b:
                denominator = mult(denominator, a ^ b)
        reciprocal_denominators.append(divide(1, denominator))
    for w in range(17):
        val = 0
        for a, d in zip(z, reciprocal_denominators):
            val ^= mult(EXP[(LOG[a] * w) % 255], d)
        if val == 0:
            zero_counts[w] += 1
assert sets_checked == 2380
assert zero_counts == [2380, 2380, 2380, 0, 0, 68, 34, 0, 34, 0, 0, 34, 0, 34, 68, 0, 0]
S = {i for i, count in enumerate(zero_counts) if count == 0}
assert S == {3, 4, 7, 9, 10, 12, 15, 16}

# Every putative distance-five extension must meet four necessary criteria:
# nonzero u,v (rectangles), and u+1,v+1,u+v+1,u-v+1 in S.
candidates = {(u, v) for u in range(1, 17) for v in range(1, 17)
              if all(w % 17 in S for w in (u + 1, v + 1, u + v + 1, u - v + 1))}
assert len(candidates) == 16


def orbit(u, v):
    return {(a % 17, b % 17)
            for p, q in ((u, v), (v, u))
            for a in (p, -p)
            for b in (q, -q)}

orbit_a = orbit(3, 6)
orbit_b = orbit(6, 8)
assert len(orbit_a) == 8 and len(orbit_b) == 8
assert not (orbit_a & orbit_b)
assert candidates == orbit_a | orbit_b

# In GF(256), coefficients from GF(16) automatically satisfy all conjugate
# Fourier equations. Each witness consists of four distinct grid positions.
witnesses = [
    ((3, 6), [(1, 5), (16, 12), (7, 9), (10, 8)], [5, 5, 8, 8]),
    ((6, 8), [(2, 4), (7, 13), (3, 16), (6, 1)], [8, 8, 15, 15]),
]
for (u, v), positions, coefficient_labels in witnesses:
    assert len(set(positions)) == 4
    coefficients = [SUBFIELD[label] for label in coefficient_labels]
    assert all(coefficients)
    sums = []
    for r, s in ((0, 0), (1, 0), (0, 1), (u, v)):
        val = 0
        for (i, j), coeff in zip(positions, coefficients):
            val ^= mult(coeff, power_unit(r * i + s * j))
        sums.append(val)
    assert sums == [0, 0, 0, 0]

print("FIELD_SIZE 256 SUBFIELD_SIZE 16 UNIT_CIRCLE_SIZE 17")
print("FOUR_SUBSETS", sets_checked)
print("DIVIDED_DIFFERENCE_ZERO_COUNTS", zero_counts)
print("UNIVERSALLY_NONZERO_EXPONENTS", sorted(S))
print("NECESSARY_EXPONENT_PAIRS", len(candidates))
print("SYMMETRY_ORBIT_SIZES", len(orbit_a), len(orbit_b))
print("WITNESS_REPRESENTATIVES", [(w[0], w[1]) for w in witnesses])
print("NO_SINGLE_NEW_CYCLOTOMIC_ORBIT_RAISES_DISTANCE_TO_FIVE")
print("VERIFY_OK")
