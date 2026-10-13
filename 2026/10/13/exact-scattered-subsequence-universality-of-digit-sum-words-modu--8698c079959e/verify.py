#!/usr/bin/env python3
"""Finite, independent checks for digit-sum-modulo-(base+1) universality formula.

The theorem is symbolic; this program checks instances and local arithmetic lemmas.
Uses only Python standard library.
"""
from itertools import product


def digit_sum(n, base):
    assert n >= 0 and base >= 2
    ans = 0
    while n:
        ans += n % base
        n //= base
    return ans


def theorem_index(base, N):
    assert base >= 2 and N >= 0
    q, r = divmod(N, base)
    ans = q // 2
    if base % 2 and q % 2:
        t = 0
        z = q
        while z % base == 0:
            z //= base
            t += 1
        d = (-2 * (t + 1)) % (base + 1)
        assert d % 2 == 0 and d < base
        ans += int(r > d)
    return ans


def direct_prefixes(base, bound):
    # Greedy full-alphabet arch factorization; independent of closed formula.
    whole = (1 << (base + 1)) - 1
    seen = 0
    count = 0
    for N in range(bound + 1):
        assert count == theorem_index(base, N), (
            "prefix", base, N, count, theorem_index(base, N)
        )
        if N < bound:
            seen |= 1 << (digit_sum(N, base) % (base + 1))
            if seen == whole:
                count += 1
                seen = 0
    return bound + 1


def contains_as_subsequence(x, p):
    i = 0
    for c in x:
        if i < len(p) and c == p[i]:
            i += 1
    return i == len(p)


def direct_universality(base, length):
    word = [digit_sum(j, base) % (base + 1) for j in range(length)]
    alphabet = range(base + 1)
    k = 0
    while True:
        probes = product(alphabet, repeat=k + 1)
        if all(contains_as_subsequence(word, p) for p in probes):
            k += 1
        else:
            return k


def check_carry(base, max_q):
    # Explicit source-letter and parity/last-element identities used in proof.
    M = base + 1
    for q in range(1, max_q + 1):
        s0 = digit_sum(q - 1, base)
        s1 = digit_sum(q, base)
        tmp = q
        t = 0
        while tmp % base == 0:
            tmp //= base
            t += 1
        assert s1 - s0 == 1 - (base - 1) * t
        if base % 2:
            if q % 2 == 1:
                d = (-2 * (t + 1)) % M
                assert d % 2 == 0 and d < base
                assert (s1 + d - (s0 - 1)) % M == 0
                if t == 0:
                    assert d == base - 1
                else:
                    assert (digit_sum(q+1, base)-s1) == 1
        elif q % 2 == 1:
            assert t == 0
            assert (s1 - s0) % M == 1
    return max_q


def run():
    direct_checks = 0
    carry_checks = 0
    for b in range(2, 31):
        upper = 5000 if b < 13 else 2000
        direct_checks += direct_prefixes(b, upper)
        carry_checks += check_carry(b, 2000)
    brute_checks = 0
    for b in range(2, 7):
        for N in range(0, 31):
            brute = direct_universality(b, N)
            expected = theorem_index(b, N)
            assert brute == expected, (b, N, brute, expected)
            brute_checks += 1
    for b in range(2, 15):
        for k in range(2, 6):
            if b ** k > 2_000_000:
                break
            assert theorem_index(b, b ** k) == b ** (k - 1) // 2
    print('VERIFY_OK direct_prefixes=%d carry_relations=%d brute_subsequence_cases=%d bases=2..30 power_prefixes=checked' % (direct_checks, carry_checks, brute_checks))


if __name__ == '__main__':
    run()
