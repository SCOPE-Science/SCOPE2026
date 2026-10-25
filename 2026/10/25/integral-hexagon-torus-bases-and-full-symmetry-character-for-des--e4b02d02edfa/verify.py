"""Exact integral-chain verification for the two-particle Desargues configuration."""
from collections import Counter
from itertools import combinations, permutations
import sympy as sp
import networkx as nx
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Vertices 0..9 represent 2-subsets of {0,...,4}; 10..19 represent 3-subsets.
TWO = list(combinations(range(5), 2))
THREE = list(combinations(range(5), 3))
SUBSETS = TWO + THREE
VERTEX = {s: i for i, s in enumerate(SUBSETS)}
V = tuple(range(20))
E = tuple(sorted((i, 10+j) for i, a in enumerate(TWO)
                 for j, b in enumerate(THREE) if set(a).issubset(b)))
assert len(E) == 30
ADJ = {i: set() for i in V}
for a, b in E:
    ADJ[a].add(b)
    ADJ[b].add(a)
assert all(len(ADJ[v]) == 3 for v in V)
assert all(len(ADJ[a] & ADJ[b]) <= 1 for a, b in combinations(V, 2))

# Standard generalized Petersen presentation gives an independent graph check.
G = nx.Graph(); G.add_nodes_from(V); G.add_edges_from(E)
GP = nx.Graph(); GP.add_nodes_from(V)
for i in range(10):
    GP.add_edges_from(((i, (i+1) % 10), (i, 10+i),
                       (10+i, 10+(i+3) % 10)))
assert nx.is_isomorphic(G, GP)
assert sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(G, G)
           .isomorphisms_iter()) == 240

# Each simple hexagon is represented by its lexicographically chosen orientation:
# least vertex first and second vertex less than last vertex.
HEX = set()
for start in V:
    def extend(path):
        if len(path) > 6:
            return
        for w in ADJ[path[-1]]:
            if w == start:
                if len(path) == 6 and path[1] < path[-1]:
                    HEX.add(tuple(path))
            elif w > start and w not in path:
                extend(path + [w])
    for w in sorted(ADJ[start]):
        if w > start:
            extend([start, w])
HEX = tuple(sorted(HEX))
assert len(HEX) == 20
PAIRS = tuple((a, b) for i, a in enumerate(HEX)
              for b in HEX[i+1:] if set(a).isdisjoint(b))
assert len(PAIRS) == 70

C0 = tuple(combinations(V, 2))
C1 = tuple((edge, v) for edge in E for v in V if v not in edge)
C2 = tuple((E[i], e) for i in range(len(E))
           for e in E[i+1:] if set(E[i]).isdisjoint(e))
IX0 = {c: i for i, c in enumerate(C0)}
IX1 = {c: i for i, c in enumerate(C1)}
IX2 = {c: i for i, c in enumerate(C2)}
assert tuple(map(len, (C0, C1, C2))) == (190, 540, 375)

D1 = sp.zeros(len(C0), len(C1))
for j, ((a, b), v) in enumerate(C1):
    D1[IX0[tuple(sorted((b, v)))], j] += 1
    D1[IX0[tuple(sorted((a, v)))], j] -= 1
D2 = sp.zeros(len(C1), len(C2))
for j, ((a, b), (c, d)) in enumerate(C2):
    for cell, coefficient in ((((c, d), b), 1), (((c, d), a), -1),
                              (((a, b), d), -1), (((a, b), c), 1)):
        D2[IX1[cell], j] += coefficient
assert D1*D2 == sp.zeros(*D1.shape[:1], D2.cols)

# Product fundamental class of two vertex-disjoint oriented hexagons.
TORI = sp.zeros(len(C2), len(PAIRS))
for j, (a, b) in enumerate(PAIRS):
    for i, u in enumerate(a):
        v = a[(i+1) % 6]
        e = tuple(sorted((u, v)))
        sign1 = 1 if u < v else -1
        for k, x in enumerate(b):
            y = b[(k+1) % 6]
            f = tuple(sorted((x, y)))
            sign2 = 1 if x < y else -1
            ef = tuple(sorted((e, f)))
            TORI[IX2[ef], j] += sign1*sign2*(1 if ef[0] == e else -1)
assert D2*TORI == sp.zeros(len(C1), len(PAIRS))

# Exact modular Gaussian rank; no floating-point rank or heuristic tolerance.
def mod_rank(matrix, prime):
    pivots = {}
    for j in range(matrix.cols):
        col = {i: int(matrix[i,j]) % prime for i in range(matrix.rows)
               if matrix[i,j] % prime}
        while col:
            k = min(col)
            if k not in pivots:
                inv = pow(col[k], -1, prime)
                pivots[k] = {i: (x*inv) % prime for i, x in col.items()}
                break
            factor = col[k]
            for i, v in pivots[k].items():
                x = (col.get(i, 0) - factor*v) % prime
                if x:
                    col[i] = x
                else:
                    col.pop(i, None)
    return len(pivots)
assert mod_rank(D2, 101) == 340

# Symmetries: every permutation of {0,...,4}, with independent complementation.
PERMS = tuple(permutations(range(5)))
def move_vertex(p, complement, v):
    a = {p[x] for x in SUBSETS[v]}
    if complement:
        a = set(range(5)).difference(a)
    return VERTEX[tuple(sorted(a))]
def hex_key(hexagon):
    return frozenset(frozenset((hexagon[i], hexagon[(i+1) % 6]))
                     for i in range(6))
HEX_ID = {hex_key(h): i for i, h in enumerate(HEX)}
TORUS_ID = {frozenset((HEX_ID[hex_key(a)], HEX_ID[hex_key(b)])): j
            for j, (a, b) in enumerate(PAIRS)}
PAIR_INDICES = tuple((HEX_ID[hex_key(a)], HEX_ID[hex_key(b)])
                     for a, b in PAIRS)
SYMMETRIES = []
for p in PERMS:
    for comp in (0, 1):
        vmap = tuple(move_vertex(p, comp, v) for v in V)
        cycmap = tuple(HEX_ID[hex_key(tuple(vmap[x] for x in h))] for h in HEX)
        tmap = tuple(TORUS_ID[frozenset((cycmap[a], cycmap[b]))]
                     for a, b in PAIR_INDICES)
        SYMMETRIES.append((p, comp, vmap, tmap))
assert len(SYMMETRIES) == 240
assert len({x[2] for x in SYMMETRIES}) == 240
unseen = set(range(70)); ORBITS = []
while unseen:
    start = min(unseen)
    orbit = sorted({x[3][start] for x in SYMMETRIES})
    ORBITS.append(orbit)
    unseen.difference_update(orbit)
assert sorted(map(len, ORBITS)) == [10, 60]
O60 = next(orb for orb in ORBITS if len(orb) == 60)
O10 = next(orb for orb in ORBITS if len(orb) == 10)

# Explicit integer determinant certificates, with zero-based indices in C2 and PAIRS.
COLS_60 = [0,1,2,3,4,7,8,9,10,11,14,15,16,17,18,21,22,23,24,
           26,28,29,30,31,33,35,36,39,40,42,43,45,49,50,56]
ROWS_60 = [0,2,3,5,6,8,11,14,25,26,28,31,34,36,39,
           75,76,78,79,84,87,98,100,104,107,110,142,143,146,
           151,162,166,202,205,219]
ROWS_10 = [3,6,11,14,26,34,75,78,104,142]
assert len(COLS_60) == len(ROWS_60) == 35
assert set(COLS_60).issubset(O60)
B = TORI.extract(ROWS_60, COLS_60)
assert B.det() == -1
assert TORI.extract(ROWS_10, O10).det() == 1
# Rank over Q(D2)=340 by an F_101-minor; 35 cycles make rank <=340.
# The unit torus minor makes their rank-35 sublattice primitive in Z^375;
# the full kernel is a saturated rank-35 lattice, so the two are equal.

# Exact SNF also identifies the integral degree-one torsion.
SN = smith_normal_form(D2, domain=ZZ)
nonzero = [abs(SN[k,k]) for k in range(min(SN.shape)) if SN[k,k]]
assert len(nonzero) == 340 and Counter(nonzero) == Counter({1:339, 2:1})
assert mod_rank(D1, 101) == 189

# Signed action on the ordered-orientation 2-cell basis.
def signed_cell_action(vmap):
    target = []
    signs = []
    for e, f in C2:
        a, b = vmap[e[0]], vmap[e[1]]
        c, d = vmap[f[0]], vmap[f[1]]
        en = tuple(sorted((a, b)))
        fn = tuple(sorted((c, d)))
        sign = ((1 if a<b else -1)*(1 if c<d else -1)*
                (1 if en < fn else -1))
        target.append(IX2[tuple(sorted((en, fn)))])
        signs.append(sign)
    return target, signs

# Because B is unimodular, the homology-action coordinates are integral.
# In addition to representative traces, check that they reproduce the
# action on ALL 375 coordinates, not merely the selected 35 rows.
B_INV = B.inv()
assert all(x.q == 1 for x in B_INV)
Z = TORI[:, COLS_60]
ROW_ID = {r:i for i,r in enumerate(ROWS_60)}
def matrix_and_trace(vmap, return_matrix=False):
    targets, signs = signed_cell_action(vmap)
    compressed = sp.zeros(35,35)
    for j, toridx in enumerate(COLS_60):
        for i in range(TORI.rows):
            value = TORI[i,toridx]
            if value and targets[i] in ROW_ID:
                compressed[ROW_ID[targets[i]],j] += signs[i]*value
    act = B_INV * compressed
    assert all(x.q == 1 for x in act)
    transformed = sp.zeros(len(C2),35)
    for j, toridx in enumerate(COLS_60):
        for i in range(TORI.rows):
            if TORI[i,toridx]:
                transformed[targets[i],j] += signs[i]*TORI[i,toridx]
    assert Z * act == transformed
    return act if return_matrix else int(sp.trace(act))

def cycle_type(p):
    unseen = set(range(5)); lengths = []
    while unseen:
        a = min(unseen); b = a; ell = 0
        while b in unseen:
            unseen.remove(b); ell += 1; b = p[b]
        lengths.append(ell)
    return tuple(sorted(lengths, reverse=True))
REP = {}
for p in PERMS:
    REP.setdefault(cycle_type(p), p)
TRACES = {}
for ct,p in sorted(REP.items()):
    for comp in (0,1):
        TRACES[(ct,comp)] = matrix_and_trace(tuple(move_vertex(p,comp,v) for v in V))
EXPECTED = {
    ((1,1,1,1,1),0):35, ((1,1,1,1,1),1):-5,
    ((2,1,1,1),0):-1, ((2,1,1,1),1):-5,
    ((2,2,1),0):-1, ((2,2,1),1):-1,
    ((3,1,1),0):-1, ((3,1,1),1):1,
    ((3,2),0):-1, ((3,2),1):1,
    ((4,1),0):1, ((4,1),1):1,
    ((5,),0):0, ((5,),1):0,
}
assert TRACES == EXPECTED
# Independently enforce defining group relations on the integral basis.
A01 = matrix_and_trace(tuple(move_vertex((1,0,2,3,4),0,v) for v in V), True)
A12 = matrix_and_trace(tuple(move_vertex((0,2,1,3,4),0,v) for v in V), True)
A5  = matrix_and_trace(tuple(move_vertex((1,2,3,4,0),0,v) for v in V), True)
AC  = matrix_and_trace(tuple(move_vertex((0,1,2,3,4),1,v) for v in V), True)
I35 = sp.eye(35)
assert A01**2 == A12**2 == A5**5 == AC**2 == I35
assert (A01*A12)**3 == I35
assert A01*AC == AC*A01 and A5*AC == AC*A5

# Irreducibles of S5 are computed from the permutation representation on
# 1- and 2-subsets and from its standard representation's exterior square.
CLASSES = Counter(cycle_type(p) for p in PERMS)
MULT = {}
for ct,p in REP.items():
    f = sum(i == p[i] for i in range(5))
    t = sum(i < p[i] and p[p[i]] == i for i in range(5))
    sign = (-1)**(5-len(ct))
    std = f-1
    s32 = f*(f-1)//2 + t - f
    wedge = ((f-1)*(f-2)-2*t)//2
    MULT[ct] = {'(5)':1, '(1^5)':sign, '(4,1)':std,
                '(2,1,1,1)':sign*std, '(3,2)':s32,
                '(2,2,1)':sign*s32, '(3,1,1)':wedge}
DECOMP = {}
for central in (1,-1):
    for part in next(iter(MULT.values())):
        numerator = sum(CLASSES[ct]*(TRACES[(ct,0)] + central*TRACES[(ct,1)])
                        * d[part] for ct,d in MULT.items())
        assert numerator % 240 == 0
        DECOMP[(central,part)] = numerator//240
assert {p:d for (s,p),d in DECOMP.items() if s==1 and d} == {
    '(2,1,1,1)':1, '(2,2,1)':1, '(3,1,1)':1}
assert {p:d for (s,p),d in DECOMP.items() if s==-1 and d} == {
    '(4,1)':1, '(3,2)':1, '(2,2,1)':1, '(3,1,1)':1}
assert all(x in (0,1) for x in DECOMP.values())
print('VERIFY_OK_DESARGUES_SHORTEST_HEXAGON_INTEGRAL_S5C2')
print('GRAPH_VERTICES_EDGES',len(V),len(E),'AUTOMORPHISMS',len(SYMMETRIES))
print('TWO_POINT_CUBICAL_CELLS',len(C0),len(C1),len(C2))
print('BOUNDARY2_RANK',340,'SMITH_NONUNIT',(2,))
print('UNORDERED_HOMOLOGY_H1_Z11_PLUS_Z2_H2_Z35')
print('HEXAGONS',len(HEX),'DISJOINT_HEXAGON_PAIRS',len(PAIRS))
print('TWO_TORUS_ORBITS',sorted(map(len,ORBITS)))
print('ORBIT_60_UNIT_35_MINOR',int(B.det()),'ORBIT_10_UNIT_10_MINOR',1)
print('CHARACTERS',sorted(TRACES.items()))
print('PLUS_AND_MINUS_S5_DECOMPOSITION',DECOMP)
