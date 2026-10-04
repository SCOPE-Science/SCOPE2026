#!/usr/bin/env python3
from fractions import Fraction

def T(p):
    a, b, g = p
    return (a * g / b, g, b)

tests = [
    (Fraction(3, 7), Fraction(5, 11), Fraction(13, 17)),
    (Fraction(2, 3), Fraction(7, 5), Fraction(11, 9)),
    (Fraction(9, 4), Fraction(8, 3), Fraction(5, 6)),
]

for p in tests:
    a, b, g = p
    q = T(p)
    assert T(q) == p
    aq, bq, gq = q
    assert aq * gq == a * g
    assert bq * gq == b * g
    assert bq + gq == b + g

p = (Fraction(4, 9), Fraction(7, 10), Fraction(7, 10))
assert T(p) == p

print("VERIFY_OK")
