#!/usr/bin/env python3
"""Exact finite-prime checks for the mixed finite-field Gram collision theorem."""
from fractions import Fraction

for p in (5, 7, 11, 13, 17, 19):
    H = [(u, pow(u, -1, p)) for u in range(1, p)]
    V = [set(((t + u) % p, (t*t + inv) % p) for u, inv in H)
         for t in range(p)]
    G = [[len(V[t] & V[s]) for s in range(p)] for t in range(p)]
    assert all(G[i][j] == G[j][i] for i in range(p) for j in range(p))
    assert all(G[i][i] == p - 1 for i in range(p))
    rows = [sum(row) for row in G]
    assert sum(rows) == 2 * (p - 1)**2
    assert len(set(rows)) > 1
    S = sum(rows)
    var = sum((Fraction(x) - Fraction(S, p))**2 for x in rows)
    assert var >= Fraction(2 * (p - 2), p)
    norm_lb = Fraction(2 * (p - 1), p) + Fraction(p-2, p*(p-1)**3)
    assert norm_lb > Fraction(2 * (p - 1), p)
    print(p, 'rows', rows, 'squared_variance', var, 'norm_lower_bound', norm_lb)
print('EXACT_CHECKS_PASS')
