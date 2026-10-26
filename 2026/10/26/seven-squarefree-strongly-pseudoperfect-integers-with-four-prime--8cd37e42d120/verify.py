#!/usr/bin/env python3
"""Exact finite certificate for the four-prime squarefree divisor-pair classification.

Requires only Python 3 standard library. All arithmetic is integral.
"""
from math import isqrt

EXPECTED = {
    210: ((5, 42), (6, 35), (7, 30), (10, 21)),
    330: ((2, 165), (15, 22)),
    546: ((6, 91), (13, 42), (14, 39), (21, 26)),
    714: ((3, 238), (17, 42)),
    1770: ((3, 590), (10, 177)),
    3198: ((6, 533), (39, 82)),
    3486: ((6, 581), (7, 498)),
}


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def divisors(n):
    return tuple(d for d in range(1, isqrt(n) + 1) if n % d == 0 for d in ((d, n // d) if d * d != n else (d,)))


def all_divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def symbolic_prime_extensions(m, last_fixed_prime):
    """All prime c>last_fixed_prime for which mc has a paired omission.

    The eight complementary pairs of mc are (d, (m/d)c), d|m;
    m here is squarefree of exactly three prime factors.
    """
    ds = all_divisors(m)
    assert len(ds) == 8
    sigma_m = sum(ds)
    coefficient = sigma_m - 2 * m
    found = {}
    for mask in range(256):
        A = sum((m // d) for j, d in enumerate(ds) if mask & (1 << j))
        B = sum(d for j, d in enumerate(ds) if mask & (1 << j))
        # If both equations held, all c would qualify; test every mask.
        if A == coefficient:
            assert B != sigma_m, (m, mask, 'coefficient identity')
            continue
        num, den = sigma_m - B, A - coefficient
        if num % den:
            continue
        c = num // den
        if c <= last_fixed_prime or not is_prime(c):
            continue
        n = m * c
        assert n not in found, (n, mask, found.get(n))
        omitted = tuple(sorted((min(d, (m // d) * c), max(d, (m // d) * c))
                               for j, d in enumerate(ds) if mask & (1 << j)))
        found[n] = omitted
    return found


def complement_omissions(n):
    ds = all_divisors(n)
    assert len(ds) == 16
    pairs = tuple((d, n // d) for d in ds if d < n // d)
    assert len(pairs) == 8
    target = sum(ds) - 2 * n
    matches = []
    for mask in range(256):
        subset = tuple(pairs[i] for i in range(8) if mask & (1 << i))
        if sum(a + b for a, b in subset) == target:
            matches.append(subset)
    return matches


def prime_factors(n):
    out=[]
    d=2
    while d*d <= n:
        if n%d == 0:
            if (n//d)%d==0: return None
            out.append(d); n//=d
        d+=1
    if n>1: out.append(n)
    return out


def main():
    # Group 2*3*b*c: b is forced into this finite list by the
    # paired-omission inequality (b-12)(c-12)<=150.
    found = {}
    for b in (5, 7, 11, 13, 17, 19):
        for n, omissions in symbolic_prime_extensions(6*b, b).items():
            assert n not in found
            found[n] = omissions
    # Group 2*5*b*c: b=7 is unbounded a priori, but the subset
    # formulas prove finiteness. For b>=11 abundance bounds b<=17.
    for b in (7, 11, 13, 17):
        assert not symbolic_prime_extensions(10*b, b)
    # The sole abundant candidate in the group beginning 2*7 is 2002.
    assert not complement_omissions(2*7*11*13)
    assert found == EXPECTED, (found, EXPECTED)
    for n, omissions in EXPECTED.items():
        assert len(complement_omissions(n)) == 1
        assert complement_omissions(n)[0] == omissions
        assert sum(a+b for a,b in omissions) == sum(all_divisors(n)) - 2*n
        assert len(prime_factors(n)) == 4
    # Independent direct census below 5000: factor and inspect all
    # 16-divisor squarefree products, without using the parameter sieve.
    brute = set()
    for n in range(2, 5001):
        factors=prime_factors(n)
        if factors is not None and len(factors)==4 and complement_omissions(n):
            brute.add(n)
    assert brute == set(EXPECTED), (sorted(brute), sorted(EXPECTED))
    print('VERIFY_OK count=7 unique_omission_masks=7 core_masks=256 per case brute_limit=5000')

if __name__ == '__main__':
    main()
