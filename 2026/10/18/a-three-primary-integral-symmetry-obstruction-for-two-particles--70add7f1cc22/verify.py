#!/usr/bin/env python3
"""Exact integral cellular certificate for two unordered points on the cube graph.
Requires Python 3 standard library only. Run next to projection.json.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path


def determinant(A):
    A = [list(map(int, row)) for row in A]
    n = len(A)
    if n == 0:
        return 1
    assert all(len(row) == n for row in A)
    prev, sign = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if A[r][k]), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        d = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = A[i][j] * d - A[i][k] * A[k][j]
                assert v % prev == 0
                A[i][j] = v // prev
            A[i][k] = 0
        prev = d
    return sign * A[-1][-1]


def matrix_mul(A, B):
    return [[sum(a * B[k][j] for k, a in enumerate(row)) for j in range(len(B[0]))] for row in A]


def linear_solution(rows, rhs, n):
    # Exact rectangular Gaussian elimination; returns solution only if unique.
    X = [[Fraction(v) for v in row] + [Fraction(b)] for row, b in zip(rows, rhs)]
    pivot_cols = []
    k = 0
    for j in range(n):
        r = next((r for r in range(k, len(X)) if X[r][j]), None)
        if r is None:
            continue
        X[k], X[r] = X[r], X[k]
        z = X[k][j]
        X[k] = [v / z for v in X[k]]
        for rr in range(len(X)):
            if rr != k and X[rr][j]:
                z = X[rr][j]
                X[rr] = [v - z * w for v, w in zip(X[rr], X[k])]
        pivot_cols.append(j)
        k += 1
    assert all(any(row[:n]) or not row[-1] for row in X)
    assert len(pivot_cols) == n
    sol = [Fraction(0) for _ in range(n)]
    for r, j in enumerate(pivot_cols):
        sol[j] = X[r][-1]
    return sol


V = range(8)
E = sorted((v, v ^ (1 << k)) for v in V for k in range(3) if v < (v ^ (1 << k)))
eidx = {e: i for i, e in enumerate(E)}
C0 = list(itertools.combinations(V, 2))
C1 = [(i, w) for i, (u, v) in enumerate(E) for w in V if w not in (u, v)]
C2 = [(i, j) for i, e in enumerate(E) for j, f in enumerate(E) if j > i and set(e).isdisjoint(f)]
zidx = {c: i for i, c in enumerate(C0)}
oidx = {c: i for i, c in enumerate(C1)}
tidx = {c: i for i, c in enumerate(C2)}
assert (len(E), len(C0), len(C1), len(C2)) == (12, 28, 72, 42)
d1 = [[0] * 72 for _ in range(28)]
d2 = [[0] * 42 for _ in range(72)]
for j, (i, w) in enumerate(C1):
    u, v = E[i]
    d1[zidx[tuple(sorted((u, w)))]][j] -= 1
    d1[zidx[tuple(sorted((v, w)))]][j] += 1
for j, (i, k) in enumerate(C2):
    u, v = E[i]
    s, t = E[k]
    for ei, w, c in [(k, v, 1), (k, u, -1), (i, t, -1), (i, s, 1)]:
        d2[oidx[(ei, w)]][j] += c
assert all(all(x == 0 for x in row) for row in matrix_mul(d1, d2))

cert = json.loads(Path(__file__).with_name('projection.json').read_text(encoding='utf-8'))
non_tree = cert['non_tree']
cols = cert['boundary_pivots']
proj = cert['projection']
assert len(non_tree) == 45 and len(set(non_tree)) == 45 and len(cols) == 39
assert cols == list(range(34)) + list(range(35, 40))
assert all(len(row) == 45 for row in proj) and len(proj) == 6
# Verify that the 27 complementary configuration edges form an actual spanning tree.
tree = sorted(set(range(72)) - set(non_tree))
par = list(range(28))
def find(x):
    while par[x] != x:
        x = par[x]
    return x
for edge_idx in tree:
    ei, w = C1[edge_idx]
    a, b = E[ei]
    x, y = zidx[tuple(sorted((a, w)))], zidx[tuple(sorted((b, w)))]
    assert find(x) != find(y)
    par[find(x)] = find(y)
assert len({find(x) for x in range(28)}) == 1

# Five fundamental graph cycles and a junction exchange loop.
paths = [([2,0,1,3,2],4), ([4,0,1,5,4],2),
         ([4,0,2,6,4],1), ([5,1,3,7,5],0),
         ([6,2,0,1,3,7,6],4)]
B = []
for path, fixed in paths:
    c = [0] * 72
    for u, v in zip(path, path[1:]):
        e = eidx[tuple(sorted((u, v)))]
        c[oidx[(e, fixed)]] += 1 if u < v else -1
    B.append(c)
seq = [(1,2),(0,2),(4,2),(4,0),(4,1),(0,1),(2,1)]
L = [0] * 72
for (u, w), (v, z) in zip(seq, seq[1:]):
    if w == z:
        e = eidx[tuple(sorted((u, v)))]
        L[oidx[(e, w)]] += 1 if u < v else -1
    else:
        assert u == v
        e = eidx[tuple(sorted((w, z)))]
        L[oidx[(e, u)]] += 1 if w < z else -1
B.append(L)
assert len(B) == 6
assert all(all(sum(d1[r][j]*v[j] for j in range(72)) == 0 for r in range(28)) for v in B)
# Original graph cycle projection is the first five basis vectors;
# the exchange L has zero total directed edge flow.
flows = [[sum(c[j] for j, (ei, _) in enumerate(C1) if ei == k) for k in range(12)] for c in B]
assert all(x == 0 for x in flows[-1])
# Fundamental cycles use these five non-tree edges, each with coefficient +1 or -1.
non_tree_graph = [(2,3),(4,5),(4,6),(5,7),(6,7)]
graph_coeff = [[flows[i][eidx[e]] for e in non_tree_graph] for i in range(5)]
assert graph_coeff == [[-int(i==j) for j in range(5)] for i in range(5)]

R = [[d2[i][j] for j in range(42)] for i in non_tree]
Q = [[B[j][i] for j in range(6)] for i in non_tree]
F = [[R[r][c] for c in cols] + Q[r] for r in range(45)]
assert determinant(F) == -1
assert matrix_mul(proj, F) == [[int(i == j + 39) for i in range(45)] for j in range(6)]
# Full R is killed by the quotient projection, not merely its 39 selected columns.
assert all(all(x == 0 for x in row) for row in matrix_mul(proj, R))

# Three opposite-square-face product tori in top-dimensional homology.
tori = []
for k in range(3):
    rem = [i for i in range(3) if i != k]
    faces = []
    for bit in (0, 1):
        v = bit << k
        a, b = rem
        corners = [v, v^(1<<a), v^(1<<a)^(1<<b), v^(1<<b), v]
        faces.append(list(zip(corners, corners[1:])))
    c = [0] * 42
    for u, v in faces[0]:
        i = eidx[tuple(sorted((u, v)))];sgni=1 if u<v else -1
        for s, t in faces[1]:
            j=eidx[tuple(sorted((s,t)))];sgnj=1 if s<t else -1
            c[tidx[tuple(sorted((i,j)))]] += sgni*sgnj*(1 if i<j else -1)
    assert all(sum(d2[r][j]*c[j] for j in range(42)) == 0 for r in range(72))
    tori.append(c)
assert determinant([[tori[j][i] for j in range(3)] for i in (0,3,7)]) == 1
# The three cycles prove rank(d2)<=39. F minor proves rank(d2)>=39,
# and the 3x3 unit torus minor makes the top kernel integral, not just rational.

def graph_aut(p, t):
    return tuple(sum(((x >> k) & 1) << p[k] for k in range(3)) ^ t for x in V)

def edge_action(g):
    out = []
    for e, w in C1:
        u,v = E[e]
        nu,nv=g[u],g[v]
        index=oidx[(eidx[tuple(sorted((nu,nv)))],g[w])]
        out.append((index,1 if nu<nv else -1))
    return out

def square_action(g):
    out=[]
    for i,j in C2:
        u,v=E[i];s,t=E[j]
        uu,vv=g[u],g[v];ss,tt=g[s],g[t]
        ei=eidx[tuple(sorted((uu,vv)))];ej=eidx[tuple(sorted((ss,tt)))]
        out.append((tidx[tuple(sorted((ei,ej)))],(1 if uu<vv else -1)*(1 if ss<tt else -1)*(1 if ei<ej else -1)))
    return out

def act_on_vec(vec, action):
    r=[0]*len(vec)
    for j,(index,s) in enumerate(action):
        r[index]+=s*vec[j]
    return r

def homology1_action(g):
    action=edge_action(g)
    cols=[]
    for b in B:
        vec=act_on_vec(b,action)
        coords=[sum(proj[k][r]*vec[non_tree[r]] for r in range(45)) for k in range(6)]
        cols.append(coords)
    return [[cols[c][r] for c in range(6)] for r in range(6)]

def homology2_action(g):
    action=square_action(g)
    cols=[]
    # selected torus minor is a permutation matrix, so inversion is immediate.
    for b in tori:
        vec=act_on_vec(b,action)
        coords=[vec[7],vec[0],vec[3]]
        assert [sum(coords[j]*tori[j][i] for j in range(3)) for i in range(42)] == vec
        cols.append(coords)
    return [[cols[c][r] for c in range(3)] for r in range(3)]

def detperm(p):
    return (-1)**(sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)))

G={}; G2={}; metadata={}
for p in itertools.permutations(range(3)):
    for t in range(8):
        g=graph_aut(p,t)
        M=homology1_action(g)
        T=homology2_action(g)
        G[g]=M; G2[g]=T; metadata[g]=(p,t)
        expected2=[[((1 if ((t>>p[c])&1)==0 else -1) if r==p[c] else 0) for c in range(3)] for r in range(3)]
        assert T==expected2
        assert all(M[r][5]==0 for r in range(5))
        assert M[5][5]==detperm(p)*(-1)**t.bit_count()
assert len(G)==48

idp=(0,1,2);identity=graph_aut(idp,0)
a=graph_aut(idp,7)
flip=graph_aut(idp,1)
swap=graph_aut((1,0,2),0)
cycle=graph_aut((1,2,0),0)
expected_flip=[[-1,0,0,0,0,0], [0,-1,0,0,0,0], [0,0,0,1,0,0], [0,0,1,0,0,0], [0,0,0,0,-1,0], [0,0,0,0,0,-1]]
expected_swap=[[-1,0,0,-1,-1,0], [0,0,1,0,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0], [0,0,0,1,0,0], [0,0,0,0,0,-1]]
expected_cycle=[[0,-1,0,1,0,0], [0,0,-1,0,1,0], [1,0,0,0,0,0], [0,0,0,0,1,0], [0,0,0,-1,-1,0], [0,0,0,0,2,1]]
assert G[flip]==expected_flip and G[swap]==expected_swap and G[cycle]==expected_cycle
assert G[identity]==[[int(i==j) for j in range(6)] for i in range(6)]
# Group representation property, including every pair of the 48 automorphisms.
for g, mg in G.items():
    for h, mh in G.items():
        composite=tuple(g[h[x]] for x in V)
        assert matrix_mul(mg,mh)==G[composite]
        assert matrix_mul(G2[g],G2[h])==G2[composite]

# Equivariant exact sequence, non-split integral and unique rational splitting.
rows=[];targets=[]
for gen in (flip,swap,cycle):
    M=G[gen]
    A=[r[:5] for r in M[:5]]
    d=M[5][5]
    # Unknown row u must satisfy uA - d*u = b.
    for k in range(5):
        rows.append([A[j][k] - d*int(j==k) for j in range(5)])
        targets.append(M[5][k])
u=linear_solution(rows,targets,5)
assert u==[Fraction(-1,3), Fraction(1,3), Fraction(-1,3), Fraction(1,3), Fraction(-2,3)]
assert all((3*x).denominator==1 for x in u)
assert any(x.denominator==3 for x in u)
# The induced canonical extension therefore splits over Z[1/3], not over Z.

# Independent integral antipodal eigenlattice index certificate.
center=G[a]
plus=[[0,-1,-1],[0,1,1],[1,0,-1],[1,0,0],[0,1,0],[0,0,1]]
minus=[[0,-1,0],[0,-1,0],[-1,0,0],[1,0,0],[0,1,0],[0,0,1]]
assert matrix_mul(center,plus)==plus
assert matrix_mul(center,minus)==[[-x for x in row] for row in minus]
assert determinant([[plus[i][j] for j in range(3)]+[minus[i][j] for j in range(3)] for i in range(6)])==4
# Primitivity: each eigensublattice has a unit 3x3 coordinate minor.
assert abs(determinant([plus[i] for i in (3,4,5)]))==1
assert abs(determinant([minus[i] for i in (2,4,5)]))==1

print('VERIFY_OK cells=28,72,42 H=(1,6,3) G=48 quotient_unit_minor=-1 torus_basis=3 extension_denominator=3 central_gluing_index=4')
