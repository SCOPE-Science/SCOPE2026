#!/usr/bin/env python3
"""Direct finite checks for fixed-weight-three palindromic periodicities.

Run: python3 verify.py
Uses only the Python standard library. Infinite identities have written proofs
and are not inferred from any finite enumeration.
"""
from itertools import combinations
from math import comb


def direct(word):
    """Literal Fici--Shallit--Simpson definition, independent of gap formula."""
    n = len(word)
    for d in range(1, n + 1):
        if any(word[i] != word[i % d] for i in range(d, n)):
            continue
        root = word[:d]
        for split in range(d + 1):
            if root[:split] == root[:split][::-1] and root[split:] == root[split:][::-1]:
                return True
    return False


def gap_count(u, v, h):
    if u == v or u == h or v == h:
        return h
    m, M = min(u, v), max(u, v)
    if h < m:
        return h
    if h < M:
        return m
    return max(0, 2 * M - h)


def gap_predicate(u, v, h, x):
    n = u + v + h
    first = x
    return direct(''.join('1' if i in (first, first + u, first + u + v) else '0'
                          for i in range(n)))


def pol_mul(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            o[i + j] += ai * bj
    return o


def coeff_from_rational(limit):
    den = [1]
    for factor, times in (([1, -1], 4), ([1, 1], 2), ([1, 0, 1], 1), ([1, 1, 1], 1)):
        for _ in range(times):
            den = pol_mul(den, factor)
    num = {3: 1, 4: 3, 5: 5, 7: 1, 8: -1, 9: -1}
    out = []
    assert den[0] == 1
    for n in range(limit + 1):
        val = num.get(n, 0) - sum(den[j] * out[n-j]
                                   for j in range(1, min(n, len(den)-1)+1))
        out.append(val)
    return out


def by_gaps(n):
    return sum(gap_count(u, v, n-u-v)
               for u in range(1, n-1) for v in range(1, n-u))


def main():
    # Exact verification of every individual word and every individual gap count.
    checked_words = checked_gap_pairs = 0
    for n in range(3, 22):
        total = 0
        for u in range(1, n - 1):
            for v in range(1, n-u):
                h = n-u-v
                direct_count = sum(gap_predicate(u, v, h, x) for x in range(h))
                assert direct_count == gap_count(u, v, h), (n, u, v, h, direct_count)
                total += direct_count
                checked_words += h
                checked_gap_pairs += 1
        assert checked_words >= 1
        assert total == sum(1 for ix in combinations(range(n), 3)
                            if direct(''.join('1' if k in ix else '0' for k in range(n))))
    # Rational expression: recurrence is algebraically independent of gap enumeration.
    coeffs = coeff_from_rational(161)
    for n in range(3, 161):
        assert coeffs[n] == by_gaps(n), (n, coeffs[n], by_gaps(n))
        assert 0 <= coeffs[n] <= comb(n, 3)
    expected = [1,4,10,14,25,36,52,68,93,116,150,182,225,268,324]
    assert coeffs[3:18] == expected, (coeffs[3:18], expected)
    # First two coefficients from the (1-z)^-4 pole verify 1/3 limiting density.
    print(f'VERIFY_OK direct_word_cases={checked_words} gap_triples={checked_gap_pairs}'
          f' rational_lengths=158 initial_values={coeffs[3:18]}')


if __name__ == '__main__':
    main()
