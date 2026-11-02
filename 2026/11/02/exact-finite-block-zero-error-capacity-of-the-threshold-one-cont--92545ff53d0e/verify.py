#!/usr/bin/env python3
"""Finite checks for the threshold-one contextual deletion theorem.

Python 3 standard library only. Run: python3 verify.py
"""
from itertools import product
from math import comb, isclose, log2, sqrt


def contextual_one(word):
    """Delete first symbol of every non-initial maximal equal-symbol run."""
    return tuple(c for i, c in enumerate(word)
                 if i == 0 or word[i-1] == c)


def run_count(word):
    return 1 + sum(word[i] != word[i-1] for i in range(1, len(word)))


def shortest_source(word):
    assert word
    output = [word[0]]
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            output.append(word[i])
        output.append(word[i])
    return tuple(output)


def pad_shortest(word, n, q):
    source = list(shortest_source(word))
    assert len(source) <= n
    while len(source) < n:
        source.append((source[-1] + 1) % q)
    return tuple(source)


def count_formula(q, n):
    return sum(q * (q - 1)**(r - 1) * comb(m - 1, r - 1)
               for m in range(1, n + 1) for r in range(1, m + 1)
               if m + r - 1 <= n)


def count_recurrence(q, n):
    a, b = 0, 1
    total = 0
    for _ in range(1, n + 1):
        total += q * b
        a, b = b, b + (q - 1) * a
    return total


NUM_EXHAUSTIVE = 0
NUM_CANONICAL = 0
for q, nmax in ((2, 12), (3, 8), (4, 7)):
    for n in range(1, nmax + 1):
        image = {}
        for src in product(range(q), repeat=n):
            y = contextual_one(src)
            image[y] = image.get(y, 0) + 1
        want = count_formula(q, n)
        assert len(image) == want == count_recurrence(q, n), (q, n, len(image), want)
        for y in image:
            short = shortest_source(y)
            assert len(short) == len(y) + run_count(y) - 1
            assert contextual_one(short) == y
            assert contextual_one(pad_shortest(y, n, q)) == y
            # All preimages are at least as long as the canonical shortest one.
            assert len(short) <= n
            NUM_CANONICAL += 1
        # Verify the unique shortest preimage when the source length is minimal.
        for y in image:
            minlen = len(y) + run_count(y) - 1
            if minlen != n:  # can be checked at a different exhaustive n
                continue
            assert image[y] == 1, (q, n, y, image[y])
        NUM_EXHAUSTIVE += q**n
    print(f'q={q}: direct enumeration through n={nmax}; image cardinality and canonical decoding OK')

for q in range(2, 20):
    for n in range(1, 151):
        assert count_formula(q, n) == count_recurrence(q, n)
    lam = (1 + sqrt(4*q-3))/2
    assert isclose(lam*lam - lam - (q-1), 0, abs_tol=1e-12)

# The binary closed form (F_0=0, F_1=1).
f0, f1 = 0, 1
fibonacci = [0, 1]
for _ in range(400):
    f0, f1 = f1, f0 + f1
    fibonacci.append(f1)
for n in range(1, 150):
    assert count_recurrence(2, n) == 2*(fibonacci[n+2] - 1)
print('q=2 binary Fibonacci formula through n=149: OK')
print('q=2..19 symbolic weighted-run recurrence vs exact binomial sum through n=150: OK')
print(f'Directly enumerated {NUM_EXHAUSTIVE} source strings and {NUM_CANONICAL} canonical representatives: OK')
print('VERIFY_OK')
