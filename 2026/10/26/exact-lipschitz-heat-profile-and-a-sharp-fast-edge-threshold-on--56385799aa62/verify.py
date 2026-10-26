#!/usr/bin/env python3
"""Reproduce the symbolic block reduction and numerical finite diagnostics.

Dependencies: Python 3, numpy, scipy, sympy. No external data or network calls.
The infinite-parameter theorem is proved in RESULT.md, not by sampling.
"""
import itertools
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

W = sp.symbols('W', positive=True)
L = sp.zeros(4, 4)
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
for (i, j), conductance in zip(edges, [W, 1, 1, 1]):
    L[i, i] += conductance
    L[j, j] += conductance
    L[i, j] -= conductance
    L[j, i] -= conductance
# Direct block check: f=(p+x,p-x,q+y,q-y), z=p-q.
p, q, x, y = sp.symbols('p q x y')
f = sp.Matrix([p + x, p - x, q + y, q - y])
g = -L * f
assert sp.simplify((g[0] + g[1] - g[2] - g[3]) / 2 + 2*(p - q)) == 0
assert sp.simplify((g[0] - g[1]) / 2 + (2*W+1)*x + y) == 0
assert sp.simplify((g[2] - g[3]) / 2 + x + 3*y) == 0
print('PASS: symbolic conjugation of the weighted graph generator')

# With f(0)=0 the graph-distance Lipschitz polytope is integral:
# its defining directed incidence matrix is totally unimodular.
# Every vertex is among the integer potentials enumerated below.
F = np.array([(0, *r) for r in itertools.product(range(-2, 3), repeat=3)
              if all(abs((0, *r)[i] - (0, *r)[j]) <= 1 for i, j in edges)],
             dtype=float)
assert len(F) == 19

def exact_formula(w, t):
    delta = math.hypot(w - 1.0, 1.0)
    lo, hi = w + 2.0 - delta, w + 2.0 + delta
    A, B = math.exp(-lo*t), math.exp(-hi*t)
    alpha, beta = (A+B)/2.0, (A-B)/(2.0*delta)
    if w <= 1.0:
        return alpha + (2.0-w)*beta
    return math.exp(-2.0*t) + (w-1.0)*beta

def independent_norm(w, t):
    graph_L = np.zeros((4,4), dtype=float)
    for (i,j), weight in zip(edges, [w, 1.0, 1.0, 1.0]):
        graph_L[i,i] += weight
        graph_L[j,j] += weight
        graph_L[i,j] -= weight
        graph_L[j,i] -= weight
    heat = expm(-t*graph_L)
    return max(float(np.max(np.abs(F @ (heat[i,:]-heat[j,:]))))
               for i,j in edges)

weights = [0.0001, 0.1, 0.3, 0.5, 1.0, 1.1, 2.0, 2.999, 3.0,
           3.0001, 4.0, 10.0, 20.0, 100.0]
times = [0.0, 1e-7, 1e-5, 0.001, 0.01, 0.1, 0.5, 1.0, 10.0, 50.0]
for w in weights:
    for t in times:
        expected = exact_formula(w,t)
        independently_computed = independent_norm(w,t)
        assert abs(expected-independently_computed) <= 2e-10, (w,t,expected,independently_computed)
print('PASS: 140 independent matrix-exponential/Lipschitz-polytope comparisons')
assert exact_formula(2.0, 0.1) < 1
assert exact_formula(3.0, 0.01) < 1
assert exact_formula(4.0, 0.01) > 1
assert abs(exact_formula(1e8, 1e-4) - 1.5) < 4e-4
print('PASS: representative contractivity and fast-edge diagnostics')
