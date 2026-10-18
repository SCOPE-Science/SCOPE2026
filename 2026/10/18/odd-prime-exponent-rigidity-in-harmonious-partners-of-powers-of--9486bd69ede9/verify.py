#!/usr/bin/env python3
"""Finite exact-arithmetic cross-check of a divisor-sum classification."""

def primes_through(bound):
    is_prime = [True] * (bound + 1)
    is_prime[0] = is_prime[1] = False
    for q in range(2, int(bound ** 0.5) + 1):
        if is_prime[q]:
            for j in range(q*q, bound + 1, q):
                is_prime[j] = False
    return [q for q in range(3, bound + 1, 2) if is_prime[q]]


def divisor_sigma(n):
    from math import isqrt
    total = 0
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            total += d
            if d != n // d:
                total += n // d
    return total


def main():
    tested = 0
    count = 0
    for k in range(1, 17):
        y = 1 << k
        sigma_a = 2*y - 1
        for r in range(1, 17):
            x = 1 << r
            for p in primes_through(997):
                power = 1
                ssum = 1
                for s in range(1, 7):
                    power *= p
                    ssum += power
                    sigma_b = (2*x - 1)*ssum
                    b = x*power
                    lhs = y*sigma_b + b*sigma_a
                    rhs = sigma_a*sigma_b
                    expected = (s == 1 and r == k and p == y-1)
                    observed = (lhs == rhs)
                    assert observed == expected, (k,r,s,p,lhs,rhs)
                    tested += 1
                    count += observed
    assert count > 0
    direct_tests = 0
    for k in range(1, 7):
        a = 2**k
        for r in range(1, 7):
            for p in primes_through(23):
                for s in (1, 2):
                    b = 2**r * p**s
                    direct = a * divisor_sigma(b) + b * divisor_sigma(a) == divisor_sigma(a) * divisor_sigma(b)
                    expected = (s == 1 and r == k and p == 2**k-1)
                    assert direct == expected, (k,r,p,s)
                    direct_tests += 1
    print(f'VERIFY_OK finite exact profiles={tested}, harmonious_matches={count}, direct_divisor_checks={direct_tests}')


if __name__ == '__main__':
    main()
