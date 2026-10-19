#!/usr/bin/env python3
"""Standalone checks for the projected Gaussian hypergradient / null-step risk law.

Uses only the Python standard library. It verifies finite-dimensional formulas
numerically and replays the original two-update stochastic algorithm with
independent Gaussian training and validation batches.
"""
import math
import random


def c(d):
    return math.gamma((d + 1.0) / 2.0) / (math.sqrt(math.pi) * math.gamma(d / 2.0))


def cosine_integral(n, theta):
    """Integral from zero to theta of cos(t)**n, via an exact recurrence."""
    assert n >= 0
    if n == 0:
        return theta
    if n == 1:
        return math.sin(theta)
    im2, im1 = theta, math.sin(theta)
    for j in range(2, n + 1):
        curr = math.sin(theta) * math.cos(theta) ** (j - 1) / j
        curr += (j - 1) * im2 / j
        im2, im1 = im1, curr
    return im1


def survival_ratio(d, value):
    """P(N/sqrt(ChiSquared(d)) >= value), for value >= 0."""
    assert value >= 0.0
    return max(0.0, .5 - c(d) * cosine_integral(d - 1, math.atan(value)))


def acceptance(d, step):
    return survival_ratio(d + 2, step / 2.0)


def simpson(f, a, b, intervals=8192):
    assert intervals % 2 == 0
    h = (b - a) / intervals
    total = f(a) + f(b)
    for k in range(1, intervals):
        total += (4 if k % 2 else 2) * f(a + k * h)
    return total * h / 3.0


def projected_moment(d, eta, cap, accepted=True):
    # A trigonometric transformation avoids heavy-tailed integral endpoints.
    bound = math.atan(cap / eta)
    def integrand(theta):
        p = min(eta * math.tan(theta), cap)
        return c(d) * math.cos(theta) ** (d - 1) * p * p * (acceptance(d, p) if accepted else 1.0)
    return simpson(integrand, 0.0, bound) + simpson(integrand, bound, math.pi / 2)


def closed_proposed(d, eta, cap):
    L = cap / eta
    if d == 1:
        return eta * eta * (L - math.atan(L)) / math.pi + cap * cap * survival_ratio(1, L)
    if d == 2:
        return (eta * eta / 2.0) * (math.asinh(L) - L / math.sqrt(1 + L * L)) + cap * cap * survival_ratio(2, L)
    raise ValueError('Only dimensions 1 and 2 have these formulas')


def dimension_one_constant(cap):
    u = cap / 2.0
    return cap / math.pi * (1.0 - 2.0 * math.atan(u) / math.pi - u / (math.pi * (1 + u * u)))


def replay(dim, batch, eta, cap, n_samples, seed):
    rng = random.Random(seed)
    noise_sd = 1.0 / math.sqrt(batch)
    total = 0.0
    n_zero = 0
    n_cap = 0
    for _ in range(n_samples):
        train0 = [rng.gauss(0.0, noise_sd) for _ in range(dim)]
        valid0 = [rng.gauss(0.0, noise_sd) for _ in range(dim)]
        r = sum(a * b for a, b in zip(train0, valid0)) / sum(a * a for a in train0)
        # Starting at the population minimizer with alpha_0 = 0, x_1 = 0.
        p = min(cap, max(0.0, eta * r))
        n_zero += int(p == 0.0)
        n_cap += int(p == cap)
        train1 = [rng.gauss(0.0, noise_sd) for _ in range(dim)]
        valid1 = [rng.gauss(0.0, noise_sd) for _ in range(dim)]
        norm_sq = sum(a * a for a in train1)
        sample_decrease = p * p * norm_sq / 2.0 - p * sum(a * b for a, b in zip(train1, valid1))
        if sample_decrease <= 0:
            total += p * p * norm_sq / 2.0
    return total / n_samples, n_zero / n_samples, n_cap / n_samples


def run_checks():
    checks = 0
    for d in range(1, 9):
        assert abs(survival_ratio(d, 0.0) - .5) < 1e-14
        assert survival_ratio(d, 3.0) < .5
        assert survival_ratio(d, 3.0) > 0
        checks += 3
    for d in (1, 2):
        for eta in (.05, .1, .2, .7):
            direct = projected_moment(d, eta, 1.0, False)
            formula = closed_proposed(d, eta, 1.0)
            assert abs(direct - formula) < 3e-8, (d, eta, direct, formula)
            checks += 1
    for d in (1, 2, 3, 4, 6):
        for eta in (.03, .1, .4):
            got = projected_moment(d, eta, 1.0, True)
            unguarded = projected_moment(d, eta, 1.0, False)
            assert 0 < got < unguarded / 2, (d, eta, got, unguarded)
            checks += 1
    eta = .001
    for d in (1, 2, 3, 4, 6):
        observed = projected_moment(d, eta, 1.0, True)
        target = (dimension_one_constant(1.0) * eta if d == 1 else
                  eta ** 2 * math.log(1 / eta) / 4 if d == 2 else
                  eta ** 2 / (4 * (d - 2)))
        assert abs(observed / target - 1.0) < (0.13 if d == 2 else .015), (d, observed, target)
        checks += 1
    for d in (1, 2, 3):
        for batch in (1, 9):
            empirical, pzero, pcap = replay(d, batch, .4, 1.0, 60000, 20261017 + d * 100 + batch)
            target = (d / (2 * batch)) * projected_moment(d, .4, 1.0, True)
            assert abs(empirical / target - 1.0) < .14, (d, batch, empirical, target)
            assert abs(pzero - .5) < .015
            assert abs(pcap - survival_ratio(d, 2.5)) < .015
            checks += 3
    print('PASS:', checks, 'families of analytical and replay checks')

if __name__ == '__main__':
    run_checks()
