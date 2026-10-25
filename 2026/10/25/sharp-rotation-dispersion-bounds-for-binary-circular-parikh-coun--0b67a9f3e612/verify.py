"""Exact exhaustive regression for circular binary scattered-01 dispersion.

Usage: python verify.py [maximum_length]; default 14.
Only the Python standard library is required.
"""
import math
import sys


def rotation_profile(word):
    n = len(word)
    f0 = sum(word[i] == 0 and word[j] == 1
             for i in range(n) for j in range(i + 1, n))
    profile = []
    f = f0
    a = word.count(0)
    b = n - a
    for c in word:
        profile.append(f)
        f += a if c == 1 else -b
    assert f == f0
    # Independently count subsequences in every rotation.
    for k in range(n):
        r = word[k:] + word[:k]
        seen_zeros = 0
        direct = 0
        for letter in r:
            if letter == 0:
                seen_zeros += 1
            else:
                direct += seen_zeros
        assert direct == profile[k]
    return profile


def cyclic_balanced(word):
    n = len(word)
    doubled = word + word
    prefix = [0]
    for x in doubled:
        prefix.append(prefix[-1] + x)
    for length in range(1, n + 1):
        sums = [prefix[i + length] - prefix[i] for i in range(n)]
        if max(sums) - min(sums) > 1:
            return False
    return True


def circular_block(word):
    n = len(word)
    return any(sum(word[(i + j) % n] for j in range(word.count(1))) == word.count(1)
               for i in range(n))


def main(limit):
    count = 0
    for n in range(2, limit + 1):
        for bits in range(1, (1 << n) - 1):
            w = tuple((bits >> j) & 1 for j in range(n))
            a = w.count(0)
            b = n - a
            d = math.gcd(a, b)
            N = n // d
            f = rotation_profile(w)
            mean_twice = a * b
            assert sum(f) * 2 == n * a * b
            num = sum((2 * x - mean_twice)**2 for x in f)
            # num = 4*n*Var; formulas both rational with denominator 12.
            assert 3 * num >= n * d * d * (N * N - 1), (n, w, 'min')
            assert 3 * num <= n * a * b * (a * b + 2), (n, w, 'max')
            min_equal = 3 * num == n * d * d * (N * N - 1)
            max_equal = 3 * num == n * a * b * (a * b + 2)
            assert min_equal == cyclic_balanced(w), (n, w, 'balance')
            assert max_equal == circular_block(w), (n, w, 'block')
            # Independently check resistance-distance identity.
            ones = [i for i, x in enumerate(w) if x]
            pair_penalty = sum((j-i) * (n-(j-i))
                               for ix, i in enumerate(ones)
                               for j in ones[ix+1:])
            assert 3 * num == n * (b*b*(n*n-1) - 12 * pair_penalty), (n, w, 'identity')
            count += 1
    print(f'VERIFY_OK exhaustive_binary_words={count} lengths=2..{limit}')


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 14)
