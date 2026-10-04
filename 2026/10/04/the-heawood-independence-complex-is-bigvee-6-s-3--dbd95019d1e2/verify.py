#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque

# Heawood graph as the point-line incidence graph of the Fano plane.
# Vertices 0,...,6 are points p_i; 7,...,13 are lines l_i.
N = 14
edges = set()
for i in range(7):
    for d in (0, 1, 3):
        j = (i + d) % 7
        edges.add(tuple(sorted((j, 7 + i))))
assert len(edges) == 21

def independent(mask):
    return all(not ((mask >> a) & 1 and (mask >> b) & 1) for a,b in edges)

faces = [m for m in range(1 << N) if independent(m)]
counts = Counter(m.bit_count() for m in faces)
expected = {0:1,1:14,2:70,3:154,4:147,5:56,6:14,7:2}
assert dict(counts) == expected, (dict(counts), expected)
assert len(faces) == 458

# Sequential vertex matching: at pivot v, pair every currently unmatched
# sigma not containing v with sigma union {v} whenever both are unmatched.
unmatched = set(faces)
pairs = []
for v in range(N):
    bit = 1 << v
    lows = []
    for m in list(unmatched):
        if m & bit:
            continue
        up = m | bit
        if up in unmatched:
            lows.append(m)
    for lo in lows:
        up = lo | bit
        if lo in unmatched and up in unmatched:
            unmatched.remove(lo)
            unmatched.remove(up)
            pairs.append((lo, up, v))

expected_critical = {
    sum(1 << x for x in (7,9,10,11)),
    sum(1 << x for x in (7,8,10,12)),
    sum(1 << x for x in (7,8,11,12)),
    sum(1 << x for x in (7,9,10,13)),
    sum(1 << x for x in (7,9,11,13)),
    sum(1 << x for x in (7,8,12,13)),
}
assert unmatched == expected_critical, sorted(unmatched)
assert all(m.bit_count() == 4 for m in unmatched)
assert len(pairs) == (len(faces)-6)//2
assert 0 not in unmatched

# Acyclicity check by orienting every unmatched Hasse cover upward and every
# matched cover downward, then topologically sorting the complete directed graph.
index = {m:i for i,m in enumerate(faces)}
matched = {(lo,up) for lo,up,_ in pairs}
adj = [[] for _ in faces]
indeg = [0] * len(faces)
for up in faces:
    for v in range(N):
        if (up >> v) & 1:
            lo = up & ~(1 << v)
            a,b = (up,lo) if (lo,up) in matched else (lo,up)
            ia,ib = index[a],index[b]
            adj[ia].append(ib)
            indeg[ib] += 1
q = deque(i for i,d in enumerate(indeg) if d == 0)
seen = 0
while q:
    i = q.popleft(); seen += 1
    for j in adj[i]:
        indeg[j] -= 1
        if indeg[j] == 0:
            q.append(j)
assert seen == len(faces), (seen, len(faces))

# Independent simplicial homology check over F_2.
bydim = {k:[tuple(c) for c in combinations(range(N), k+1)
             if independent(sum(1 << x for x in c))] for k in range(7)}

def rank_f2(columns):
    piv = {}
    rank = 0
    for x in columns:
        while x:
            p = x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                rank += 1
                break
    return rank

ranks = {}
for k in range(1,7):
    lower = {f:i for i,f in enumerate(bydim[k-1])}
    cols = []
    for f in bydim[k]:
        col = 0
        for i in range(len(f)):
            g = f[:i] + f[i+1:]
            col ^= 1 << lower[g]
        cols.append(col)
    ranks[k] = rank_f2(cols)
assert ranks == {1:13,2:57,3:97,4:44,5:12,6:2}, ranks
bettis = {}
for k in range(7):
    bettis[k] = len(bydim[k]) - ranks.get(k,0) - ranks.get(k+1,0)
assert bettis == {0:1,1:0,2:0,3:6,4:0,5:0,6:0}, bettis

# The comparison graph G_7^3 from the cyclic-neighborhood regular-bipartite
# family has the explicit 4-cycle a0-b0-a6-b1-a0, so it is not Heawood.
def g73_edge(a,b):
    # a in 0..6 and b in 0..6; neighbors b_a,b_{a+1},b_{a+2}
    return (b-a) % 7 in (0,1,2)
assert g73_edge(0,0) and g73_edge(6,0) and g73_edge(6,1) and g73_edge(0,1)
# Heawood has no 4-cycle because distinct point vertices have exactly one common line.
for x,y in combinations(range(7),2):
    common = 0
    for i in range(7):
        if tuple(sorted((x,7+i))) in edges and tuple(sorted((y,7+i))) in edges:
            common += 1
    assert common == 1

print('HEAWOOD_INDEPENDENCE_VERIFY_OK')
print('face_counts', [expected[k] for k in range(8)])
print('critical_3_cells', 6)
print('f2_betti', [bettis[k] for k in range(7)])
