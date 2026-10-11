#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque, Counter
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
CERT = json.loads((HERE / 'integral_certificate.json').read_text(encoding='utf-8'))
CENSUS = json.loads((HERE / 'carrier_census.json').read_text(encoding='utf-8'))

V = tuple(CERT['vertices'])
FACETS = {tuple(x) for x in CERT['facets']}

def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
Q = faces(4)
assert E == [tuple(x) for x in CERT['edges']]
assert T == [tuple(x) for x in CERT['triangles']]
assert Q == [tuple(x) for x in CERT['tetrahedra']]
assert (len(V),len(E),len(T),len(Q)) == (17,117,200,100)
EI = {e:i for i,e in enumerate(E)}
TI = {t:i for i,t in enumerate(T)}

# Integral chain matrices in increasing simplex orientation.
d2 = [[0]*len(T) for _ in E]
for j,(a,b,c) in enumerate(T):
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        d2[EI[e]][j] = s

d3 = [[0]*len(Q) for _ in T]
for j,(a,b,c,d) in enumerate(Q):
    for t,s in [((b,c,d),1),((a,c,d),-1),((a,b,d),1),((a,b,c),-1)]:
        d3[TI[t]][j] = s

def rank_mod(A,p):
    M = [[x % p for x in row] for row in A]
    m = len(M); n = len(M[0]) if m else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r,m) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r],M[piv] = M[piv],M[r]
        inv = pow(M[r][c], -1, p)
        M[r] = [(inv*x) % p for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] % p:
                q = M[i][c] % p
                M[i] = [(x-q*y) % p for x,y in zip(M[i],M[r])]
        r += 1
        if r == m:
            break
    return r

assert rank_mod(d2,3) == 100

# Integral H2 certificate: B is a primitive Z-basis of ker(d2), certified by L B = I.
B = CERT['integral_h2']['cycle_basis_B_rows']
L = CERT['integral_h2']['left_inverse_L_rows']
assert len(B) == 200 and len(B[0]) == 100
assert len(L) == 100 and len(L[0]) == 200
for i,row in enumerate(d2):
    for j in range(100):
        assert sum(row[k]*B[k][j] for k in range(200)) == 0
for i in range(100):
    for j in range(100):
        assert sum(L[i][k]*B[k][j] for k in range(200)) == (1 if i==j else 0)

H = [[sum(L[i][k]*d3[k][j] for k in range(200)) for j in range(100)] for i in range(100)]

def det_bareiss(A):
    M = [row[:] for row in A]
    n = len(M)
    sign = 1
    prev = 1
    for k in range(n-1):
        if M[k][k] == 0:
            piv = next((i for i in range(k+1,n) if M[i][k] != 0), None)
            if piv is None:
                return 0
            M[k],M[piv] = M[piv],M[k]
            sign *= -1
        pivot = M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j] = (M[i][j]*pivot - M[i][k]*M[k][j]) // prev
        for i in range(k+1,n):
            M[i][k] = 0
        prev = pivot
    return sign*M[n-1][n-1]

hdet = det_bareiss(H)
assert hdet == CERT['integral_h2']['expected_boundary_coordinate_det'] == -2
# The primitive rank-100 cycle lattice modulo the rank-100 boundary lattice therefore has order two.

# Integral H1 certificate from the contracted graph presentation.
TREE = {tuple(x) for x in CERT['integral_h1']['spanning_tree_edges']}
NTE = [tuple(x) for x in CERT['integral_h1']['non_tree_edges']]
assert len(TREE) == 16 and len(NTE) == 101 and set(NTE) == set(E)-TREE
NEI = {e:i for i,e in enumerate(NTE)}
R = []
for a,b,c in T:
    row = [0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in NEI:
            row[NEI[e]] += s
    R.append(row)

def unit_reduce(A):
    M = [row[:] for row in A]
    m = len(M); n = len(M[0]) if m else 0
    k = 0
    while k < min(m,n):
        pos = None
        for i in range(k,m):
            for j in range(k,n):
                if abs(M[i][j]) == 1:
                    pos = (i,j); break
            if pos is not None: break
        if pos is None: break
        i,j = pos
        M[k],M[i] = M[i],M[k]
        for rr in range(m):
            M[rr][k],M[rr][j] = M[rr][j],M[rr][k]
        if M[k][k] == -1:
            M[k] = [-x for x in M[k]]
        for i in range(m):
            if i != k and M[i][k]:
                q = M[i][k]
                M[i] = [x-q*y for x,y in zip(M[i],M[k])]
        for j in range(n):
            if j != k and M[k][j]:
                q = M[k][j]
                for i in range(m):
                    M[i][j] -= q*M[i][k]
        k += 1
    return k,M

r1,RR = unit_reduce(R)
assert r1 == 99
for i in range(len(RR)):
    for j in range(len(RR[0])):
        if i < 99 or j < 99:
            assert RR[i][j] == (1 if i==j and i<99 else 0)
residual = [row[99:] for row in RR[99:]]
assert all(x % 4 == 0 for row in residual for x in row)
r2,SS = unit_reduce([[x//4 for x in row] for row in residual])
assert r2 == 1
for i in range(len(SS)):
    for j in range(len(SS[0])):
        assert SS[i][j] == (1 if i==j and i<1 else 0)
# Hence H1 = Z + Z/4.

FREE = CERT['integral_h1']['free_cocycle']
TORS = CERT['integral_h1']['torsion_cocycle_mod4']
assert len(FREE) == len(TORS) == len(NTE)
assert all(sum(a*b for a,b in zip(row,FREE)) == 0 for row in R)
assert all(sum((a%4)*b for a,b in zip(row,TORS)) % 4 == 0 for row in R)

def graph_cycle(tr):
    a,b,c = tr
    row = [0]*len(NTE)
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        if e in NEI:
            row[NEI[e]] += s
    return row

def h1coord_from_graph(row):
    return (sum(a*b for a,b in zip(row,FREE)), sum((a%4)*b for a,b in zip(row,TORS)) % 4)

def h1coord_triangle(tr):
    return h1coord_from_graph(graph_cycle(tuple(tr)))

assert h1coord_triangle(CERT['integral_h1']['free_generator_triangle']) == (1,0)
assert h1coord_triangle(CERT['integral_h1']['torsion_generator_triangle']) == (0,1)

# Mod-two H2 and coefficient Bockstein.
D2bits = []
for t in T:
    b = 0
    for e in combinations(t,2): b ^= 1 << EI[e]
    D2bits.append(b)
D3bits = []
for q in Q:
    b = 0
    for t in combinations(q,3): b ^= 1 << TI[t]
    D3bits.append(b)

def basis_reduce(vectors):
    Bx = {}
    for x in vectors:
        y = x
        for p in sorted(Bx,reverse=True):
            if (y>>p)&1: y ^= Bx[p]
        if not y: continue
        p = y.bit_length()-1
        for q in list(Bx):
            if (Bx[q]>>p)&1: Bx[q] ^= y
        Bx[p] = y
    return dict(sorted(Bx.items(),reverse=True))

def reduce_bits(x,Bx):
    y = x
    for p,row in Bx.items():
        if (y>>p)&1: y ^= row
    return y

# Full mod-two cycle basis by tracking dependencies among triangle boundaries.
piv = {}; K2 = []
for i,b in enumerate(D2bits):
    y = b; combo = 1 << i
    for p in sorted(piv,reverse=True):
        if (y>>p)&1:
            y ^= piv[p][0]; combo ^= piv[p][1]
    if y:
        piv[y.bit_length()-1] = (y,combo)
    else:
        K2.append(combo)
B3 = basis_reduce(D3bits)
assert len(piv) == 99 and len(K2) == 101 and len(B3) == 99

# Deterministic quotient basis and coordinate map H2(F2) -> F2^2.
track = {}; qdim = 0
for z in K2:
    r = reduce_bits(z,B3)
    if not r: continue
    y = r; c = 0
    for p in sorted(track,reverse=True):
        if (y>>p)&1:
            y ^= track[p][0]; c ^= track[p][1]
    if y:
        p = y.bit_length()-1
        c ^= 1 << qdim
        for q in list(track):
            if (track[q][0]>>p)&1:
                track[q] = (track[q][0]^y, track[q][1]^c)
        track[p] = (y,c)
        qdim += 1
assert qdim == 2

def h2coord(z):
    r = reduce_bits(z,B3); c = 0
    for p in sorted(track,reverse=True):
        if (r>>p)&1:
            r ^= track[p][0]; c ^= track[p][1]
    assert r == 0
    return c

reps = {}
for z in K2:
    c = h2coord(z)
    if c and c not in reps: reps[c] = z
assert set(reps) == {1,2,3}

def bockstein(z):
    edge = [0]*len(E)
    for i,t in enumerate(T):
        if (z>>i)&1:
            a,b,c = t
            for e,s in [((b,c),1),((a,c),-1),((a,b),1)]: edge[EI[e]] += s
    assert all(v%2 == 0 for v in edge)
    half = [v//2 for v in edge]
    graph = [half[EI[e]] for e in NTE]
    return h1coord_from_graph(graph)

betas = {c:bockstein(z) for c,z in reps.items()}
assert betas == {1:(0,2),2:(0,0),3:(0,2)}

# Exhaust every support through eight vertices.
TMASK = [sum(1<<v for v in t) for t in T]
def local_cycle_basis(mask):
    piv = {}; out = []
    for i,b in enumerate(D2bits):
        if TMASK[i] & ~mask: continue
        y = b; combo = 1 << i
        for p in sorted(piv,reverse=True):
            if (y>>p)&1:
                y ^= piv[p][0]; combo ^= piv[p][1]
        if y: piv[y.bit_length()-1] = (y,combo)
        else: out.append(combo)
    return out

def image_subgroup(S):
    mask = sum(1<<v for v in S)
    vals = {0}
    for z in local_cycle_basis(mask):
        g = h2coord(z)
        vals |= {x^g for x in tuple(vals)}
    return vals

mins = {1:None,2:None,3:None}
carriers = {1:[],2:[],3:[]}
for size in range(1,9):
    for S in combinations(V,size):
        img = image_subgroup(S)
        for c in (1,2,3):
            if c in img:
                if mins[c] is None: mins[c] = size
                if mins[c] == size: carriers[c].append(S)
assert mins == {1:8,2:7,3:8}
expected = CENSUS['minimum_carriers']
assert [list(s) for s in carriers[2]] == expected['10']
assert [list(s) for s in carriers[1]] == expected['01']
assert [list(s) for s in carriers[3]] == expected['11']
assert (len(carriers[2]),len(carriers[1]),len(carriers[3])) == (7,15,20)
assert all(image_subgroup(S) == {0,2} for S in carriers[2])
assert all(image_subgroup(S) == {0,1} for S in carriers[1])
assert all(image_subgroup(S) == {0,3} for S in carriers[3])

# The seven integral-lift minimizers are induced orientable tori.
def orientable_closed_surface(S):
    ss = set(S)
    tris = [t for t in T if set(t) <= ss]
    tets = [q for q in Q if set(q) <= ss]
    edges = [e for e in E if set(e) <= ss]
    assert (len(edges),len(tris),len(tets)) == (21,14,0)
    inc = defaultdict(list)
    for i,(a,b,c) in enumerate(tris):
        for e,s in [((b,c),1),((a,c),-1),((a,b),1)]: inc[e].append((i,s))
    if len(inc) != 21 or any(len(v) != 2 for v in inc.values()): return False
    signs = {0:1}; dq = deque([0])
    while dq:
        i = dq.popleft(); a,b,c = tris[i]
        for e,si in [((b,c),1),((a,c),-1),((a,b),1)]:
            pair = inc[e]
            j,sj = pair[0] if pair[1][0] == i else pair[1]
            want = -signs[i]*si*sj
            if j in signs and signs[j] != want: return False
            if j not in signs:
                signs[j] = want; dq.append(j)
    return len(signs) == 14

assert all(orientable_closed_surface(S) for S in carriers[2])

print(
    'VERIFY_OK f=17,117,200,100 '
    'H1_Z=Z+Z/4 H2_Z=Z/2 H2_F2_dim=2 '
    'bockstein=nonzero_classes_to_order2 '
    'integral_reduction_min_support=7 integral_reduction_carriers=7 '
    'all_integral_min_carriers_induced_tori=yes '
    'bockstein_min_supports=8,8 bockstein_carrier_counts=15,20 '
    'minimal_support_images_rank1=yes'
)
