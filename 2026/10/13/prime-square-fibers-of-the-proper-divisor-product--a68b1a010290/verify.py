#!/usr/bin/env python3
from math import isqrt

LIMIT = 5000

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]

def factorint(n):
    f = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def sigma(n):
    out = 1
    for p, a in factorint(n).items():
        out *= (p**(a+1)-1)//(p-1)
    return out

def s(n):
    return sigma(n) - n

def divisors(n):
    ds = [1]
    for p, a in factorint(n).items():
        old = list(ds)
        mul = 1
        add = []
        for _ in range(a):
            mul *= p
            add.extend(d*mul for d in old)
        ds.extend(add)
    return sorted(ds)

def main():
    ps = primes_upto(LIMIT)
    tested_divisors = 0
    exceptional = []
    for p in ps:
        M = p*p*(p+1)
        fib = []
        for n in divisors(M):
            tested_divisors += 1
            if n*s(n) == M:
                fib.append(n)
        expected = [6, 9] if p == 3 else [p*p]
        assert fib == expected, (p, M, fib, expected)
        if len(fib) > 1:
            exceptional.append((p, fib))
    assert exceptional == [(3, [6, 9])]
    print("VERIFY_OK")
    print("prime_limit=" + str(LIMIT))
    print("primes_checked=" + str(len(ps)))
    print("target_divisors_checked=" + str(tested_divisors))
    print("exceptional_fiber=p=3:{6,9}")

if __name__ == "__main__":
    main()
