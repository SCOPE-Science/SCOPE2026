#!/usr/bin/env python3
from math import isqrt
from collections import defaultdict

BOUND = 11776

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

def bit_sums(a, mask):
    A = 0
    B = 0
    I = []
    for i in range(a + 1):
        if (mask >> i) & 1:
            I.append(i)
            A += 1 << i
            B += 1 << (a - i)
    return A, B, tuple(I)

def direct_check(a, p, I):
    n = (1 << a) * p
    omitted = set()
    for i in I:
        omitted.add(1 << i)
        omitted.add(p * (1 << (a - i)))
    divisors = sorted({1 << i for i in range(a + 1)} | {p * (1 << i) for i in range(a + 1)})
    assert all(n % d == 0 for d in divisors)
    retained = [d for d in divisors if d not in omitted]
    assert sum(retained) == 2 * n
    assert all((n // d in retained) for d in retained)

found = defaultdict(list)
for a in range(1, 12):
    M = (1 << (a + 1)) - 1
    for mask in range(1 << (a + 1)):
        A, B, I = bit_sums(a, mask)
        num = M - A
        den = 1 + B
        if num <= 0 or num % den:
            continue
        p = num // den
        if p % 2 == 0 or not is_prime(p):
            continue
        n = (1 << a) * p
        if n <= BOUND:
            direct_check(a, p, I)
            found[(n, a, p)].append(I)

expected = {
    (6, 1, 3): [()],
    (28, 2, 7): [()],
    (352, 5, 11): [(3,)],
    (496, 4, 31): [()],
    (8128, 6, 127): [()],
    (11776, 9, 23): [(4, 6)],
}
assert dict(found) == expected, (dict(found), expected)

# Boundary uniqueness, checked independently against all 2^10 masks.
a, p = 9, 23
boundary = []
M = (1 << (a + 1)) - 1
for mask in range(1 << (a + 1)):
    A, B, I = bit_sums(a, mask)
    if M - A == p * (1 + B):
        boundary.append(I)
assert boundary == [(4, 6)]
assert 3 * (1 << 12) > BOUND
print(f"VERIFY_OK candidates={len(found)} boundary_representations={len(boundary)}")
