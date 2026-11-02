#!/usr/bin/env python3
"""Standalone reproducibility checks for a last-iterate weak-limit theorem.

Requires Python 3 standard library only. Finite checks corroborate, but do not
replace, the analytic convergence arguments documented in RESULT.md.
"""
import math
import random


def soft(x, level):
    return math.copysign(max(abs(x) - level, 0.0), x) if x else 0.0


def cdf_tail(x):
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)


def rate(theta):
    return theta * (phi(theta) - theta * cdf_tail(theta))


def sign(x):
    return (x > 0) - (x < 0)


def trial_perturbation(initial, drifts, W):
    state = initial
    for j, drift in enumerate(drifts):
        state -= drift * sign(state)
        state += W[j + 1] - W[j]
    D = sum(drifts)
    delta = max(abs(x) for x in W)
    bound = 3 * delta + max(drifts, default=0.0)
    return abs(state - soft(initial, D)), bound


def check():
    checks = 0
    rng = random.Random(1873)
    # Exact finite combinatorial search over small rational drifts / cumulative noise.
    from itertools import product
    grid = [-0.25, 0.0, 0.25]
    for initial in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        for drifts in product([0.0, 0.1, 0.3], repeat=3):
            for endnoise in product(grid, repeat=3):
                err, bound = trial_perturbation(initial, drifts, (0.0,) + endnoise)
                assert err <= bound + 1e-12, (initial, drifts, endnoise, err, bound)
                checks += 1
    # Independent randomized, variable-length finite path checks of the lemma.
    for j in range(10000):
        count = rng.randrange(1, 30)
        h = rng.random() * .3
        drifts = [rng.random() * h for _ in range(count)]
        delta = rng.random() * .3
        W = [0.0] + [rng.uniform(-delta, delta) for _ in range(count)]
        initial = rng.uniform(-5, 5)
        err, bound = trial_perturbation(initial, drifts, W)
        assert err <= bound + 1e-10
        checks += 1

    # Root uniqueness is established analytically in RESULT.md;
    # numerical bisection here only reproduces the reported value.
    low, high = 0.1, 2.0
    g = lambda x: phi(x) - 2 * x * cdf_tail(x)
    assert g(low) > 0 > g(high)
    for _ in range(100):
        mid = (low + high) / 2
        if g(mid) > 0: low = mid
        else: high = mid
        checks += 1
    root = (low + high) / 2
    assert abs(root - 0.612003180962481) < 1e-12
    assert abs(rate(root) - 0.10122824509401235) < 1e-12
    assert abs((2*(1-cdf_tail(root))-1) - 0.4594643470245685) < 1e-12
    checks += 3

    # Finite-N computation of the stated original recursion (no surrogate update).
    theta = root
    for n in [100, 400, 1600, 6400]:
        H = sum(1.0/t for t in range(1,n))
        S = sum(1.0/math.sqrt(t) for t in range(1,n))
        epsilon = theta * math.sqrt(H)/S
        assert 0 < epsilon < 0.5
        assert abs(epsilon*S/math.sqrt(H) - theta) < 1e-12
        checks += 2
        samples=[]
        for _ in range(250):
            x=0.0
            for t in range(1,n):
                xi = rng.choice([-1,1])
                x -= (epsilon * sign(x) + (1-epsilon)*xi) / math.sqrt(t)
            samples.append(x / math.sqrt(H))
        assert all(math.isfinite(x) for x in samples)
        checks+=1
        print('N',n,'normalized mean |last iterate|',sum(abs(x) for x in samples)/len(samples))
    print('critical slope optimum', format(root,'.15f'))
    print('leading expectation coefficient', format(rate(root),'.15f'))
    print('limit atom mass',format(1-2*cdf_tail(root),'.15f'))
    print('PASS', checks, 'finite/algebraic checks')


if __name__=='__main__':
    check()
