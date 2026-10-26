"""Finite exact tests for late-observation invariance of record values."""
from itertools import product, permutations, combinations
from fractions import Fraction
from collections import Counter


def record_values(word):
    m = None
    out = []
    for x in word:
        if m is None or x > m:
            out.append(x)
            m = x
    return tuple(out)


def sample_records(word, indices):
    m = None
    total = 0
    for j in indices:
        x = word[j]
        if m is None or x > m:
            total += 1
            m = x
    return total


def swap_under_threshold(word, before, t):
    threshold = max(word[i] for i in before)
    res = list(word)
    if (res[t] > threshold) != (res[t+1] > threshold):
        res[t], res[t+1] = res[t+1], res[t]
    return tuple(res)


def test_words(word):
    n = len(word)
    values = record_values(word)
    checks = 0
    for k in range(1, n-1):
        for mask in range(1, 1 << k):
            T = tuple(i for i in range(k) if (mask >> i) & 1)
            if T[-1] != k-1:
                continue
            for t in range(k, n-1):
                swapped = swap_under_threshold(word, T, t)
                assert record_values(swapped) == values
                assert sample_records(word, T + (t+1,)) == sample_records(swapped, T + (t,))
                assert swap_under_threshold(swapped, T, t) == word
                assert sorted(swapped) == sorted(word)
                checks += 4
    return checks


def main():
    checks = 0
    tests = 0
    for n in range(2, 8):
        for word in product(range(3), repeat=n):
            checks += test_words(word)
            tests += 1
    for n in range(2, 9):
        for word in permutations(range(n)):
            checks += test_words(word)
            tests += 1
    # Exhaustive finite joint-distribution identity beyond the pointwise involution.
    for n in range(3, 8):
        words = list(permutations(range(n)))
        for k in range(n-2):
            for mask in range(1, 1 << (k+1)):
                if not (mask & (1 << k)):
                    continue
                T = tuple(i for i in range(k+1) if mask & (1 << i))
                targets = [Counter((record_values(w), sample_records(w, T + (t,))) for w in words)
                           for t in range(k+1, n)]
                assert all(c == targets[0] for c in targets)
                checks += len(targets) - 1
    # Two retained positions: exact covariance does not depend on the final one.
    for n in range(2, 9):
        words = list(permutations(range(n)))
        full = [len(record_values(w)) for w in words]
        ef = Fraction(sum(full), len(full))
        for k in range(1, n):
            for t in range(k+1, n+1):
                q = [sample_records(w, (k-1,t-1)) for w in words]
                cov = Fraction(sum(a*b for a,b in zip(full,q)),len(words)) - ef*Fraction(sum(q),len(words))
                assert cov == Fraction(1, 2*k*(k+1)), (n,k,t,cov)
                checks += 1
    print('VERIFY_OK', tests, 'full words;', checks, 'exact identity checks; ties and distinct ranks')

if __name__ == '__main__':
    main()
