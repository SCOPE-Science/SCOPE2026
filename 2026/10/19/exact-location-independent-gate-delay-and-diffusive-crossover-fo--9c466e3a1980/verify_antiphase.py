"""Finite-state verification of the alternating-endpoint escape theorem.

Use: python3 verify_antiphase.py
Only Python's standard library is required.
"""
from fractions import Fraction
from math import acosh, cosh, sinh, tanh, sqrt, isclose


def exact_formula(n, rate):
    h_prev, h_cur = Fraction(0), Fraction(1)
    for _ in range(1, n):
        h_prev, h_cur = h_cur, 2 * (1 + rate) * h_cur - h_prev
    c = Fraction((n + 1), 2) * h_cur / ((1 + 2 * rate) * h_cur + 1 - h_prev)
    return [Fraction(i * (n - i), 2) + c for i in range(n + 1)]


def solve_linear(mat, b):
    n = len(b)
    a = [row[:] + [b[i]] for i, row in enumerate(mat)]
    for col in range(n):
        pivot = next((j for j in range(col, n) if a[j][col]), None)
        assert pivot is not None
        a[col], a[pivot] = a[pivot], a[col]
        lead = a[col][col]
        a[col] = [v / lead for v in a[col]]
        for row in range(n):
            if row != col:
                multiplier = a[row][col]
                if multiplier:
                    a[row] = [a[row][j] - multiplier * a[col][j] for j in range(n + 1)]
    return [a[i][-1] for i in range(n)]


def exact_generator(n, rate):
    states = [(i, g) for i in range(n + 1) for g in range(2)
              if not ((i == 0 and g == 0) or (i == n and g == 1))]
    indices = {s: k for k, s in enumerate(states)}
    dim = len(states)
    a = [[Fraction(0) for _ in range(dim)] for _ in range(dim)]
    for (i, g), row in indices.items():
        transitions = [(i, 1 - g, rate)] + [(j, g, Fraction(1))
                                               for j in (i - 1, i + 1) if 0 <= j <= n]
        for ii, gg, r in transitions:
            a[row][row] += r
            if (ii, gg) in indices:
                a[row][indices[(ii, gg)]] -= r
    solved = solve_linear(a, [Fraction(1)] * dim)
    return [sum((solved[indices[(i, g)]] if (i, g) in indices else Fraction(0))
                 for g in range(2)) / 2 for i in range(n + 1)]


def c_hyperbolic(n, rate):
    theta = acosh(1 + rate)
    return (n + 1) / (2 * (rate + sinh(theta) / tanh(n * theta / 2)))


comparison_count = 0
for n in range(1, 14):
    for rate in (Fraction(1, 7), Fraction(1, 2), Fraction(1), Fraction(5, 2), Fraction(4)):
        left = exact_generator(n, rate)
        right = exact_formula(n, rate)
        assert left == right, (n, rate, left, right)
        comparison_count += n + 1
        assert isclose(float(right[0]), c_hyperbolic(n, float(rate)), rel_tol=2e-12)

# Diffusive crossover is a limit, so these are consistency checks, not a proof.
scaling_checks = 0
for c in (0.1, 1.0, 10.0):
    limit = tanh(sqrt(c / 2)) / (2 * sqrt(2 * c))
    errors = [abs(c_hyperbolic(n, c / n**2) / n**2 - limit) for n in (40, 80, 160)]
    assert errors[2] < errors[1] < errors[0]
    assert errors[2] < 0.003
    scaling_checks += 3

monotonic_checks = 0
for n in (1, 2, 3, 8, 21, 100):
    vals = [c_hyperbolic(n, r) for r in (0.001, 0.01, 0.1, 1, 10)]
    assert all(vals[i] > vals[i + 1] for i in range(4))
    monotonic_checks += 4

print(f"CHECK_OK exact_source_state_comparisons={comparison_count} "
      f"diffusive_checks={scaling_checks} monotonic_checks={monotonic_checks}")
