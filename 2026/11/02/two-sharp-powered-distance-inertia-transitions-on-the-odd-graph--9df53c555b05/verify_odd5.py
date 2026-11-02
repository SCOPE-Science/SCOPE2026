"""Reproduce exact graph and spectral identities for the odd graph KG(9,4).

Only the Python standard library is required. The analytic inequalities governing
all real exponents are provided in the accompanying mathematical proof.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations
from decimal import Decimal, localcontext

N = 9
K = 4
VERTICES = [sum(1 << j for j in c) for c in combinations(range(N), K)]
M = len(VERTICES)
assert M == 126
NEIGHBORS = [[j for j, t in enumerate(VERTICES)
              if not (s & t)] for s in VERTICES]
assert all(len(a) == 5 for a in NEIGHBORS)

# Every ordered vertex-pair distance is obtained independently by BFS.
DIST = []
for i in range(M):
    d = [-1] * M
    d[i] = 0
    todo = deque([i])
    while todo:
        j = todo.popleft()
        for t in NEIGHBORS[j]:
            if d[t] == -1:
                d[t] = d[j] + 1
                todo.append(t)
    assert all(0 <= z <= 4 for z in d)
    for j, v in enumerate(VERTICES):
        common = (VERTICES[i] & v).bit_count()
        assert d[j] == min(2 * (K - common), 2 * common + 1)
    DIST.append(d)
assert Counter(DIST[0]) == {0: 1, 1: 5, 2: 20, 3: 40, 4: 60}
print('BFS_OK vertices=126 ordered_distances=15876 valencies=1,5,20,40,60')

# Verify all distance-regular intersection identities, entry by entry.
# A*A_j = b_(j-1)*A_(j-1) + a_j*A_j + c_(j+1)*A_(j+1).
REC = (
    {1: 1},
    {0: 5, 2: 1},
    {1: 4, 3: 2},
    {2: 4, 4: 2},
    {3: 3, 4: 3},
)
for i in range(M):
    for j in range(M):
        for h in range(5):
            lhs = sum(DIST[z][j] == h for z in NEIGHBORS[i])
            rhs = sum(coef * (DIST[i][j] == d) for d, coef in REC[h].items())
            assert lhs == rhs, (i, j, h, lhs, rhs)
print('RECURRENCE_OK 79380 exact entries checked')

# Adjacency spectrum is certified by P(A)=0 (from the recurrence),
# plus 0th-through-4th trace moments. Solve the exact Vandermonde system.
ADJ_EIG = [5, -4, 3, -2, 1]
TRACES = [126, 0, 630, 0, 5670]
aug = [[Fraction(z ** power) for z in ADJ_EIG] +
       [Fraction(TRACES[power])] for power in range(5)]
for col in range(5):
    pivot = next(i for i in range(col, 5) if aug[i][col])
    aug[col], aug[pivot] = aug[pivot], aug[col]
    v = aug[col][col]
    aug[col] = [z / v for z in aug[col]]
    for i in range(5):
        if i != col:
            f = aug[i][col]
            aug[i] = [x - f * y for x, y in zip(aug[i], aug[col])]
mult = [int(aug[i][-1]) for i in range(5)]
assert all(aug[i][-1].denominator == 1 for i in range(5))
assert mult == [1, 8, 27, 48, 42]

# Independently reconstruct trace(A^4) from common-neighbor counts.
a2 = [[len(set(NEIGHBORS[i]).intersection(NEIGHBORS[j]))
       for j in range(M)] for i in range(M)]
assert sum(a2[i][j] ** 2 for i in range(M) for j in range(M)) == 5670
assert all(not any(j in NEIGHBORS[i] for j in NEIGHBORS[z])
           for i in range(M) for z in NEIGHBORS[i])
print('ADJACENCY_SPECTRUM_OK eigenvalues=5,-4,3,-2,1 multiplicities=1,8,27,48,42')

# Polynomials P_j(A), j=1,...,4, evaluated on each eigenspace.
def distance_sector(lam):
    return [lam, lam*lam-5, (lam**3-9*lam)//2,
            (lam**4-17*lam*lam+40)//4]
coeffs = [distance_sector(x) for x in ADJ_EIG]
assert coeffs == [
    [5, 20, 40, 60],
    [-4, 11, -14, 6],
    [3, 4, 0, -8],
    [-2, -1, 5, -3],
    [1, -4, -4, 6],
]
# Compare two independently formed exact powered-distance Frobenius norms
# against the spectral decomposition (and the zero diagonal trace).
for p in (1, 2, 3):
    mat_trace_square = sum(DIST[i][j]**(2*p)
                           for i in range(M) for j in range(M))
    eigen = [sum(c * j**p for j, c in enumerate(row, 1)) for row in coeffs]
    assert sum(m * e for m, e in zip(mult, eigen)) == 0
    assert sum(m * e * e for m, e in zip(mult, eigen)) == mat_trace_square
print('POWERED_DISTANCE_SPECTRA_OK p=1,2,3 exact trace and Frobenius checks')

# Numerical diagnostics only; uniqueness and global signs are analytical.
with localcontext() as ctx:
    ctx.prec = 55
    two = Decimal(2)
    three = Decimal(3)
    four = Decimal(4)
    def main_eigen(p):
        return Decimal(1) - 4*two**p - 4*three**p + 6*four**p
    lo, hi = Decimal(0), Decimal('0.5')
    for _ in range(210):
        md = (lo + hi)/2
        if main_eigen(md) > 0:
            hi = md
        else:
            lo = md
    pstar = (lo + hi)/2
    assert Decimal('.4095761090') < pstar < Decimal('.4095761092')
    def signs(p):
        vals = [sum(Decimal(c) * (Decimal(j)**p)
                    for j,c in enumerate(row,1)) for row in coeffs[1:]]
        return ['+' if x>0 else '-' if x<0 else '0' for x in vals]
    assert signs(Decimal('.2')) == ['-', '-', '-', '-']
    assert signs(Decimal('.6')) == ['-', '-', '-', '+']
    assert signs(Decimal(1)) == ['0', '-', '-', '+']
    assert signs(Decimal(2)) == ['+', '-', '-', '+']
    print('ROOT_DIAGNOSTIC pstar=',format(pstar,'.16f'))
    print('INERTIA_SIGNATURES_OK at sampled exponents')
print('ALL_ODD_GRAPH_KG94_CHECKS_OK')
