#!/usr/bin/env python3
"""Reproducible sanity checks for the exact sparse-control gap formula."""
from math import exp, isclose


def exact_gap(a, c, lam, eps):
    vals = [eps * (2 * ci - lam) / (2 * ai + lam)
            for ai, ci in zip(a, c) if 2 * ai + lam > 0]
    return min(vals) if vals else None


def trigger_gap(a, c, lam, eps, weights):
    alphas = [(2 * ci - lam) * eps for ci in c]
    betas = [2 * ai + lam for ai in a]
    if not any(p > 0 and b > 0 for p, b in zip(weights, betas)):
        return None
    dstar = exact_gap(a, c, lam, eps)

    def g(d):
        return sum(p * exp(-alpha + beta * d)
                   for p, alpha, beta in zip(weights, alphas, betas))

    lo = dstar
    hi = max(2 * dstar, 1e-12)
    while g(hi) < 1:
        hi *= 2
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(mid) >= 1:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def main():
    a = [1.0, 0.0, -1.0]
    c = [2.0, 1.0, 3.0]
    lam = 0.5
    eps = 0.2
    dstar = exact_gap(a, c, lam, eps)
    assert isclose(dstar, 0.28, rel_tol=1e-12, abs_tol=1e-12)

    pure = trigger_gap(a, c, lam, eps, [1.0, 0.0, 0.0])
    mixed = trigger_gap(a, c, lam, eps, [0.5, 0.5, 0.0])
    stable_only = trigger_gap(a, c, lam, eps, [0.0, 0.0, 1.0])
    assert pure is not None and isclose(pure, dstar, rel_tol=1e-10, abs_tol=1e-10)
    assert mixed is not None and mixed > dstar
    assert stable_only is None

    amax = max(a)
    cmin = min(c)
    mu = 2 * abs(amax)
    tau_generic = (2 * cmin - lam) * eps / (2 * (mu + lam))
    assert dstar >= 2 * tau_generic

    no_trigger = exact_gap([-1.0, -0.5], [1.0, 2.0], 0.5, eps)
    assert no_trigger is None
    print("PASS: pure mode attains d* =", dstar)
    print("PASS: mixed state gap =", mixed, "> d*")
    print("PASS: stable-only support has no finite trigger")
    print("PASS: exact gap >= twice generic bound (tau =", tau_generic, ")")
    print("PASS: empty trigger-capable set gives no finite gap")


if __name__ == "__main__":
    main()
