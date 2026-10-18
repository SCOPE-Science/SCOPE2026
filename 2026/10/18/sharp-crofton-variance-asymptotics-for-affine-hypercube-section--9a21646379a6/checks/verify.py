#!/usr/bin/env python3
"""Independent finite simulations of the affine-hypercube Crofton formula.

Requires numpy. Simulations test normalization and finite-dimensional overlap
identities; the all-dimensional limit follows from the accompanying proof.
"""
import itertools
import math
import numpy as np

SEED = 20261015
rng = np.random.default_rng(SEED)
mu = math.sqrt(2.0 / math.pi)
limit = 1.0 / (2.0 * math.sqrt(2.0) * math.pi)

# A width-biased Gaussian normal can be sampled by selecting one random
# coordinate to have the size-biased half-normal (Rayleigh) magnitude.
def direct_crofton_vertices(n, sample_count=40_000):
    g = rng.normal(size=(sample_count, n))
    marked = rng.integers(n, size=sample_count)
    rr = np.arange(sample_count)
    rayleigh = np.sqrt(-2.0 * np.log(rng.random(sample_count)))
    g[rr, marked] = np.where(rng.random(sample_count) < 0.5, -rayleigh, rayleigh)
    levels = rng.uniform(-1, 1, sample_count) * np.abs(g).sum(axis=1)
    count = np.zeros(sample_count, dtype=np.int32)
    for j in range(n):
        free = [i for i in range(n) if i != j]
        signs = np.array(list(itertools.product((-1, 1), repeat=n-1)), dtype=float)
        centers = g[:, free] @ signs.T
        count += (np.abs(centers - levels[:, None]) < np.abs(g[:, j, None])).sum(axis=1)
    return float(count.mean())

for n in (3, 4, 5):
    observed = direct_crofton_vertices(n)
    expected = float(2 ** (n-1))
    assert abs(observed / expected - 1.0) < 0.035, (n, observed, expected)
    print(f"direct Crofton n={n}: estimated mean {observed:.4f}; exact mean {expected:.4f}")

# Independently sample two uniform cube edges.  For distinct coordinate
# directions, mismatched endpoint signs produce a Gaussian N(0,4H)
# shift, where H~Bin(n-2,1/2).  The same-direction case has H~Bin(n-1,1/2).
samples = 350_000
for n in (8, 16, 32, 64, 128, 256, 512):
    h = rng.binomial(n-2, 0.5, size=samples)
    a = np.abs(rng.normal(size=samples))
    b = np.abs(rng.normal(size=samples))
    s = rng.choice((-1.0, 1.0), (2, samples))
    z = rng.normal(size=samples) * 2.0 * np.sqrt(h)
    delta = z + s[0] * b - s[1] * a
    ell_dist = np.maximum(0.0, np.minimum(a, delta+b) - np.maximum(-a, delta-b)).mean()
    hs = rng.binomial(n-1, 0.5, size=samples)
    aa = np.abs(rng.normal(size=samples))
    zs = rng.normal(size=samples) * 2.0 * np.sqrt(hs)
    ell_same = np.maximum(0.0, 2.0 * aa - np.abs(zs)).mean()
    mean_overlap = (ell_same + (n-1) * ell_dist) / n
    normalized_second = math.sqrt(n) * mean_overlap / (8.0 * mu)
    normalized_variance = normalized_second - 1.0 / (4.0 * math.sqrt(n))
    if n >= 128:
        assert abs(normalized_second - limit) < 0.021, (n, normalized_second, limit)
    print(f"pair overlap n={n}: normalized variance {normalized_variance:.6f}; limit {limit:.6f}")

print("Numerical checks passed; finite tests do not prove the asymptotic theorem.")
