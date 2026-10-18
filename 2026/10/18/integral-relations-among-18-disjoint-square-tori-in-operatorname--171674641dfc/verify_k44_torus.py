#!/usr/bin/env python3
"""Exact finite chain and lattice checks for two-point configurations of K_{4,4}."""
from itertools import combinations

LEFT = tuple(range(4))
RIGHT = tuple(range(4, 8))
VERTICES = LEFT + RIGHT
EDGES = tuple((a, b) for a in LEFT for b in RIGHT)  # oriented left to right
EDGE_ID = {e: i for i, e in enumerate(EDGES)}
PAIRS = tuple((i, j) for i, j in combinations(range(16), 2)
              if set(EDGES[i]).isdisjoint(EDGES[j]))
PAIR_ID = {p: i for i, p in enumerate(PAIRS)}
ONE_CELLS = tuple((v, i) for i, e in enumerate(EDGES)
                  for v in VERTICES if v not in e)
ONE_ID = {p: i for i, p in enumerate(ONE_CELLS)}

# Exact signed cellular boundary, rows indexed by (stationary vertex, moving edge).
B = [[0] * len(PAIRS) for _ in ONE_CELLS]
for col, (i, j) in enumerate(PAIRS):
    a, b = EDGES[i]
    c, d = EDGES[j]
    for key, coeff in [((b, j), 1), ((a, j), -1), ((d, i), -1), ((c, i), 1)]:
        B[ONE_ID[key]][col] += coeff

# The oriented four-cycle on L=(a<b), R=(u<v) has chain
# (a,u)-(b,u)+(b,v)-(a,v) in the fixed left-to-right edge basis.
def four_cycle(L, R):
    a, b = L
    u, v = R
    return ((EDGE_ID[a, u], 1), (EDGE_ID[b, u], -1),
            (EDGE_ID[b, v], 1), (EDGE_ID[a, v], -1))

LPARTS = tuple(pair for pair in combinations(LEFT, 2) if pair[0] == 0)
RPAIRS = tuple(combinations(RIGHT, 2))
TORUS_KEYS = tuple((L, R) for L in LPARTS for R in RPAIRS)

T = [[0] * 18 for _ in PAIRS]
for col, (L, R) in enumerate(TORUS_KEYS):
    L2 = tuple(v for v in LEFT if v not in L)
    R2 = tuple(v for v in RIGHT if v not in R)
    for i, x in four_cycle(L, R):
        for j, y in four_cycle(L2, R2):
            if i < j:
                T[PAIR_ID[i, j]][col] += x * y
            else:
                T[PAIR_ID[j, i]][col] -= x * y

# Relations use column order i*6+j for the 3 left partitions and 6 right pairs.
R = [[0] * 6 for _ in range(18)]
def set_rel(col, pairs):
    for row, coeff in pairs:
        R[row][col] += coeff
for i in range(3):
    set_rel(i, [(6*i + j, v) for j, v in enumerate((1, -1, 1, 1, -1, 1))])
# M1: (z00-z01+z02)-(z10-z11+z12)+(z20-z21+z22)
set_rel(3, [(0,1),(1,-1),(2,1),(6,-1),(7,1),(8,-1),(12,1),(13,-1),(14,1)])
# M2: (-z01+z04)+(z11-z14)+(-z21+z24)
set_rel(4, [(1,-1),(4,1),(7,1),(10,-1),(13,-1),(16,1)])
# M3: (-z00+z05)+(z10-z15)+(-z20+z25)
set_rel(5, [(0,-1),(5,1),(6,1),(11,-1),(12,-1),(17,1)])

def rank_mod_p(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix]
    nrows, ncols = len(a), len(a[0])
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        for j in range(c, ncols):
            a[r][j] = a[r][j] * inv % p
        for i in range(r+1, nrows):
            f = a[i][c]
            if f:
                for j in range(c, ncols):
                    a[i][j] = (a[i][j] - f*a[r][j]) % p
        r += 1
        if r == nrows:
            break
    return r

def det_bareiss(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign, denominator = 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            t = next((j for j in range(k + 1, n) if a[j][k]), None)
            if t is None:
                return 0
            a[k], a[t] = a[t], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * p - a[i][k] * a[k][j]
                assert num % denominator == 0
                a[i][j] = num // denominator
        for i in range(k + 1, n):
            a[i][k] = 0
        denominator = p
    return sign * a[n-1][n-1]

assert len(ONE_CELLS) == 96 and len(PAIRS) == 72 and len(TORUS_KEYS) == 18
assert all(sum(B[i][k]*T[k][j] for k in range(72)) == 0
           for i in range(96) for j in range(18))
assert all(sum(T[i][k]*R[k][j] for k in range(18)) == 0
           for i in range(72) for j in range(6))

rank_B = rank_mod_p(B, 3)
assert rank_B == 60
T_cols = (0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13)
T_rows = (0, 1, 3, 4, 9, 10, 12, 13, 18, 21, 36, 37)
det_T = det_bareiss([[T[i][j] for j in T_cols] for i in T_rows])
assert abs(det_T) == 1
R_rows = (5, 11, 14, 15, 16, 17)
det_R = det_bareiss([[R[i][j] for j in range(6)] for i in R_rows])
assert abs(det_R) == 1
# Note: The rational upper bound on ker(B) is 72-rank_B=12;
# T has 12 independent columns by its unit minor, hence rank_Q(B)=60.
# Unit minors make im(T) and im(R) saturated sublattices of their ambient lattices.
print('VERIFY_OK_K44_UNORDERED_TWO_PARTICLE_PRODUCT_TORUS_PRESENTATION')
print('CELLS_C0_C1_C2', 28, len(ONE_CELLS), len(PAIRS))
print('RANK_B2_MOD3', rank_B, 'H2_FREE_RANK', 72-rank_B)
print('FOUR_CYCLE_TORUS_GENERATORS', len(TORUS_KEYS), 'CYCLE_BOUNDARIES_ZERO')
print('TWELVE_BY_TWELVE_UNIT_DET', det_T, 'ROWS', T_rows, 'COLS', T_cols)
print('SIX_RELATIONS_BOUNDARY_ZERO', 'SIX_BY_SIX_UNIT_DET', det_R, 'ROWS', R_rows)
print('FULL_INTEGRAL_KERNEL_AND_RELATIONS_CERTIFIED')
