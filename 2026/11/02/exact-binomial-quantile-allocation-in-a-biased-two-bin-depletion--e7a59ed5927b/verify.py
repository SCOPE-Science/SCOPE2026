"""Exact checks for a two-colour depletion process and its binomial loss identity.

Requires only the Python standard library. All finite tests use rational arithmetic.
They are supporting diagnostics; the general theorem follows from the proof.
"""
from fractions import Fraction
from math import comb


def binomial_probabilities(n, p):
    q = 1 - p
    return [Fraction(comb(n, k)) * p**k * q**(n-k) for k in range(n+1)]


def remainder_by_recurrence(n, p):
    q = 1 - p
    f = [[Fraction(0) for _ in range(n+1)] for _ in range(n+1)]
    for a in range(n+1):
        f[a][0] = Fraction(a)
        f[0][a] = Fraction(a)
    for a in range(1, n+1):
        for b in range(1, n+1):
            f[a][b] = p*f[a-1][b] + q*f[a][b-1]
    return f


def check():
    count = 0
    for p in [Fraction(1, 2), Fraction(1, 3), Fraction(2, 3),
              Fraction(2, 5), Fraction(3, 7), Fraction(5, 6),
              Fraction(1, 10), Fraction(9, 10)]:
        q = 1-p
        for n in range(2, 28):
            probability = binomial_probabilities(n, p)
            assert sum(probability) == 1
            count += 1
            f = remainder_by_recurrence(n, p)
            values = []
            for a in range(n+1):
                left = sum((a-k)*probability[k] for k in range(a))
                right = sum((k-a)*probability[k] for k in range(a+1, n+1))
                value = left/q + right/p
                assert value == f[a][n-a], (n, p, a, value, f[a][n-a])
                count += 1
                values.append(value)
            cumulative = Fraction(0)
            for a in range(n):
                cumulative += probability[a]
                slope = (cumulative-q)/(p*q)
                assert values[a+1]-values[a] == slope, (n, p, a)
                count += 1
            quantile = next(a for a in range(n+1) if sum(probability[:a+1]) >= q)
            minimum = min(values)
            minimizers = [a for a in range(n+1) if values[a] == minimum]
            assert quantile in minimizers
            count += 1
            assert minimizers in ([quantile], [quantile, quantile+1]), (n,p,minimizers)
            count += 1
            assert 1 <= quantile <= n-1
            count += 1
    p = Fraction(5, 6)
    f = remainder_by_recurrence(6, p)
    assert f[4][2] == Fraction(139, 81)
    assert f[5][1] == Fraction(3125, 1296)
    count += 2
    print(f'PASS: {count} exact-rational assertions')


if __name__ == '__main__':
    check()
