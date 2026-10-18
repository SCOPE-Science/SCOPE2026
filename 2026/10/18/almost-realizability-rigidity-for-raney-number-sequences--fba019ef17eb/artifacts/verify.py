#!/usr/bin/env python3
"""Finite arithmetic spot checks for a theorem on Raney sequences.
The infinite theorem is proved algebraically in RESULT.md.
"""
from math import comb, isqrt


def raney(p, r, n):
    num = r * comb(p * n + r, n)
    den = p * n + r
    assert num % den == 0
    return num // den


def primes_upto(n):
    return [q for q in range(2, n + 1)
            if all(q % d for d in range(2, isqrt(q) + 1))]


def run():
    assert all(raney(1, 1, n) == 1 for n in range(1, 201))
    checked_integrality = 0
    for p in range(1, 10):
        for r in range(1, 11):
            for n in range(1, 33):
                assert raney(p, r, n) > 0
                checked_integrality += 1

    checked_prime = 0
    checked_semiprime = 0
    primes = [q for q in primes_upto(97) if q >= 5]
    for p in range(1, 10):
        for r in range(1, 11):
            for q in primes:
                if q <= max(p, r):
                    continue
                a1 = raney(p, r, 1)
                aq = raney(p, r, q)
                assert a1 == r
                assert aq % q == p % q
                assert (aq - a1) % q == (p-r) % q
                checked_prime += 1
    for s in range(1, 13):
        a1 = raney(s, s, 1)
        a2 = raney(s, s, 2)
        for q in primes:
            if q <= max(2*s, s*(s-1)//2):
                continue
            aq = raney(s, s, q)
            a2q = raney(s, s, 2*q)
            assert a2q % q == (s*(2*s-1)) % q
            defect = a2q - aq - a2 + a1
            assert defect % q == (s*(s-1)//2) % q
            if s > 1:
                assert defect % q != 0
            checked_semiprime += 1
    print('VERIFY_OK')
    print(f'positive integer values checked: {checked_integrality}')
    print(f'prime-index Lucas congruence checks: {checked_prime}')
    print(f'diagonal 2-prime-index Möbius checks: {checked_semiprime}')
    print('singleton constant sequence checked through n=200')
    print('limits: finite spot checks; the unrestricted result uses the published proof in RESULT.md')


if __name__ == '__main__':
    run()
