#!/usr/bin/env python3
"""Independent finite checks for binary length-four substring-permutation balls.

Usage: python verify_binary_four_permutation_ball.py
Requires only Python's standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def direct_ball_size(word):
    out = {word}
    for i in range(len(word) - 3):
        prefix, block, suffix = word[:i], word[i:i + 4], word[i + 4:]
        for perm in set(__import__('itertools').permutations(block)):
            out.add(prefix + perm + suffix)
    return len(out)


def local_value(bits):
    a, b, c, d = bits
    j = b + c + d + (-1 if a == 0 else 1)
    return comb(3, j) if 0 <= j <= 3 else 0


def center_formula(word):
    return sum(local_value(word[i:i + 4]) for i in range(len(word)-3)) + comb(3, sum(word[-3:]))


def transfer_histogram(n):
    # Count all initial triples directly; no complement reduction is needed.
    dp = {(state, 0): 1 for state in product((0, 1), repeat=3)}
    for _ in range(n - 3):
        new = Counter()
        for (state, size), multiplicity in dp.items():
            for v in (0, 1):
                nxt = state[1:] + (v,)
                new[(nxt, size + local_value(state + (v,)))] += multiplicity
        dp = new
    ans = Counter()
    for (state, size), multiplicity in dp.items():
        ans[size + comb(3, sum(state))] += multiplicity
    return ans


def all_maximizers(n):
    return {tuple(int('0011'[(i + d) % 4]) for i in range(n)) for d in range(4)} | {
        tuple(int('01'[(i + d) % 2]) for i in range(n)) for d in range(2)}


def moments(hist):
    N = sum(hist.values())
    mu = Fraction(sum(k * v for k, v in hist.items()), N)
    var = Fraction(sum(k*k * v for k, v in hist.items()), N) - mu*mu
    return mu, var


def main():
    count = 0
    for n in range(4, 13):
        hist_direct = Counter()
        maximizers = set()
        for word in product((0, 1), repeat=n):
            actual = direct_ball_size(word)
            assert actual == center_formula(word), (n, word, actual)
            hist_direct[actual] += 1
            if actual == 3*n-6:
                maximizers.add(word)
            count += 1
        assert hist_direct == transfer_histogram(n), n
        assert maximizers == all_maximizers(n), n
        mu, var = moments(hist_direct)
        assert mu == Fraction(15*n-25, 8), (n, mu)
        expected_var = Fraction(159, 64) if n == 4 else Fraction(119*n-319, 64)
        assert var == expected_var, (n, var, expected_var)
        assert hist_direct[3*n-6] == 6, n
        assert hist_direct[3*n-8] == 6*n-16, n
        assert hist_direct[3*n-10] == 3*(n-3)*(n-4), n
        assert hist_direct[3*n-11] == 2*(n-3), n
        assert hist_direct[3*n-7] == 0 and hist_direct[3*n-9] == 0, n
    for n in range(13, 36):
        hist = transfer_histogram(n)
        mu, var = moments(hist)
        assert sum(hist.values()) == 2**n, n
        assert mu == Fraction(15*n-25, 8), n
        assert var == Fraction(119*n-319, 64), n
        assert hist[3*n-6] == 6, n
        assert hist[3*n-8] == 6*n-16, n
        assert hist[3*n-10] == 3*(n-3)*(n-4), n
        assert hist[3*n-11] == 2*(n-3), n
        assert hist[3*n-7] == 0 and hist[3*n-9] == 0, n
    print('VERIFY_OK')
    print('exhaustive_direct_words=', count)
    print('exact_transfer_histograms= n=4..35')
    print('maximizing_center_count= 6 for n=4..35')
    print('near-max deficits 2,4,5: 6n-16, 3(n-3)(n-4), 2(n-3); deficits 1,3 absent')
    print('mean= (15n-25)/8')
    print('variance= 159/64 at n=4; (119n-319)/64 for n>=5')
    for n in (4, 5, 6, 7):
        print('histogram n=', n, 'values=', sorted(transfer_histogram(n).items()))


if __name__ == '__main__':
    main()
