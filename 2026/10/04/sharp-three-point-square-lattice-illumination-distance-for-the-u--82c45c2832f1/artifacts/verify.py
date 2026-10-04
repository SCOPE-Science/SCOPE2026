#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement

Q = (1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20)

def heron16(a, b, c):
    return 2*(a*b + b*c + c*a) - (a*a + b*b + c*c)

found = {q for q in combinations_with_replacement(Q, 3)
         if heron16(*q) in (484, 576)}
expected = {
    (10, 13, 17),
    (8, 20, 20),
    (9, 17, 20),
    (10, 16, 18),
    (13, 13, 16),
}
assert found == expected
assert all(max(q) >= 16 for q in found)

# One exact member of the sharp family, delta = 1/10.
delta = Fraction(1, 10)
assert 1 + delta > 1
# (4 - 2 delta)/sqrt(13) > 1, after squaring positive quantities.
assert (4 - 2*delta)**2 > 13
# Endpoint contradiction template: L >= 4 and h > 1 imply radius^2 > 5.
assert Fraction(4*4, 4) + 1 == 5
# The strict inequality comes from h^2 > 1.

print('VERIFY_OK')
