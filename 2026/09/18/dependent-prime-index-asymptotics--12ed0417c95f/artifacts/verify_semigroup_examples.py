#!/usr/bin/env python3
"""Exact arithmetic checks for numerical-semigroup examples in RESULT.md."""
from math import gcd, log, pi, sqrt


def gaps(u, v):
    assert gcd(u, v) == 1
    # Frobenius number uv-u-v bounds all gaps.
    F = u * v - u - v
    if F < 1:
        return []
    representable = {u*a + v*b for a in range(F//u + 2) for b in range(F//v + 2)}
    return [n for n in range(1, F + 1) if n not in representable]


def nth_prime(n):
    assert n >= 1
    ps = []
    x = 2
    while len(ps) < n:
        isprime = True
        d = 2
        while d*d <= x:
            if x % d == 0:
                isprime = False
                break
            d += 1
        if isprime:
            ps.append(x)
        x += 1
    return ps[-1]


def check_pair(u, v):
    G = gaps(u, v)
    genus = (u - 1) * (v - 1) // 2
    assert len(G) == genus
    return G


cases = [(1, 2), (2, 3), (3, 5), (4, 7), (5, 8)]
for u, v in cases:
    G = check_pair(u, v)
    print(f"(u,v)=({u},{v}) gaps={G} genus={len(G)}")

assert gaps(2, 3) == [1]
assert gaps(3, 5) == [1, 2, 4, 7]

m = 2
kappa = pi / sqrt(6 * log(m))
const_4_8 = kappa * log(nth_prime(2))       # gap e=1, p_{2^1}=p_2=3
assert nth_prime(2) == 3
print(f"kappa_2={kappa:.12f}")
print(f"K_(m=2;u=2,v=3)={const_4_8:.12f}")

G = gaps(3, 5)
prime_indices = [m**e for e in G]
prime_values = [nth_prime(j) for j in prime_indices]
assert prime_indices == [2, 4, 16, 128]
assert prime_values == [3, 7, 53, 719]
const_8_32 = (kappa ** len(G))
for p in prime_values:
    const_8_32 *= log(p)
print(f"indices_(3,5)={prime_indices}")
print(f"primes_(3,5)={prime_values}")
print(f"K_(m=2;u=3,v=5)={const_8_32:.12f}")
print("all exact gap/genus assertions passed")
