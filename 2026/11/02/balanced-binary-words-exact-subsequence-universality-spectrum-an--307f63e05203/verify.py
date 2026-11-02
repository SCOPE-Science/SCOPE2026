#!/usr/bin/env python3
"""Independent finite checks for the balanced-word universality series."""
from collections import Counter
from itertools import combinations, product
from math import comb


def greedy_index(w):
    seen = set()
    count = 0
    for symbol in w:
        seen.add(symbol)
        if len(seen) == 2:
            count += 1
            seen.clear()
    return count


def subsequence(word, pattern):
    it = iter(word)
    return all(any(letter == c for letter in it) for c in pattern)


def direct_index(w):
    k = 0
    while all(subsequence(w, pat) for pat in product('01', repeat=k + 1)):
        k += 1
    return k


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def poly_add(a, b, scale=1):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += scale * v
    return c


def predicted_coeffs(max_n):
    # B^2 (1-(1+4u)t+4u^2t^2) = 1-t, B(0,u)=1.
    # Coefficients solved inductively; no use of greedy arches in this check.
    b = [[1]]
    for n in range(1, max_n + 1):
        rhs = [-1] if n == 1 else [0]
        # subtract all coefficients except the two appearances of b_n in B^2
        s = [0]
        for i in range(1, n):
            s = poly_add(s, poly_mul(b[i], b[n - i]))
        prev_sq = [0]
        for i in range(n):
            prev_sq = poly_add(prev_sq, poly_mul(b[i], b[n - 1 - i]))
        s = poly_add(s, poly_mul([-1, -4], prev_sq))
        if n >= 2:
            prior_sq = [0]
            for i in range(n - 1):
                prior_sq = poly_add(prior_sq, poly_mul(b[i], b[n - 2 - i]))
            s = poly_add(s, poly_mul([0, 0, 4], prior_sq))
        # 2*b_n = rhs - s, must be integer coefficientwise
        target = poly_add(rhs, s, -1)
        assert all(v % 2 == 0 for v in target)
        b.append([v // 2 for v in target])
    return b


def main():
    coeffs = predicted_coeffs(8)
    tests = 0
    for n in range(9):
        counts = Counter()
        for inds in combinations(range(2 * n), n):
            on = set(inds)
            w = ''.join('1' if i in on else '0' for i in range(2 * n))
            idx = greedy_index(w)
            counts[idx] += 1
            tests += 1
            if n <= 4:
                assert direct_index(w) == idx, (w, idx)
        expected = [counts.get(k, 0) for k in range(len(coeffs[n]))]
        assert coeffs[n] == expected, (n, coeffs[n], expected)
        assert sum(expected) == comb(2 * n, n)
        print(f'n={n}: ' + ','.join(map(str, expected)))
    # Independently check greedy-index identity for all binary words to length 10.
    for n in range(11):
        for w_tuple in product('01', repeat=n):
            w = ''.join(w_tuple)
            assert greedy_index(w) == direct_index(w), w
    assert coeffs[8][8] == 2 ** 8
    print(f'VERIFY_OK total_balanced_words={tests}; all_words_upto_length=10')


if __name__ == '__main__':
    main()
