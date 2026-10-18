#!/usr/bin/env python3
"""Independent finite linear programs for weighted-cube Walsh star projections.

Requires numpy and scipy. This is a finite check; the accompanying proof establishes
all dimensions and all positive real weights.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linprog


def value(m, w):
    return max(1.0, sum(math.comb(m, k) * abs(m - 2*k) * min(abs(m - 2*k), w)
                        for k in range(m + 1)) / (2**m * w))


def verify(m, w):
    n = m + 1
    vertices = list(itertools.product((-1, 1), repeat=n))
    pos = {v: i for i, v in enumerate(vertices)}
    N = len(vertices)
    chosen = [(0, j) for j in range(1, n)]
    # Fourier projection matrix, computed from characters, not from claimed value.
    chi = np.array([[v[0] * v[j] for j in range(1, n)] for v in vertices], dtype=float)
    Q = chi @ chi.T / N
    upper = []
    rhs = []
    lengths = [w] + [1.0] * m
    for a, v in enumerate(vertices):
        for j in range(n):
            flipped = list(v)
            flipped[j] *= -1
            b = pos[tuple(flipped)]
            if a < b:
                row = np.zeros(N)
                row[a] = 1.0
                row[b] = -1.0
                upper.extend([row, -row])
                rhs.extend([lengths[j], lengths[j]])
    origin = pos[(1,) * n]
    measured = []
    # Coordinate permutation on the last m coordinates makes these two
    # representative directions sufficient; flips and translations fix norms.
    for j in (0, 1):
        flipped = [1] * n
        flipped[j] = -1
        target = (Q[origin, :] - Q[pos[tuple(flipped)], :]) / lengths[j]
        sol = linprog(-target, A_ub=np.array(upper), b_ub=np.array(rhs),
                      A_eq=np.eye(N)[0:1], b_eq=[0.0],
                      bounds=[(None, None)] * N, method="highs")
        if not sol.success:
            raise RuntimeError(f"LP failed: {sol.message}")
        measured.append(-float(sol.fun))
    answer = value(m, w)
    assert abs(max(measured) - answer) < 2e-8, (m, w, measured, answer)
    return measured, answer


def main():
    instances = 0
    for m in (2, 3, 4, 5):
        for w in (0.5, 1.0, 1.5, 2.5, float(m), float(m) + 1.0):
            g, sharp = verify(m, w)
            print(f"m={m}, w={w:g}: edge-LP norms={g[0]:.9g},{g[1]:.9g}; formula={sharp:.9g}")
            instances += 1
    print(f"PASS: {instances} full primal edge-LP instances (two directions each)")


if __name__ == "__main__":
    main()
