"""Finite exact-rational tests of comb-ultrametric basis norm formulas.

Requires Python 3.11 or newer. The optional independent LP checks require
SciPy 1.11+ (any compatible HiGHS-backed release).
This executable checks finite cases; the proof covers arbitrary lengths.
"""
from fractions import Fraction
from itertools import product
from random import Random


def flow_norm(a, c):
    """Tree-transport norm of sum c[j] (delta_j-delta_(j-1))."""
    n = len(a)
    assert len(c) == n + 1 and c[0] == 0
    return (
        sum(a[i] * abs(c[i] - c[i + 1]) for i in range(n))
        + a[-1] * abs(c[n])
        + sum((a[i] - a[i + 1]) * abs(c[i + 1]) for i in range(n - 1))
    ) / 2


def formula_suppression(a):
    return max(sum(a[l::2]) / a[l] for l in range(len(a)))


def formula_sign(a):
    return 1 + max(sum(a[l + 1 :]) / a[l] for l in range(len(a)))


def norm_on_molecules(a, multipliers):
    n = len(a)
    best = Fraction(0)
    for l in range(n):
        for k in range(l + 1, n + 1):
            c = [0] * (n + 1)
            for j in range(l + 1, k + 1):
                c[j] = multipliers[j - 1]
            best = max(best, flow_norm(a, c) / a[l])
    return best


def independent_lipschitz_lp(a, c):
    """Independent floating point LP check of the leaf Lipschitz dual."""
    from scipy.optimize import linprog
    n = len(a)
    rows, bounds = [], []
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            row = [0.0] * n
            if i:
                row[i - 1] += 1.0
            row[j - 1] -= 1.0
            rows.extend((row, [-v for v in row]))
            bounds.extend((float(a[i]), float(a[i])))
    objective = [float(c[j] - (c[j + 1] if j < n else 0)) for j in range(1, n + 1)]
    result = linprog([-v for v in objective], A_ub=rows, b_ub=bounds,
                     bounds=[(None, None)] * n, method="highs")
    assert result.success, result.message
    return -result.fun


def main():
    rng = Random(41753)
    count = 0
    lp_tests = 0
    for n in range(1, 6):
        for _ in range(3):
            a = [Fraction(v, 97) for v in sorted(rng.sample(range(1, 90), n), reverse=True)]
            measured_s = max(norm_on_molecules(a, mask)
                             for mask in product((0, 1), repeat=n))
            measured_u = max(norm_on_molecules(a, mask)
                             for mask in product((-1, 1), repeat=n))
            assert measured_s == formula_suppression(a), (n, a, measured_s)
            assert measured_u == formula_sign(a), (n, a, measured_u)
            count += 1
            for _ in range(4):
                c = [0] + [rng.choice((-1, 0, 1)) for _ in range(n)]
                predicted = flow_norm(a, c)
                actual = independent_lipschitz_lp(a, c)
                assert abs(float(predicted) - actual) < 1e-8, (a, c, predicted, actual)
                lp_tests += 1
    print("COMB_ULTRAMETRIC_VERIFIED", "cases", count, "LP", lp_tests)


if __name__ == "__main__":
    main()
