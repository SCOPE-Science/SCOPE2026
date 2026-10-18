#!/usr/bin/env python3
"""Exact finite checks for the quadratic generator cutoff theorem.
Only standard-library arithmetic is used; all asymptotic steps require the proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import gcd, prod
from random import Random


def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for a in range(2, int(n**0.5) + 1):
        if sieve[a]:
            for b in range(a*a, n+1, a):
                sieve[b] = False
    return [a for a, flag in enumerate(sieve) if flag]


def binary_rank(columns, r):
    pivots = {}
    for col in columns:
        v = col
        while v:
            b = v.bit_length() - 1
            if b in pivots:
                v ^= pivots[b]
            else:
                pivots[b] = v
                break
    return len(pivots)


def theoretical_full_rank(r, t):
    out = Fraction(1)
    if t < r:
        return Fraction(0)
    for j in range(r):
        out *= Fraction(2**t - 2**j, 2**t)
    return out


def dynamic_full_rank(r, t):
    # Number of matrices of each rank after adjoining random binary columns.
    ways = [0] * (r + 1)
    ways[0] = 1
    for _ in range(t):
        next_ways = [0] * (r+1)
        for k in range(r+1):
            next_ways[k] += ways[k] * 2**k
            if k < r:
                next_ways[k+1] += ways[k] * (2**r - 2**k)
        ways = next_ways
    assert sum(ways) == 2**(r*t)
    return Fraction(ways[r], 2**(r*t))


def legendre_bit(a, p):
    v = pow(a, (p-1)//2, p)
    assert v in (1, p-1)
    return int(v == p-1)


def legendre_rank(p_tuple, prime_bases):
    columns = [sum(legendre_bit(a,p) << i for i,p in enumerate(p_tuple))
               for a in prime_bases]
    return binary_rank(columns, len(p_tuple))


def jacobi_symbol(a, n):
    """Exact Jacobi symbol for an odd positive denominator."""
    assert n > 0 and n % 2 == 1
    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): sign = -sign
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: sign = -sign
        a %= n
    return sign if n == 1 else 0


def generated_cutoff(n):
    units = {a for a in range(1,n) if gcd(a,n)==1}
    subgroup = {1}
    for a in range(2,n):
        if gcd(a,n) > 1:
            continue
        subgroup = {x * pow(a, e, n) % n for x in subgroup
                    for e in range(1, n+1)} | subgroup
        if subgroup == units:
            return a
    raise AssertionError('No generating cutoff')


def first_quadratic_cutoff(p_tuple, bases):
    eligible = [a for a in bases if a not in p_tuple]
    for t in range(1,len(eligible)+1):
        if legendre_rank(p_tuple, eligible[:t]) == len(p_tuple):
            return eligible[t-1]
    return None


def main():
    checks=0
    for r in range(1,9):
        for t in range(0,r+8):
            assert theoretical_full_rank(r,t) == dynamic_full_rank(r,t)
            checks +=1
    # Completely enumerate all binary matrices of moderate size; independent
    # verification of exact counting recurrence and the product formula.
    for r in range(1,5):
        for t in range(r,min(r+5,7)):
            if r*t > 15: continue
            count=0
            for cols in product(range(2**r), repeat=t):
                count += binary_rank(cols,r)==r
            assert Fraction(count,2**(r*t))==theoretical_full_rank(r,t)
            checks+=1
    bases=primes_up_to(130)
    # Check exact sign-pattern independence on every coprime residue modulo
    # the combined quadratic-conductor modulus for the first few prime bases.
    for t in range(1, 6):
        small = bases[:t]
        modulus = 8 * prod(a for a in small if a != 2)
        counts = {}
        for a in range(1, modulus):
            if gcd(a, modulus) > 1: continue
            signature = tuple(jacobi_symbol(b, a) for b in small)
            assert all(bit in (-1,1) for bit in signature)
            counts[signature] = counts.get(signature,0)+1
        assert len(counts) == 2**t
        assert len(set(counts.values())) == 1
        checks+=1
    # Directly compute the generator bound in small squarefree moduli.
    for ps in [(3,5),(3,7),(5,7),(5,11),(7,11),(7,13),(11,13),(3,5,7)]:
        n=prod(ps)
        q=first_quadratic_cutoff(ps,bases)
        g=generated_cutoff(n)
        assert q is not None and g >= q and g in bases
        checks+=1
    # A finite sample illustrates, but does not prove, the prime asymptotics.
    rng=Random(20261014)
    eligible=[p for p in primes_up_to(60000) if p>=30000]
    output=[]
    for r,t in [(2,2),(2,3),(3,3),(3,4)]:
        success=0
        trials=5000
        for _ in range(trials):
            ps=rng.sample(eligible,r)
            success+=legendre_rank(ps,bases[:t])==r
        frequency=success/trials
        predicted=float(theoretical_full_rank(r,t))
        output.append((r,t,success,trials,frequency,predicted))
        assert abs(frequency-predicted)<0.045
        checks+=1
    print('EXACT_CHECKS',checks)
    for row in output:
        print('SAMPLE r=%d t=%d success=%d/%d empirical=%.5f predicted=%.5f'%row)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
