"""Exact arithmetic diagnostics for a continuous expectile-order counterexample."""
from fractions import Fraction as Q

ALPHAS = (Q(1, 6), Q(1, 4), Q(1, 3))
J = (Q(0), Q(1), Q(2))
V = (Q(0), Q(1), Q(4))


def score(values, alpha, trial):
    return sum((alpha * max(value - trial, Q(0))
                - (1 - alpha) * max(trial - value, Q(0)))
               for value in values) / len(values)


u = [Q(3, 7), Q(3, 5), Q(3, 4)]
v = [Q(5, 7), Q(1), Q(6, 5)]
for levels, support in [(u, J), (v, V)]:
    for alpha, trial in zip(ALPHAS, levels):
        assert score(support, alpha, trial) == 0

assert (v[1] - v[0]) / (u[1] - u[0]) == Q(5, 3)
assert (v[2] - v[1]) / (u[2] - u[1]) == Q(4, 3)
D = (v[1] - v[0]) * (u[2] - u[1]) - (v[2] - v[1]) * (u[1] - u[0])
assert D == Q(3, 350)
eta = Q(1, 10**6)

assert u[1] - u[0] == Q(6, 35)
assert u[2] - u[1] == Q(3, 20)
assert v[1] - v[0] == Q(2, 7)
assert v[2] - v[1] == Q(1, 5)
assert min(u[1]-u[0], u[2]-u[1]) > 30 * eta
bound = 30 * eta * (Q(2, 7)+Q(1, 5)) + 120*eta*(Q(3, 20)+Q(6, 35)) + 7200*eta**2
assert bound == Q(372, 7)*eta + 7200*eta**2
assert D - bound > 0
assert max(max(a, 1-a) / min(a, 1-a) for a in ALPHAS) == 5
print('PASS: exact expectiles, two slopes, positive determinant and smoothing bounds')
print('certified determinant lower bound =', D-bound)
