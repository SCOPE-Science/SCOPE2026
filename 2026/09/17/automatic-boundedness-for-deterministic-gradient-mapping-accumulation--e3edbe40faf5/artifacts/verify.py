#!/usr/bin/env python3
"""Compact numerical checks for the deterministic smooth boundedness lemma.

This script is diagnostic only.  It tests the one-step convex inequality on
random scalar quadratic + l1 composite problems and simulates the gradient-
mapping accumulation rule.  The theorem itself is proved analytically.
"""
from __future__ import annotations
import math
import random

RNG = random.Random(20260917)


def soft(z: float, t: float) -> float:
    if z > t:
        return z - t
    if z < -t:
        return z + t
    return 0.0


def objective(x: float, q: float, b: float, lam: float) -> float:
    return 0.5 * q * x * x + b * x + lam * abs(x)


def minimizer(q: float, b: float, lam: float) -> float:
    # q>0; exact minimizer of 0.5*q*x^2+b*x+lam*|x|
    return soft(-b / q, lam / q)


def check_one_step(trials: int = 10000) -> float:
    worst = -math.inf
    for _ in range(trials):
        q = 10 ** RNG.uniform(-3, 3)
        b = RNG.uniform(-5, 5)
        lam = 10 ** RNG.uniform(-3, 2)
        xstar = minimizer(q, b, lam)
        x = RNG.uniform(-20, 20)
        alpha = 10 ** RNG.uniform(-3, 3) / q
        xp = soft(x - alpha * (q * x + b), alpha * lam)
        d = xp - x
        lhs = (xp - xstar) ** 2 - (x - xstar) ** 2
        rhs = (alpha * q / 2.0 - 1.0) * d * d
        err = lhs - rhs
        worst = max(worst, err)
        tol = 1e-9 * (1.0 + abs(lhs) + abs(rhs))
        if err > tol:
            raise AssertionError((q, b, lam, x, alpha, lhs, rhs, err))
    return worst


def simulate(trials: int = 200, steps: int = 2000) -> tuple[float, float]:
    max_step_seen = 0.0
    max_dist_seen = 0.0
    for _ in range(trials):
        q = 10 ** RNG.uniform(-2, 2)
        b = RNG.uniform(-3, 3)
        lam = 10 ** RNG.uniform(-3, 1)
        eta = 10 ** RNG.uniform(-2, 2)
        gamma = 10 ** RNG.uniform(-2, 2)
        xstar = minimizer(q, b, lam)
        x = RNG.uniform(-10, 10)
        S = gamma
        for _ in range(steps):
            alpha = eta / S
            xp = soft(x - alpha * (q * x + b), alpha * lam)
            d = xp - x
            S = S * math.sqrt(1.0 + (d / eta) ** 2)
            x = xp
            max_step_seen = max(max_step_seen, abs(d))
            max_dist_seen = max(max_dist_seen, abs(x - xstar))
            if not (math.isfinite(x) and math.isfinite(S)):
                raise AssertionError("non-finite iterate")
    return max_step_seen, max_dist_seen


if __name__ == "__main__":
    worst = check_one_step()
    ms, md = simulate()
    print("one-step inequality: PASS (10000 randomized scalar quadratic+l1 tests)")
    print(f"max(lhs-rhs) = {worst:.6e}")
    print("accumulator simulation: PASS (200 problems x 2000 steps)")
    print(f"largest finite step observed = {ms:.6e}")
    print(f"largest finite optimizer distance observed = {md:.6e}")
