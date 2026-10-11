#!/usr/bin/env python3
from functools import lru_cache
from collections import defaultdict
import json

# Standard 5-regular Clebsch / Greenwood-Gleason graph:
# even-weight vectors of F_2^5; adjacency at Hamming distance 4.
V = [x for x in range(32) if x.bit_count() % 2 == 0]
index = {x:i for i,x in enumerate(V)}
E = []
for i,a in enumerate(V):
    for j in range(i+1,len(V)):
        b = V[j]
        if (a ^ b).bit_count() == 4:
            E.append((i,j))
assert len(V) == 16 and len(E) == 40
adj = [set() for _ in V]
for u,v in E:
    adj[u].add(v); adj[v].add(u)
assert all(len(adj[u]) == 5 for u in range(16))
# Strongly regular parameters (16,5,0,2).
for u in range(16):
    for v in range(u+1,16):
        c = len(adj[u] & adj[v])
        if v in adj[u]:
            assert c == 0
        else:
            assert c == 2

# Exhaustively enumerate all matchings as edge masks.
m = len(E)
faces_by_size = defaultdict(list)
def enum_edges(i, used_vertices, edge_mask):
    if i == m:
        faces_by_size[edge_mask.bit_count()].append(edge_mask)
        return
    enum_edges(i+1, used_vertices, edge_mask)
    u,v = E[i]
    if not ((used_vertices >> u) & 1 or (used_vertices >> v) & 1):
        enum_edges(i+1, used_vertices | (1<<u) | (1<<v), edge_mask | (1<<i))
enum_edges(0,0,0)
face_counts = [len(faces_by_size[s]) for s in range(0,9)]
expected_counts = [1,40,620,4760,19190,39640,37740,12840,705]
assert face_counts == expected_counts, (face_counts, expected_counts)

# Independent matching-polynomial count by vertex-deletion recurrence.
edge_exists = [[False]*16 for _ in range(16)]
for u,v in E:
    edge_exists[u][v]=edge_exists[v][u]=True
@lru_cache(None)
def matching_poly(vertices_mask):
    if vertices_mask == 0:
        return (1,)
    lb = vertices_mask & -vertices_mask
    v = lb.bit_length()-1
    rest = vertices_mask ^ lb
    p0 = matching_poly(rest)
    out = list(p0)
    for u in range(16):
        if ((rest >> u) & 1) and edge_exists[v][u]:
            pu = matching_poly(rest ^ (1<<u))
            if len(out) < len(pu)+1:
                out.extend([0]*(len(pu)+1-len(out)))
            for k,a in enumerate(pu):
                out[k+1] += a
    return tuple(out)
poly = matching_poly((1<<16)-1)
assert list(poly) == expected_counts

# Exact boundary matrices over F_2, columns represented as arbitrary-size ints.
def boundary_columns(size):
    # C_{size-1} -> C_{size-2}; size is cardinality of upper simplex.
    lows = faces_by_size[size-1]
    idx = {f:i for i,f in enumerate(lows)}
    cols = []
    for f in faces_by_size[size]:
        vec = 0
        x = f
        while x:
            b = x & -x
            x ^= b
            vec ^= 1 << idx[f ^ b]
        cols.append(vec)
    return cols, len(lows)

def gf2_rank_high(cols):
    basis = {}
    for x in cols:
        while x:
            p = x.bit_length()-1
            y = basis.get(p)
            if y is None:
                basis[p] = x
                break
            x ^= y
    return len(basis)

def gf2_rank_low(cols):
    basis = {}
    for x in cols:
        while x:
            b = x & -x
            p = b.bit_length()-1
            y = basis.get(p)
            if y is None:
                basis[p] = x
                break
            x ^= y
    return len(basis)

ranks = {0:0}
rank_list = []
for size in range(2,9):
    cols, nrows = boundary_columns(size)
    rh = gf2_rank_high(cols)
    rl = gf2_rank_low(cols)
    assert rh == rl
    ranks[size-1] = rh
    rank_list.append(rh)
expected_ranks = [39,581,4179,15011,24629,12135,705]
assert rank_list == expected_ranks, (rank_list, expected_ranks)

# Explicit d^2=0 parity check on every simplex of cardinality >= 3.
for size in range(3,9):
    for f in faces_by_size[size]:
        parity = {}
        bits=[]; x=f
        while x:
            b=x & -x; x ^= b; bits.append(b)
        for i in range(len(bits)):
            for j in range(len(bits)):
                if i==j: continue
                h=f ^ bits[i] ^ bits[j]
                parity[h] = parity.get(h,0)^1
        assert not any(parity.values())

betti_red = []
for d in range(8):
    c = len(faces_by_size[d+1])
    rd = ranks.get(d,0)
    rup = ranks.get(d+1,0)
    h = c - rd - rup
    if d == 0:
        h -= 1
    betti_red.append(h)
expected_betti = [0,0,0,0,0,976,0,0]
assert betti_red == expected_betti, (betti_red, expected_betti)
chi_red = -1 + sum(((-1)**d)*len(faces_by_size[d+1]) for d in range(8))
assert chi_red == -976
assert chi_red == sum(((-1)**d)*b for d,b in enumerate(betti_red))

out = {
    "graph": {"vertices":16,"edges":40,"degree":5,"srg":[16,5,0,2]},
    "matching_face_counts_including_empty": face_counts,
    "simplicial_boundary_ranks_mod2_Cd_to_Cdminus1": expected_ranks,
    "reduced_betti_mod2_degrees_0_through_7": betti_red,
    "reduced_euler_characteristic": chi_red,
    "independent_matching_polynomial_recurrence": list(poly),
}
print(json.dumps(out, sort_keys=True))
print("VERIFY_OK")
