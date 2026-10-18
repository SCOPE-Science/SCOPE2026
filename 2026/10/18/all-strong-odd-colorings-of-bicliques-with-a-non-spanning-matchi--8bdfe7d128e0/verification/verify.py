#!/usr/bin/env python3
"""Independent finite checks of strong odd colorings of matching-deleted bicliques.
Usage: python3 verify_matching_deleted_strong_odd.py
Requires only Python 3 standard library.  The universal result is established by proof,
not by the finite tests in this file.
"""
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def odd_partitions(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0:
        return 0
    return sum(comb(n - 1, j - 1) * odd_partitions(n - j, k - 1)
               for j in range(1, n + 1, 2))


def formula(a, b, t):
    r, s = a - t, b - t
    result = {}
    for fused in range(t + 1):
        for k in range(r + 1):
            for l in range(s + 1):
                mult = comb(t, fused) * odd_partitions(r, k) * odd_partitions(s, l)
                if mult:
                    c = 2 * t - fused + k + l
                    result[c] = result.get(c, 0) + mult
    return result


def direct_partition_histogram(a, b, t):
    N = a + b
    adj = [0] * N
    for x in range(a):
        for y in range(b):
            if x < t and x == y:
                continue
            z = a + y
            adj[x] |= 1 << z
            adj[z] |= 1 << x
    blocks = []
    hist = {}
    tested = [0]
    def enum(v):
        if v == N:
            tested[0] += 1
            for x in range(N):
                for block in blocks:
                    count = (adj[x] & block).bit_count()
                    if count != 0 and count % 2 == 0:
                        return
            hist[len(blocks)] = hist.get(len(blocks), 0) + 1
            return
        bit = 1 << v
        for idx in range(len(blocks)):
            if adj[v] & blocks[idx]:
                continue
            blocks[idx] |= bit
            enum(v + 1)
            blocks[idx] ^= bit
        blocks.append(bit)
        enum(v + 1)
        blocks.pop()
    enum(0)
    return hist, tested[0]


def optimal_profile(a, b, t):
    r, s = a - t, b - t
    chi = t + 2 + int(r % 2 == 0) + int(s % 2 == 0)
    m = (2 ** (r - 2) if r % 2 == 0 else 1)
    m *= (2 ** (s - 2) if s % 2 == 0 else 1)
    return chi, m


def fall(q, k):
    if q < k:
        return 0
    answer = 1
    for v in range(k):
        answer *= (q - v)
    return answer


def main():
    cases = 0
    seen = 0
    for a in range(2, 6):
        for b in range(a, 6):
            for t in range(a):
                predicted = formula(a, b, t)
                actual, tested = direct_partition_histogram(a, b, t)
                assert predicted == actual, (a, b, t, predicted, actual)
                chi, opt = optimal_profile(a, b, t)
                assert min(actual) == chi and actual[chi] == opt, (a, b, t)
                for q in range(1, a + b + 3):
                    assert sum(coefficient * fall(q, k) for k, coefficient in actual.items()) == \
                           sum(coefficient * fall(q, k) for k, coefficient in predicted.items())
                cases += 1
                seen += tested
    for a, b, t in [(4, 4, 0), (4, 4, 1), (4, 4, 2), (4, 4, 3),
                    (5, 5, 0), (5, 5, 1), (5, 5, 4), (6, 9, 5), (20, 21, 7)]:
        cc = formula(a, b, t)
        chi, opt = optimal_profile(a, b, t)
        assert min(cc) == chi and cc[chi] == opt
        print(f'CHECK a={a} b={b} t={t}: minimum={chi}, minimum_partitions={opt}, colors_at_minimum={opt*factorial(chi)}')
    print(f'VERIFICATION_OK exhaustive_profile_cases={cases} canonical_partitions_tested={seen}')

if __name__ == '__main__':
    main()
