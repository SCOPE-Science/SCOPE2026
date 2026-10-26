#!/usr/bin/env python3
"""Exact independent small-edge census and the prime-divisor parametrization."""
from fractions import Fraction
from itertools import combinations
from math import isqrt


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(n) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * ((n-d*d)//d+1)
    return [k for k in range(n+1) if sieve[k]]


def divisors(n):
    result = []
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            result.append(d)
            if n//d != d:
                result.append(n//d)
    return sorted(result)


def formula(p, all_primes):
    if p == 2:
        return set()
    ans = set()
    for t in divisors(p*(p+6)):
        if t % 2 == 0:
            continue
        q = (p+t)//2
        r = (p+2+p*(p+6)//t)//2
        if 2*q-p != t:
            continue
        if len({p,q,r,2}) != 4 or q not in all_primes or r not in all_primes:
            continue
        ds = tuple(sorted((2*q, 2*r, q*r, p*r)))
        assert Fraction(1,p) == sum((Fraction(1,d) for d in ds), Fraction(0))
        ans.add(ds)
    if p == 3:
        ans.add((6,14,15,35))
    return ans


def main():
    ps = primes_upto(31)
    semiprimes = sorted({a*b for a,b in combinations(ps, 2)})
    limits = set(primes_upto(2000000))
    assert len(semiprimes) == 55
    actual = {}
    for ds in combinations(semiprimes, 4):
        total = Fraction(0)
        for d in ds:
            total += Fraction(1,d)
        if total.numerator == 1 and total.denominator in ps:
            actual.setdefault(total.denominator,set()).add(ds)
    predicted = {p:formula(p,limits) for p in ps}
    predicted = {p:{ds for ds in ss if all(d in semiprimes for d in ds)} for p,ss in predicted.items()}
    actual = {p:s for p,s in actual.items() if s}
    predicted = {p:s for p,s in predicted.items() if s}
    assert actual == predicted, (actual, predicted)
    assert actual == {3:{(6,14,15,35)},5:{(6,62,93,155)}}
    witness_count = 0
    for p in primes_upto(997):
        for ds in formula(p,limits):
            assert len(ds) == len(set(ds)) == 4
            assert Fraction(1,p) == sum((Fraction(1,d) for d in ds),Fraction(0))
            witness_count += 1
    print('VERIFY_OK prime_vertex_limit=31 edges=55 four_edge_sets=341055')
    print('small_census=',actual)
    print('parameter_witnesses_p_le_997=',witness_count)

if __name__ == '__main__':
    main()
