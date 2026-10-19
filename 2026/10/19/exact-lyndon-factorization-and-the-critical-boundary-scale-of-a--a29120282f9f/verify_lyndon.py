#!/usr/bin/env python3
"""Reproducible finite checks of a two-parameter Lyndon decomposition.

Runs locally with only Python's standard library; no network or dependencies.
"""
from itertools import product


def duval(word):
    factors = []
    size = len(word)
    i = 0
    while i < size:
        j, k = i + 1, i
        while j < size and word[k] <= word[j]:
            if word[k] < word[j]:
                k = i
            else:
                k += 1
            j += 1
        unit = j - k
        while i <= k:
            factors.append(word[i:i + unit])
            i += unit
    return factors


def subst(word, q, r):
    return ''.join('0' * q if ch == '0' else '1' + '0' * r + '1'
                   for ch in word)


def exact_n(j, q, r):
    if q == 2:
        return (2 ** j) + r * j * (2 ** (j - 1) if j else 0)
    return 2 ** j + r * ((q ** j - 2 ** j) // (q - 2))


def check():
    iterations = 0
    cases = 0
    maxlen = 200_000
    for q, r in product(range(2, 10), range(1, 9)):
        cases += 1
        w = '1'
        b = '0' * r + '1'
        expected = ['1']
        assert duval(w) == expected
        for j in range(8):
            neww = subst(w, q, r)
            if len(neww) > maxlen:
                break
            assert neww == w + '0' * (r * (q ** j)) + w
            assert len(w) == exact_n(j, q, r)
            assert len(neww) == exact_n(j + 1, q, r)
            expected.append(b)
            assert ''.join(expected) == neww
            actual = duval(neww)
            assert actual == expected, (q, r, j, actual, expected)
            assert all(actual[t] > actual[t + 1]
                       for t in range(len(actual) - 1))
            assert duval(b) == [b]
            assert sum(len(part) for part in actual[:-1]) == exact_n(j, q, r)
            iterations += 1
            w = neww
            b = subst(b, q, r)
    print(f'VERIFY_OK parameter_pairs={cases} finite_iterates={iterations}')


if __name__ == '__main__':
    check()
