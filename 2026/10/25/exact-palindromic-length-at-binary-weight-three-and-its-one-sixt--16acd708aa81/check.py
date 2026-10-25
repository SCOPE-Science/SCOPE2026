#!/usr/bin/env python3
"""Independent finite checks for the three-marker palindromic-length theorem."""
from itertools import product, combinations
from collections import defaultdict


def length_dp(word):
    n = len(word)
    pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            pal[i][j] = word[i] == word[j] and (j - i < 2 or pal[i + 1][j - 1])
    dp = [0] + [n + 1] * n
    for end in range(1, n + 1):
        dp[end] = min(dp[start] + 1 for start in range(end) if pal[start][end - 1])
    return dp[n]


def theoretical(a, b, c, d):
    if a == d and b == c:
        return 1
    if b == c or b == a + d or c == a + d:
        return 2
    if b != c and min(a, d) > max(b, c):
        return 4
    return 3


def main():
    cases = 0
    for a, b, c, d in product(range(11), repeat=4):
        w = '0' * a + '1' + '0' * b + '1' + '0' * c + '1' + '0' * d
        actual = length_dp(w)
        predicted = theoretical(a, b, c, d)
        assert actual == predicted, (a, b, c, d, actual, predicted)
        cases += 1
    print('four-gap triples checked:', cases)
    # A length-limited enumeration, with no reliance on the gap-based generation.
    max_n = 28
    direct = [0] * (max_n + 1)
    for n in range(3, max_n + 1):
        for i, j, k in combinations(range(n), 3):
            w = ['0'] * n
            w[i] = w[j] = w[k] = '1'
            if length_dp(''.join(w)) == 4:
                direct[n] += 1
    # Coefficients of 2*z^8 / ((1-z)^2*(1-z^3)*(1-z^4)).
    generating = [0] * (max_n + 1)
    for r in range(max_n + 1):
        for s in range(max_n + 1):
            for t in range(max_n + 1):
                n = 8 + r + 3 * s + 4 * t
                if n <= max_n:
                    generating[n] += 2 * (r + 1)
    assert direct == generating, (direct, generating)
    assert direct[8] == 2 and sum(direct[:8]) == 0
    print('lengths checked:', '3 through', max_n)
    print('extremal counts n=8..20:', direct[8:21])
    print('first extremal examples:', [
        ''.join('1' if t in triple else '0' for t in range(8))
        for triple in combinations(range(8), 3)
        if length_dp(''.join('1' if t in triple else '0' for t in range(8))) == 4
    ])
    print('PASS')


if __name__ == '__main__':
    main()
