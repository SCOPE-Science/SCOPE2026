"""Exact cubical-chain verification for unordered two-point configurations of K4.

Requires Python 3 and sympy. All calculations are over the integers.
"""
from itertools import combinations, permutations
from sympy import Matrix, zeros, ones

V = tuple(range(4))
E = tuple(combinations(V, 2))
C0 = tuple(combinations(V, 2))
C1 = tuple((e, v) for e in E for v in V if v not in e)
C2 = tuple((e, f) for e, f in combinations(E, 2) if set(e).isdisjoint(f))
i0 = {a: j for j, a in enumerate(C0)}
i1 = {a: j for j, a in enumerate(C1)}
d1 = zeros(6, 12)
d2 = zeros(12, 3)
for j, ((a, b), v) in enumerate(C1):
    d1[i0[tuple(sorted((b, v)))], j] += 1
    d1[i0[tuple(sorted((a, v)))], j] -= 1
for j, ((a, b), (c, d)) in enumerate(C2):
    for sign, cell in [(1, ((c, d), b)), (-1, ((c, d), a)),
                       (-1, ((a, b), d)), (1, ((a, b), c))]:
        d2[i1[cell], j] += sign

def move(x, y):
    common = set(x) & set(y)
    assert len(common) == 1
    a = next(iter(set(x) - common))
    b = next(iter(set(y) - common))
    v = next(iter(common))
    return i1[(tuple(sorted((a, b))), v)], (1 if a < b else -1)

F = zeros(12, 4)
Y = zeros(12, 4)
for i in V:
    tri = [x for x in V if x != i]
    for a, b in zip(tri, tri[1:] + tri[:1]):
        F[i1[(tuple(sorted((a, b))), i)], i] += (-1)**i * (1 if a < b else -1)
    a, b, c = tri
    path = [(a, b), (i, b), (c, b), (i, c), (a, c), (i, a), (a, b)]
    for x, y in zip(path, path[1:]):
        j, sign = move(x, y)
        Y[j, i] += sign
assert d1 * d2 == zeros(6, 3)
assert d1 * F == zeros(6, 4)
assert d1 * Y == zeros(6, 4)
assert d1.rank() == 5 and d2.rank() == 3

# A spanning tree on the six unordered vertex-pair configurations.
parent = list(range(6))
tree = []
def root(j):
    while parent[j] != j:
        j = parent[j]
    return j
for j, ((a, b), v) in enumerate(C1):
    x = i0[tuple(sorted((a, v)))]
    y = i0[tuple(sorted((b, v)))]
    rx, ry = root(x), root(y)
    if rx != ry:
        parent[rx] = ry
        tree.append(j)
non = [j for j in range(12) if j not in tree]
assert tree == [0, 1, 2, 3, 4]
assert non == [5, 6, 7, 8, 9, 10, 11]
# Non-tree edge coefficients are integral coordinates on ker d1.
face_det = d2.row_join(F)[non, :].det()
assert face_det == 2
basis_det = d2.row_join(F[:, :3]).row_join(Y[:, 0])[non, :].det()
assert basis_det == -1
# Explicit signed square boundary: 2Y_0 + F_0+...+F_3.
assert 2*Y[:, 0] + F*ones(4, 1) == d2*Matrix([-1, 1, -1])
for i in V:
    rhs = 2*((-1)**i)*Y[:, i] + F*ones(4, 1)
    assert (d2.row_join(rhs)).rank() == 3

for perm in permutations(V):
    sign = (-1)**sum(perm[i] > perm[j] for i in V for j in V if i < j)
    action = zeros(12, 12)
    for j, ((a, b), v) in enumerate(C1):
        pa, pb = perm[a], perm[b]
        action[i1[(tuple(sorted((pa, pb))), perm[v])], j] += (1 if pa < pb else -1)
    for i in V:
        assert action * F[:, i] == sign * F[:, perm[i]]
    assert (d2.row_join(action * Y[:, 0] - sign * Y[:, 0])).rank() == 3
print('PASS: cells (6,12,3), ranks (5,3), face index 2, unimodular determinant -1')
print('PASS: integral face/Y relation and all 24 exact signed permutation actions')
