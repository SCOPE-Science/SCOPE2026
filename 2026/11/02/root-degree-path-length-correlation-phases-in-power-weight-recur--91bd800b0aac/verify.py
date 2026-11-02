"""Standalone exact finite checks for power-weight recursive-tree covariance laws.

Uses only the Python standard library. Finite checks are supplementary to
analytic proofs and do not certify the infinite asymptotic statements.
"""
from fractions import Fraction
from itertools import product
from math import factorial, isclose, pi, sqrt


def parameters(n, alpha):
    weights = [Fraction(k) ** alpha for k in range(1, n + 1)]
    total = Fraction(0)
    p = [Fraction(0)] * (n + 1)
    q = [Fraction(0)] * (n + 1)
    for j, w in enumerate(weights, 1):
        if j >= 2:
            q[j] = 1 / total
        total += w
        p[j] = w / total
    return weights, p, q


def moments_by_enumeration(n, weights):
    sums = [Fraction(0) for _ in range(6)]
    options = [range(1, j) for j in range(2, n + 1)]
    for parents in product(*options):
        depth = [0] * (n + 1)
        degree = 0
        total_depth = 0
        prob = Fraction(1)
        prefix = weights[0]
        for j, parent in enumerate(parents, 2):
            depth[j] = depth[parent] + 1
            total_depth += depth[j]
            degree += (parent == 1)
            prob *= weights[parent - 1] / prefix
            prefix += weights[j - 1]
        r = degree
        t = total_depth
        for i, value in enumerate((1, r, t, r * r, t * t, r * t)):
            sums[i] += prob * value
    return sums


def predicted_moments(n, p, q):
    running = Fraction(0)
    covariance = Fraction(0)
    for j in range(2, n + 1):
        covariance -= q[j] * running * (1 + (n - j) * p[j])
        running += p[j]
    var_r = sum((q[j] * (1 - q[j]) for j in range(2, n + 1)), Fraction(0))
    # Innovation variances: v_2=0,
    # v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j).
    v = [Fraction(0)] * (n + 1)
    for j in range(2, n):
        v[j + 1] = (1 - p[j] ** 2) * v[j] + p[j] * (1 - p[j])
    var_t = sum(((1 + (n - j) * p[j]) ** 2 * v[j]
                 for j in range(2, n + 1)), Fraction(0))
    return covariance, var_r, var_t


def run():
    checks = 0
    cases = 0
    for alpha in (-2, -1, 0, 1, 2):
        for n in range(2, 9):
            weights, p, q = parameters(n, alpha)
            z, er, et, er2, et2, ert = moments_by_enumeration(n, weights)
            cov, vr, vt = predicted_moments(n, p, q)
            assert z == 1
            assert ert - er * et == cov
            assert er2 - er * er == vr
            assert et2 - et * et == vt
            assert er == sum(q[2:n + 1])
            checks += 5
            cases += 1
    # The linear-weight asymptotic covariance coefficient is
    # 7 - 2*pi^2/3; its root-degree variance limit is twice this.
    n = 400000
    weights_dummy, p_dummy, q_dummy = parameters(2, 1)
    # Numerically compute only the deterministic coefficients, not trees.
    w = 0.0
    aa = 0.0
    asym_cov = 0.0
    asym_var = 0.0
    for j in range(1, n + 1):
        if j >= 2:
            q = 1.0 / w
            asym_cov += q * aa * (1.0 / n + (1 - j / n) * (2.0 / (j + 1)))
            asym_var += q * (1 - q)
        w += float(j)
        if j >= 2:
            aa += 2.0 / (j + 1)
    target = 7.0 - 2.0 * pi * pi / 3.0
    assert abs(asym_cov - target) < 0.00001
    assert abs(asym_var - 2 * target) < 0.00001
    checks += 2
    print(f"PASS: {checks} assertions in {cases} exhaustive rational models; "
          "two finite-size numerical convergence checks.")


if __name__ == "__main__":
    run()
