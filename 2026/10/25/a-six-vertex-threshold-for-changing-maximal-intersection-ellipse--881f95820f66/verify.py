"""Exact rational verification of John/Löwner contact certificates.

Run with Python 3, no third-party packages.  This checks only finite
rational identities; the geometric deductions are proved separately.
"""
from fractions import Fraction as F
from itertools import combinations, product


def outer(a, b):
    return [[a[i] * b[j] for j in range(2)] for i in range(2)]


def weighted_moment(points, weights):
    return [[sum(weights[k] * points[k][i] * points[k][j]
                 for k in range(len(points))) for j in range(2)]
            for i in range(2)]


def quadratic(q, v):
    return sum(v[i] * q[i][j] * v[j] for i in range(2) for j in range(2))


strips = [(F(1), F(0), F(1)), (F(3), F(4), F(5)),
          (F(-5), F(12), F(13))]
normals = [(F(1), F(0)), (F(3, 5), F(4, 5)),
           (F(-5, 13), F(12, 13))]
weights_j = [F(11, 16), F(125, 224), F(169, 224)]
vertices = [(F(1), F(1, 2)), (F(-1), F(2, 3)),
            (F(1, 7), F(8, 7))]
Q0 = [[F(49, 65), F(4, 65)], [F(4, 65), F(48, 65)]]
weights_l = [F(6929, 12264), F(12375, 16352), F(4753, 7008)]
Q0_inv = [[F(195, 146), -F(65, 584)],
          [-F(65, 584), F(3185, 2336)]]

# All six half-planes contain the unit disk; equality at the normal contacts.
assert all(x*x + y*y == 1 for x, y in normals)
assert all(w > 0 for w in weights_j)
assert sum(weights_j) == 2
assert weighted_moment(normals, weights_j) == [[F(1), F(0)], [F(0), F(1)]]

# All three opposite vertex pairs are feasible and have two active boundaries.
for vertex in vertices:
    values = [(a*vertex[0] + b*vertex[1])/c for a, b, c in strips]
    assert max(map(abs, values)) == 1
    assert sum(abs(t) == 1 for t in values) == 2
    assert quadratic(Q0, vertex) == 1

# Exhaustively derive the six distinct vertices from all strip-line crossings.
all_verts = set()
for (a, b, c), (d, e, f) in combinations(strips, 2):
    determinant = a*e-b*d
    assert determinant != 0
    for s, t in product((-1, 1), repeat=2):
        x = (s*c*e-b*t*f)/determinant
        y = (a*t*f-s*c*d)/determinant
        if all(abs(g*x+h*y) <= r for g, h, r in strips):
            all_verts.add((x, y))
assert all_verts == set(vertices + [(-x, -y) for x, y in vertices])

# Positive symmetric contacts certify the unique Löwner ellipsoid.
assert Q0[0][0] > 0
assert Q0[0][0]*Q0[1][1] - Q0[0][1]*Q0[1][0] == F(2336, 4225)
assert all(w > 0 for w in weights_l)
assert sum(weights_l) == 2
assert weighted_moment(vertices, weights_l) == Q0_inv
assert [[sum(Q0[i][k]*Q0_inv[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)] == [[F(1), F(0)], [F(0), F(1)]]

# After (x,y)->(2x,y), the endpoint quadratic forms fail to commute.
QJ = [[F(1, 4), F(0)], [F(0), F(1)]]
QL = [[F(49, 260), F(2, 65)], [F(2, 65), F(48, 65)]]
assert (QJ[0][0]-QJ[1][1])*QL[0][1] == -F(3, 130)
assert sum(QJ[0][k]*QL[k][1]-QL[0][k]*QJ[k][1]
           for k in range(2)) == -F(3, 130)
print('PASS: six vertices, both positive contact certificates, nonzero commutator')
