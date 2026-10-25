#!/usr/bin/env python3
"""Exact local and finite checks for shifted-flat prime densities."""
import math
from fractions import Fraction


def sieve(limit):
    spf = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for multiple in range(p * p, limit + 1, p):
                if spf[multiple] == multiple:
                    spf[multiple] = p
    return spf


def odd_squarefree(n, spf):
    assert n > 0
    while n % 2 == 0:
        n //= 2
    while n > 1:
        q = spf[n]
        n //= q
        if n % q == 0:
            return False
        while n % q == 0:
            n //= q
    return True


def run():
    shifts = (1, 3, 5, 7, 9, 15, 21, 35, 105)
    limit = 600000
    spf = sieve(limit + max(shifts))
    local_checks = 0
    primes = [q for q in range(3, 102, 2) if spf[q] == q]
    for h in shifts:
        for q in primes:
            phi = q * (q - 1)
            allowed = sum(1 for a in range(q * q) if a % q != 0
                          and (a - h) % (q * q) != 0
                          and (a + h) % (q * q) != 0)
            assert allowed == phi - (0 if h % q == 0 else 2)
            local_checks += 1

    small = (3, 5, 7)
    modulus = math.prod(q * q for q in small)
    crt_checks = 0
    for h in shifts:
        actual = sum(1 for a in range(modulus)
                     if all(a % q != 0 and (a - h) % (q*q) != 0
                            and (a + h) % (q*q) != 0 for q in small))
        expected = math.prod(q * (q - 1) - (0 if h % q == 0 else 2)
                             for q in small)
        assert actual == expected
        crt_checks += 1

    base = Fraction(1)
    for q in primes:
        base *= Fraction(q * (q - 1) - 2, q * (q - 1))
    for h in shifts:
        corrected = base
        recomputed = Fraction(1)
        for q in primes:
            if h % q == 0:
                corrected *= Fraction(q * (q - 1), q * (q - 1) - 2)
            else:
                recomputed *= Fraction(q * (q - 1) - 2, q * (q - 1))
        assert corrected == recomputed

    prime_inputs = [p for p in range(107, limit + 1)
                    if spf[p] == p]
    observations = []
    for h in shifts:
        count = sum(odd_squarefree(p - h, spf) and
                    odd_squarefree(p + h, spf) for p in prime_inputs)
        observations.append((h, count, len(prime_inputs)))
    print('VERIFY_OK', 'local_residue_cases', local_checks,
          'exact_CRT_cases', crt_checks, 'finite_primes', len(prime_inputs))
    for h, count, total in observations:
        print('OBSERVED', h, count, total)


if __name__ == '__main__':
    run()
