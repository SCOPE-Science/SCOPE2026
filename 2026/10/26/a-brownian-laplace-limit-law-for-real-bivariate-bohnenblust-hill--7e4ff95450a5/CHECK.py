#!/usr/bin/env python3
"""Finite algebra/covariance checks accompanying the Brownian Laplace limit law.

These checks are diagnostics, not a proof of a weak limit. Requires numpy.
"""
import numpy as np


def check():
    rng = np.random.default_rng(20261022)
    for m in (2, 3, 10, 29, 101):
        g = rng.normal(size=m + 1)
        for sign in (1, -1):
            a = sign ** np.arange(m + 1) * g / np.sqrt(m)
            cumul = np.r_[0.0, np.cumsum(a)]
            for s in (0.0, 0.000001, 0.01, 0.2, 1.0, 5.0, 50.0, 1000.0):
                w = np.exp(-s * np.arange(m + 1) / m)
                direct = np.dot(a, w)
                abel = np.exp(-s) * cumul[m + 1] + np.dot(w[:-1] - w[1:], cumul[1:m + 1])
                assert np.isclose(direct, abel, atol=1e-12)
            for t in (-1.0, -0.73, 0.0, 0.45, 1.0):
                forward = sum(g[j] * t ** j for j in range(m + 1))
                backward = sum(g[j] * t ** (m - j) for j in range(m + 1))
                assert np.isclose(forward, np.dot(g, t ** np.arange(m + 1)))
                assert np.isclose(backward, np.dot(g, t ** np.arange(m, -1, -1)))
        for k in range(m + 1):
            cross_covariance = sum((-1) ** j for j in range(k)) / m
            assert abs(cross_covariance) <= 1 / m + 1e-14
    print('PASS: Abel identities, forward/reverse boundary evaluation, signed covariance bound')


if __name__ == '__main__':
    check()
