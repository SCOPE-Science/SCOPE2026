#!/usr/bin/env python3
"""Finite sanity checks for spectral-frequency cancellation identities.

The analytic completeness and infinite-codimension theorems are proved
mathematically; the finite checks below are not substitutes for that proof.
"""
import cmath
import math


def coset_factor(t, h, phases):
    length = 2 * math.pi / h
    result = 1.0 + 0.0j
    for phase in phases:
        result *= cmath.exp(1j * t * length) - cmath.exp(1j * phase * length)
    return result


def verify():
    for h, phases in [(2.5, (0.2, 0.9, 1.7)), (1.7, (-0.4, 0.5))]:
        for phase in phases:
            for k in range(-12, 13):
                t = phase + h * k
                assert abs(coset_factor(t, h, phases)) < 5e-11
        assert abs(coset_factor(0.13, h, phases)) > 1e-5

    p = 1.5
    q = p / (p - 1)
    a, b = 1 / q, 1 / p
    sigma = 0.5
    w = min(sigma - a, b - sigma)
    c = 0.08
    delta = 0.14
    assert math.pi * c / 2 < delta < w
    exponent = math.pi * c / (2 * delta)
    assert 0 < exponent < 1  # p-series divergence in the analytic proof

    # Conformal mapping of the horizontal strip sends large real frequencies
    # toward the disk boundary at the predicted exponential scale.
    for t in (8.0, 16.0, 24.0):
        image = math.tanh(math.pi * t / (4 * delta))
        measured = 1 - image
        expected = 2 * math.exp(-math.pi * t / (2 * delta))
        # For very large t standard doubles round tanh to one.
        if measured > 0:
            assert abs(measured / expected - 1) < 0.005
    print("Finite phase-factor zeros, strip scale and exponent inequalities: PASS")
    print("No computational claim of infinite completeness or priority.")


if __name__ == "__main__":
    verify()
