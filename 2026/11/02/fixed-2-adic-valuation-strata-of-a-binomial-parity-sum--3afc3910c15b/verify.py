#!/usr/bin/env python3
"""Independent finite tests of a binomial-parity valuation theorem.

Requires Python 3.9+ standard library only. Exhaustive numerical tests corroborate,
but do not replace, the symbolic proof of the infinite theorem.
"""
from collections import Counter


def recurrence(count):
    s = [1, 1, 1, 1]
    for _ in range(4, count):
        s.append(s[-1] + s[-2] - s[-3] + s[-4])
    return s


def val2(x):
    assert x > 0
    return (x & -x).bit_length() - 1


def valuation_of_word(n, s):
    value = 0
    run = 0
    while n:
        if n & 1:
            run += 1
        else:
            if run:
                value += val2(s[run])
                run = 0
        n >>= 1
    if run:
        value += val2(s[run])
    return value


def run_product(n, s):
    result, run = 1, 0
    while n:
        if n & 1:
            run += 1
        else:
            if run:
                result *= s[run]
                run = 0
        n >>= 1
    if run:
        result *= s[run]
    return result


def binomial_parity_sum(n):
    total = 0
    for k in range(n + 1):
        numerator = n + 5 * k
        denominator = 2 * n + 2 * k
        if denominator > numerator:
            continue
        if (denominator & ~numerator) or (k & ~n):
            continue
        total += 1
    return total


def polynomial_multiply(a, b):
    p = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            p[i + j] += x * y
    return p


def rational_coefficients(numerator, denominator, count):
    assert denominator[0] == 1
    coeff = [0] * count
    for n in range(count):
        coefficient = numerator[n] if n < len(numerator) else 0
        coefficient -= sum(denominator[j] * coeff[n-j]
                           for j in range(1, min(n, len(denominator)-1) + 1))
        coeff[n] = coefficient
    return coeff


def main():
    length = 18
    s = recurrence(256)
    assert s[:11] == [1, 1, 1, 1, 2, 3, 5, 7, 11, 16, 25]
    assert [x % 2 for x in s[:5]] == [1, 1, 1, 1, 0]
    assert [x % 4 for x in s[:10]] == [1, 1, 1, 1, 2, 3, 1, 3, 3, 0]
    for modulus, period in ((2, 5), (4, 10)):
        assert tuple(x % modulus for x in s[:4]) == tuple(x % modulus for x in s[period:period+4])
        assert all(s[j] % modulus == s[j + period] % modulus
                   for j in range(256 - period))
    assert all(s[j] > 0 for j in range(256))
    for n in range(2000):
        assert binomial_parity_sum(n) == run_product(n, s), n

    q = [1, -1, -1, -1, -1, -1]
    g0 = rational_coefficients([1, 1, 1, 1], q, length)
    q_square = polynomial_multiply(q, q)
    factor = [1, 0, 0, 0, 0, 1]
    g1_denom = polynomial_multiply(q_square, factor)
    g1_num = [0] * 10
    g1_num[4] = 1
    g1_num[9] = -1
    g1 = rational_coefficients(g1_num, g1_denom, length)

    assert g0[:12] == [1, 2, 4, 8, 15, 30, 59, 116, 228, 448, 881, 1732]
    assert g1[:12] == [0, 0, 0, 0, 1, 2, 5, 12, 28, 62, 138, 302]
    for r in range(length):
        histogram = Counter(valuation_of_word(n, s) for n in range(1 << r))
        assert histogram[0] == g0[r], (r, histogram[0], g0[r])
        assert histogram[1] == g1[r], (r, histogram[1], g1[r])
        assert sum(histogram.values()) == 1 << r
    print('VERIFY_OK binomial=2000 binary_words=262143 depths=0..17')


if __name__ == '__main__':
    main()
