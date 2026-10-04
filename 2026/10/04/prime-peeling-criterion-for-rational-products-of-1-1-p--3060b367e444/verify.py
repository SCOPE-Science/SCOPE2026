#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import gcd, isqrt

PRIMES = (2,3,5,7,11,13,17,19)

def factorint(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d,0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n,0) + 1
    return out

def valuations(q):
    fn = factorint(q.numerator)
    fd = factorint(q.denominator)
    ps = set(fn) | set(fd)
    return {p: fn.get(p,0)-fd.get(p,0) for p in ps}

def decode(q):
    q = Fraction(q)
    if q <= 0:
        return None
    original = q
    recovered = {}
    while True:
        vals = valuations(q)
        big = [p for p,v in vals.items() if p >= 5 and v != 0]
        if not big:
            break
        P = max(big)
        v = vals[P]
        if v >= 0:
            return None
        a = -v
        recovered[P] = a
        q *= Fraction(P, P+1) ** a

    vals = valuations(q)
    if any(p not in (2,3) and v != 0 for p,v in vals.items()):
        return None
    x = vals.get(2,0)
    y = vals.get(3,0)
    a2 = x + 2*y
    a3 = x + y
    if a2 < 0 or a3 < 0:
        return None
    if a2:
        recovered[2] = a2
    if a3:
        recovered[3] = a3

    rebuilt = Fraction(1,1)
    for p,a in recovered.items():
        assert a >= 0
        rebuilt *= Fraction(p+1,p) ** a
    if rebuilt != original:
        return None
    return dict(sorted(recovered.items()))

def is_three_smooth(n):
    for p in (2,3):
        while n % p == 0:
            n //= p
    return n == 1

def main():
    generated = 0
    for exps in product(range(3), repeat=len(PRIMES)):
        if not any(exps):
            continue
        q = Fraction(1,1)
        expected = {}
        for p,a in zip(PRIMES, exps):
            if a:
                q *= Fraction(p+1,p) ** a
                expected[p] = a
        got = decode(q)
        assert got == expected, (q, expected, got)
        generated += 1
    assert generated == 6560

    for n in range(1, 20001):
        got = decode(Fraction(n,1))
        assert (got is not None) == is_three_smooth(n), (n, got)

    rational_grid = 0
    accepted_grid = 0
    for a in range(1,251):
        for b in range(1,251):
            if gcd(a,b) != 1:
                continue
            q = Fraction(a,b)
            rational_grid += 1
            got = decode(q)
            if got is not None:
                accepted_grid += 1
                rebuilt = Fraction(1,1)
                for p,e in got.items():
                    assert e >= 0
                    rebuilt *= Fraction(p+1,p) ** e
                assert rebuilt == q

    print("VERIFY_OK")
    print("generated_vectors_checked=" + str(generated))
    print("integer_limit=20000")
    print("rational_grid_reduced_count=" + str(rational_grid))
    print("rational_grid_accepted_count=" + str(accepted_grid))

if __name__ == "__main__":
    main()
