"""Verify the cyclic unbordered-conjugate spectrum for weight-three binary words.

Uses only Python standard library. The finite exhaustive checks corroborate,
but do not replace, the independent all-length combinatorial proof.
"""
from collections import Counter
from itertools import combinations
from math import comb


def unbordered(s):
    return all(s[:k] != s[-k:] for k in range(1, len(s)))


def brute_count(s):
    n = len(s)
    return sum(unbordered(s[j:] + s[:j]) for j in range(n))


def cyclic_gaps(s):
    n = len(s)
    ones = [i for i, x in enumerate(s) if x == '1']
    assert len(ones) == 3
    return tuple((ones[(j + 1) % 3] - ones[j] - 1) % n for j in range(3))


def gap_count(g):
    return sum(g[j] != g[(j + 1) % 3] for j in range(3))


def spectrum(n):
    z = int(n % 3 == 0)
    two = n * ((n - 3) // 2 + 1 - z)
    zero = n // 3 if z else 0
    three = comb(n, 3) - zero - two
    assert three >= 0
    return {0: zero, 2: two, 3: three}


def verify():
    tested = 0
    for n in range(3, 24):
        tally = Counter()
        for positions in combinations(range(n), 3):
            s = ''.join('1' if k in positions else '0' for k in range(n))
            k = brute_count(s)
            g = cyclic_gaps(s)
            assert k == gap_count(g), (s, g, k)
            tally[k] += 1
            tested += 1
        assert all(tally[j] == expected for j, expected in spectrum(n).items()), (n, tally)
        assert not (tally.keys() - {0, 2, 3}), (n, tally)
    for n in range(3, 121):
        gap_tally = Counter()
        for a in range(n - 2):
            for b in range(n - 2 - a):
                c = n - 3 - a - b
                assert c >= 0
                gap_tally[gap_count((a, b, c))] += 1
        for r, expected in spectrum(n).items():
            assert n * gap_tally[r] == 3 * expected, (n, r, gap_tally[r], expected)
        assert sum(gap_tally.values()) == comb(n - 1, 2)
    print('ALL_CHECKS_PASS', 'exhaustive_words', tested, 'gap_n_max', 120)


if __name__ == '__main__':
    verify()
