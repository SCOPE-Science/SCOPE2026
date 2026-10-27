#!/usr/bin/env python3
"""Finite independent checks for the three-marker palindromic defect identity.

The all-parameter proof is in RESULT.md; this program checks finite ranges only.
Run: python3 verify.py
"""
from itertools import product


def pal_factors(word):
    """Generate palindromes by substring comparison (not from the formula)."""
    return {word[i:j] for i in range(len(word))
            for j in range(i + 1, len(word) + 1)
            if word[i:j] == word[i:j][::-1]}


def direct_defect(word):
    return len(word) - len(pal_factors(word))


def prediction(a, b, c, d):
    return 0 if b == c else max(0, min(a, d) - max(b, c))


def level_identity(bits):
    a, b, c, d = bits
    left = (a + b + c + d - int(any(bits))
            - int((a and b) or (b and c) or (c and d))
            - (a and c) - (b and d))
    right = int(a and d and not b and not c)
    return left, right


def run():
    for bits in product((0, 1), repeat=4):
        assert level_identity(bits)[0] == level_identity(bits)[1], bits
    cases = 0
    for a, b, c, d in product(range(9), repeat=4):
        word = '0' * a + '1' + '0' * b + '1' + '0' * c + '1' + '0' * d
        got = direct_defect(word)
        target = prediction(a, b, c, d)
        assert got == target, ((a, b, c, d), got, target)
        cases += 1
    two_cases = 0
    for k in range(3):
        if k == 0:
            for a in range(30):
                assert direct_defect('0' * a) == 0
                two_cases += 1
        elif k == 1:
            for a, b in product(range(16), repeat=2):
                assert direct_defect('0' * a + '1' + '0' * b) == 0
                two_cases += 1
        else:
            for a, b, c in product(range(9), repeat=3):
                assert direct_defect('0' * a + '1' + '0' * b + '1' + '0' * c) == 0
                two_cases += 1
    for n in range(3, 23):
        m = n - 3
        cases_at_n = []
        for a in range(m + 1):
            for b in range(m - a + 1):
                for c in range(m - a - b + 1):
                    d = m - a - b - c
                    cases_at_n.append(((a, b, c, d), prediction(a, b, c, d)))
        best = max(z for _, z in cases_at_n)
        target = max(0, (n - 6) // 2)
        assert best == target, (n, best, target)
        if n >= 8:
            expected = {(a, b, c, m - 1 - a)
                        for a in (m // 2, (m - 1) // 2)
                        for b, c in ((0, 1), (1, 0))
                        if m - 1 - a >= 0}
            actual = {t for t, z in cases_at_n if z == best}
            assert actual == expected, (n, actual, expected)
    print('PASS: 16 Boolean levels; 6561 three-marker words;'
          f' {two_cases} zero-to-two-marker words; exact maxima at lengths 3..22.')


if __name__ == '__main__':
    run()
