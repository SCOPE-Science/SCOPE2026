"""Exact rational certificate for a four-point Lipschitz-free numerical index.

Run: python3 artifacts/verify.py
Only Python's standard library is required.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations
from pathlib import Path
import json

M = 4
N = M - 1
D = [[Q(0) if i == j else (Q(1, 2) if {i, j} == {0, 1} else Q(1))
      for j in range(M)] for i in range(M)]


def determinant(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def solve3(a, b):
    den = determinant(a)
    if den == 0:
        return None
    return tuple(determinant([[b[r] if k == col else a[r][k] for k in range(3)]
                               for r in range(3)]) / den for col in range(3))


constraints = []
for i, j in permutations(range(M), 2):
    constraints.append((tuple(Q((i == k) - (j == k)) for k in range(N)), D[i][j]))

vertices = set()
for indices in combinations(range(len(constraints)), N):
    u = solve3([constraints[k][0] for k in indices],
               [constraints[k][1] for k in indices])
    if u is not None and all(sum(x * y for x, y in zip(a, u)) <= bound
                             for a, bound in constraints):
        vertices.add(u)
vertices = sorted(vertices)
assert len(vertices) == 18


def evaluate(f, i, j):
    return (f[i] if i < N else Q(0)) - (f[j] if j < N else Q(0))


def tensor(i, j, f):
    mol = tuple(Q((i == k) - (j == k)) / D[i][j] for k in range(N))
    return tuple(f[a] * mol[k] for a in range(N) for k in range(N))


rows = []
labels = []
for i, j in permutations(range(M), 2):
    for fid, f in enumerate(vertices):
        if evaluate(f, i, j) == D[i][j]:
            rows.append(tensor(i, j, f))
            labels.append((i, j, fid))
assert len(rows) == 56
signed_rows = rows + [tuple(-v for v in row) for row in rows]

artifact = Path(__file__).resolve().with_name('certificates.json')
data = json.loads(artifact.read_text(encoding='utf-8'))
assert [tuple(Q(q) for q in f) for f in data['dual_extreme_vertices']] == vertices
assert [tuple(l) for l in data['supporting_rows']] == labels
assert len(data['certificates']) == 216
cases = set()
max_certificate_cost = Q(0)
for entry in data['certificates']:
    i, j = entry['pair']
    fid = entry['fid']
    assert i != j and 0 <= i < M and 0 <= j < M and 0 <= fid < len(vertices)
    assert (i, j, fid) not in cases
    cases.add((i, j, fid))
    total = Q(0)
    reconstructed = [Q(0)] * (N * N)
    for index, weight_text in entry['terms']:
        weight = Q(weight_text)
        assert 0 <= index < len(signed_rows) and weight >= 0
        total += weight
        reconstructed = [a + weight * b for a, b in zip(reconstructed, signed_rows[index])]
    assert total <= 2
    assert tuple(reconstructed) == tensor(i, j, vertices[fid])
    max_certificate_cost = max(max_certificate_cost, total)
assert len(cases) == 216
assert max_certificate_cost == 2

# Sharpness: T acts diagonally by (1,1,-1) in the evaluation-vector basis.
T = ((Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(-1)))

def pairing(row):
    return sum(row[k * N + l] * T[k][l] for k in range(N) for l in range(N))

vT = max(abs(pairing(row)) for row in signed_rows)
normT = max(abs(pairing(tensor(i, j, f)))
            for i, j in permutations(range(M), 2) for f in vertices)
assert vT == 1 and normT == 2
print('VERIFY_OK vertices=18 supporting=56 objectives=216 bound=2 radius=1 norm=2')
