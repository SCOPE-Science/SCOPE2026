#!/usr/bin/env python3
import math


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factor_multiset(n):
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    return out


def sigma(n):
    total = 1
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            power_sum = 1
            power = 1
            while x % p == 0:
                x //= p
                power *= p
                power_sum += power
            total *= power_sum
        p = 3 if p == 2 else p + 2
    if x > 1:
        total *= 1 + x
    return total


def primes_upto(n):
    return [p for p in range(2, n + 1) if is_prime(p)]


def predicted(a, b, k, limit):
    c = a - b
    T = a * b - c * k
    ans = set()

    # Prime branch.
    num = b - k
    if num % c == 0:
        p = num // c
        if p <= limit and is_prime(p):
            ans.add(p)

    # Prime-square branch.
    Delta = b * b + 4 * c * (b - k)
    if Delta >= 0:
        s = math.isqrt(Delta)
        if s * s == Delta:
            for num in (b + s, b - s):
                den = 2 * c
                if num % den == 0:
                    p = num // den
                    if p >= 2 and p * p <= limit and is_prime(p):
                        ans.add(p * p)

    # Distinct-prime branch.
    if T == 0:
        if c == 1 and is_prime(b):
            for q in primes_upto(limit // b):
                if q != b:
                    ans.add(b * q)
    else:
        A = abs(T)
        for d in range(1, math.isqrt(A) + 1):
            if A % d:
                continue
            mags = {d, A // d}
            for m in mags:
                if A % m:
                    continue
                for u in (m, -m):
                    if T % u:
                        continue
                    v = T // u
                    if (u + b) % c or (v + b) % c:
                        continue
                    p = (u + b) // c
                    q = (v + b) // c
                    if p != q and is_prime(p) and is_prime(q) and p * q <= limit:
                        ans.add(p * q)
    return ans


def brute(a, b, k, limit):
    ans = set()
    for n in range(2, limit + 1):
        if len(factor_multiset(n)) <= 2 and b * sigma(n) == a * n + k:
            ans.add(n)
    return ans


def main():
    limit = 1000
    triples = 0
    checked_inputs = 0
    exceptional_triples = 0
    for a in range(2, 10):
        for b in range(1, a):
            if math.gcd(a, b) != 1:
                continue
            for k in range(-25, 41):
                if k == 0:
                    continue
                triples += 1
                got = brute(a, b, k, limit)
                want = predicted(a, b, k, limit)
                checked_inputs += limit - 1
                if got != want:
                    raise AssertionError((a, b, k, sorted(got ^ want)[:20]))
                c = a - b
                T = a * b - c * k
                if T == 0:
                    exceptional = (c == 1 and is_prime(b) and k == b * (b + 1))
                    if any(len(factor_multiset(n)) == 2 and len(set(factor_multiset(n))) == 2 for n in got):
                        assert exceptional, (a, b, k, got)
                    if exceptional:
                        exceptional_triples += 1
    # Explicit unbounded-family shape checks for several prime bases.
    for r in (2, 3, 5, 7, 11, 13):
        a, b, k = r + 1, r, r * (r + 1)
        for q in primes_upto(200):
            if q != r:
                n = r * q
                assert b * sigma(n) == a * n + k
    print(f"VERIFY_OK parameter_triples={triples} checked_inputs={checked_inputs} exceptional_triples={exceptional_triples} mismatches=0")


if __name__ == '__main__':
    main()
