#!/usr/bin/env python3
"""Exact finite-state and asymptotic checks for a two-coupling ferromagnetic Ising ring."""
from fractions import Fraction
from itertools import combinations, product
from math import gcd

def balanced(n, m):
    return tuple(((i + 1) * m) // n - (i * m) // n for i in range(n))

def direct_formula(word, x, y):
    n = len(word)
    t = [x if c else y for c in word]
    full = product_fraction(t)
    arcs = Fraction(0)
    for i in range(n):
        a = Fraction(1)
        for k in range(1, n):
            a *= t[(i + k - 1) % n]
            arcs += a
    return Fraction(n) + 2 * arcs / (1 + full)

def product_fraction(items):
    v = Fraction(1)
    for item in items:
        v *= item
    return v

def formula_min(n, m, x, y):
    q = x / y
    P = x ** m * y ** (n - m)
    terms = Fraction(0)
    for k in range(1, n):
        a, s = divmod(k * m, n)
        terms += y ** k * ((n - s) * q ** a + s * q ** (a + 1))
    return Fraction(n) + 2 * terms / (1 + P)

def direct_spins(word, x, y):
    n = len(word)
    t = [x if c else y for c in word]
    z, second = Fraction(0), Fraction(0)
    for signs in product((-1, 1), repeat=n):
        w = product_fraction(1 + t[i] * signs[i] * signs[(i+1) % n]
                             for i in range(n))
        z += w
        second += w * sum(signs) ** 2
    return second / z

def balanced_circular(word):
    n = len(word)
    for k in range(1, n):
        counts = [sum(word[(i + j) % n] for j in range(k))
                  for i in range(n)]
        if max(counts) - min(counts) > 1:
            return False
    return True

def run():
    x, y = Fraction(3, 4), Fraction(1, 4)
    checked_layouts = checked_spins = checked_minima = 0
    for n in range(3, 13):
        for m in range(1, n):
            b = balanced(n, m)
            assert sum(b) == m and balanced_circular(b)
            target = formula_min(n, m, x, y)
            assert direct_formula(b, x, y) == target
            shifts = {b[j:] + b[:j] for j in range(n)}
            winners = set()
            for pick in combinations(range(n), m):
                layout = tuple(int(i in pick) for i in range(n))
                value = direct_formula(layout, x, y)
                checked_layouts += 1
                assert value >= target, (n, m, layout)
                if value == target:
                    winners.add(layout)
            assert winners == shifts, (n, m, winners, shifts)
            checked_minima += 1
            if n <= 7:
                for pick in combinations(range(n), m):
                    layout = tuple(int(i in pick) for i in range(n))
                    assert direct_spins(layout, x, y) == direct_formula(layout, x, y)
                    checked_spins += 1
    # A separate temperature-independent test at a substantially different contrast.
    x2, y2 = Fraction(5, 6), Fraction(1, 3)
    for n in range(3, 11):
        for m in range(1, n):
            assert formula_min(n, m, x2, y2) == direct_formula(balanced(n, m), x2, y2)
    # Long-ring values from finite expressions versus independently derived limits.
    import math
    xf, yf = 0.82, 0.23
    pred_bal = (1 + xf) * (1 + yf) / (1 - xf * yf)
    pred_seg = ((1 + xf)/(1 - xf) + (1 + yf)/(1 - yf)) / 2
    pred_gap = (xf - yf)**2 / ((1 - xf)*(1-yf)*(1-xf*yf))
    assert abs((pred_seg - pred_bal) - pred_gap) < 1e-12
    for n in (200, 400, 800):
        m = n // 2
        b = balanced(n, m)
        cluster = tuple([1] * m + [0] * m)
        def floating(word):
            t = [xf if c else yf for c in word]
            # Evaluate using forward arcs until exponentially small contribution.
            s = 0.
            for i in range(n):
                a = 1.
                for k in range(1, min(n, 210)):
                    a *= t[(i + k - 1) % n]
                    s += a
            return 1 + 2 * s / n
        a, v = floating(b), floating(cluster)
        assert abs(a - pred_bal) < 5e-10
        assert abs(v - pred_seg) < 0.19 * 200 / n
    print(f'PASS: {checked_layouts} exact layouts, {checked_spins} independent exact spin-ensemble checks, {checked_minima} distinct (n,m) minima, asymptotic comparisons')

if __name__ == '__main__':
    run()
