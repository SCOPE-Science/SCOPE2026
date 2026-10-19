#!/usr/bin/env python3
"""Finite consistency checks for five-neighbor ring median pinning.

The analytical theorem is proved in RESULT.md; finite checks here are not
used as a substitute for its all-size or all-initial-state arguments.
"""
from __future__ import annotations

import math
import random


def neighbors(n, i):
    return {(i + d) % n for d in (-2, -1, 1, 2)}


def is_induced_forest(n, pinned):
    keep = set(range(n)) - set(pinned)
    visited = set()

    def dfs(v, parent):
        visited.add(v)
        for w in neighbors(n, v) & keep:
            if w == parent:
                continue
            if w in visited or not dfs(w, v):
                return False
        return True

    return all(v in visited or dfs(v, -1) for v in keep)


def has_safe_gaps(n, pinned):
    p = sorted(pinned)
    if not p:
        return False
    gaps = [(p[(j + 1) % len(p)] - p[j]) % n or n
            for j in range(len(p))]
    return max(gaps) <= 3 and min(gaps) == 1


def minimum_pins(n):
    return (n + 4) // 3


def predicted_optimal_count(n):
    p = minimum_pins(n)
    if n % 3 == 0:
        return n * (p - 1)
    if n % 3 == 1:
        return n
    return n * (p - 1) ** 2 // 2


def construct_optimal(n):
    p = minimum_pins(n)
    gaps = [1] + [3] * (p - 1)
    gaps[1] -= sum(gaps) - n
    assert all(1 <= g <= 3 for g in gaps) and 1 in gaps
    sites = [0]
    for gap in gaps[:-1]:
        sites.append((sites[-1] + gap) % n)
    return set(sites)


def rhs(t, x, pinned, target):
    n = len(x)
    return [(target - x[i]) if i in pinned else
            (sorted(x[(i + j) % n] for j in (-2, -1, 0, 1, 2))[2] - x[i])
            for i in range(n)]


def rk4(x, h, pinned, target):
    a = rhs(0.0, x, pinned, target)
    y = [q + h * k / 2 for q, k in zip(x, a)]
    b = rhs(0.0, y, pinned, target)
    y = [q + h * k / 2 for q, k in zip(x, b)]
    c = rhs(0.0, y, pinned, target)
    y = [q + h * k for q, k in zip(x, c)]
    d = rhs(0.0, y, pinned, target)
    return [q + h * (ka + 2 * kb + 2 * kc + kd) / 6
            for q, ka, kb, kc, kd in zip(x, a, b, c, d)]


def poisson_bound(t, m, r):
    return r * math.exp(-t) * sum(t ** j / math.factorial(j) for j in range(m + 1))


def main():
    tested = 0
    for n in range(5, 19):
        minimum = n
        opt_count = 0
        for mask in range(1 << n):
            pinned = {i for i in range(n) if mask & (1 << i)}
            forest = is_induced_forest(n, pinned)
            gap = has_safe_gaps(n, pinned)
            assert forest == gap, ('forest-gap', n, mask)
            if forest:
                s = len(pinned)
                if s < minimum:
                    minimum = s
                    opt_count = 1
                elif s == minimum:
                    opt_count += 1
            tested += 1
        assert minimum == minimum_pins(n), ('minimum', n)
        assert opt_count == predicted_optimal_count(n), ('count', n)
        assert is_induced_forest(n, construct_optimal(n))
    for n in range(19, 1001):
        p = construct_optimal(n)
        assert len(p) == minimum_pins(n)
        assert has_safe_gaps(n, p)
    rng = random.Random(58117)
    trajectories = 0
    for n in range(5, 13):
        for _ in range(6):
            pinned = construct_optimal(n)
            target = rng.uniform(-1, 1)
            x = [rng.uniform(-3, 3) for i in range(n)]
            radius = max(abs(v - target) for v in x)
            m = n - len(pinned)
            h = 0.025
            for step in range(1, 481):
                x = rk4(x, h, pinned, target)
                if step % 20 == 0:
                    t = step * h
                    err = max(abs(v - target) for v in x)
                    assert err <= poisson_bound(t, m, radius) + 4e-6, (n, t, err)
            trajectories += 1
    print('PASS: %d exact subset tests (orders 5..18); %d optimal constructions; %d RK4 trajectories.' %
          (tested, 1000 - 19 + 1, trajectories))
    print('Numerical trajectories are diagnostic only; proofs are independent of them.')


if __name__ == '__main__':
    main()
