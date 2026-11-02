#!/usr/bin/env python3
"""Exact square-divisor sieve for a first usable power-of-two exponent.

Run: python3 verify.py
Uses only Python's standard library and exact integer arithmetic.
"""
from math import isqrt

BOUND = 1_000_000_000
EXPONENTS = (0, 1, 2, 3, 5)
EXPECTED_CANDIDATES = (
    9976579, 87018271, 189954151, 360530683, 530060227,
    861270307, 949293907, 978131779, 998649907,
)
EXPECTED_PRIMES = (189954151, 998649907)


def prime_sieve(limit):
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit) + 1):
        if is_prime[d]:
            is_prime[d*d::d] = b'\x00' * ((limit - d*d)//d + 1)
    return [d for d in range(limit + 1) if is_prime[d]]


def factor(n, primes):
    result = []
    for q in primes:
        if q*q > n:
            break
        if n % q == 0:
            exp = 0
            while n % q == 0:
                n //= q
                exp += 1
            result.append((q, exp))
    if n > 1:
        result.append((n, 1))
    return result


def squarefree(n, primes):
    if n <= 0:
        return False
    return all(exponent == 1 for _, exponent in factor(n, primes))


def main():
    primes = prime_sieve(isqrt(BOUND))
    K = (BOUND - 7)//36
    mask = bytearray(K + 1)
    for q in primes:
        if q < 5:
            continue
        modulus = q*q
        inverse = pow(36, -1, modulus)
        for bit, a in enumerate(EXPONENTS):
            power = 1 << a
            residue = ((power - 7) * inverse) % modulus
            # A positive remainder containing q^2 must be at least q^2.
            min_k = max(0, (power + modulus - 7 + 35)//36)
            if residue < min_k:
                residue += ((min_k - residue + modulus - 1)//modulus) * modulus
            for k in range(residue, K + 1, modulus):
                mask[k] |= 1 << bit
    candidates = [36*k + 7 for k, bits in enumerate(mask) if bits == 31]
    assert tuple(candidates) == EXPECTED_CANDIDATES, candidates
    prime_hits = [p for p in candidates if len(factor(p, primes)) == 1 and factor(p, primes)[0] == (p, 1)]
    assert tuple(prime_hits) == EXPECTED_PRIMES, prime_hits
    checks = {}
    for p in prime_hits:
        # All six lower exponents fail: a=4 because 9 divides p-16.
        assert (p - 16) % 9 == 0
        for a in EXPONENTS:
            assert not squarefree(p - (1 << a), primes)
            assert (p - (1 << a)) > 0
        assert squarefree(p - 64, primes)
        checks[p] = factor(p - 64, primes)
    assert prime_hits[0] == min(prime_hits)
    assert all(p % 36 == 7 for p in prime_hits)
    print('VERIFY_OK')
    print('bound=', BOUND, 'residue_classes=', K + 1,
          'obstructing_primes=', len([q for q in primes if q >= 5]))
    print('all_integer_five_obstruction_candidates=', candidates)
    print('prime_candidates=', prime_hits)
    print('first_minimum_exponent_6=', prime_hits[0])
    print('sixth_exponent_factorizations=', checks)
    print('exact_modular_congruence_sieve=PASS deterministic_trial_division=PASS')

if __name__ == '__main__':
    main()
