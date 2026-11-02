#!/usr/bin/env python3
"""Reproducible exact checks for the q-ary two-deletion ball theorem.

Stdlib only. This is finite testing, not the all-length mathematical proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def deletion_ball_size(word):
    n = len(word)
    return len({tuple(word[k] for k in range(n) if k != i and k != j)
                for i in range(n) for j in range(i + 1, n)})


def parameters(word):
    changes = [int(word[i] != word[i + 1]) for i in range(len(word) - 1)]
    s = sum(changes)
    z = sum(changes[i] * changes[i + 1] for i in range(len(changes) - 1))
    e = changes[0] + changes[-1]
    t = sum(word[i] == word[i + 2] != word[i + 1]
            for i in range(len(word) - 2))
    return s, z, e, t, tuple(changes)


def size_formula(word):
    s, z, e, t, _ = parameters(word)
    return comb(s + 2, 2) - e - z - t


def expected_moments(q, n):
    m = n - 1
    p = Fraction(q - 1, q)
    a = Fraction(1, q - 1)
    mean = 1 + (m - 1) * p + comb(m, 2) * p * p
    variance = (m * (m - 1) ** 2 * p ** 3 * (1 - p)
                + (m - 1) * (Fraction(m - 2, 2) + a * a) * p ** 2 * (1 - p) ** 2
                + (m - 1) * a * (1 - a) * p * p)
    return mean, variance


def check_full(q, n, check_moments=True):
    counts = Counter()
    conditional = defaultdict(Counter)
    total = 0
    for word in product(range(q), repeat=n):
        b = deletion_ball_size(word)
        assert b == size_formula(word), (q, n, word, b, size_formula(word))
        s, z, e, t, changes = parameters(word)
        conditional[changes][t] += 1
        counts[b] += 1
        total += 1
    assert total == q ** n
    if check_moments:
        actual_mean = Fraction(sum(v * ct for v, ct in counts.items()), total)
        actual_var = Fraction(sum(v * v * ct for v, ct in counts.items()), total) - actual_mean ** 2
        ex_mean, ex_var = expected_moments(q, n)
        assert (actual_mean, actual_var) == (ex_mean, ex_var), (q, n, actual_mean, actual_var, ex_mean, ex_var)
    # The number of words with a specified transition vector is
    # q * (q-1)**S. Independence of ABA indicators makes exact
    # conditional probabilities binomial for every transition vector.
    for changes, ct in conditional.items():
        s = sum(changes)
        z = sum(changes[i] * changes[i+1] for i in range(len(changes)-1))
        denominator = q * (q - 1) ** s
        assert sum(ct.values()) == denominator
        for t in range(z + 1):
            expected = comb(z, t) * q * (q - 2) ** (z - t) * (q - 1) ** (s - z)
            assert ct[t] == expected, (q, n, changes, t, ct[t], expected)
    return len(conditional), total


def check_transition_only(q, m):
    # Enumerate each transition-vector with no word enumeration, and
    # evaluate total conditional variance and mean independently.
    p = Fraction(q - 1, q)
    a = Fraction(1, q - 1)
    mean = Fraction(0)
    moment2 = Fraction(0)
    for changes in product((0, 1), repeat=m):
        s = sum(changes)
        z = sum(changes[i] * changes[i + 1] for i in range(m - 1))
        e = changes[0] + changes[-1]
        probability = p ** s * (1 - p) ** (m - s)
        conditional_mean = Fraction(comb(s + 2, 2) - e - z) - a * z
        conditional_variance = a * (1 - a) * z
        mean += probability * conditional_mean
        moment2 += probability * (conditional_mean ** 2 + conditional_variance)
    em, ev = expected_moments(q, m + 1)
    assert (mean, moment2 - mean ** 2) == (em, ev)


def main():
    examined = 0
    vectors = 0
    for q, upper in ((2, 10), (3, 8), (4, 6)):
        for n in range(2, upper + 1):
            nv, cnt = check_full(q, n)
            examined += cnt
            vectors += nv
    for q in (2, 3, 4, 5, 7, 11):
        for m in range(1, 13):
            check_transition_only(q, m)
    print(f'VERIFY_OK exact_words={examined} transition_vector_cases={vectors} symbolic_parameter_checks={6*12}')


if __name__ == '__main__':
    main()
