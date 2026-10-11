#!/usr/bin/env python3
"""Finite computational sanity checks of the directional cube-section law.

The proof is analytic; these finite checks are not a certificate for the limit.
Run: python verify.py
"""
import itertools
import math
import numpy as np

C = math.sqrt(2.0 / math.pi)

def edge_crossing_counts(g):
    """Enumerate cube *edges*, testing the signs of their actual endpoints."""
    n = len(g)
    counts = [0] * n
    for i in range(n):
        for eps in itertools.product((-1, 1), repeat=n-1):
            z = sum(e * g[j] for e, j in zip(eps, (j for j in range(n) if j != i)))
            if (z-g[i]) * (z+g[i]) < 0:
                counts[i] += 1
    return counts

def threshold_counts(g):
    n = len(g)
    return [sum(abs(sum(e * g[j] for e, j in zip(eps, (j for j in range(n) if j != i)))) < abs(g[i]) for eps in itertools.product((-1,1), repeat=n-1)) for i in range(n)]

for n in range(3, 10):
    # A generic integer normal with no zero cube-vertex scalar product.
    g = [(2 * j + 1) for j in range(n)]
    if sum(g) % 2 == 0:
        g[0] += 1
    a, b = edge_crossing_counts(g), threshold_counts(g)
    assert a == b, (n,a,b)
    assert all(0 <= z <= 2**(n-1) for z in a)

rng = np.random.default_rng(20261010)
for n in [3, 5, 8, 12]:
    m = n - 1
    eps = np.array(list(itertools.product((-1.0, 1.0), repeat=m)), dtype=np.float64)
    sample_n = 2000 if n < 10 else 1000
    x = rng.normal(size=sample_n)
    y = rng.normal(size=(sample_n, m))
    # Independently implement the formula for i=1 using batched matrix multiplication.
    sums = y @ eps.T
    frac = (np.abs(sums) < np.abs(x[:,None])).mean(axis=1)
    target = C*np.abs(x)
    scaled = math.sqrt(m)*frac
    mse = np.mean((scaled-target)**2)
    claimed_bound = (2 / math.pi) * math.atan(1 / math.sqrt(m)) + 5/(6*math.pi*m*m)
    assert mse <= claimed_bound * 1.15, (n,mse,claimed_bound)
    # The Gaussian conditional mean agrees with the error-function expression.
    conditional_mean = np.array([math.erf(abs(xx)/math.sqrt(2*m)) for xx in x])
    predicted_abs_difference = np.mean(np.abs(scaled - conditional_mean * math.sqrt(m)))
    assert predicted_abs_difference < 0.35
    print(f'n={n}, samples={sample_n}, L2_MSE={mse:.6f}, bound={claimed_bound:.6f}')
print('DIRECTIONAL_CUBE_SANITY_OK')
