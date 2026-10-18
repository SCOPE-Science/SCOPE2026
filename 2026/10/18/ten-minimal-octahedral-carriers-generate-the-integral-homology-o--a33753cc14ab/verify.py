"""Exact integral simplicial-chain verification for the folded five-cube independence complex.

Run with Python 3 and SymPy 1.13 or later. This program proves a specific finite
chain calculation, not publication priority or results for larger cubes.
"""
from collections import Counter
from itertools import combinations, product
from sympy import Matrix, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 16
GEN = (1, 2, 4, 8, 15)
EDGE = lambda a, b: (a ^ b) in GEN

# Enumerate every simplex using the defining Cayley graph, in increasing bit-mask order.
faces_by_size = {k: [] for k in range(1, 6)}
for mask in range(1, 1 << N):
    verts = tuple(i for i in range(N) if (mask >> i) & 1)
    if all(not EDGE(a, b) for a, b in combinations(verts, 2)):
        faces_by_size[len(verts)].append(verts)
assert tuple(len(faces_by_size[k]) for k in range(1, 6)) == (16, 80, 160, 120, 16)
assert len({(a,b) for a in range(N) for b in range(a+1,N) if EDGE(a,b)}) == 40

# The ten candidate minimal supports are all induced four-edge matchings.
carriers = []
for W in combinations(range(N), 8):
    edge_list = [(a,b) for a,b in combinations(W,2) if EDGE(a,b)]
    if len(edge_list) == 4 and len({v for e in edge_list for v in e}) == 8:
        carriers.append((W, edge_list))
assert len(carriers) == 10

# Verify structural description as two affine hyperplanes for each of five directions.
def dot_parity(x, y):
    return ((x & y).bit_count() & 1)
for s in GEN:
    norm = next(m for m in range(1,16) if dot_parity(s,m) == 0
                and all(dot_parity(t,m) == 1 for t in GEN if t != s))
    for eps in (0,1):
        W = tuple(x for x in range(N) if dot_parity(x,norm) == eps)
        assert len(W) == 8
        assert (W, [(a,b) for a,b in combinations(W,2) if EDGE(a,b)]) in carriers

simp2 = faces_by_size[3]
simp3 = faces_by_size[4]
simp4 = faces_by_size[5]
index2 = {f: j for j,f in enumerate(simp2)}
index3 = {f: j for j,f in enumerate(simp3)}
B3 = zeros(len(simp2),len(simp3))
for j,f in enumerate(simp3):
    for k in range(4):
        B3[index2[f[:k]+f[k+1:]],j] = (-1)**k
B4 = zeros(len(simp3),len(simp4))
for j,f in enumerate(simp4):
    for k in range(5):
        B4[index3[f[:k]+f[k+1:]],j] = (-1)**k
assert B3*B4 == zeros(B3.rows,B4.cols)

# Each oriented fundamental 3-cycle is the join of four (first endpoint - second endpoint).
Z = zeros(len(simp3),len(carriers))
for j, (W, edge_list) in enumerate(carriers):
    for choice in product((0,1),repeat=4):
        v = [edge_list[k][choice[k]] for k in range(4)]
        inversions = sum(v[k] > v[l] for k in range(4) for l in range(k+1,4))
        coeff = (-1)**(inversions + sum(choice))
        Z[index3[tuple(sorted(v))],j] += coeff
assert B3*Z == zeros(B3.rows,Z.cols)
assert all(sum(abs(int(Z[i,j])) for i in range(Z.rows)) == 16 for j in range(Z.cols))

# Independent mod-two computation of rank(B3), using XOR integer bitsets.
basis = {}
for j in range(B3.cols):
    b = 0
    for i in range(B3.rows):
        if B3[i,j]:
            b ^= (1 << i)
    while b:
        h = b.bit_length()-1
        if h in basis:
            b ^= basis[h]
        else:
            basis[h] = b
            break
assert len(basis) == 95

# Integral Smith form proves that the boundaries and all ten cycles form a saturated
# rank-25 sublattice of the free 3-chain group.
A = B4.row_join(Z)
D = smith_normal_form(A, domain=ZZ)
invariants = [abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]]
assert invariants == [1]*25, invariants

# Exact certificate for the unique primitive relation. Columns are ordered by
# increasing simplex bit-mask for B4 and lexicographic support for Z.
t = Matrix([1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,1])
q = Matrix([1,-1,1,-1,1,1,-1,1,-1,1])
assert B4*t + Z*q == zeros(B3.cols,1)
assert all(abs(int(c)) == 1 for c in q)

# B3 has rational rank at least its mod-2 rank 95. A is in ker(B3) and
# has rank 25, so its rational rank is exactly 95, ker(B3) has rank 25,
# and the primitive image(A) equals ker(B3) integrally.
# The 16 independent B4 columns and the ten Z columns therefore present H3.
assert invariants.count(1) == 25 and len(simp3)-len(basis) == 25
assert B4.rank() == 16
assert Z.rank() == 10
assert A.rank() == 25
print('VERIFY_OK FOLDED5_INDEPENDENCE')
print('FACE_VECTOR',tuple(len(faces_by_size[k]) for k in range(1,6)))
print('SHORTEST_SPHERES',len(carriers),'HYPERPLANES_5x2')
print('B3_RANK_MOD2',len(basis),'B4_RANK',B4.rank())
print('SMITH_BOUNDARIES_PLUS_SPHERES',len(invariants),'UNIT_FACTORS')
print('RELATION',list(q),'H3_FREE_RANK',len(carriers)-1)
