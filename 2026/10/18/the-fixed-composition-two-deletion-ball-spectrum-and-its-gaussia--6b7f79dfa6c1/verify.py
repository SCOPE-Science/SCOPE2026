#!/usr/bin/env python3
"""Independent finite checks of a fixed-composition two-deletion ball law.

Run: python3 verify.py
The checks supplement rather than replace the unrestricted combinatorial proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def deletion_ball_size(word):
    n = len(word)
    return len({word[:i] + word[i+1:j] + word[j+1:]
                for i in range(n) for j in range(i + 1, n)})


def transition_formula(word):
    n = len(word)
    z = [int(word[i] != word[i + 1]) for i in range(n - 1)]
    t = sum(z)
    return (t + 1) * (t + 2) // 2 - z[0] - z[-1] - 2 * sum(a * b for a, b in zip(z, z[1:]))


def formal_run_product_hist(n):
    """Expand the theorem's alternating-run Laurent products to total length n."""
    histogram = defaultdict(Counter)
    if n < 2:
        return histogram
    histogram[0][1] += 1
    histogram[n][1] += 1
    for r in range(2, n + 1):
        for first in (0, 1):
            states = {(0, 0, 0): 1}  # length, ones, Laurent exponent
            for i in range(r):
                bit = first ^ (i % 2)
                nxt = defaultdict(int)
                remaining_runs = r - 1 - i
                for (length, ones, exponent), coeff in states.items():
                    for runlength in range(1, n - length - remaining_runs + 1):
                        penalty = 0
                        if runlength == 1:
                            penalty = -1 if i in (0, r - 1) else -2
                        key = (length + runlength, ones + bit * runlength,
                               exponent + penalty)
                        nxt[key] += coeff
                states = nxt
            for (length, ones, exponent), coeff in states.items():
                if length == n:
                    size = r * (r + 1) // 2 + exponent
                    assert size >= 1
                    histogram[ones][size] += coeff
    return histogram


def conditional_mean(n, k):
    a = n - k
    return 1 + Fraction(3 * (n - 2) * k * a +
                        2 * k * (k - 1) * a * (a - 1), n * (n - 1))


def main():
    checked = 0
    for n in range(2, 14):
        direct = defaultdict(Counter)
        for tup in product('01', repeat=n):
            word = ''.join(tup)
            a = deletion_ball_size(word)
            b = transition_formula(word)
            assert a == b, (word, a, b)
            direct[word.count('1')][a] += 1
            checked += 1
        via_runs = formal_run_product_hist(n)
        for k in range(n + 1):
            assert direct[k] == via_runs[k], (n, k, direct[k], via_runs[k])
            assert sum(via_runs[k].values()) == comb(n, k), (n, k)
            mean = Fraction(sum(s * z for s, z in via_runs[k].items()), comb(n, k))
            assert mean == conditional_mean(n, k), (n, k, mean, conditional_mean(n, k))
    # Beyond direct enumeration: check coefficient mass and exact moments.
    for n in range(14, 19):
        via_runs = formal_run_product_hist(n)
        for k in range(n + 1):
            assert sum(via_runs[k].values()) == comb(n, k), (n, k)
            mean = Fraction(sum(s * z for s, z in via_runs[k].items()), comb(n, k))
            assert mean == conditional_mean(n, k), (n, k)
    print(f'PASS_FIXED_COMPOSITION_TWO_DELETION size_formula_words={checked} direct_lengths=2..13 formal_product_lengths=2..18 all_weights=verified')


if __name__ == '__main__':
    main()
