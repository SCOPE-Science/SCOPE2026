#!/usr/bin/env python3
"""Independent finite checks for the exact coding and square-block identities.

All computations are integral or rational; this script does not certify
infinite-size renewal asymptotics.
"""
from itertools import product
from fractions import Fraction
from math import isqrt

P, Q = 2, 4
ALPHABET = ((0, 0),) + tuple((a, b) for a in range(1, P + 1) for b in range(Q))


def restricted(word, mode):
    if not word or word[0][0] == 0:
        return False
    if any(a != word[0][0] for a, b in word):
        return False
    n = len(word)
    indices = range(1, isqrt(n) + 1) if mode == 'prefix' else (i * i for i in range(1, isqrt(n) + 1))
    return all(word[i-1][1] == 0 for i in indices)


def good(word, mode, cache):
    if not word:
        return True
    if word[0] != (0, 0):
        return False
    for j in range(1, len(word) + 1):
        if (j == 1 or restricted(word[1:j], mode)) and valid_good_suffix(word[j:], mode, cache):
            return True
    return False


def valid_good_suffix(word, mode, cache):
    key = (word, mode)
    if key not in cache:
        cache[key] = good(word, mode, cache)
    return cache[key]


def in_language(word, mode, cache):
    if not word:
        return True
    # The word may consist entirely of one nonzero color.
    if all(a == word[0][0] and a != 0 for a, b in word):
        return True
    for j in range(len(word)):
        if (j == 0 or (word[0][0] != 0 and all(a == word[0][0] for a, b in word[:j]))) and valid_good_suffix(word[j:], mode, cache):
            return True
    return False


def recurrences(nmax):
    free = [0] * (nmax + 1)
    g = [0] * (nmax + 1)
    b = [0] * (nmax + 1)
    g[0] = 1
    for n in range(1, nmax + 1):
        free[n] = 1 if n == 1 else P * Q**(n - 1 - isqrt(n - 1))
        g[n] = sum(free[m] * g[n-m] for m in range(1, n+1))
        b[n] = P*Q**n + g[n] + P * sum(Q**(n-j) * g[j] for j in range(1,n))
    return free, g, b


def tail_exact(n, p=P, q=Q):
    assert n >= 2
    k = isqrt(n-1)
    s = n-1-k*k
    return Fraction(p, q) * Fraction(1,q**k) * (
        2*k+1-s + Fraction(2*k+1,q-1) + Fraction(2*q,(q-1)**2)
    )


def main():
    free, g, b = recurrences(12)
    brute_cases = 0
    for mode in ('prefix','squares'):
        cache = {}
        for n in range(1,6):
            brute = sum(in_language(w,mode,cache) for w in product(ALPHABET,repeat=n))
            assert brute == b[n], (mode, n, brute, b[n])
            brute_cases += len(ALPHABET)**n
        for n in range(2,12):
            # Direct bounded square-block summation plus analytic remote tail.
            k = isqrt(n-1)
            finite = sum(Fraction(P,Q) * Fraction(1,Q**isqrt(j)) for j in range(n-1,(k+4)**2))
            b0 = k+4
            remote = Fraction(P,Q) * Fraction(1,Q**b0) * (Fraction((2*b0+1)*Q,Q-1) + Fraction(2*Q,(Q-1)**2))
            assert finite + remote == tail_exact(n)
    assert Fraction(1 + P*Fraction(3*Q-1,(Q-1)**2),Q) == Fraction(31,36)
    assert Fraction(P,1-Fraction(31,36)) == Fraction(72,5)
    assert Fraction(P*P,Q) / ((1-Fraction(31,36))**2) == Fraction(1296,25)
    # The two distinct asymptotic phases have exact endpoint values.
    assert Fraction(1296,25)*Fraction(8,3)==Fraction(3456,25)
    assert Fraction(1296,25)*(Fraction(8,3)-2)==Fraction(864,25)
    print(f'VERIFY_OK: {brute_cases} independent words; 20 exact square tails; rational constants')

if __name__ == '__main__':
    main()
