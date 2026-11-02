#!/usr/bin/env python3
"""Exact point-count census for a bi-cubic genus-four Hurwitz family over F_25.

Field is F_5[a]/(a*a - 2). Integers 0..24 encode c+5*d.
No external packages or empirical randomness are used.
"""
from collections import Counter

P = 5
F = range(25)

def add(x, y):
    return ((x % P + y % P) % P) + P * (((x // P) + (y // P)) % P)

def sub(x, y):
    return ((x % P - y % P) % P) + P * (((x // P) - (y // P)) % P)

def mul(x, y):
    a, b = x % P, x // P
    c, d = y % P, y // P
    return ((a*c + 2*b*d) % P) + P * ((a*d + b*c) % P)

def power(x, n):
    y = 1
    while n:
        if n % 2:
            y = mul(y, x)
        x = mul(x, x)
        n //= 2
    return y

# Basic finite-field consistency checks, including field inversion.
assert all(power(x, 24) == 1 for x in F if x)
assert all(mul(x, power(x, 23)) == 1 for x in F if x)
assert all(mul(x, add(y, z)) == add(mul(x, y), mul(x, z))
           for x in F for y in F for z in F)
assert all(add(mul(mul(x, y), z), 0) == mul(x, mul(y, z))
           for x in F for y in F for z in F)

roots = Counter(power(w, 3) for w in F)
assert sorted(roots.values()) == [1] + [3]*8

def finite_count(lam):
    return sum(roots[mul(x, sub(x, 1))] * roots[sub(x, lam)] for x in F)

def direct_count(lam):
    # Independent path: enumerate ordered affine (x,u,v) directly.
    return sum(1 for x in F for u in F for v in F
               if power(u, 3) == mul(x, sub(x, 1))
               and power(v, 3) == sub(x, lam))

counts = {}
for lam in F:
    if lam in (0, 1):
        continue
    assert finite_count(lam) == direct_count(lam)
    # Three rational places over infinity, one for each cube root of unity.
    counts[lam] = 3 + finite_count(lam)

assert len(counts) == 23
assert Counter(counts.values()) == {15:4, 33:4, 39:4, 42:6, 48:2, 60:2, 66:1}
assert [lam for lam, val in counts.items() if val == 66] == [3]
assert finite_count(3) == 63

# Independently check the three positive-genus quotient point counts at lambda=3.
def quotient_counts(lam):
    e0 = 1 + sum(roots[mul(x, sub(x, 1))] for x in F)
    e1 = 3 + sum(roots[mul(mul(x, sub(x, 1)), sub(x, lam))] for x in F)
    d  = 1 + sum(roots[mul(mul(x, sub(x, 1)),
                              power(sub(x, lam), 2))] for x in F)
    return e0, e1, d
assert quotient_counts(3) == (36, 36, 46)
assert sum(quotient_counts(3)) - 2 * 26 == 66

print('FIELD_OK: F25 = F5[a]/(a^2-2); all nonzero elements have inverses')
print('GEOMETRIC_INPUT: each smooth normalization has genus 4 and exactly three F25-rational infinity points')
print('INDEPENDENT_COUNTS_OK: direct triples and cube-root summation agree for all 23 allowed parameters')
print('SPECTRUM_OK: (15,4), (33,4), (39,4), (42,6), (48,2), (60,2), (66,1)')
print('MAXIMAL_OK: lambda=3 alone attains 66 = 25+1+8*5')
print('QUOTIENTS_OK: at lambda=3 quotient counts 36, 36, 46; 36+36+46-52=66')
print('LAMBDA_COUNTS:', [(lam, counts[lam]) for lam in sorted(counts)])
