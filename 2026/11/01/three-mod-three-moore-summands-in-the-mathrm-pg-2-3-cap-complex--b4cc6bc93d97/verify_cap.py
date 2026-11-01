"""Exact integral topology of the noncollinearity complex of PG(2,3).

Requires SymPy 1.14.0. All simplices and integer matrices are reconstructed
from finite-field projective incidence; no external data files are needed.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

P = 3

def canonical(v):
    a = next(x for x in v if x)
    inv = pow(a, -1, P)
    return tuple((inv*x) % P for x in v)

points = tuple(sorted({canonical(v) for v in product(range(P), repeat=3)
                       if any(v)}))
assert len(points) == 13
lines = tuple(sorted({tuple(i for i, v in enumerate(points)
                             if sum(a*b for a, b in zip(u, v)) % P == 0)
                      for u in points}))
assert len(lines) == 13
assert all(len(line) == 4 for line in lines)
assert all(sum({i,j} <= set(line) for line in lines) == 1
           for i,j in combinations(range(13), 2))

# Independent published-style incidence table in lexicographic point order:
line_table = tuple(sorted([
 (1,4,7,10), (0,4,5,6), (3,4,9,11), (2,4,8,12),
 (0,1,2,3), (1,6,9,12), (1,5,8,11), (0,10,11,12),
 (3,6,8,10), (2,5,9,10), (0,7,8,9), (2,6,7,11),
 (3,5,7,12)
]))
assert lines == line_table
bad = {triple for line in lines for triple in combinations(line, 3)}
assert len(bad) == 52

def is_arc(subset):
    return not any(triple in bad for triple in combinations(subset, 3))

faces = {k: tuple(s for s in combinations(range(13), k) if is_arc(s))
         for k in range(1, 6)}
assert tuple(len(faces[k]) for k in (1,2,3,4,5)) == (13,78,234,234,0)
assert all(sum(is_arc(tuple(sorted(s+(v,)))) for v in range(13) if v not in s) == 4
           for s in faces[3])

# Each missing triangular 2-face admits a cone filling of its boundary.
for tri in bad:
    assert any(all(is_arc(tuple(sorted(edge + (v,))))
                   for edge in combinations(tri, 2))
               for v in range(13) if v not in tri)

def boundary(k):
    row = {f:i for i,f in enumerate(faces[k-1])}
    A = zeros(len(row), len(faces[k]))
    for j, face in enumerate(faces[k]):
        for i in range(k):
            A[row[face[:i] + face[i+1:]],j] = (-1)**i
    return A

D1 = zeros(13, 78)
for j, (i,k) in enumerate(faces[2]):
    D1[i,j], D1[k,j] = -1, 1
D2 = boundary(3)
D3 = boundary(4)
assert D1*D2 == zeros(13,234)
assert D2*D3 == zeros(78,234)

def invariants(A):
    B = smith_normal_form(A, domain=ZZ)
    return Counter(abs(int(B[i,i])) for i in range(min(B.rows,B.cols)))

inv1, inv2, inv3 = invariants(D1), invariants(D2), invariants(D3)
assert inv1 == Counter({1:12, 0:1}), inv1
assert inv2 == Counter({1:66, 0:12}), inv2
assert inv3 == Counter({1:165, 3:3, 0:66}), inv3

def rankmod3(matrix):
    A = [[int(x) % 3 for x in row] for row in matrix.tolist()]
    n, m = len(A), len(A[0])
    r = 0
    for c in range(m):
        p = next((t for t in range(r,n) if A[t][c] != 0), None)
        if p is None:
            continue
        A[p], A[r] = A[r], A[p]
        if A[r][c] == 2:
            A[r] = [(2*x)%3 for x in A[r]]
        for t in range(r+1,n):
            if A[t][c]:
                q = A[t][c]
                A[t] = [(u-q*v)%3 for u,v in zip(A[t],A[r])]
        r += 1
        if r==n:
            break
    return r
assert rankmod3(D3) == 165
assert rankmod3(D2) == 66

# A second chain sanity check: Euler characteristic = 13-78+234-234=-65;
# the claimed homology has 1-66=-65.
assert 13-78+234-234 == 1-66
encoded = json.dumps({"points":points,"lines":lines,
                      "four_arcs":faces[4]}, separators=(',',':'))
print('points=13, lines=13, line_length=4, f=(13,78,234,234)')
print('all 234 noncollinear triples extend to exactly four 4-arcs')
print('all 52 missing triangle boundaries fill in the 2-skeleton')
print('boundary_smith_d1=1^12,0^1')
print('boundary_smith_d2=1^66,0^12')
print('boundary_smith_d3=1^165,3^3,0^66')
print('boundary_d3_rank_mod3=165')
print('integral_reduced_h2=(Z/3)^3; h3=Z^66')
print('complex_data_sha256=' + sha256(encoded.encode()).hexdigest())
print('VERIFY_OK')
