#!/usr/bin/env python3
"""Finite checks for the binary-block binomial nondivisibility theorem."""
from itertools import product
from math import comb, gcd


def lucas_binom_mod(n, k, p):
    answer = 1
    while n or k:
        a, b = n % p, k % p
        if b > a:
            return 0
        answer = (answer * comb(a, b)) % p
        n //= p
        k //= p
    return answer


def block_parameters(a, b, p):
    assert a > 0 and b > 0 and a % p == 0 and b % p != 0
    m = a + b
    s = 1
    residue = p % m
    while residue != 1:
        residue = residue * p % m
        s += 1
    n0 = (p**s - 1) // m
    assert (a+b)*n0 == p**s-1 and n0 > 0
    return s, n0


cases = 0
for a in range(2, 17):
    for b in range(1, 10):
        for p in (2, 3, 5, 7):
            if a % p or b % p == 0:
                continue
            s, n0 = block_parameters(a, b, p)
            if s > 8:
                continue
            for r in range(1, 6):
                seen = set()
                for high in product((0, 1), repeat=r-1):
                    n = n0*(1+sum(t*p**(s*j) for j,t in enumerate(high,1)))
                    seen.add(n)
                    assert 0 < n < p**(s*r)
                    assert (b*n+1) % p == 0
                    assert lucas_binom_mod((a+b)*n, a*n,p) != 0
                    if (a+b)*n <= 80:
                        assert comb((a+b)*n,a*n) % p != 0
                        assert comb((a+b)*n,a*n) % (b*n+1) != 0
                    cases += 1
                assert len(seen) == 2**(r-1)
print('VERIFY_OK:',cases,'binary-block samples; Lucas residues and exact small-binomial divisibility replays')
