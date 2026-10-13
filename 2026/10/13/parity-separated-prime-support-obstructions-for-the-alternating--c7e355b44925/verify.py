"""Finite checks supporting an elementary theorem about beta(n) | n-1.

This check does not establish statements for unbounded n; the accompanying
proof supplies that part. Run: python3 verify.py [limit]
"""
import sys
from math import gcd


def local_beta(p, exponent):
    value = 0
    sign = 1
    for j in range(exponent, -1, -1):
        value += sign * p ** j
        sign = -sign
    return value


def beta(n, spf):
    result = 1
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        result *= local_beta(p, e)
    return result


def small_direct_beta(n):
    # Toth's characterization: count k with gcd(k,n) a square.
    return sum(1 for k in range(1, n + 1)
               if is_square(gcd(k, n)))


def is_square(x):
    from math import isqrt
    return isqrt(x) ** 2 == x


def run(limit):
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, int(limit ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, limit + 1, p):
                if spf[m] == m:
                    spf[m] = p
    matches = []
    odd_support3 = 0
    even_support4 = 0
    for n in range(2, limit + 1):
        b = beta(n, spf)
        if n <= 300:
            assert b == small_direct_beta(n), (n, b)
        if (n - 1) % b:
            continue
        if spf[n] == n:
            continue  # primes are the trivial infinite family
        matches.append(n)
        factors = set()
        m = n
        while m > 1:
            p = spf[m]
            factors.add(p)
            while m % p == 0:
                m //= p
        if n % 2:
            odd_support3 += int(len(factors) <= 3)
        else:
            even_support4 += int(len(factors) <= 4 and n != 4)
    assert matches == [4], matches
    assert odd_support3 == 0 and even_support4 == 0
    print(f'CHECK_OK limit={limit} composite_hits={matches} '
          f'odd_support_le3={odd_support3} even_support_le4_excluding4={even_support4}')


if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 200000)
