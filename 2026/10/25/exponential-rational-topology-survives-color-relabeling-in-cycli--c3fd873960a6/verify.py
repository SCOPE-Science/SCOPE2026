#!/usr/bin/env python3
"""Independent exact checks of cycle partial-coloring quotient Euler formulas."""
from math import comb, factorial
from collections import Counter

def derangements(m):
    if m == 0: return 1
    if m == 1: return 0
    a, b = 1, 0
    for k in range(2, m + 1):
        a, b = b, (k - 1) * (a + b)
    return b

def lucas(n, f):
    a, b = 2, 2 - f
    if n == 0: return a
    if n == 1: return b
    for k in range(2, n + 1):
        a, b = b, (2 - f) * b - a
    return b

def z(n, f):
    return f - 1 + lucas(n, f)

def formula(n, q):
    total = sum(comb(q, f) * derangements(q - f) * z(n, f)
                for f in range(q + 1))
    assert total % factorial(q) == 0
    return -total // factorial(q)

def enumerate_orbit_representatives(n, q):
    """Enumerate canonical partial colorings; do not use transfer/Burnside."""
    f = Counter()
    def rec(i, used, sequence):
        if i == n:
            if n >= 3 and sequence[0] and sequence[-1] and sequence[0] == sequence[-1]:
                return
            k = sum(t != 0 for t in sequence)
            f[k] += 1
            return
        for c in range(used + 2):
            if c > q: break
            if i and c and sequence[-1] == c: continue
            rec(i + 1, max(c, used), sequence + (c,))
    rec(0, 0, ())
    return -sum((-1) ** k * nfaces for k, nfaces in f.items()), f

def labelled_face_sum(n, q):
    zsum = 0
    def rec(i, first, prev, chosen):
        nonlocal zsum
        if i == n:
            if first and prev == first: return
            zsum += (-1) ** chosen
            return
        for color in range(q + 1):
            if color and color == prev: continue
            rec(i+1, color if not i else first, color, chosen + (color != 0))
    rec(0, 0, 0, 0)
    return zsum

def main():
    tests = 0
    for q in range(1, 9):
        for n in range(3, 10):
            expected = formula(n, q)
            got, _ = enumerate_orbit_representatives(n, q)
            assert got == expected, (n, q, expected, got)
            tests += 1
    for q in range(1, 6):
        for n in range(3, 7):
            assert labelled_face_sum(n, q) == z(n, q)
            tests += 1
    print('VERIFIED', tests, 'exact independent checks')
    for q in (4, 5, 6):
        print('q=', q, 'Euler quotient n=3..10', [formula(n, q) for n in range(3, 11)])
if __name__ == '__main__': main()
