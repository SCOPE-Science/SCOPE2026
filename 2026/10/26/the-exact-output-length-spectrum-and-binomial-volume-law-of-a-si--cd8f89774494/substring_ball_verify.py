"""Exhaustively verify local substring-edit shell sizes and the entire size spectrum.

Run: python3 substring_ball_verify.py
Only Python standard library is used.
"""
from collections import Counter
from itertools import product
from math import comb


def observed_shells(word, q, k):
    n = len(word)
    shells = {offset: set() for offset in range(-k, k + 1)}
    for deleted in range(k + 1):
        for inserted in range(k + 1):
            for start in range(n - deleted + 1):
                left = word[:start]
                right = word[start + deleted:]
                for middle in product(range(q), repeat=inserted):
                    shells[inserted - deleted].add(left + middle + right)
    return {offset: len(outputs) for offset, outputs in shells.items()}


def predicted_shells(word, q, k):
    n = len(word)
    r = n - k
    shells = {-k: 1 + sum(word[j] != word[j+k] for j in range(r))}
    for inserted in range(1, k + 1):
        shells[inserted - k] = q**(inserted - 1) * (q + r * (q - 1))
    for deleted in range(k):
        shells[k - deleted] = q**(k - 1) * (q + (n - deleted) * (q - 1))
    return shells


def expected_histogram(n, q, k):
    r = n - k
    baseline = sum(predicted_shells((0,) * n, q, k).values())
    return Counter({baseline + j: q**k * comb(r, j) * (q-1)**j
                    for j in range(r+1)})


cases = words = 0
for q in (2, 3, 4):
    for k in (1, 2, 3):
        for n in range(k, k + 5):
            if q**n > 10000:
                continue
            histogram = Counter()
            for word in product(range(q), repeat=n):
                got = observed_shells(word, q, k)
                predicted = predicted_shells(word, q, k)
                assert got == predicted, (word, q, k, got, predicted)
                histogram[sum(got.values())] += 1
                words += 1
            assert histogram == expected_histogram(n, q, k), (q, n, k, histogram)
            cases += 1
            print('PASS q=%d n=%d k=%d centers=%d bins=%d' %
                  (q, n, k, q**n, len(histogram)))
print('VERIFIED_CASES=%d VERIFIED_CENTERS=%d' % (cases, words))
print('VERIFY_OK')
