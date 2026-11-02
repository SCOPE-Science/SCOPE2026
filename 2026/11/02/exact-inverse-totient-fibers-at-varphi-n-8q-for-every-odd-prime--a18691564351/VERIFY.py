#!/usr/bin/env python3
"""Independent bounded checks for the exact inverse-totient 8q theorem.

Uses a totient sieve, independent of the theorem's prime-support proof.
Finite checks are not a proof for all primes.
"""
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def totient_sieve(limit):
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for k in range(p, limit + 1, p):
                phi[k] -= phi[k] // p
    return phi


def predicted(q):
    if q == 3:
        return {35, 39, 45, 52, 56, 70, 72, 78, 84, 90}
    if q == 5:
        return {41, 55, 75, 82, 88, 100, 110, 132, 150}
    r1, r2, r3 = 2 * q + 1, 4 * q + 1, 8 * q + 1
    if q % 3 == 1:
        return {j * r2 for j in (3, 4, 6)} if is_prime(r2) else set()
    answer = set()
    if is_prime(r1):
        answer.update(j * r1 for j in (5, 8, 10, 12))
    if is_prime(r3):
        answer.update((r3, 2 * r3))
    return answer


def main():
    q_max = 2000
    phi = totient_sieve(6 * 8 * q_max)
    primes = [q for q in range(3, q_max + 1, 2) if is_prime(q)]
    by_value = {}
    for n in range(1, len(phi)):
        by_value.setdefault(phi[n], []).append(n)
    hist = {}
    count = 0
    for q in primes:
        target = set(by_value.get(8 * q, []))
        expected = predicted(q)
        assert target == expected, (q, sorted(target), sorted(expected))
        assert len(target) != 1
        hist[len(expected)] = hist.get(len(expected), 0) + 1
        count += len(target)
    # The universal 6k bound follows from prime-divisor support; the bound
    # is checked here by a larger sieve at the largest q only as a safeguard.
    q = primes[-1]
    bigger = totient_sieve(10 * 8 * q)
    assert {n for n in range(1, len(bigger)) if bigger[n] == 8 * q} == predicted(q)
    print('VERIFY_OK primes=%d q_max=%d independent_totient_sieve=yes cardinality_histogram=%s checked_preimages=%d enlarged_boundary=yes' % (len(primes), q_max, sorted(hist.items()), count))


if __name__ == '__main__':
    main()
