#!/usr/bin/env python3
import math
import random


def solve(a, G, g):
    n = len(a)
    order = sorted(range(n), key=lambda j: G[j] / a[j])
    rho = [G[j] / a[j] for j in order]
    A = 0.0
    B = g
    k = None
    for pos, j in enumerate(order):
        A += a[j]
        B += G[j]
        next_rho = rho[pos + 1] if pos + 1 < n else math.inf
        tau = B / A
        if tau <= next_rho + 1e-14:
            k = pos + 1
            break
    assert k is not None
    tau = B / A
    r = [1.0] * n
    tail = 0.0
    for pos, j in enumerate(order):
        if pos >= k:
            r[j] = math.sqrt((G[j] / a[j]) / tau)
            tail += math.sqrt(a[j] * G[j])
    exact = (math.sqrt(A * B) + tail) ** 2
    return order, k, tau, r, exact


def objective(a, G, g, r):
    return sum(x * y for x, y in zip(a, r)) * (g + sum(x / y for x, y in zip(G, r)))


def check_case(a, G, g):
    order, k, tau, r, exact = solve(a, G, g)
    rho = [G[j] / a[j] for j in order]
    left = rho[k - 1]
    right = rho[k] if k < len(rho) else math.inf
    assert left <= tau * (1 + 2e-12)
    assert tau <= right * (1 + 2e-12)
    for pos, j in enumerate(order):
        if pos < k:
            deriv = a[j] * (g + sum(G[q] / r[q] for q in range(len(a)))) - sum(a[q] * r[q] for q in range(len(a))) * G[j]
            assert deriv >= -1e-9 * max(1.0, exact)
            assert abs(r[j] - 1.0) < 1e-14
        else:
            assert r[j] >= 1.0 - 1e-13
            assert abs(r[j] * r[j] - (G[j] / a[j]) / tau) <= 1e-10 * max(1.0, r[j] * r[j])
    val = objective(a, G, g, r)
    assert abs(val - exact) <= 2e-10 * max(1.0, exact)
    rounded = [math.ceil(x - 1e-14) for x in r]
    rounded_val = objective(a, G, g, rounded)
    assert rounded_val <= 2.0 * exact * (1 + 1e-12)


def main():
    cases = [
        ([1.0], [1.0], 1.0),
        ([1.0, 1.0], [1.0, 16.0], 1.0),
        ([3.0, 2.0, 5.0], [1.0, 20.0, 7.0], 4.0),
        ([0.5, 4.0, 2.0, 7.0], [12.0, 1.0, 30.0, 3.0], 2.5),
    ]
    rng = random.Random(1729)
    for n in range(2, 9):
        for _ in range(50):
            a = [math.exp(rng.uniform(-2.5, 2.5)) for _ in range(n)]
            G = [math.exp(rng.uniform(-2.5, 2.5)) for _ in range(n)]
            g = math.exp(rng.uniform(-2.5, 2.5))
            cases.append((a, G, g))
    for a, G, g in cases:
        check_case(a, G, g)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
