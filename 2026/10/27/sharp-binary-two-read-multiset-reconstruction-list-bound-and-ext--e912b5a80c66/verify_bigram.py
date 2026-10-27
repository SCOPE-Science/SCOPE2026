#!/usr/bin/env python3
"""Finite cross-checks for binary adjacent-pair multiset reconstruction."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb


def predicted(n, signature):
    a, b, c, d = signature
    assert a + b + c + d == n - 1
    if b == c == 0:
        return 1 if (a == n - 1 and d == 0) or (d == n - 1 and a == 0) else 0
    if b == c and b > 0:
        t = b
        return (n - 1) * comb(a + t - 1, t - 1) * comb(d + t - 1, t - 1) // t
    if abs(b - c) == 1:
        t = max(b, c)
        return comb(a + t - 1, t - 1) * comb(d + t - 1, t - 1)
    return 0


def optimum(n):
    assert n >= 3
    m = n - 1
    u, v = (m - 2) // 2, (m - 1) // 2
    vals = [m * comb(u, k) * comb(v, k) // (k + 1) for k in range(u + 1)]
    top = max(vals)
    ks = {k for k, value in enumerate(vals) if value == top}
    maximal = set()
    for k in ks:
        t = k + 1
        loops = m - 2 * t
        a_choices = range(loops + 1) if k == 0 else {loops // 2, (loops + 1) // 2}
        for a in a_choices:
            maximal.add((a, t, t, loops - a))
    return top, maximal


def test_exhaustive():
    examined = 0
    signatures = 0
    for n in range(3, 19):
        counts = Counter()
        for word in product((0, 1), repeat=n):
            signature = [0, 0, 0, 0]
            for a, b in zip(word, word[1:]):
                signature[2 * a + b] += 1
            counts[tuple(signature)] += 1
            examined += 1
        for signature, multiplicity in counts.items():
            expected = predicted(n, signature)
            assert multiplicity == expected, (n, signature, multiplicity, expected)
        signatures += len(counts)
        top, maximal = optimum(n)
        assert top == max(counts.values())
        assert maximal == {s for s, multiplicity in counts.items() if multiplicity == top}
        assert sum(counts.values()) == 2 ** n
    print(f'EXHAUSTIVE_OK words={examined} signatures={signatures} n=3..18')


def test_large_finite_parameters():
    cases = 0
    for n in range(19, 191):
        m = n - 1
        M, maximizing = optimum(n)
        seen = set()
        for b in range(m + 1):
            for c in (b - 1, b, b + 1):
                if c < 0 or b + c > m:
                    continue
                for a in range(m - b - c + 1):
                    d = m - b - c - a
                    signature = a, b, c, d
                    count = predicted(n, signature)
                    if not count:
                        continue
                    assert count <= M, (n, signature, count, M)
                    if count == M:
                        seen.add(signature)
                    cases += 1
        assert seen == maximizing, (n, seen, maximizing)
    print(f'PARAMETER_OK realized_signature_tests={cases} n=19..190')


if __name__ == '__main__':
    test_exhaustive()
    test_large_finite_parameters()
    for n in range(3, 21):
        M, maximizers = optimum(n)
        print(f'n={n} max_list={M} maximizer_spectra={len(maximizers)} maximizer_words={M*len(maximizers)}')
    print('VERIFY_OK')
