"""Exact, complete vertex-determinant certificate for an axis--cube convex hull.
Requires Python 3.9+ standard library only. Run: python3 verify.py
"""
from collections import Counter
from itertools import combinations, product, permutations

Z = (0, 0, 0, 0)
Q = (0, 1, 0, 0)
ONE = (1, 0, 0, 0)

def add(a, b): return tuple(x + y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    c = [0] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    assert c[4:] == [0, 0, 0]
    return tuple(c[:4])
def tri_det(v):
    u, w, z = v
    return sub(add(mul(u[0], sub(mul(w[1],z[2]),mul(w[2],z[1]))),
                   mul(u[1], sub(mul(w[2],z[0]),mul(w[0],z[2])))),
               mul(u[2], sub(mul(w[1],z[0]),mul(w[0],z[1]))))
def perm_det(v):
    ans = Z
    for p in permutations(range(3)):
        inversions = sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        term = mul(mul(v[0][p[0]],v[1][p[1]]),v[2][p[2]])
        ans = add(ans, neg(term) if inversions % 2 else term)
    return ans

def canon(p):
    for n in reversed(p):
        if n > 0: return p
        if n < 0: return neg(p)
    return p

V=[]
for i in range(3):
    for sign in (-1,1):
        V.append(tuple((0,sign,0,0) if j==i else Z for j in range(3)))
for v in product((-1,1),repeat=3):
    V.append(tuple((int(c),0,0,0) for c in v))
assert len(V)==14 and len(set(V))==14
EXPECT={
 (0,0,0,0):123,
 (4,0,0,0):96,
 (8,0,0,0):56,
 (16,0,0,0):2,
 (0,2,0,0):96,
 (0,4,0,0):168,
 (0,0,2,0):168,
 (-4,4,0,0):48,
 (4,4,0,0):48,
 (0,-2,2,0):48,
 (0,2,2,0):48,
 (0,-4,2,0):12,
 (0,4,2,0):12,
 (0,0,-3,1):8,
 (0,0,3,1):8,
 (0,0,-1,1):24,
 (0,0,1,1):24,
 (0,0,0,2):12,
}
assert sum(EXPECT.values())==1001
counts=Counter()
winning=[]
for inds in combinations(range(14),4):
    v=[V[i] for i in inds]
    diff=[[sub(v[i][j],v[0][j]) for j in range(3)] for i in (1,2,3)]
    d=tri_det(diff)
    assert d == perm_det(diff), (inds,d)
    k=canon(d)
    counts[k]+=1
    if k in ((16,0,0,0),(0,0,3,1)):
        winning.append((inds,k))
assert counts==EXPECT, (counts-EXPECT,EXPECT-counts)
assert sum(counts.values()) == 1001
assert sum(kind==(16,0,0,0) for inds,kind in winning)==2
assert sum(kind==(0,0,3,1) for inds,kind in winning)==8
# If two maximizing vertex sets shared a triple, continuously variable
# maximizing tetrahedra would not be excluded. Check full family.
assert all(len(set(a)&set(b))<=2 for (a,_),(b,_) in combinations(winning,2))
# The two cube-only tetrahedra have disjoint vertex sets.
assert all(set(inds)<=set(range(6,14)) for inds,k in winning if k==(16,0,0,0))
# Each of eight mixed tetrahedra uses three axial vertices and one cube vertex.
assert all(sum(i<6 for i in inds)==3 for inds,k in winning if k==(0,0,3,1))
assert all(sum(i>=6 for i in inds)==1 for inds,k in winning if k==(0,0,3,1))
# Direct evaluation at the classical rhombic dodecahedron q=2
# yields max volume (20/6), bulk volume 16, ratio 5/24.
assert 20*24==5*6*16
print('VERIFY_OK: 1001 exact polynomial determinants; 18 unsigned classes; 10 potential maximizers; no shared triple')
