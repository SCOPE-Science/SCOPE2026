#!/usr/bin/env python3
"""Exact finite verification of the independence complexes of the four (28,12,6,4) graphs.

Only the Python standard library is used. Graph vertices are the 28 edges of K_8.
"""
from itertools import combinations
from collections import Counter

VERTICES = list(combinations(range(8), 2))
INDEX = {v: i for i, v in enumerate(VERTICES)}
SWITCH = {
    "triangular": (),
    "matching": ((0,1), (2,3), (4,5), (6,7)),
    "eight_cycle": tuple(tuple(sorted((i, (i+1) % 8))) for i in range(8)),
    "three_plus_five": ((0,1), (1,2), (0,2), (3,4), (4,5), (5,6), (6,7), (3,7)),
}
EXPECTED = {"triangular": (105, 132), "matching": (73,164),
            "eight_cycle": (65,172), "three_plus_five": (65,172)}

def make_graph(switch_edges):
    chosen = {INDEX[tuple(sorted(p))] for p in switch_edges}
    adjacent = [[False]*28 for _ in range(28)]
    for i,j in combinations(range(28),2):
        old = bool(set(VERTICES[i]) & set(VERTICES[j]))
        new = old ^ ((i in chosen) != (j in chosen))
        adjacent[i][j] = adjacent[j][i] = new
    return adjacent

def enumerate_independent(adjacent):
    # Each independent face is visited exactly once in increasing vertex order.
    neighbors = [sum((1<<j) for j in range(28) if adjacent[i][j]) for i in range(28)]
    faces = {-1:[()],0:[],1:[],2:[],3:[],4:[]}
    def visit(prefix, available):
        while available:
            bit = available & -available
            i = bit.bit_length()-1
            available ^= bit
            f = prefix+(i,)
            assert len(f) <= 5
            faces[len(f)-1].append(f)
            visit(f, available & ~neighbors[i])
    visit((), (1<<28)-1)
    return faces

def rank_over_F2(columns):
    basis={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p]=x
                break
    return len(basis)

def test_one(name, switch_edges):
    g=make_graph(switch_edges)
    deg=[sum(row) for row in g]
    assert set(deg)=={12}
    for i,j in combinations(range(28),2):
        common = sum(g[i][k] and g[j][k] for k in range(28))
        assert common == (6 if g[i][j] else 4)
    f=enumerate_independent(g)
    counts=tuple(len(f[d]) for d in range(5))
    assert counts[:3] == (28,210,420), (name,counts)
    assert counts[4]==0, (name,"an independent quintuple exists")
    triangles={t:i for i,t in enumerate(f[2])}
    edges={e:i for i,e in enumerate(f[1])}
    # Over F_2, the boundary of (a,b,c) is (b,c)+(a,c)+(a,b).
    columns=[sum(1<<edges[sub] for sub in combinations(t,2)) for t in f[2]]
    r2=rank_over_F2(columns)
    assert r2==183, (name,r2)
    # Every triangle extends to at most one tetrahedron, so ∂_3 is split injective over Z.
    extension_count=Counter(sub for tet in f[3] for sub in combinations(tet,3))
    assert all(x==1 for x in extension_count.values())
    assert len(extension_count)==4*len(f[3])
    # Confirm ∂_1∂_2=0 and ∂_2∂_3=0 by exact bit parity.
    for tri in f[2]:
        vertex_boundary=0
        for e in combinations(tri,2):
            vertex_boundary ^= (1<<e[0]) ^ (1<<e[1])
        assert vertex_boundary == 0
    for tet in f[3]:
        edge_boundary=0
        for sub in combinations(tet,3):
            edge_boundary ^= columns[triangles[sub]]
        assert edge_boundary == 0
    # The complement's one-skeleton is connected, so rank ∂_1=27.
    seen={0};todo=[0]
    while todo:
        i=todo.pop()
        for j in range(28):
            if not g[i][j] and i!=j and j not in seen:
                seen.add(j);todo.append(j)
    assert len(seen)==28
    # rank_Q ∂_2 is ≥ its rank mod 2, and ≤ dim ker ∂_1=210-27=183.
    # The split-injective ∂_3 has rank equal to the number of tetrahedra.
    h2=420-183-len(f[3])
    assert (len(f[3]),h2)==EXPECTED[name]
    print(f"{name}: f=(28,210,420,{len(f[3])}), rank_d1=27, rank_d2=183, rank_d3={len(f[3])}, H2_Z_rank={h2}, unique_triangle_faces={4*len(f[3])}")

if __name__=="__main__":
    for name, selected in SWITCH.items():
        test_one(name, selected)
    print("ALL FOUR GRAPH COMPUTATIONS VERIFIED")
