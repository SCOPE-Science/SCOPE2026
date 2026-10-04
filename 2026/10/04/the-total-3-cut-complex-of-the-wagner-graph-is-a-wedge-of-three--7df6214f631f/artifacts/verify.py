#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque

V = tuple(range(8))
edges = {tuple(sorted((i, (i + 1) % 8))) for i in V}
edges |= {tuple(sorted((i, (i + 4) % 8))) for i in range(4)}

def independent(S):
    S = set(S)
    return all(not ({a, b} <= S) for a, b in edges)

ind3 = [c for c in combinations(V, 3) if independent(c)]
expected_ind3 = [
    (0, 2, 5), (0, 3, 5), (0, 3, 6), (1, 3, 6),
    (1, 4, 6), (1, 4, 7), (2, 4, 7), (2, 5, 7),
]
assert ind3 == expected_ind3
facets = [tuple(sorted(set(V) - set(c))) for c in ind3]
faces = set()
for F in facets:
    for r in range(1, len(F) + 1):
        faces.update(combinations(F, r))
face_vector = tuple(sum(len(F) == r for F in faces) for r in range(1, 6))
assert face_vector == (8, 28, 48, 32, 8)

# Greedy vertex matching on the nonempty face poset, vertices in order 0,...,7.
unmatched = set(faces)
pairs = []
for v in V:
    lows = sorted((F for F in unmatched if v not in F), key=lambda F: (len(F), F))
    for F in lows:
        if F not in unmatched:
            continue
        U = tuple(sorted(F + (v,)))
        if U in unmatched:
            pairs.append((F, U, v))
            unmatched.remove(F)
            unmatched.remove(U)
critical = sorted(unmatched, key=lambda F: (len(F), F))
assert len(pairs) == 60
assert critical == [(0,), (1, 2, 5), (1, 2, 6), (1, 3, 7)]

# Exhaustively verify acyclicity of the Morse orientation of every Hasse edge.
matched = {(L, U) for L, U, _ in pairs}
adj = defaultdict(list)
indegree = {F: 0 for F in faces}
edge_count = 0
for U in faces:
    if len(U) < 2:
        continue
    for j in range(len(U)):
        L = U[:j] + U[j + 1:]
        if L not in faces:
            continue
        edge_count += 1
        if (L, U) in matched:
            src, dst = L, U
        else:
            src, dst = U, L
        adj[src].append(dst)
        indegree[dst] += 1
assert edge_count == 368
q = deque(sorted((F for F, d in indegree.items() if d == 0), key=lambda F: (len(F), F)))
seen = 0
while q:
    F = q.popleft()
    seen += 1
    for G in adj[F]:
        indegree[G] -= 1
        if indegree[G] == 0:
            q.append(G)
assert seen == len(faces) == 124

# Independent mod-2 homology check of the same complex.
def gf2_rank(columns):
    basis = {}
    rank = 0
    for x in columns:
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                rank += 1
                break
    return rank

by_dim = {d: sorted(F for F in faces if len(F) == d + 1) for d in range(5)}
ranks = []
for d in range(1, 5):
    rows = {F: i for i, F in enumerate(by_dim[d - 1])}
    cols = []
    for U in by_dim[d]:
        bits = 0
        for j in range(len(U)):
            L = U[:j] + U[j + 1:]
            bits ^= 1 << rows[L]
        cols.append(bits)
    ranks.append(gf2_rank(cols))
assert tuple(ranks) == (7, 21, 24, 8)
betti = []
for d in range(5):
    dim_cd = len(by_dim[d])
    rank_d = 0 if d == 0 else ranks[d - 1]
    rank_next = 0 if d == 4 else ranks[d]
    betti.append(dim_cd - rank_d - rank_next)
assert tuple(betti) == (1, 0, 3, 0, 0)
assert sum((-1) ** d * len(by_dim[d]) for d in range(5)) == 4

print('independent_triples=8')
print('face_vector=(8,28,48,32,8)')
print('matching_pairs=60 critical=(1 in dim0, 3 in dim2)')
print('morse_orientation_DAG=124/124 hasse_edges=368')
print('mod2_boundary_ranks=(7,21,24,8) betti=(1,0,3,0,0)')
print('VERIFY_OK')
