#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import gcd

EXPECTED_NUMERATORS = {
    1,2,3,4,6,7,8,9,11,13,17,19,21,23,29,31,37,39,41,43,47,49,
    53,61,67,73,77,83,97,107,113,137
}
EXPECTED_BAD_PRIMES = {
    2,3,7,11,13,17,19,23,29,31,37,41,43,47,53,61,67,73,83,97,107,113,137
}
EXPECTED_GOOD_UP_TO_137 = {5,59,71,79,89,101,103,109,127,131}


def prime_factors(n):
    n = abs(n)
    out = set()
    d = 2
    while d*d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.add(n)
    return out


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

rows = []
for w1, w2, w3, w4 in product((-1,0,1), repeat=4):
    r = Fraction(1,5) - Fraction(w1,1) - Fraction(w2,2) - Fraction(w3,3) - Fraction(w4,4)
    A = 12 - 60*w1 - 30*w2 - 20*w3 - 15*w4
    g = gcd(abs(A), 60)
    if A == 0:
        reduced_num = 0
        reduced_den = 1
    else:
        reduced_num = A // g
        reduced_den = 60 // g
    assert r == Fraction(reduced_num, reduced_den)
    rows.append(((w1,w2,w3,w4), r))

assert len(rows) == 81
assert all(r != 0 for _, r in rows), "5 would not lie in U"
numerators = {abs(r.numerator) for _, r in rows}
assert numerators == EXPECTED_NUMERATORS

bad = set()
for a in numerators:
    bad |= prime_factors(a)
assert bad == EXPECTED_BAD_PRIMES

good = {p for p in range(2,138) if is_prime(p) and p not in bad}
assert good == EXPECTED_GOOD_UP_TO_137
assert max(numerators) == 137

# Thus every prime > 137 is automatically compatible, since no reduced
# numerator has absolute value above 137.
print("VERIFY_OK")
print("residual_count=81")
print("nonzero_residuals=81")
print("absolute_reduced_numerators=" + ",".join(map(str, sorted(numerators))))
print("incompatible_primes=" + ",".join(map(str, sorted(bad))))
print("compatible_primes_le_137=" + ",".join(map(str, sorted(good))))
