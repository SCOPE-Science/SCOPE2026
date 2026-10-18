#!/usr/bin/env python3
"""Independent exhaustive face recursion and mod-two homology verification.
Only the Python standard library is needed. Does not reuse the Morse algorithm.
"""
from collections import Counter

# Separate construction: each triangle is a clique and corresponding points
# on the two triangles are connected by three vertical edges.
EDGES = []
for layer in (0, 3):
    for u in range(layer, layer + 3):
        for v in range(u + 1, layer + 3):
            EDGES.append((u, v))
for k in range(3):
    EDGES.append((k, k + 3))
ARCS = sorted((a, b) for u, v in EDGES for a, b in ((u, v), (v, u)))
assert len(ARCS) == 18

faces = []

def recurse(i, mask, incoming, outgoing, nxt):
    if i == len(ARCS):
        faces.append(mask)
        return
    recurse(i + 1, mask, incoming, outgoing, nxt)
    u, v = ARCS[i]
    if incoming[v] or outgoing[u]:
        return
    # Adding u->v creates a directed cycle precisely when v already reaches u.
    w = v
    while w != -1:
        if w == u:
            return
        w = nxt[w]
    incoming[v] = outgoing[u] = 1
    nxt[u] = v
    recurse(i + 1, mask | (1 << i), incoming, outgoing, nxt)
    nxt[u] = -1
    incoming[v] = outgoing[u] = 0


recurse(0, 0, [0] * 6, [0] * 6, [-1] * 6)
assert len(faces) == 687 and len(set(faces)) == 687
by_dimension = {d: sorted(f for f in faces if f.bit_count() == d + 1)
                for d in range(5)}
fvec = [len(by_dimension[d]) for d in range(5)]
assert fvec == [18, 108, 260, 240, 60]


def rank_gf2(columns):
    pivot = {}
    for v in columns:
        while v:
            k = v.bit_length() - 1
            if k in pivot:
                v ^= pivot[k]
            else:
                pivot[k] = v
                break
    return len(pivot)


ranks = {}
for d in (1, 2, 3, 4):
    index = {face: idx for idx, face in enumerate(by_dimension[d - 1])}
    columns = []
    for face in by_dimension[d]:
        column = 0
        for vertex in range(18):
            if face & (1 << vertex):
                column ^= 1 << index[face ^ (1 << vertex)]
        columns.append(column)
    ranks[d] = rank_gf2(columns)
assert [ranks[d] for d in (1, 2, 3, 4)] == [17, 91, 164, 54]
betti = [fvec[d] - ranks.get(d, 0) - ranks.get(d + 1, 0)
         for d in range(5)]
assert betti == [1, 0, 5, 22, 6]

# Independent chain-level Lefschetz computation for 12 graph automorphisms.
loc = {a: j for j, a in enumerate(ARCS)}

def vertex_map(u, rot, reflection, exchange):
    return (((-1 if reflection else 1) * (u % 3) + rot) % 3) + 3 * ((u // 3) ^ exchange)


def simplex_trace(perm, dim):
    trace = 0
    for face in by_dimension[dim]:
        old = [i for i in range(18) if face & (1 << i)]
        images = [perm[i] for i in old]
        if sum(1 << i for i in images) != face:
            continue
        trace += (-1) ** sum(images[i] > images[j]
                             for i in range(len(images))
                             for j in range(i + 1, len(images)))
    return trace


expected_homology_characters = {
    (0, 0, 0): (5, 22, 6),
    (0, 0, 1): (1, 2, 0),
    (1, 0, 0): (5, 4, 0),
    (1, 0, 1): (1, 2, 0),
    (0, 1, 0): (-1, 0, 0),
    (0, 1, 1): (-1, 0, -2),
    (1, 1, 0): (-1, 0, 0),
    (1, 1, 1): (-1, 0, -2),
}
for rot in range(3):
    for reflection in range(2):
        for exchange in range(2):
            p = [loc[vertex_map(u, rot, reflection, exchange),
                     vertex_map(v, rot, reflection, exchange)] for u, v in ARCS]
            actual_reduced_L = sum(((-1) ** dim) * simplex_trace(p, dim)
                                   for dim in range(5)) - 1
            types = (0 if rot == 0 else 1, reflection, exchange)
            h2, h3, h4 = expected_homology_characters[types]
            assert actual_reduced_L == h2 - h3 + h4

print('recursive_face_count_including_empty:', len(faces))
print('dim_0_through_4:', fvec)
print('mod_two_boundary_ranks_d1_through_d4:', [ranks[d] for d in range(1, 5)])
print('mod_two_betti_0_through_4:', betti)
print('signed_Lefschetz_identity_all_twelve: PASS')
