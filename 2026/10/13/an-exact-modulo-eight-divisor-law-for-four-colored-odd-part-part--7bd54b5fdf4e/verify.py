#!/usr/bin/env python3
"""Finite independent checks of odd-index congruence for four-coloured odd-part partitions.

All computations use Python's integer arithmetic and the standard library.
These checks are finite illustrations, not a replacement for the proof.
"""
from math import isqrt

LIMIT = 1200

def colored_partition_coefficients(limit):
    coeff = [0] * (limit + 1)
    coeff[0] = 1
    # Four freely repeated colours for each odd weight; one for each even weight.
    for part in range(1, limit + 1):
        for color in range(4 if part % 2 else 1):
            for n in range(part, limit + 1):
                coeff[n] = (coeff[n] + coeff[n-part]) % 8
    return coeff

def chi3(d):
    return 0 if d % 3 == 0 else (1 if d % 3 == 1 else -1)

def divsum_chi3(n):
    return sum(chi3(d) + (chi3(n//d) if d * d != n else 0)
               for d in range(1, isqrt(n) + 1) if n % d == 0)

def norm_reps(n):
    count = 0
    for y in range(-isqrt(n//3), isqrt(n//3) + 1):
        m = n - 3*y*y
        if m < 0:
            continue
        x = isqrt(m)
        if x*x == m:
            count += 1 if x == 0 else 2
    return count

def pentagonal_square_count(n):
    count = 0
    for j in range(-isqrt(n)-1, isqrt(n)+2):
        rest = n - j * (3*j - 1)
        if rest <= 0:
            continue
        s = isqrt(rest)
        if s*s == rest and s % 2:
            count += 1
    return count

def residue_four_by_prime_exponents(N):
    factors = {}
    d = 2
    while d*d <= N:
        while N % d == 0:
            factors[d] = factors.get(d, 0) + 1
            N //= d
        d += 1
    if N > 1:
        factors[N] = factors.get(N, 0) + 1
    if any(p % 3 == 2 and e % 2 for p,e in factors.items()):
        return False
    special = [e for p,e in factors.items() if p % 3 == 1 and e % 2]
    return len(special) == 1 and special[0] % 4 == 1

A = colored_partition_coefficients(LIMIT)
classes = {0: 0, 4: 0}
for n in range(1, LIMIT+1, 2):
    N = 12*n + 1
    H = divsum_chi3(N)
    r = norm_reps(N)
    R = pentagonal_square_count(n)
    assert N % 24 == 13
    assert r == 2*H, ('norm divisor formula',n,N,r,H)
    assert r == 4*R, ('norm bijection',n,N,r,R)
    expected = (2*H) % 8
    assert expected in classes, ('residue',n,expected)
    assert A[n] == expected, ('four-color partition congruence',n,A[n],expected)
    assert (expected == 4) == residue_four_by_prime_exponents(N), ('prime-exponent residue criterion',n,N,expected)
    classes[expected] += 1
# An entirely separate integer exact count at small indices, without modular reduction.
def exact_small(limit):
    coeff = [0] * (limit+1)
    coeff[0] = 1
    for part in range(1,limit+1):
        for color in range(4 if part%2 else 1):
            for n in range(part,limit+1):
                coeff[n] += coeff[n-part]
    return coeff
small = exact_small(18)
assert all(small[n] % 8 == A[n] for n in range(19))
print('VERIFY_OK odd_indices=600 independent_colored_DPs=19 norm_divisor_equalities=600 norm_bijections=600 prime_residue_tests=600')
print('odd_residues_mod8=' + repr(classes))
print('examples=' + repr([(n,A[n]) for n in range(1,22,2)]))
