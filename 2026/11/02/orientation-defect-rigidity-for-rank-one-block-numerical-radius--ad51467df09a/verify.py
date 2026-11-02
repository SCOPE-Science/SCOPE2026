"""Finite supplementary checks for the rank-one orientation-path formulas.

Requires Python 3 with NumPy. Does not serve as an infinite proof.
"""
import itertools
import math
import numpy as np


def gram_radius(word, r):
    e = len(word)
    go, ge = np.eye(e), np.eye(e)
    for j in range(e - 1):
        t = 1.0 if word[j] != word[j + 1] else r
        g = ge if j % 2 == 0 else go
        g[j, j + 1] = g[j + 1, j] = t
    lam = max(np.linalg.eigvals(go @ ge).real)
    return math.sqrt(max(0.0, lam)) / 2


def direct_radius(word, r, phase=0.0, scale=1.0):
    n = len(word) + 1
    u = np.array([1.0, 0.0], dtype=complex)
    v = np.array([r, math.sqrt(max(0.0, 1 - r*r))], dtype=complex)
    t = scale * np.exp(1j * phase) * np.outer(u, v.conj())
    s = np.zeros((2*n, 2*n), dtype=complex)
    for j, sign in enumerate(word):
        s[2*j:2*j+2, 2*j+2:2*j+4] = t if sign == '+' else t.conj().T
    h = (s + s.conj().T) / 2
    return np.linalg.eigvalsh(h)[-1]


def longest_alternating(word):
    best = run = 1
    for j in range(1, len(word)):
        run = run + 1 if word[j] != word[j-1] else 1
        best = max(best, run)
    return best


count = 0
for n in range(3, 11):
    for word in map(''.join, itertools.product('+-', repeat=n-1)):
        for r in (0, .13, .43, .81, 1):
            actual = direct_radius(word, r)
            predicted = gram_radius(word, r)
            assert abs(actual-predicted) < 2e-10, (word, r, actual, predicted)
            count += 1
        l = longest_alternating(word)
        assert abs(gram_radius(word, 0)-math.cos(math.pi/(l+2))) < 2e-10
        count += 1
        theta = math.pi/(n+1)
        cost = sum(math.sin((j+1)*theta)*math.sin((j+3)*theta)
                   for j in range(n-2) if word[j] == word[j+1]) / ((n+1)*math.cos(theta))
        h = 1e-6
        slope = (gram_radius(word, 1)-gram_radius(word, 1-h))/h
        assert abs(slope-cost)<1e-4, (word, slope, cost)
        count += 1
        if any(word[j] == word[j+1] for j in range(n-2)):
            values = [gram_radius(word, r) for r in (0, .2, .6, .99, 1)]
            assert all(b>a+1e-8 for a,b in zip(values,values[1:]))
            count += 1

for word in ('++-', '++--', '+-+-', '-++-', '++++', '---++'):
    for r in (0, .2, .73, 1):
        for phase in (.19, 1.76, 3.28):
            actual = direct_radius(word,r,phase,scale=1.37)
            predicted = 1.37 * gram_radius(word,r)
            assert abs(actual-predicted)<2e-10
            count += 1

print(f'PASS: {count} supplementary assertions')
