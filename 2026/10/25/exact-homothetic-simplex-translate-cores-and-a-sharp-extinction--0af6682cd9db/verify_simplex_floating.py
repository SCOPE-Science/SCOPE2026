"""Separate LP checks for the exact high-mass translated-simplex core.

Each translation is represented by a real facet-threshold vector a with
sum a_i = 1-s. Overlap at least beta is equivalent to
sum max(0,a_i) <= 1-beta**(1/d). The LP computes each largest a_j.
This numerical checker is ancillary to the unrestricted-dimensional proof.
"""
from fractions import Fraction
from scipy.optimize import linprog


def highest_threshold(d, s, beta, j):
    h = 1 - float(beta) ** (1 / d)
    num = d + 1
    # Variables a_0,...,a_d, t_0,...,t_d; t_i >= a_i, t_i >= 0.
    objective = [0.] * (2 * num)
    objective[j] = -1.
    rows, bounds = [], []
    for i in range(num):
        row = [0.] * (2 * num)
        row[i], row[num + i] = 1., -1.
        rows.append(row); bounds.append(0.)
    rows.append([0.] * num + [1.] * num)
    bounds.append(h)
    return linprog(objective, A_ub=rows, b_ub=bounds,
                   A_eq=[[1.] * num + [0.] * num],
                   b_eq=[1-float(s)],
                   bounds=[(None, None)] * num + [(0, None)] * num,
                   method='highs')

count = 0
for d in range(2, 7):
    for s in [Fraction(1, 3), Fraction(3, 5), Fraction(3, 4),
              Fraction(9, 10), Fraction(1), Fraction(5, 4), Fraction(2)]:
        cap = min(s, 1) ** d
        for ratio in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]:
            beta = cap * ratio
            h = 1 - float(beta) ** (1 / d)
            for j in range(d + 1):
                answer = highest_threshold(d, s, beta, j)
                assert answer.success, (d, s, beta, j, answer.message)
                assert abs(-answer.fun - h) < 5e-8, (d, s, beta, j, -answer.fun, h)
                count += 1
print('PASS', count, 'separate LP extreme-threshold checks; dimension 2..6')
