#!/usr/bin/env python3
"""Verify exact rate formulas for a delayed two-coordinate randomized Gauss-Seidel model.

The delay law is a dictionary {delay: probability}.  The asymptotic mean-square
factor q is the unique root in (1/2,1) of

    2 q - 1 = r^2 sum_d p_d q^{-d},

and the scalar second-moment recurrence is

    S_{k+1} = (1/2) S_k + (r^2/2) sum_d p_d S_{k-d}.

Only the Python standard library is required.
"""

from math import isclose


def rate(r, probs, iters=200):
    assert 0.0 <= r < 1.0
    assert probs and all(isinstance(d, int) and d >= 0 for d in probs)
    assert all(p >= 0.0 for p in probs.values())
    assert isclose(sum(probs.values()), 1.0, rel_tol=0.0, abs_tol=1e-14)
    if r == 0.0:
        return 0.5

    def f(q):
        return 2.0 * q - 1.0 - r * r * sum(
            p * q ** (-d) for d, p in probs.items()
        )

    lo, hi = 0.5, 1.0
    for _ in range(iters):
        mid = (lo + hi) / 2.0
        if f(mid) > 0.0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


def recurrence_ratio(r, probs, steps=500):
    tau = max(probs)
    values = [1.0] * (tau + 1)  # S_{-tau},...,S_0
    for k in range(steps):
        idx = tau + k
        delayed = sum(p * values[idx - d] for d, p in probs.items())
        values.append(0.5 * values[idx] + 0.5 * r * r * delayed)
    return values[-1] / values[-2]


def main():
    r = 0.8
    cases = [
        ("no delay", {0: 1.0}),
        ("deterministic delay 1", {1: 1.0}),
        ("same-mean bursty delay {0,2}", {0: 0.5, 2: 0.5}),
        ("deterministic delay 2", {2: 1.0}),
    ]
    for name, probs in cases:
        q = rate(r, probs)
        ratio = recurrence_ratio(r, probs)
        assert abs(q - ratio) < 1e-11
        print(f"{name:31s} q = {q:.12f}")

    q1 = rate(r, {1: 1.0})
    assert abs(2.0*q1*q1 - q1 - r*r) < 1e-13

    # Same mean (=1): the more variable {0,2} law is slower than D=1.
    assert rate(r, {1: 1.0}) < rate(r, {0: 0.5, 2: 0.5})


if __name__ == "__main__":
    main()
