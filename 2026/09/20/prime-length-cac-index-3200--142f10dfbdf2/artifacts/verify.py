#!/usr/bin/env python3
"""Reproduce the finite computation used in the index-3200 CAC theorem.

Pure Python 3.10+. All arithmetic is exact. Primality testing is deterministic in
the 32-bit numerical range containing every candidate.
"""
from __future__ import annotations
import hashlib

LOW = 2**30
LO_ELL = 3001
HI_ELL = 3200

def factorint_small(n: int) -> dict[int, int]:
    f: dict[int, int] = {}
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            f[d] = e
        d = 3 if d == 2 else d + 2
    if n > 1:
        f[n] = 1
    return f

def omega(n: int) -> int:
    return len(factorint_small(n))

def delta(ell: int) -> int:
    return 1 if ell % 4 == 0 else 0

def bound(ell: int) -> int:
    return (2**omega(ell) * (ell - 3 - delta(ell)) + 2)**2 - 2

def isprime32(n: int) -> bool:
    if n < 2:
        return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0:
            return n == p
    # Bases 2, 7, 61 are deterministic for 32-bit unsigned integers.
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2,7,61):
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1:
                break
        else:
            return False
    return True

def order_two_given_divisor(p: int, m: int) -> int | None:
    if pow(2, m, p) != 1:
        return None
    d = m
    for r in factorint_small(m):
        while d % r == 0 and pow(2, d//r, p) == 1:
            d //= r
    return d

def subgroup_index_candidate(p: int, ell: int, m: int) -> tuple[int,int] | None:
    d = order_two_given_divisor(p, m)
    if d is None:
        return None
    h = d if d % 2 == 0 else 2*d
    if h != m:
        return None
    return ell, d

def theorem_5_1_covers(ell: int) -> bool:
    w = omega(ell)
    return (
        ell < 2070
        or (w == 1 and ell < 16411)
        or (w == 2 and ell < 8197)
        or (w == 3 and ell < 4100)
    )

def gap_primes(ell: int) -> list[tuple[int,int,int]]:
    B = bound(ell)
    m0 = LOW // ell + 1
    while 1 + ell*m0 <= LOW:
        m0 += 1
    if m0 % 2:
        m0 += 1
    m1 = (B - 1) // ell
    out: list[tuple[int,int,int]] = []
    # H=<-1,2> contains -1, hence |H|=m is even.
    for m in range(m0, m1 + 1, 2):
        p = ell*m + 1
        if not isprime32(p):
            continue
        ans = subgroup_index_candidate(p, ell, m)
        if ans is not None:
            _, d2 = ans
            out.append((p, m, d2))
    return out

def is_primitive_root(g: int, p: int, factors: dict[int,int]) -> bool:
    n = p - 1
    return all(pow(g, n//r, p) != 1 for r in factors)

def smallest_primitive_root(p: int) -> int:
    factors = factorint_small(p-1)
    for g in range(2, p):
        if is_primitive_root(g, p, factors):
            return g
    raise AssertionError("primitive root not found")

def first_coset_witness(ell: int, p: int, m: int, d2: int) -> tuple[int,int,int,int]:
    g = smallest_primitive_root(p)
    hgen = pow(g, ell, p)
    target = pow(g, 2*m, p)
    b = g
    for j in range(m):
        c = (-1-b) % p
        # c in g^2 H iff c^m=(g^2)^m in F_p^*.
        if c and pow(c, m, p) == target:
            assert (1+b+c) % p == 0
            assert (p-1)//m == ell
            assert d2 == order_two_given_divisor(p, m)
            return g, j, b, c
        b = b*hgen % p
    raise AssertionError((ell, p, "no witness"))

exceptional = [
    ell for ell in range(LO_ELL, HI_ELL + 1)
    if not theorem_5_1_covers(ell)
]
assert exceptional == [
    3003,3010,3030,3036,3045,3060,3066,3080,3090,3094,
    3102,3108,3120,3135,3150,3162,3180,3190,3192,3198,
]

records: list[str] = []
for ell in exceptional:
    for p, m, d2 in gap_primes(ell):
        g, j, b, c = first_coset_witness(ell, p, m, d2)
        records.append(f"{ell},{p},{g},{j},{b},{c},{m},{d2}")

assert len(records) == 165
digest = hashlib.sha256(("\n".join(records)+"\n").encode()).hexdigest()

print("exceptional_indices =", exceptional)
print("gap_prime_count =", len(records))
print("all_gap_primes_exhaustively_enumerated = True")
print("all_primitive_root_coset_witnesses_verified = True")
print("canonical_witness_sha256 =", digest)
