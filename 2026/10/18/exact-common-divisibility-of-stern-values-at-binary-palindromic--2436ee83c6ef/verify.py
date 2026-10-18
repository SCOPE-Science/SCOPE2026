"""Reproducibility checks for binary-palindromic Stern common divisors."""
from math import gcd
from functools import reduce


def stern(n: int) -> int:
    if n == 0:
        return 0
    a, b = 1, 1
    for digit in bin(n)[3:]:
        if digit == '0':
            b = a + b
        else:
            a = a + b
    return a


def binary_palindromes(length: int):
    half = (length + 1) // 2
    for first in range(1 << (half - 1), 1 << half):
        stem = format(first, f'0{half}b')
        word = stem + (stem[::-1] if length % 2 == 0 else stem[-2::-1])
        assert len(word) == length and word == word[::-1] and word[0] == '1'
        yield int(word, 2)


def value_by_word(word: str) -> int:
    assert word[0] == '1'
    a, b = 1, 1
    for digit in word[1:]:
        if digit == '0':
            b = a + b
        else:
            a = a + b
    return a


def template_coefficients(prefix: str):
    # Values a0+a1*t and b0+b1*t after reading prefix and t zero bits.
    a0, b0 = 1, 1
    for digit in prefix[1:]:
        if digit == '0':
            b0 += a0
        else:
            a0 += b0
    a = (a0, 0)
    b = (b0, a0)
    for digit in prefix[::-1]:
        if digit == '0':
            b = (b[0]+a[0],b[1]+a[1])
        else:
            a = (a[0]+b[0],a[1]+b[1])
    return a # constant and slope


def main():
    expected = [1, 2, 3, 4, 1, 6, 1]
    observed = []
    count = 0
    for length in range(1, 23):
        vals = []
        for n in binary_palindromes(length):
            v = stern(n)
            vals.append(v)
            assert value_by_word(bin(n)[2:]) == v
            count += 1
        g = reduce(gcd, vals)
        target = expected[length-1] if length <= 7 else (2 if length % 2 == 0 else 1)
        assert g == target, (length, g, target)
        observed.append(g)
        if length % 2 == 0:
            assert all(n % 3 == 0 for n in binary_palindromes(length))
            assert all(v % 2 == 0 for v in vals)
    coeff_expected = {'1000': (8, 1), '1100': (20, 4),
                      '1010': (30, 9), '1001': (24, 16)}
    for prefix, expected_coeff in coeff_expected.items():
        assert template_coefficients(prefix) == expected_coeff
        c, slope = expected_coeff
        for t in (0, 1, 2, 9, 37, 113):
            word = prefix + '0'*t + prefix[::-1]
            assert stern(int(word,2)) == c+slope*t
    print('STERN_PALINDROME_REGRESSION_OK lengths=1..22',
          'values_checked=', count, 'gcds=', observed)

if __name__ == '__main__':
    main()
