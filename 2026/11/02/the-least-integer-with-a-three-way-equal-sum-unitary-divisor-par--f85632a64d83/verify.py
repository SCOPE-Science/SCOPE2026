"""Exact arithmetic check of a three-way unitary-divisor partition and support bound."""
from fractions import Fraction
from math import gcd, prod

N = 30030
A = {14, 210, 2002, 30030}
B = {455, 770, 6006, 10010, 15015}
D = {d for d in range(1, N + 1) if N % d == 0 and gcd(d, N // d) == 1}
C = D - A - B
assert len(D) == 64
assert len(A) == 4 and len(B) == 5 and len(C) == 55
assert A <= D and B <= D and A.isdisjoint(B)
assert not (A & C or B & C)
assert A | B | C == D
assert sum(D) == prod(p + 1 for p in [2, 3, 5, 7, 11, 13]) == 96768
assert (sum(A), sum(B), sum(C)) == (32256, 32256, 32256)
P = (2, 3, 5, 7, 11)
r = prod(Fraction(p + 1, p) for p in P)
assert r == Fraction(1152, 385) and r < 3
assert prod(P + (13,)) == N
# Verify each displayed number really is a unitary divisor.
assert all(gcd(d, N // d) == 1 for d in A | B)
print('VERIFY_OK: unitary_divisors=64; class_sizes=4,5,55; class_sum=32256; support_bound=1152/385; least_integer=30030')
