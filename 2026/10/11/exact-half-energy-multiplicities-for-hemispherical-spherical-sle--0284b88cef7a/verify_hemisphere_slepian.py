#!/usr/bin/env python3
"""Numerical corroboration for the hemispherical spherical-Slepian theorem."""
import math
import random
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import gammaln, lpmv


def colatitudinal(l, m, x):
    """X_lm with 2*pi*integral_{-1}^1 X_lm X_km = delta_lk."""
    logn = 0.5 * (
        math.log(2 * l + 1)
        - math.log(4 * math.pi)
        + gammaln(l - m + 1)
        - gammaln(l + m + 1)
    )
    return math.exp(logn) * lpmv(m, l, x)


def hemisphere_block(degrees, m):
    degrees = [l for l in degrees if l >= m]
    if not degrees:
        return np.empty((0, 0))
    nodes, weights = leggauss(max(degrees) + 5)
    x = (nodes + 1.0) / 2.0
    weights = weights / 2.0
    vals = np.stack([colatitudinal(l, m, x) for l in degrees])
    return 2.0 * math.pi * ((vals * weights) @ vals.T)


def half_multiplicity(degrees, m):
    active = [l for l in degrees if l >= m]
    even = sum((l + m) % 2 == 0 for l in active)
    odd = len(active) - even
    return abs(even - odd)


def main():
    rng = random.Random(2705)
    masks = []
    for top in range(21):
        masks.append(list(range(top + 1)))
        for _ in range(5):
            mask = [l for l in range(top + 1) if rng.random() < 0.55]
            if mask:
                masks.append(mask)

    blocks = 0
    max_pair_error = 0.0
    max_half_error = 0.0
    for degrees in masks:
        top = max(degrees)
        for m in range(top + 1):
            active = [l for l in degrees if l >= m]
            if not active:
                continue
            eig = np.linalg.eigvalsh(hemisphere_block(degrees, m))
            predicted = half_multiplicity(degrees, m)
            is_half = np.isclose(eig, 0.5, atol=2e-10, rtol=0.0)
            observed = int(np.sum(is_half))
            if observed != predicted:
                raise AssertionError((degrees, m, predicted, observed, eig))
            if predicted:
                max_half_error = max(max_half_error, float(np.max(np.abs(eig[is_half] - 0.5))))
            for j in range(len(eig) // 2):
                max_pair_error = max(max_pair_error, abs(eig[j] + eig[-1 - j] - 1.0))
            blocks += 1

    for L in range(41):
        total = half_multiplicity(range(L + 1), 0)
        total += 2 * sum(half_multiplicity(range(L + 1), m) for m in range(1, L + 1))
        if total != L + 1:
            raise AssertionError((L, total))

    print(
        "VERIFY_OK "
        f"blocks={blocks} lowpass_L=0..40 "
        f"max_pair_err={max_pair_error:.3e} max_half_err={max_half_error:.3e}"
    )


if __name__ == "__main__":
    main()
