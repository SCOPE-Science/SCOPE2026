"""Exact two-method verification of prime-Fibonacci seed thresholds."""
from functools import lru_cache
from math import isqrt

CAP = 4919
EXPECTED = {
    2: 5, 3: 7, 4: 7, 5: 11, 6: 11, 7: 19, 8: 29,
    9: 41, 10: 47, 11: 53, 12: 53, 13: 131, 14: 443,
    15: 461, 16: 521, 17: 521, 18: 761, 19: 1487,
    20: 2381, 21: 3863, 22: 3863, 23: 4919,
}


def trial_is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def direct_next(a, b):
    s = a + b
    if s & (s - 1) == 0:
        return None
    while s % 2 == 0:
        s //= 2
    for d in range(3, isqrt(s) + 1, 2):
        if s % d == 0:
            return d
    return s


def direct_depth(a, b):
    depth = 2
    while (r := direct_next(a, b)) is not None:
        a, b = b, r
        depth += 1
    return depth


def smallest_factor_sieve(limit):
    result = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if result[p] == p:
            for j in range(p * p, limit + 1, p):
                if result[j] == j:
                    result[j] = p
    return result


def sieve_primes(limit):
    ok = bytearray(b'\x01') * (limit + 1)
    ok[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if ok[p]:
            ok[p * p:limit + 1:p] = b'\x00' * ((limit - p * p) // p + 1)
    return [n for n in range(3, limit + 1, 2) if ok[n]]


def verify():
    primes_sieve = sieve_primes(CAP)
    primes_trial = [n for n in range(3, CAP + 1, 2) if trial_is_prime(n)]
    assert primes_trial == primes_sieve
    assert len(primes_sieve) == 656 and primes_sieve[-1] == 4919
    smallest_factor = smallest_factor_sieve(2 * CAP)

    @lru_cache(None)
    def cached_depth(a, b):
        s = a + b
        if s & (s - 1) == 0:
            return 2
        while s % 2 == 0:
            s //= 2
        return 1 + cached_depth(b, smallest_factor[s])

    first = {}
    witnesses = {k: [] for k in EXPECTED}
    largest_before = 0
    max_depth = 2
    compared = 0
    for index, p in enumerate(primes_sieve):
        for q in primes_sieve[:index]:
            for a, b in ((p, q), (q, p)):
                length_a = direct_depth(a, b)
                length_b = cached_depth(a, b)
                assert length_a == length_b, (a, b, length_a, length_b)
                compared += 1
                max_depth = max(max_depth, length_a)
                for length in EXPECTED:
                    if length_a >= length:
                        if length not in first:
                            first[length] = p
                        if first[length] == p:
                            witnesses[length].append((a, b, length_a))
        if p < CAP:
            largest_before = max_depth
    assert compared == 429680
    assert first == EXPECTED, (first, EXPECTED)
    assert largest_before == 22 and max_depth == 23
    assert witnesses[23] == [(4007, 4919, 23)]

    path = [4007, 4919]
    while (r := direct_next(path[-2], path[-1])) is not None:
        path.append(r)
    assert path == [4007, 4919, 4463, 4691, 23, 2357, 5, 1181,
                    593, 887, 5, 223, 3, 113, 29, 71, 5, 19,
                    3, 11, 7, 3, 5]
    assert path[-2] + path[-1] == 8
    print('PASS: 656 odd primes, 429680 ordered seed pairs, both algorithms agree')
    print('PASS: exact thresholds for all lengths 2..23')
    print('PASS: maximal depth below 4919 = 22')
    print('PASS: sole 23-term pair at cap = (4007, 4919)')
    print('thresholds:', sorted(EXPECTED.items()))
    return 0


if __name__ == '__main__':
    raise SystemExit(verify())
