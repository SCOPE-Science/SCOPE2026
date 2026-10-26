#!/usr/bin/env python3
"""Independent finite arithmetic tests for the complete Harshad-base classification."""
from math import isqrt

def prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0: return False
    return True

def digit_sum(n, b):
    if b == 1: return n
    total = 0
    while n:
        n, d = divmod(n, b)
        total += d
    return total

def is_fermat_form(p):
    x = p - 1
    if x <= 0 or (x & (x - 1)):
        return False
    a = x.bit_length() - 1
    return a > 0 and (a & (a - 1)) == 0

def predicted(p):
    assert p >= 3 and prime(p)
    q = 2*p - 1
    out = {1, p, p+1, q, 2*p}
    if is_fermat_form(p): out.add(2)
    t = 1
    while 3**(1<<t) <= q:
        e = 1<<t
        lo, hi = 2, isqrt(q) + 1
        while lo < hi:
            mid = (lo + hi)//2
            if mid**e < q: lo = mid + 1
            else: hi = mid
        if lo**e == q: out.add(lo)
        t += 1
    return out

def run():
    tests = 0
    for p in range(3, 1201, 2):
        if not prime(p): continue
        n = 2*p
        actual = {1}
        for b in range(2, n+1):
            if n % digit_sum(n,b) == 0:
                actual.add(b)
        expect = predicted(p)
        assert actual == expect, (p,sorted(actual), sorted(expect))
        tests += 1
    example_p = (3**16 + 1)//2
    assert example_p == 21523361 and prime(example_p)
    example_bases = sorted(predicted(example_p))
    assert example_bases == [1,3,9,81,6561,21523361,21523362,43046721,43046722]
    for b in example_bases:
        assert (2*example_p) % digit_sum(2*example_p,b) == 0
    assert len(predicted(3)) == 6
    assert len(predicted(5)) == 7
    assert len(predicted(41)) == 7
    print('VERIFY_OK: {} odd primes exhaustively tested through 1200; 9-base prime witness 21523361; Fermat and perfect-fourth boundaries'.format(tests))

if __name__ == '__main__': run()
