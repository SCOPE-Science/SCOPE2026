#!/usr/bin/env python3
"""Exact, dependency-free verification of a graph-path simplicial complex.

The undirected graph is specified by its bipartite incidence rule.  Faces are
stored as 18-bit masks of graph edges.  Acyclicity is independently certified
by topological sorting the entire reversed-matching Hasse digraph.
"""
from collections import Counter, deque
from itertools import permutations
from math import factorial

N = 11
E = sorted(
    (i, 5+j)
    for j in range(6)
    for i in list(k for k in range(3) if k != j % 3) + [3+j % 2]
)
assert len(E) == 18 and len(set(E)) == 18
EI = {e:i for i,e in enumerate(E)}
ADJ = [set() for _ in range(N)]
for a,b in E:
    ADJ[a].add(b)
    ADJ[b].add(a)
assert sorted(map(len, ADJ)) == [3]*8+[4]*3
assert all(a < 5 <= b for a,b in E)

# Every oriented spanning simple path is visited by this exhaustive DFS.
facets = set()
oriented_paths = 0
def dfs(path, visited, edge_mask):
    global oriented_paths
    if len(path) == N:
        oriented_paths += 1
        assert edge_mask.bit_count() == N-1
        facets.add(edge_mask)
        return
    last = path[-1]
    for nxt in ADJ[last]:
        if not (visited >> nxt) & 1:
            e = tuple(sorted((last, nxt)))
            dfs(path + (nxt,), visited | (1 << nxt), edge_mask | (1 << EI[e]))
for start in range(N):
    dfs((start,), 1 << start, 0)
assert oriented_paths == 444 and len(facets) == 222

# Independent Held--Karp dynamic-programming count, with no path DFS reuse.
dp = {(1<<s, s):1 for s in range(N)}
for size in range(1, N):
    q = {}
    for (subset,v), count in dp.items():
        assert subset.bit_count() == size
        for w in ADJ[v]:
            if not (subset >> w) & 1:
                key = (subset | (1<<w), w)
                q[key] = q.get(key, 0) + count
    dp = q
assert sum(dp.values()) == 444

faces = {0}
for facet in facets:
    sub = facet
    while sub:
        faces.add(sub)
        sub = (sub-1) & facet
nonempty = faces - {0}
fvector = [sum(mask.bit_count() == i for mask in nonempty) for i in range(1, 11)]
assert fvector == [18,153,796,2742,6402,9913,9738,5694,1776,222]
assert len(nonempty) == 37454
assert sum((-1)**(i-1)*fvector[i-1] for i in range(1,11)) == 6

# Explicit element-toggle matching; zero mask is excluded so one 0-cell remains.
vertex_order = (6,12,16,13,9,11,5,0,2,4,14,3,15,1,10,8,17,7)
remaining = set(nonempty)
pair_up = {}  # lower face -> its unique upper matched face
for vertex in vertex_order:
    bit = 1 << vertex
    for face in tuple(remaining):
        if not face & bit and (face | bit) in remaining:
            remaining.remove(face)
            remaining.remove(face | bit)
            pair_up[face] = face | bit
assert len(pair_up) == 18724
assert len(remaining) == 6
crit_counts = Counter(mask.bit_count()-1 for mask in remaining)
assert crit_counts == {0:1, 6:5}, crit_counts

# Independent global acyclicity certificate: each unmatched codimension-one
# incidence points down, and every matched incidence points up.
indegree = {mask:0 for mask in nonempty}
out = {mask:[] for mask in nonempty}
incidence_count = 0
for upper in nonempty:
    bmask = upper
    while bmask:
        bit = bmask & -bmask
        bmask -= bit
        lower = upper ^ bit
        if lower == 0:
            continue
        incidence_count += 1
        if pair_up.get(lower) == upper:
            out[lower].append(upper)
            indegree[upper] += 1
        else:
            out[upper].append(lower)
            indegree[lower] += 1
assert incidence_count == 237072, incidence_count
q = deque(mask for mask,deg in indegree.items() if deg == 0)
visited = 0
while q:
    face = q.popleft()
    visited += 1
    for nxt in out[face]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)
assert visited == len(nonempty), (visited,len(nonempty))

# The complete graph automorphism group consists of all permutations of the
# three degree-four vertices and an independent flip of vertices 3 and 4.
# Right-side vertices j are uniquely determined by (j mod 3, j mod 2).
def edge_action(sigma, flip):
    V = {0:sigma[0], 1:sigma[1], 2:sigma[2], 3:3+flip,4:4-flip}
    for j in range(6):
        k = next(k for k in range(6)
                 if k % 3 == sigma[j%3] and k % 2 == (j%2)^flip)
        V[5+j] = 5+k
    mapped_edges = [EI[tuple(sorted((V[a],V[b])))] for a,b in E]
    assert len(set(mapped_edges)) == 18
    return mapped_edges

def sign_of_permutation(v):
    inversions = sum(v[i] > v[j] for i in range(len(v))
                     for j in range(i+1,len(v)))
    return -1 if inversions & 1 else 1

character = {}
for sigma in permutations(range(3)):
    for flip in (0,1):
        action = edge_action(sigma,flip)
        trace = 0
        fixed = 0
        for face in nonempty:
            mapped = [action[i] for i in range(18) if face & (1<<i)]
            image = sum(1 << k for k in mapped)
            if image != face:
                continue
            fixed += 1
            trace += (-1 if (face.bit_count()-1)%2 else 1) * sign_of_permutation(mapped)
        # Ordinary Lefschetz: L=1+tr(H_6) because reduced homology is in degree 6.
        chi_6 = trace - 1
        fixed_high = sum(sigma[i] == i for i in range(3))
        expected = {
            (3,0):5,(3,1):1,
            (1,0):-1,(1,1):-1,
            (0,0):-1,(0,1):1
        }[(fixed_high, flip)]
        assert chi_6 == expected, (sigma, flip, chi_6, expected)
        character[(tuple(sigma),flip)] = chi_6
assert len(character) == 12
assert sum(character.values()) == 0   # No full-group fixed vector.
# Since the character of S_3 standard equals fixed_high-1 and sign is
# (-1)^(3 - #cycles), the decomposition is
# (sgn + std) tensor trivial_C2 + std tensor sign_C2.
for (sigma,flip), actual in character.items():
    inversions = sum(sigma[i]>sigma[j] for i in range(3) for j in range(i+1,3))
    sgn = (-1)**inversions
    std = sum(sigma[i]==i for i in range(3))-1
    assert actual == sgn + std*(1+(-1)**flip)

print('VERIFY_OK')
print('oriented_spanning_paths',oriented_paths)
print('undirected_spanning_paths',len(facets))
print('nonempty_faces',len(nonempty))
print('f_vector',fvector)
print('morse_pairs',len(pair_up))
print('critical_cells',dict(sorted(crit_counts.items())))
print('nonempty_hasse_incidences',incidence_count)
print('acyclic_vertices_toposorted',visited)
print('S3_times_C2_character_classes',
      'id=5,transposition=-1,threecycle=-1,central=1,central_transposition=-1,central_threecycle=1')
print('full_group_invariant_dimension',0)
