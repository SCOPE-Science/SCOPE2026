#!/usr/bin/env python3
"""Reproducible finite certificate for an order-sixteen binary de Bruijn cycle.

Uses only Python's standard library. Positions are zero-based and cyclic.
"""
from collections import Counter

ORDER = 16
N = 1 << ORDER
# The six length-thirteen factors and all their circular starting positions.
CERTIFICATE = (
    ('0000100000000', (12, 268, 524, 780, 1036, 1292, 1548, 1804), (9, 10, 11)),
    ('0001000000000', (13, 141, 269, 397, 525, 653, 781, 909), (10, 11, 12)),
    ('1000000000001', (128, 144, 160, 176, 192, 208, 224, 240), (13, 14, 15)),
    ('0010000000100', (2054, 2118, 2182, 2246, 2310, 2374, 2438, 2502), (3, 4, 5)),
    ('1100010001001', (29331, 29347, 29379, 29411, 29443, 29459, 29491, 29523), (0, 1, 2)),
    ('1111000100111', (33033, 33081, 33193, 33305, 33417, 33513, 33625, 33737), (6, 7, 8)),
)

def fkm_binary(n):
    a = [0] * (2 * n)
    output = []
    def visit(t, p):
        if t > n:
            if n % p == 0:
                output.extend(a[1:p + 1])
            return
        a[t] = a[t - p]
        visit(t + 1, p)
        for j in range(a[t - p] + 1, 2):
            a[t] = j
            visit(t + 1, t)
    visit(1, 1)
    return bytes(output)

def independent_lyndon(n):
    # Directly list primitive lexicographically least conjugates.
    words = []
    for d in range(1, n + 1):
        if n % d:
            continue
        for v in range(1 << d):
            s = format(v, '0%db' % d)
            if all(s < s[j:] + s[:j] for j in range(1, d)):
                words.append(s)
    return bytes(int(c) for c in ''.join(sorted(words)))

def window_codes(word, length):
    q = (1 << length) - 1
    value = 0
    for j in range(length - 1):
        value = ((value << 1) | word[j]) & q
    for i in range(len(word)):
        value = ((value << 1) | word[(i + length - 1) % len(word)]) & q
        yield i, value

def admissible_periodic_offsets(word, k):
    # A uniformly k-spaced set covers every distinct factor iff each
    # distinct length-l factor has some occurrence intersecting that residue.
    n = len(word)
    valid = set(range(k))
    for length in range(1, k + 1):
        incidence = {}
        for start, code in window_codes(word, length):
            residues = {(start + j) % k for j in range(length)}
            incidence.setdefault(code, set()).update(residues)
        valid.intersection_update(*(incidence.values()))
    return sorted(valid)

def run():
    word = fkm_binary(ORDER)
    assert len(word) == N
    assert word == independent_lyndon(ORDER)
    unique = set(value for _, value in window_codes(word, ORDER))
    assert len(unique) == N
    assert unique == set(range(N))

    removed_residues = set()
    for factor, expected_starts, expected_forbidden in CERTIFICATE:
        code = int(factor, 2)
        actual_starts = tuple(i for i, v in window_codes(word, len(factor)) if v == code)
        assert actual_starts == expected_starts, (factor, actual_starts)
        all_offsets_hit = {
            (start + j) % ORDER
            for start in actual_starts for j in range(len(factor))
        }
        forbidden = tuple(sorted(set(range(ORDER)) - all_offsets_hit))
        assert forbidden == expected_forbidden, (factor, forbidden)
        removed_residues.update(forbidden)
        print('factor', factor, 'occurrences', len(actual_starts),
              'forbidden offsets', ','.join(map(str, forbidden)))
    assert removed_residues == set(range(ORDER))
    print('all sixteen equally-spaced offsets excluded')

    # Supporting dyadic comparison, using all factor lengths up to the order.
    for k in (1, 2, 4, 8):
        w = fkm_binary(k)
        assert len(w) == 1 << k
        if (1 << k) % k == 0:
            admissible = admissible_periodic_offsets(w, k)
            assert admissible, (k, admissible)
            print('smaller dyadic order', k, 'admissible offsets', admissible)
    print('CERTIFICATE_OK: no circular string attractor of size 4096')

if __name__ == '__main__':
    run()
