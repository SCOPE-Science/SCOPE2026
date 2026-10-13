#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt

EXPECTED = [
    (5, 11, 23, 109),
    (5, 13, 17, 127),
    (5, 13, 19, 71),
    (5, 13, 23, 43),
    (5, 13, 29, 31),
    (5, 17, 19, 31),
    (7, 11, 13, 29),
    (7, 11, 17, 19),
]


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def H(p):
    return Fraction(p + 1, p - 1)


def sigma_squarefree(ps):
    z = 1
    for p in ps:
        z *= p + 1
    return z


def phi_squarefree(ps):
    z = 1
    for p in ps:
        z *= p - 1
    return z

# Candidate pairs proved in RESULT.md after the p- and q-bounds.
pairs = [(5, 11), (5, 13), (5, 17), (7, 11)]
# First prime r beyond each proved cutoff.
first_excluded_r = {(5, 11): 41, (5, 13): 31, (5, 17): 29, (7, 11): 19}

triples = []
solutions = []
for p, q in pairs:
    cutoff = first_excluded_r[(p, q)]
    assert H(p) * H(q) * H(cutoff) ** 2 < 2
    for r in range(q + 1, cutoff):
        if not is_prime(r):
            continue
        # Only triples satisfying the necessary monotone r-bound are relevant.
        if H(p) * H(q) * H(r) ** 2 <= 2:
            continue
        triples.append((p, q, r))
        A = H(p) * H(q) * H(r)
        if A >= 2:
            continue
        s = (Fraction(2, 1) + A) / (Fraction(2, 1) - A)
        if s.denominator != 1:
            continue
        s = s.numerator
        if not (s > r and is_prime(s)):
            continue
        ps = (p, q, r, s)
        assert sigma_squarefree(ps) == 2 * phi_squarefree(ps)
        solutions.append(ps)

assert len(triples) == 15, triples
assert sorted(solutions) == sorted(EXPECTED), solutions

# Check every stated integer and factorization.
integers = sorted(p*q*r*s for p,q,r,s in solutions)
expected_integers = [24871, 29029, 50065, 58435, 64285, 87685, 137885, 140335]
assert integers == expected_integers, integers

# Directly check the p- and q-stage cutoffs used before the four candidate pairs.
assert H(13) ** 4 < 2
assert H(5) * H(23) ** 3 < 2
assert H(7) * H(17) ** 3 < 2
assert H(11) * H(13) ** 3 < 2
assert H(5) * H(7) == 2
assert H(5) * H(19) * H(23) ** 2 < 2
assert H(7) * H(13) * H(17) ** 2 < 2

print(
    'VERIFY_OK',
    f'triples={len(triples)}',
    f'solutions={len(solutions)}',
    f'integers={integers}',
    f'quadruples={sorted(solutions)}',
)
