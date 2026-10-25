#!/usr/bin/env python3
"""Independent finite checks for scattered palindromes in alternating binary words."""
from collections import Counter, defaultdict


def expected_histograms(limit):
    # Formal expansion of the proposed rational generating function
    # Q(z,t) / (1-z), using coefficient convolution without sympy.
    inverse = defaultdict(int)
    inverse[(0, 0)] = 1
    for n in range(1, limit + 1):
        for k in range(1, limit + 1):
            inverse[(n, k)] = (
                (inverse[(n-2, k-2)] if n >= 2 and k >= 2 else 0)
                + (inverse[(n-4, k-2)] if n >= 4 and k >= 2 else 0)
            )
    short = {(1, 1): 1, (2, 1): 1}
    numerator = ((3,2), (4,2), (3,3), (4,3), (5,3), (6,3))
    for (n, k), coeff in list(inverse.items()):
        if coeff == 0:
            continue
        for shift_n, shift_k in numerator:
            if n + shift_n <= limit and k + shift_k <= limit:
                key = (n+shift_n, k+shift_k)
                short[key] = short.get(key, 0) + coeff
    current = Counter()
    output = []
    for n in range(limit + 1):
        for (cost, length), coeff in short.items():
            if cost == n:
                current[length] += coeff
        output.append(dict(current))
    return output


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def independent_subsequences(limit):
    seen = {''}
    output = []
    for n in range(limit + 1):
        if n:
            char = '0' if n % 2 else '1'
            seen |= {sub + char for sub in seen}
        palindromes = (word for word in seen if word and word == word[::-1])
        histogram = dict(Counter(map(len, palindromes)))
        output.append(histogram)
    return output


def main():
    limit = 22
    exp = expected_histograms(limit)
    actual = independent_subsequences(limit)
    assert len(exp) == len(actual) == limit + 1
    for n in range(limit + 1):
        assert actual[n] == exp[n], (n, actual[n], exp[n])
        target = 0 if n == 0 else (
            2*fibonacci(n//2 + 3)-4 if n%2 == 0
            else fibonacci((n-1)//2 + 5)-4
        )
        assert sum(actual[n].values()) == target, (n, target, actual[n])
    assert [sum(actual[n].values()) for n in range(1, 11)] == [1,2,4,6,9,12,17,22,30,38]
    print(f'VERIFY_OK alternating_prefix_lengths=0..{limit} exact_length_spectra=TRUE Fibonacci_formula=TRUE original_table_n=1..10=TRUE')


if __name__ == '__main__':
    main()
