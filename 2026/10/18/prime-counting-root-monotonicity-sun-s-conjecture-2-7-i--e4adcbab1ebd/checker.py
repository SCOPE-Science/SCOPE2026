"""Reproducible integer certificate for a prime-counting monotonicity theorem.

The infinite part of the theorem uses the classical Brun--Titchmarsh
and Rosser--Schoenfeld bounds; these are mathematical inputs, not
conclusions of the finite code.
"""
from math import isqrt

MAX_N = 299
LIMIT = MAX_N * (MAX_N + 1)


def sieve_prime_counts(limit):
    isprime = bytearray(b'\x01') * (limit + 1)
    isprime[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if isprime[p]:
            for composite in range(p * p, limit + 1, p):
                isprime[composite] = 0
    counts = [0] * (limit + 1)
    count = 0
    for m, prime in enumerate(isprime):
        count += prime
        counts[m] = count
    return counts


def trial_prime_counts(limit):
    # Independently test divisibility by every candidate up to sqrt(m).
    counts = [0] * (limit + 1)
    count = 0
    for m in range(2, limit + 1):
        primal = True
        for d in range(2, isqrt(m) + 1):
            if m % d == 0:
                primal = False
                break
        if primal:
            count += 1
        counts[m] = count
    return counts


def main():
    assert LIMIT == 89700
    first = sieve_prime_counts(LIMIT)
    second = trial_prime_counts(LIMIT)
    assert first == second, 'Two prime-count implementations disagree'
    assert first[300] == 62
    total = 0
    minimum = None
    witnesses = []
    for n in range(5, MAX_N + 1):
        for k in range(1, n + 1):
            a = first[n * k]
            b = first[n * (k + 1)]
            assert a >= 3 and b >= a
            difference = pow(a, k + 1) - pow(b, k)
            assert difference > 0, (n, k, a, b, difference)
            total += 1
            if minimum is None or difference < minimum:
                minimum = difference
                witnesses = [(n, k, a, b)]
            elif difference == minimum:
                witnesses.append((n, k, a, b))
    assert total == 44840
    assert pow(11, 4) < 62 * pow(4, 4)  # e < 11/4 implies e^4 < 62.
    print('verified exact small cases:', total)
    print('maximum argument counted:', LIMIT)
    print('prime-count at 300:', first[300])
    print('minimum positive integer-power margin:', minimum)
    print('minimum-margin cases:', witnesses)
    print('prime-count cross-check: agrees at all integers 0..89700')
    print('certificate: PASS')


if __name__ == '__main__':
    main()
