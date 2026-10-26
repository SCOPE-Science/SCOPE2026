#!/usr/bin/env python3
"""Exact rational checks for the two-qutrit APPT purity-gap bound."""
from fractions import Fraction as Q

d = 9
vertices = []
for i in range(d - 2, d + 1):
    vertices.append((f"type1-{i}", [Q(1, i)] * i + [Q(0)] * (d - i)))
for i in range(1, d - 2):
    vertices.append((
        f"type2-{i}",
        [Q(2, d - 1 + i)] * i + [Q(1, d - 1 + i)] * (d - 1 - i) + [Q(0)]
    ))
for i in range(1, d - 2):
    vertices.append((
        f"type3-{i}",
        [Q(3, d + 2 * i)] * i + [Q(1, d + 2 * i)] * (d - i)
    ))

def dot(x, y):
    return sum(a * b for a, b in zip(x, y))

def purity(x):
    return dot(x, x)

def distance_squared(x, y):
    return sum((a - b) ** 2 for a, b in zip(x, y))

star = [Q(3, 13), Q(3, 13)] + [Q(1, 13)] * 7
assert len(vertices) == 15
assert sum(star) == 1
assert star in [v for _, v in vertices]

ordered = sorted(((purity(v), name, v) for name, v in vertices), reverse=True)
F_star = Q(25, 169)
gamma = Q(16, 12675)
q0 = Q(16, 845)
D2 = Q(58, 1183)
t_star = Q(784, 2175)
gap = Q(12544, 27568125)
upper = Q(312737, 2120625)

assert ordered[0][0] == F_star and ordered[0][1] == "type3-2"
assert ordered[1][0] == Q(11, 75) and ordered[1][1] == "type3-3"
assert F_star - ordered[1][0] == gamma
other = [(name, v) for name, v in vertices if v != star]
q_values = [2 * dot(star, [a - b for a, b in zip(star, v)]) for _, v in other]
d2_values = [distance_squared(star, v) for _, v in other]
assert min(q_values) == q0
assert max(d2_values) == D2
assert t_star == (q0 - gamma) / D2
assert gap == gamma * t_star
assert upper == F_star - gap

# The first Hildebrand matrix at star is 1/13 times
# [[2,-2,-2],[-2,2,0],[-2,0,2]], whose eigenvalues are
# 2, 2+2*sqrt(2), 2-2*sqrt(2). Its least eigenvalue is negative.
M = [[2, -2, -2], [-2, 2, 0], [-2, 0, 2]]
trace = sum(M[i][i] for i in range(3))
sum_principal_minors = (
    M[0][0] * M[1][1] - M[0][1] ** 2
    + M[0][0] * M[2][2] - M[0][2] ** 2
    + M[1][1] * M[2][2] - M[1][2] ** 2
)
det = (
    M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
    - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
    + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
)
assert (trace, sum_principal_minors, det) == (6, 4, -8)

# t0 = 7*(sqrt(2)-1)/sqrt(406). Exact rational comparisons:
# sqrt(2) > 7/5, sqrt(406) < 21 imply t0 > 2/15.
# sqrt(2) < 3/2, sqrt(406) > 20 imply t0 < 7/40 < 1/3.
assert Q(2, 15) < Q(7, 40) < Q(1, 3) < t_star < Q(1, 2)
# q0*t0 - D2*t0^2 > q0*(2/15) - 1/676 > gamma/2 > gamma*t_star.
lower_endpoint = q0 * Q(2, 15) - Q(1, 676)
assert lower_endpoint > Q(8, 12675)
assert Q(8, 12675) > gamma * t_star
assert Q(24, 12675) > Q(1, 676)

print("PASS: 15 exact vertices; unique outer maximizer and second vertex checked.")
print("PASS: gamma, q0, D^2, t*, gap, and final purity bound checked exactly.")
print("PASS: Hildebrand-matrix characteristic data and endpoint inequalities checked.")
print(f"Outer maximum: {F_star}; rational gap: {gap}; APPT upper bound: {upper}.")
