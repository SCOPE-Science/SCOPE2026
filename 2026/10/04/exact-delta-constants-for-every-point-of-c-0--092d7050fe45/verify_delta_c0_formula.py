#!/usr/bin/env python3
"""Finite-coordinate checks for the exact Delta-constant formula on c0.

The proof in RESULT.md is analytic.  This script checks the constructive slice
functional, recovers the known equal-coordinate family, verifies a new exact
heterogeneous example, and runs deterministic numerical searches on sample
vectors.  It uses only the Python standard library.
"""
import math
import random


def phi(x, r):
    x = [abs(float(v)) for v in x]
    return sum((1.0 - s) / (r + 1.0 - s) for s in x if s > r - 1.0 + 1e-15)


def delta_formula(x):
    x = [abs(float(v)) for v in x if abs(float(v)) > 0]
    if not x:
        return 1.0
    lo, hi = 1.0, 1.0 + max(x)
    for _ in range(110):
        mid = (lo + hi) / 2.0
        if phi(x, mid) <= 1.0:
            hi = mid
        else:
            lo = mid
    # The active set can jump at r=1+|x_i|; include every jump explicitly.
    candidates = [1.0, hi] + [1.0 + s for s in x]
    feasible = [r for r in candidates if phi(x, r) <= 1.0 + 1e-12]
    return min(feasible)


def witness_weights(x, r):
    """Weights of the supporting functional from the upper-bound proof."""
    x = [abs(float(v)) for v in x]
    active = [i for i, s in enumerate(x) if s > r - 1.0 + 1e-12]
    if not active:
        return [0.0] * len(x), 1.0
    b = {i: 1.0 / (r + 1.0 - x[i]) for i in active}
    ph = sum(b[i] * (1.0 - x[i]) for i in active)
    q = 1.0 / (1.0 + sum(b[i] * x[i] for i in active))
    w = [0.0] * len(x)
    for i in active:
        w[i] = q * b[i]
    tail = q * (1.0 - ph)
    assert tail >= -2e-9
    assert abs(sum(w) + tail - 1.0) < 2e-8
    return w, max(0.0, tail)


def closed_cap_radius(x, w, tail):
    """Exact limiting radius of the closed cap defined by nonnegative weights."""
    x = [abs(float(v)) for v in x]
    c = sum(a * s for a, s in zip(w, x))
    assert abs(sum(w) + tail - 1.0) < 1e-7
    radius = 1.0  # an unused tail coordinate is always available in c0
    for a, s in zip(w, x):
        if a <= 1e-14:
            ymin = -1.0
        else:
            ymin = max(-1.0, (c - (1.0 - a)) / a)
        radius = max(radius, 1.0 - s, s - ymin)
    return radius


def random_simplex(m):
    z = [-math.log(max(1e-300, random.random())) for _ in range(m)]
    total = sum(z)
    return [v / total for v in z]


def direct_random_search(x, trials=25000):
    best = float("inf")
    for _ in range(trials):
        weights = random_simplex(len(x) + 1)
        radius = closed_cap_radius(x, weights[:-1], weights[-1])
        best = min(best, radius)
    return best


def main():
    random.seed(230710647)

    count = 0
    for n in range(1, 8):
        for j in range(11):
            t = j / 10.0
            got = delta_formula([t] * n)
            expected = min(1.0 + t, max(1.0, (1.0 - t) * (n - 1)))
            assert abs(got - expected) < 2e-8, (n, t, got, expected)
            count += 1
    print("equal-coordinate identities checked:", count)

    exact = [0.75, 0.25, 0.25]
    exact_value = (3.0 + math.sqrt(33.0)) / 8.0
    got = delta_formula(exact)
    assert abs(got - exact_value) < 2e-10, (got, exact_value)
    print("heterogeneous exact example:", f"{got:.12f}")

    # The infinite vector x_i=1/i has value 5/4: the fourth coordinate drops
    # from the active set exactly at r=5/4, while the pre-jump sum exceeds 1.
    prefix = [1.0 / i for i in range(1, 21)]
    got = delta_formula(prefix)
    assert abs(got - 1.25) < 2e-10, got
    print("harmonic-prefix threshold check:", f"{got:.12f}")

    examples = [
        [0.9, 0.9, 0.1],
        [0.8, 0.45, 0.2],
        [0.7, 0.7, 0.7, 0.15],
        [1.0, 0.6, 0.2],
        [0.75, 0.25, 0.15],
        [0.1, 0.7, 0.4, 0.15],
    ]
    for x in examples:
        r = delta_formula(x)
        w, tail = witness_weights(x, r)
        cap = closed_cap_radius(x, w, tail)
        assert cap <= r + 2e-7, (x, r, cap, w, tail)
        print("witness", x, "formula", f"{r:.12f}", "cap", f"{cap:.12f}")

    # Independent deterministic random search over positive slice functionals.
    # It is only a sanity check and is not used in the proof.
    for case in range(10):
        n = random.randint(2, 5)
        x = [random.randint(1, 19) / 20.0 for _ in range(n)]
        r = delta_formula(x)
        search = direct_random_search(x)
        assert search >= r - 5e-5, (x, r, search)
    print("deterministic stochastic sanity cases checked: 10")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
