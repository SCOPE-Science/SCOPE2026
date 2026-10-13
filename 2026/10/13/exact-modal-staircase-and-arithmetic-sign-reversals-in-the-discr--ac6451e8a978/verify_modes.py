#!/usr/bin/env python3
"""Finite numerical illustrations for a two-sided linear-geometric law.

The exact modal phase classification is proved analytically in RESULT.md.
This program tests selected finite instances, not all positive parameters.
"""
import math


def pmf(x, theta, tau):
    left = math.exp(-theta / tau)
    right = math.exp(-theta * tau)
    sleft = tau * left / (1 - left) + left / (1 - left) ** 2
    sright = tau / (1 - right) + tau * tau * right / (1 - right) ** 2
    norm = 1 / (sleft + sright)
    if x < 0:
        return norm * (tau - x) * math.exp(theta * x / tau)
    return norm * tau * (1 + tau * x) * math.exp(-theta * tau * x)


def site_data(p=3, q=2, last=120):
    h = 1 / math.sqrt(p * q)
    v = [m for m in range(last + 1) if m % p == 0 or m % q == 0]
    sites = [m * h for m in v]
    labels = [([m // p] if m % p == 0 and m > 0 else []) +
              ([-m // q] if m % q == 0 and m > 0 else []) if m else [0]
              for m in v]
    slopes = [math.log1p((sites[i + 1] - sites[i]) / (1 + sites[i])) /
              (sites[i + 1] - sites[i]) for i in range(len(sites) - 1)]
    return sites, labels, slopes


def verify():
    p, q = 3, 2
    tau = math.sqrt(p / q)
    sites, labels, slopes = site_data(p, q)
    assert all(slopes[i] > slopes[i + 1] > 0 for i in range(50))
    print('first merged lattice labels:', labels[:13])
    print('first transition parameters:', [round(z, 12) for z in slopes[:9]])
    witnesses = []
    for i in range(1, 22):
        theta = (slopes[i - 1] + slopes[i]) / 2
        weights = {x: pmf(x, theta, tau) for x in range(-350, 351)}
        maximizers = [x for x, w in weights.items()
                      if w >= max(weights.values()) - 1e-13 * max(weights.values())]
        expected = sorted(labels[i])
        assert sorted(maximizers) == expected, (i, theta, expected, maximizers)
        if len(expected) == 1 and expected[0] != 0:
            witnesses.append((round(theta, 9), expected[0]))
    for i in range(1, 15):
        theta = slopes[i]
        vals = [pmf(x, theta, tau) for x in labels[i] + labels[i + 1]]
        assert max(vals) - min(vals) < 5e-13 * max(vals)
    for theta in (0.07, 0.3, 0.5, 1.4):
        for x in range(-24, 25):
            z = (tau * x if x >= 0 else -x / tau)
            f = (1 + z) * math.exp(-theta * z)
            ratio = pmf(x, theta, tau) / pmf(0, theta, tau)
            assert abs(f - ratio) < 5e-12
        assert abs(sum(pmf(x, theta, tau) for x in range(-1800, 1801)) - 1) < 1e-11
    print('unique-mode witnesses (theta, x):', witnesses[:15])
    print('normalized weights, transition ties, and direct mode scans: PASS')


if __name__ == '__main__':
    verify()
