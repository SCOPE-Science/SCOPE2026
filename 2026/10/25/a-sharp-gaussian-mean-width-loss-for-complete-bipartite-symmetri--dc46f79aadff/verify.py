"""Standalone numerical and exhaustive diagnostics for a symmetric-edge mean-width gap.
Run: python verify.py (requires Python 3 and NumPy). Finite checks are not proofs of limits.
"""
import itertools
import math
import numpy as np


def extrema_gap(g, p):
    a = g[:p]
    b = g[p:]
    full = float(max(np.max(a), np.max(b)) - min(np.min(a), np.min(b)))
    bip = float(max(np.max(a) - np.min(b), np.max(b) - np.min(a)))
    return full-bip


def vertex_gap(g, p):
    n = len(g)
    full = max(abs(float(g[i]-g[j])) for i in range(n) for j in range(i+1,n))
    bip = max(abs(float(g[i]-g[j])) for i in range(p) for j in range(p,n))
    return full-bip


rng = np.random.default_rng(881493)
vertex_tests = 0
for p, q in [(1,2), (2,2), (2,3), (3,4), (5,5), (7,3)]:
    for _ in range(125):
        g = rng.normal(size=p+q)
        direct = vertex_gap(g,p)
        fast = extrema_gap(g,p)
        assert abs(direct-fast) < 1e-11, (p,q,direct,fast)
        assert fast >= -1e-11
        vertex_tests += 1

# Enumerate every strict linear order of the coordinate values: the top and
# bottom belong to the same group exactly in the event predicted by the formula.
rank_tests = 0
for p,q in [(1,2),(2,2),(2,3),(3,3),(3,4)]:
    total = positive = 0
    for perm in itertools.permutations(range(p+q)):
        values = np.asarray(perm,dtype=float)
        positive += extrema_gap(values,p)>0.5
        total += 1
    predicted = (p*(p-1)+q*(q-1))/( (p+q)*(p+q-1))
    assert abs(positive/total-predicted)<1e-13
    rank_tests += 1

# Cross-check the non-obvious independent-logistic identity by numerical
# quadrature, separately from the Gumbel Monte Carlo below.
M = 100000
u = (np.arange(M,dtype=float)+0.5)/M
integral = 2*np.mean(u*np.log(u/(1-u)))
assert abs(integral-1.0)<1e-5, integral

# The proposed limit uses FOUR independent Gumbels, not independent maxima
# and minima from a single finite sample.
limit_cases = 0
samples = rng.gumbel(size=(400000,4))
for alpha in [.15, .35, .5, .8]:
    beta = 1-alpha
    x1 = math.log(alpha) + samples[:,0]
    x2 = math.log(beta) + samples[:,1]
    y1 = math.log(alpha) + samples[:,2]
    y2 = math.log(beta) + samples[:,3]
    d = np.maximum(x1,x2) + np.maximum(y1,y2) - np.maximum(x1+y2,x2+y1)
    expectation = -math.log(alpha*beta)-1
    atom = 2*alpha*beta
    assert np.min(d)>-1e-12
    assert abs(float(d.mean())-expectation)<.016, (alpha,d.mean(),expectation)
    assert abs(float(np.mean(d < 1e-12))-atom)<.006, (alpha, np.mean(d<1e-12),atom)
    limit_cases += 1

print(f"VERIFY_OK vertex_support={vertex_tests} exhaustive_rank={rank_tests} gaussian_limit_cases={limit_cases} logistic_quadrature={M}")
