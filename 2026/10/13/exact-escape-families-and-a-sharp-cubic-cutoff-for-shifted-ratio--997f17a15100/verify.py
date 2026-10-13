"""Finite arithmetic regression for the shifted rational-perfect classification.

The unbounded result is proved in RESULT.md. This script only cross-checks
small parameter and argument ranges by direct integer computation.
Run: python3 verify.py
"""
from math import isqrt

LIMIT = 200000
R_MAX = 35


def prime_sieve(limit):
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if is_prime[p]:
            for j in range(p * p, limit + 1, p):
                is_prime[j] = 0
    return is_prime


def sigma_sieve(limit):
    sigma = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            sigma[multiple] += divisor
    return sigma


def verify():
    primes = prime_sieve(LIMIT)
    sigma = sigma_sieve(LIMIT)
    solutions = {r: set() for r in range(1, R_MAX + 1)}
    for k in range(2, LIMIT + 1):
        for n in range(k, LIMIT + 1, k):
            r = sigma[n] - (k + 1) * (n // k)
            if 1 <= r <= R_MAX:
                solutions[r].add((k, n))

    expected_first = {(p, p*p) for p in range(2, isqrt(LIMIT)+1) if primes[p]}
    assert solutions[1] == expected_first, ('r1', solutions[1] ^ expected_first)
    assert solutions[2] == {(4, 4)}, ('r2', solutions[2])
    expected_third = {(2, 8), (9, 9)} | {
        (2, 2*q) for q in range(3, LIMIT//2+1, 2) if primes[q]
    }
    assert solutions[3] == expected_third, ('r3', solutions[3] ^ expected_third)

    all_non_escape = 0
    max_r_bound = 0
    for r in range(4, R_MAX + 1):
        p = r - 1
        cutoff = p**3
        max_r_bound = max(max_r_bound, cutoff)
        expected_escape = (
            {(p, p*q) for q in range(2, LIMIT//p + 1)
             if primes[q] and q != p} if primes[p] else set()
        )
        assert expected_escape <= solutions[r], ('missing_family', r)
        for k, n in solutions[r]:
            escape = (k == p and primes[p] and n % p == 0
                      and n//p != p and primes[n//p])
            assert escape or n <= cutoff, ('unbounded_candidate', r, k, n)
            if not escape:
                all_non_escape += 1

    sharp_instances = 0
    for p in range(3, R_MAX, 2):
        if not primes[p] or p**3 > LIMIT:
            continue
        r = p + 1
        if r < 4:
            continue
        assert (p, p**3) in solutions[r], ('missing_cubic_sharp_case', p)
        assert p**3 == (r-1)**3
        sharp_instances += 1

    print('VERIFY_OK')
    print(f'n_max={LIMIT} r_max={R_MAX}')
    print(f'r1_prime_square_cases={len(solutions[1])}')
    print(f'r2_cases={sorted(solutions[2])}')
    print(f'r3_cases={len(solutions[3])} exceptional=[(2,8),(9,9)]')
    print(f'r_ge4_non_escape_checked={all_non_escape}')
    print(f'largest_tested_cubic_cutoff={max_r_bound}')
    print(f'cubic_equality_prime_instances={sharp_instances}')
    print('all_ranged_comparisons=PASS')


if __name__ == '__main__':
    verify()
