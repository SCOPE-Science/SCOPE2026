#!/usr/bin/env python3
"""Exact finite checks for a weighted-path rearrangement energy theorem.

Run with: python CHECK.py
Only standard-library arithmetic is used. These tests are not an infinite proof.
"""
from fractions import Fraction as F
from itertools import combinations, product


def boundary(weights, subset):
    members = set(subset)
    return sum(weights[i] for i in range(len(weights))
               if ((i in members) != (i + 1 in members)))


def profile(weights):
    n = len(weights) + 1
    return [min(boundary(weights, s) for s in combinations(range(n), k))
            for k in range(1, n)]


def sharp_factor(weights):
    h = profile(weights)
    return max(v / c for v, c in zip(weights, h))


def central_weights(n, t):
    weights = [F(1) for _ in range(n - 1)]
    if n % 2 == 0:
        weights[n // 2 - 1] = t
    else:
        weights[n // 2 - 1] = t
        weights[n // 2] = t
    return weights


def predicted(n, t):
    if n % 2 == 0:
        return max(F(1), t / 2)
    return max(F(1), t / 2, 1 / (2 * t))


def energy(weights, data, phi):
    return sum(v * phi(abs(a - b)) for v, a, b in
               zip(weights, data, data[1:]))


def main():
    tests = 0
    ts = [F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(1),
          F(3, 2), F(2), F(5), F(20)]
    for n in range(4, 12):
        for t in ts:
            weights = central_weights(n, t)
            assert sharp_factor(weights) == predicted(n, t), (n, t)
            tests += 1
            h = profile(weights)
            m = n // 2
            if n % 2 == 0:
                assert all(c == F(1) for j, c in enumerate(h, 1) if j != m)
                assert h[m - 1] == min(t, F(2))
            else:
                assert h[0] == h[-1] == min(F(1), 2 * t)
                assert h[m - 1] == h[m] == min(t, F(2))
                assert all(c == F(1) for j, c in enumerate(h, 1)
                           if j not in (1, m, m + 1, n - 1))
            tests += 1
    phi_list = [lambda z: z, lambda z: z * z,
                lambda z: z ** 3, lambda z: z * z + z ** 4,
                lambda z: max(F(0), z - F(1)) ** 2]
    # Complete small-dimensional tests: all 0/1/2 assignments, all displayed
    # weights, several convex functions, each evaluated with exact rationals.
    for n in range(2, 7):
        for weights_tuple in product([F(1), F(2)], repeat=n - 1):
            weights = list(weights_tuple)
            sharp = sharp_factor(weights)
            h = profile(weights)
            assert sharp == max(weights[j] / h[j] for j in range(n - 1))
            tests += 1
            for data in product([F(0), F(1), F(2)], repeat=n):
                sorted_data = sorted(data)
                for phi in phi_list:
                    e = energy(weights, data, phi)
                    e_sorted = energy(weights, sorted_data, phi)
                    assert e_sorted <= sharp * e, (n, weights, data, sharp)
                    tests += 1
            # Every profile minimum is a two-level exact extremizer.
            for k in range(1, n):
                subset = next(s for s in combinations(range(n), k)
                              if boundary(weights, s) == h[k - 1])
                data = [F(0) if i in subset else F(2) for i in range(n)]
                assert energy(weights, sorted(data), lambda z: z * z) * h[k - 1] == \
                       energy(weights, data, lambda z: z * z) * weights[k - 1]
                tests += 1
    print(f'PASS: {tests} exact checks; central defect, cut profiles, convex energies, equality witnesses')


if __name__ == '__main__':
    main()
