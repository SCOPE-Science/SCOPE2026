"""Exact small-instance check for the seasonal root-cancellation matrix."""
from fractions import Fraction as F


def multiply(u, v):
    out = [F(0)] * (len(u) + len(v) - 1)
    for i, a in enumerate(u):
        for j, b in enumerate(v):
            out[i + j] += a * b
    return out


def evaluate(coeff, z):
    return sum((a * z ** i for i, a in enumerate(coeff)), F(0))


g1 = [F(3, 4), F(0), F(1, 4)]
g2 = [F(2, 3), F(0), F(1, 3)]
q = [-a for a in multiply(g1, g2)]
q[2] += F(1)
assert q == [F(-1, 2), F(0), F(7, 12), F(0), F(-1, 12)]
assert evaluate(q, F(1)) == evaluate(q, F(-1)) == 0
assert evaluate(q, F(2)) != 0
assert F(2) * g1[2] + F(2) * g2[2] == F(7, 6) < 2

root = F(-1)
a1, a2 = g1[0], g2[0]
matrix = [[a2, a1 * evaluate(g2, root) / root], [a2, a1]]
assert matrix == [[F(2, 3), F(-3, 4)], [F(2, 3), F(3, 4)]]
determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
assert determinant == F(1)
print("VERIFY_OK kernel_factorization=exact root=-1 determinant=1")
