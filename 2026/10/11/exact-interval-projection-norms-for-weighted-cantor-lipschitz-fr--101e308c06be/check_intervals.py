"""Finite-cube linear-program crosschecks of all interval projection norms.

Each finite-dimensional dual linear program maximizes the image of a
molecule under a coordinate-block truncation difference. The computed
operator norms are compared with the closed formula for every interval.
"""
import itertools
import numpy as np
from scipy.optimize import linprog


def verify(weights):
    d = len(weights)
    points = list(itertools.product((0, 1), repeat=d))
    index = {p: i for i, p in enumerate(points)}
    num = len(points)
    dist = np.zeros((num, num))
    for i, p in enumerate(points):
        for j, q in enumerate(points):
            dist[i, j] = sum(w for w, a, b in zip(weights, p, q) if a != b)
    constraints = []
    rhs = []
    for i in range(num):
        for j in range(i):
            a = np.zeros(num)
            a[i], a[j] = 1, -1
            constraints.extend((a, -a))
            rhs.extend((dist[i, j], dist[i, j]))
    constraints = np.asarray(constraints)
    rhs = np.asarray(rhs)
    errors = []
    for n in range(d):
        for m in range(n + 1, d + 1):
            best = 0.0
            for i, p in enumerate(points):
                for j in range(i):
                    q = points[j]
                    coeff = np.zeros(num)
                    for sign, x in ((1, p), (-1, q)):
                        at_m = x[:m] + (0,) * (d-m)
                        at_n = x[:n] + (0,) * (d-n)
                        coeff[index[at_m]] += sign
                        coeff[index[at_n]] -= sign
                    sol = linprog(-coeff, A_ub=constraints, b_ub=rhs,
                                  A_eq=np.eye(1, num, 0), b_eq=np.array([0.]),
                                  bounds=[(None, None)] * num, method='highs')
                    assert sol.success, (weights, n, m, p, q, sol.message)
                    value = -sol.fun / dist[i, j]
                    best = max(best, value)
            W = sum(weights[n:m])
            expected = 1.0 if n == 0 else max(1.0, 2.0 * min(1.0, W / min(weights[:n])))
            err = abs(best - expected)
            assert err < 1.0e-8, (weights, n, m, best, expected)
            errors.append(err)
            print(f"weights={weights}, interval=({n},{m}], dual_LP_norm={best:.12g}, formula={expected:.12g}, error={err:.2g}")
    return len(errors), max(errors)


def main():
    suites = [
        [0.5, 0.25, 0.125],
        [1.0, 0.25, 1.0 / 9.0],
        [0.125, 0.75, 0.25],
        [0.1, 0.3, 0.05, 0.2],
        [0.5, 0.25, 0.125, 0.0625],
        [1.0, 0.25, 1.0 / 9.0, 1.0 / 16.0],
    ]
    tests, worst = 0, 0.0
    for weights in suites:
        number, error = verify(weights)
        tests += number
        worst = max(worst, error)
    print(f"ALL {tests} interval projection checks in {len(suites)} finite weighted cubes PASS; max discrepancy={worst:.3g}")


if __name__ == '__main__':
    main()
