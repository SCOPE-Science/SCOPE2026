#!/usr/bin/env python3
"""Exact finite check of the necessary column inequalities for d'=10.

For a candidate shape S subset {2,...,9}, the low-count columns from the
left and right have counts S increasing followed by 10, and S^c increasing
followed by 10. Lemma 9.1 of He (arXiv:1703.00819) requires
c[n*k] >= k*c[n] - (k-1) whenever n*k is among these columns.
The code uses only integer arithmetic and exhausts all shapes up to reflection.
"""
from itertools import combinations

D = 10
VALUES = tuple(range(2, D))

def satisfies_lemma_9_1(counts):
    length = len(counts)
    for n in range(1, length + 1):
        for k in range(1, length // n + 1):
            if counts[n * k - 1] < k * counts[n - 1] - (k - 1):
                return False
    return True

survivors = []
for size in range(0, len(VALUES) // 2 + 1):
    for S in combinations(VALUES, size):
        Sset = set(S)
        T = tuple(v for v in VALUES if v not in Sset)
        left = S + (D,)
        right = T + (D,)
        if satisfies_lemma_9_1(left) and satisfies_lemma_9_1(right):
            survivors.append((S, T))

expected = [
    ((), VALUES),
    ((4, 7), (2, 3, 5, 6, 8, 9)),
    ((4, 8), (2, 3, 5, 6, 7, 9)),
]
assert survivors == expected, (survivors, expected)
print(f"tested_shapes={sum(1 for size in range(5) for _ in combinations(VALUES, size))}")
print("survivors:")
for S, T in survivors:
    print(f"S={list(S)}; T={list(T)}")
print("CHECK_OK")
