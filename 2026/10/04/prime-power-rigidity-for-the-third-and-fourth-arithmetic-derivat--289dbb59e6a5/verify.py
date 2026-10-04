#!/usr/bin/env python3
from math import isqrt

def primes_below(n):
    s = bytearray(b"\x01") * n
    if n > 0: s[0] = 0
    if n > 1: s[1] = 0
    for p in range(2, isqrt(n - 1) + 1):
        if s[p]:
            start = p * p
            s[start:n:p] = b"\x00" * (((n - 1 - start) // p) + 1)
    return [i for i in range(2, n) if s[i]]

def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def D(n):
    if n <= 1:
        return 0
    return sum(a * (n // p) for p, a in factorint(n).items())

def iterate(n, r):
    for _ in range(r):
        n = D(n)
    return n

def main():
    c2 = 0
    for p in primes_below(64):
        if p >= 3:
            n = p * p
            assert iterate(n, 4) != n
            c2 += 1

    c3 = 0
    for p in primes_below(128):
        if p >= 5:
            n = p ** 3
            assert iterate(n, 4) != n
            c3 += 1

    for p in primes_below(500):
        for e in range(1, 13):
            n = p ** e
            for r in (3, 4):
                assert (iterate(n, r) == n) == (e == p), (p, e, r)

    for p in (2, 3, 5, 7):
        n = p ** p
        assert D(n) == n
        assert iterate(n, 3) == n
        assert iterate(n, 4) == n

    print("VERIFY_OK")
    print("fourth_iterate_e2_primes_checked=" + str(c2))
    print("fourth_iterate_e3_primes_checked=" + str(c3))
    print("regression_prime_bound=500")
    print("regression_exponent_bound=12")

if __name__ == "__main__":
    main()
