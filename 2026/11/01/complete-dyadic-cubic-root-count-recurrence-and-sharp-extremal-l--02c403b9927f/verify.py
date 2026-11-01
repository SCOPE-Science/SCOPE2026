#!/usr/bin/env python3
"""Exact, standalone checks for dyadic monic-cubic root-count law."""
from collections import Counter


def count_roots(a, b, c, modulus):
    return sum((x * x * x + a * x * x + b * x + c) % modulus == 0
               for x in range(modulus))


def direct_cubic_hist(k):
    q = 1 << k
    ans = Counter()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                ans[count_roots(a, b, c, q)] += 1
    return ans


def direct_square_hist(k):
    q = 1 << k
    return Counter(sum((x * x - d) % q == 0 for x in range(q))
                   for d in range(q))


def square_hist(k):
    assert k >= 1
    dcount = Counter()
    dcount[1 << (k // 2)] += 1  # d = 0
    for j in range((k - 1) // 2 + 1):
        m = k - 2 * j
        if m == 1:
            count, roots = 1, 1 << j
        elif m == 2:
            count, roots = 1, 1 << (j + 1)
        else:
            count, roots = 1 << (m - 3), 1 << (j + 2)
        dcount[roots] += count
    dcount[0] = (1 << k) - sum(dcount.values())
    return dcount


def cubic_hist(k, stored):
    if k <= 3:
        return stored[k]
    h = Counter()
    h[0] += (1 << (3 * k - 2)) + 10 * (1 << (3 * k - 6))
    h[1] += 1 << (3 * k - 2)
    h[2] += 1 << (3 * k - 4)
    for roots, freq in square_hist(k).items():
        h[1 + roots] += (1 << (2 * k - 2)) * freq
    for roots, freq in stored[k - 3].items():
        h[4 * roots] += 16 * freq
    return h


def expected_max(k):
    t, j = divmod(k - 1, 3)
    return (2, 3, 5)[j] * (4 ** t), (2, 8, 16)[j] * (16 ** t)


def main():
    table = {
        1: Counter({0: 2, 1: 4, 2: 2}),
        2: Counter({0: 24, 1: 24, 2: 8, 3: 8}),
        3: Counter({0: 208, 1: 208, 2: 32, 3: 32, 4: 16, 5: 16}),
    }
    for k in range(1, 10):
        assert square_hist(k) == direct_square_hist(k), ('square', k)
    checked = 0
    for k in range(1, 7):
        predicted = cubic_hist(k, table)
        measured = direct_cubic_hist(k)
        assert predicted == measured, ('cubic', k, predicted, measured)
        checked += 1 << (3 * k)
        table[k] = predicted
    for k in range(7, 25):
        table[k] = cubic_hist(k, table)
    for k in range(1, 25):
        hist = table[k]
        assert sum(hist.values()) == 1 << (3 * k)
        assert sum(roots * count for roots, count in hist.items()) == 1 << (3 * k)
        expected, number = expected_max(k)
        assert max(roots for roots, count in hist.items() if count) == expected
        assert hist[expected] == number
    assert table[4] == Counter({0: 1696, 1: 1792, 2: 256, 4: 64, 5: 256, 8: 32})
    assert table[5] == Counter({0: 13696, 1: 14592, 2: 2048, 4: 384,
                               5: 1536, 8: 128, 9: 256, 12: 128})
    print('VERIFY_OK direct_moduli=6 direct_cubics=%d quadratic_moduli=9 '
          'recurrence_levels=24 exact_integer=yes max_cycle=2,3,5' % checked)


if __name__ == '__main__':
    main()
