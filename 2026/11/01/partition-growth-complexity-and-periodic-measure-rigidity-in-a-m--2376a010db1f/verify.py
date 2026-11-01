"""Exact finite checks for the monotone-gap binary subshift.

This program uses only the Python standard library. It checks finite words,
periodic binary rings, and truncated generating-function identities.
The infinite proofs are in RESULT.md, not in this finite computation.
"""
from itertools import product


def partitions_upto(bound):
    p = [1] + [0] * bound
    for part in range(1, bound + 1):
        for total in range(part, bound + 1):
            p[total] += p[total - part]
    return p


def allowed_word(word):
    ones = [i for i, bit in enumerate(word) if bit]
    gaps = [b - a for a, b in zip(ones, ones[1:])]
    return all(a <= b for a, b in zip(gaps, gaps[1:]))


def allowed_ring(word):
    n = len(word)
    ones = [i for i, bit in enumerate(word) if bit]
    if not ones:
        return True
    gaps = [ones[i + 1] - ones[i] for i in range(len(ones) - 1)]
    gaps.append(n + ones[0] - ones[-1])
    return all(a <= b for a, b in zip(gaps, gaps[1:] + gaps[:1]))


def sigma(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)


def verify():
    p = partitions_upto(800)
    pword = [1]
    for n in range(1, 15):
        exact = sum(allowed_word(w) for w in product((0, 1), repeat=n))
        formula = 1 + sum((n-s) * p[s] for s in range(n))
        assert exact == formula, (n, exact, formula)
        pword.append(exact)
    for n in range(1, 14):
        assert pword[n + 1] - pword[n] == sum(p[:n + 1]), n
    for n in range(1, 13):
        exact = sum(allowed_ring(w) for w in product((0, 1), repeat=n))
        assert exact == 1 + sigma(n), (n, exact, 1 + sigma(n))
    # Truncated coefficient identity: (1-z) C(z) = 1 + z Z(z),
    # with Z(z)=P(z)/(1-z). Both sides are verified coefficientwise.
    for n in range(1, 14):
        assert pword[n] - pword[n - 1] == sum(p[:n])
    from math import exp, pi, sqrt
    c = pi * sqrt(2.0 / 3.0)
    leading = sqrt(3.0) / (2 * pi * pi)
    for n in (200, 400, 800):
        words = 1 + sum((n - s) * p[s] for s in range(n))
        ratio = words / (leading * exp(c * sqrt(n)))
        assert abs(ratio - 1.0) < 0.02, (n, ratio)
        print('asymptotic sample n=', n, ' ratio=', f'{ratio:.9f}')
    print('PASS: length 1..14 exhaustive words; rings 1..12; all exact identities and asymptotic checks')


if __name__ == '__main__':
    verify()
