#!/usr/bin/env python3
import itertools, math

def smallest_prime(n):
    for p in range(2, n+1):
        if n % p == 0:
            return p
    raise ValueError

def regular_residue(a, n):
    return math.gcd(a, n) == 1

def upper_cover(n):
    p = smallest_prime(n)
    S = list(range(p))
    for a in range(n):
        assert any(not regular_residue(a+s, n) for s in S)
    return p

def lower_exhaustive(n):
    p = smallest_prime(n)
    if p == n:
        return True
    residues = range(n)
    for k in range(p):
        for S in itertools.combinations(residues, k):
            witness = None
            for a in residues:
                if all(regular_residue(a+s, n) for s in S):
                    witness = a
                    break
            assert witness is not None, (n, S)
    return True

for n in range(2, 31):
    p = smallest_prime(n)
    assert upper_cover(n) == p
    assert lower_exhaustive(n)

print("VERIFY_OK")
print("checked_exponents=2..30")
print("statement=minimum translate-cover number of nonunits in Z/nZ equals the smallest prime divisor")
