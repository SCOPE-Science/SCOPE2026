#!/usr/bin/env python3
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def q(x):
    return x*x + x - 1

def squares_mod(p):
    return {pow(a, 2, p) for a in range(1, p)}

# Lower-bound local obstruction.
admissible = []
for r in [3, 5, 7, 11, 13, 17]:
    good = [x for x in squares_mod(r) if q(x) % r == 0]
    if good:
        admissible.append((r, good))
assert admissible == [(11, [3])]

# tau=11 and tau=121 shapes force n == 1 mod 11.
# Exponent patterns: [10], [120], [10,10].
for a in [2,3,5,7,13,17,19,23,31]:
    if a != 11:
        assert pow(a, 10, 11) == 1
        assert pow(a, 120, 11) == 1
for a,b in [(2,3),(5,7),(13,17),(19,23)]:
    assert (pow(a,10,11)*pow(b,10,11)) % 11 == 1
assert q(1) % 11 == 1

# Infinite-family residue checks.
assert pow(31, 18, 11) == 3
assert pow(4, 10, 19) == 4
assert q(3) % 11 == 0
assert q(4) % 19 == 0

# Check several actual primes p == 4 mod 19.
found = []
p = 2
while len(found) < 8:
    if is_prime(p) and p % 19 == 4:
        found.append(p)
    p += 1

for p in found:
    n = p**10 * 31**18
    tau_n = 11 * 19
    assert (n*n + n - 1) % tau_n == 0

first = 23**10 * 31**18
assert first == 28959352627832366137714333358514333819409
assert len(str(first)) == 41
print("VERIFY_OK")
