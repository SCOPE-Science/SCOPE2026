#!/usr/bin/env python3
"""Exact finite-size checks for sibling-leaf pairs in degree-preferential trees.

Standard-library-only, deterministic, self-contained. Run with Python 3.9+.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def H(r):
    return sum((Fraction(1, j) for j in range(1, r + 1)), Fraction(0))

def stats(parent):
    n = len(parent)
    degree = [0] * n
    for v in range(1, n):
        w = parent[v]
        degree[v] += 1
        degree[w] += 1
    neighbor_leaves = [0] * n
    for v in range(1, n):
        w = parent[v]
        if degree[v] == 1:
            neighbor_leaves[w] += 1
        if degree[w] == 1:
            neighbor_leaves[v] += 1
    squares = sum(d * d for d in degree)
    weighted_leaves = sum(d * l for d, l in zip(degree, neighbor_leaves))
    pairs = sum(comb(l, 2) for l in neighbor_leaves)
    cubed = sum(d**3 for d in degree)
    return squares, weighted_leaves, pairs, cubed, degree

def means(n):
    sx = 2 * (n - 1) * H(n - 1)
    xx = 2 + (n - 1) * H(n - 2)
    if n == 2:
        cc = Fraction(0)
    else:
        cc = ((n - 2) + Fraction(n * (n - 3) + 2, 4) * H(n - 3)
              - Fraction(n * (n - 3), 8)) / (n - 2)
    return sx, xx, cc

# State probabilities enumerate all attachment histories exactly.
level = {(None, 0): Fraction(1)}
for n in range(2, 10):
    verify(sum(level.values(), Fraction(0)) == 1, f'probabilities n={n}')
    expected = [Fraction(0)] * 3
    new_level = defaultdict(Fraction)
    for parent, mass in level.items():
        s, x, c, t, degree = stats(parent)
        for i, v in enumerate((s, x, c)):
            expected[i] += mass * v
        if n >= 3:
            ds = dx = dc = dt = Fraction(0)
        for v, d in enumerate(degree):
            w = Fraction(d, 2 * (n - 1))
            next_parent = parent + (v,)
            s2, x2, c2, t2, _ = stats(next_parent)
            new_level[next_parent] += mass * w
            if n >= 3:
                ds += w * s2
                dx += w * x2
                dc += w * c2
                dt += w * t2
        if n >= 3:
            verify(ds == Fraction(n, n-1) * s + 2, f'S conditional n={n}')
            verify(dx == x + 1 + Fraction(s, 2*(n-1)), f'X conditional n={n}')
            verify(dc == Fraction(n-2,n-1)*c + Fraction(x,2*(n-1)), f'C conditional n={n}')
            verify(dt == t + Fraction(3*t+3*s+4*(n-1), 2*(n-1)), f'T3 conditional n={n}')
    verify(tuple(expected) == means(n), f'exact expectations n={n}: {expected}')
    if n < 9:
        level = new_level

# Initial non-degeneracy of the quadratic-degree martingale.
origin = (None,0,0)
vals = []
for v,d in enumerate(stats(origin)[4]):
    p = origin+(v,)
    sv = stats(p)[0]
    vals.append((Fraction(d,4),Fraction(sv,3)-2*H(3)))
verify(sorted([z for _,z in vals]) == [Fraction(-1,3),Fraction(-1,3),Fraction(1,3)],'quadratic martingale branches')
verify(sum((w*z for w,z in vals),Fraction()) == 0,'martingale centered')
verify(sum((w*z*z for w,z in vals),Fraction()) == Fraction(1,9),'martingale variance')

print(f'PASS: {checks} exact checks, attachment histories through 9 vertices.')
print('Exact means n=9:', ', '.join(str(y) for y in means(9)))
print('First nontrivial martingale variance: 1/9 at four vertices.')
print('Finite enumeration does not certify the infinite almost-sure limit.')
