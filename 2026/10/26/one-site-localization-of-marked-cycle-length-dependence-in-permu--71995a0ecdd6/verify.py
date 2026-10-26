"""Exact finite-check companion for the marked-cycle descent theorem.

Usage: python3 verify.py  (Python standard library only)
The finite enumeration checks examples, not the universal proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def q(n, k):
    assert n >= 3 and 1 <= k <= n
    if k == 1:
        return Fraction(0)
    if k == 2:
        return Fraction(n + 1, 2 * (n - 1))
    if k == n:
        return Fraction(1, 2)
    return Fraction(n, 2 * (n - 1))


def marked_cycle_length(p):
    i = 0
    k = 0
    while True:
        k += 1
        i = p[i]
        if i == 0:
            return k


def main():
    checks = 0
    for n in range(3, 10):
        # Probability counts by length of cycle containing value 1.
        cnt = [0] * (n + 1)
        desc = [[0] * (n - 1) for _ in range(n + 1)]
        for p in permutations(range(n)):
            k = marked_cycle_length(p)
            cnt[k] += 1
            for i in range(n - 1):
                desc[k][i] += (p[i] > p[i + 1])
        for k in range(1, n + 1):
            assert cnt[k] == factorial(n - 1), (n, k, cnt[k])
            checks += 1
            assert Fraction(desc[k][0], cnt[k]) == q(n, k), (n, k, 1)
            checks += 1
            for i in range(1, n - 1):
                assert Fraction(desc[k][i], cnt[k]) == Fraction(1, 2), (n, k, i + 1)
                checks += 1
            avg = Fraction(sum(desc[k]), cnt[k])
            assert avg == Fraction(n - 2, 2) + q(n, k), (n, k, avg)
            checks += 1
        s = sum(Fraction(k * sum(desc[k]), cnt[k]) for k in range(1, n + 1)) / n
        cov = s - Fraction(n + 1, 2) * Fraction(n - 1, 2)
        assert cov == Fraction(n * n - 3 * n + 4, 4 * n * (n - 1)), (n, cov)
        checks += 1
        assert sum(q(n, k) for k in range(1, n + 1)) == Fraction(n, 2)
        checks += 1
        print('n=', n, 'permutations=', factorial(n), 'checks=', checks)
    print('VERIFICATION_OK', checks)


if __name__ == '__main__':
    main()
