#!/usr/bin/env python3
"""Reproducible exact arithmetic checks for the Zumkeller-plus-square residue sieve.
Only standard Python is required. These finite checks supplement the written proof.
"""
from fractions import Fraction
from math import isqrt

PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
EXPECTED = Fraction(63520442937841228526, 83108492151210387225)

def level(p):
    a = 1
    while (1 << (a + 1)) - 1 < p:
        a += 1
    return a

def square_residues(m):
    return {x*x % m for x in range(m)}

def vp_exactly_one(z, p):
    return z % p == 0 and z % (p*p) != 0

def good_p_modulus(p):
    q = p*p
    squares = [x*x % q for x in range(q)]
    return {n for n in range(q)
            if any(vp_exactly_one(n-sq, p) for sq in squares)}

def local_count_formula(p):
    return (p-1)*(p+2)//2

def bound(primes):
    top = max(level(p) for p in primes)
    mu = {a: Fraction(len(square_residues(1<<a)), 1<<a)
          for a in range(1, top+2)}
    product = {a: __import__('functools').reduce(
        lambda v, p: v*(1-Fraction(local_count_formula(p), p*p)),
        (p for p in primes if level(p)<=a), Fraction(1))
        for a in range(1, top+1)}
    failure = sum(((mu[a]-mu[a+1])*product[a]
                   for a in range(1,top+1)), Fraction(0))
    failure += mu[top+1]*product[top]
    return 1-failure, mu, product

def main():
    assert all(level(p)>=1 and (1<<(level(p)+1))-1>=p for p in PRIMES)
    for p in PRIMES:
        good = good_p_modulus(p)
        assert len(good) == local_count_formula(p), (p,len(good))
        nonzero_qr = {x*x%p for x in range(1,p)}
        elementary = {n for n in range(p*p)
                      if n%p in nonzero_qr or (n%p==0 and n%(p*p)!=0)}
        assert good == elementary, p
    # The 2-adic square-residue recurrence holds at every tested depth.
    for a in range(3,14):
        val = Fraction(len(square_residues(1<<a)), 1<<a)
        prev = Fraction(len(square_residues(1<<(a-2))), 1<<(a-2))
        assert val == Fraction(1,8) + prev/Fraction(4), a
    actual, mu, product = bound(PRIMES)
    assert actual == EXPECTED, (actual,EXPECTED)
    assert actual > Fraction(7643,10000)
    assert bound(PRIMES[:5])[0] > Fraction(3,4)
    # Direct enumeration of the entire finite simultaneous CRT residue space for 3,5,7.
    small = PRIMES[:3]
    small_M = 4
    for p in small:
        small_M *= p*p
    good = {p:good_p_modulus(p) for p in small}
    roots2 = {a:square_residues(1<<a) for a in (1,2)}
    hit_count = sum(any(n % (1<<level(p)) in roots2[level(p)]
                        and n%(p*p) in good[p] for p in small)
                    for n in range(small_M))
    small_bound = bound(small)[0]
    assert Fraction(hit_count,small_M) == small_bound, (hit_count,small_M,small_bound)
    # Construct positive-square witnesses using CRT in sampled residue classes.
    for p in PRIMES:
        a = level(p)
        two = 1<<a
        q = p*p
        M = two*q
        qr2 = square_residues(two)
        goodp = sorted(good_p_modulus(p))
        # For each sample, select an x-mod-p^2 witness with v_p(n-x^2)=1.
        samples = [0, len(goodp)//4, len(goodp)//2, 3*len(goodp)//4, len(goodp)-1]
        for idx in samples:
            pp_res = goodp[idx]
            root2 = sorted(qr2)[idx % len(qr2)]
            roots_p = [x for x in range(q) if vp_exactly_one(pp_res-x*x,p)]
            assert roots_p
            u = next(x for x in range(two) if x*x % two == root2)
            v = roots_p[0]
            # CRT: x=v+q*t, (q*t)=(u-v) mod two.
            t = (u-v)*pow(q,-1,two)%two
            x = (v + q*t)%M or M
            n_res = pp_res + q*((root2-pp_res)*pow(q,-1,two)%two)
            N = M*M + M + n_res
            z = N-x*x
            assert z>0 and z % two==0 and vp_exactly_one(z,p)
    print('Local residue counts: 10/10 exact')
    print('Binary square recurrence: a=3..13 exact')
    print('Small CRT exhaustive:',hit_count,'/',small_M)
    print('Five-prime fraction:',bound(PRIMES[:5])[0])
    print('Ten-prime fraction:',actual, '=',float(actual))
    print('Constructive CRT witness samples: 50/50')
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
