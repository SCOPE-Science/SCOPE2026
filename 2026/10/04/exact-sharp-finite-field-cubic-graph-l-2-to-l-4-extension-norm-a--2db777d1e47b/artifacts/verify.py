#!/usr/bin/env python3
from fractions import Fraction

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

def verify_pair_geometry(p):
    fibers = {}
    for a in range(p):
        for b in range(p):
            key = ((a+b) % p, (a*a*a+b*b*b) % p)
            fibers.setdefault(key, []).append((a,b))
    zero = fibers.get((0,0), [])
    assert len(zero) == p
    assert set(zero) == {(a, (-a) % p) for a in range(p)}
    for (s, t), pairs in fibers.items():
        if s == 0:
            assert t == 0 and len(pairs) == p
        else:
            # Every nonzero-sum fiber is exactly one unordered pair,
            # represented by one ordered pair on the diagonal or two off it.
            a, b = pairs[0]
            expected = {(a,b)} if a == b else {(a,b),(b,a)}
            assert set(pairs) == expected

def verify_closed_form(p):
    q = p
    den = 2*q + 1
    alpha = Fraction(3, den)
    beta = Fraction(2, den)
    assert alpha + (q-1)*beta == 1
    p4 = alpha*alpha + (q-1)*beta*beta
    R = p4
    B2 = Fraction(1,1)  # positive extremizer has B = alpha+(q-1)beta = 1
    Q = Fraction(2,1) - p4 - 2*R + alpha*alpha + B2
    target = Fraction(3*(2*q-1), 2*q+1)
    assert Q == target
    m = (q-1)//2
    # Verify the one-variable quadratic optimization exactly.
    # penalty(alpha)=2 alpha^2 + 3/(2m)*(1-alpha)^2
    penalty = 2*alpha*alpha + Fraction(3,2*m)*(1-alpha)*(1-alpha)
    assert penalty == Fraction(6, 2*q+1)
    assert Fraction(3,1) - penalty == target

for p in PRIMES:
    verify_pair_geometry(p)
    verify_closed_form(p)

print(f"VERIFY_OK primes={len(PRIMES)} max_prime={max(PRIMES)}")
