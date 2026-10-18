#!/usr/bin/env python3
"""Independent direct simplicial boundary ranks over F2 for a graph complex.

Requires only Python's standard library; avoids the Morse pairing entirely.
"""
from collections import defaultdict
EDGES = [(0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),
         (3,4),(3,10),(4,5),(4,15),(5,6),(6,7),(6,11),
         (7,8),(7,14),(8,9),(9,10),(9,16),(10,11),(11,12),
         (12,13),(12,17),(13,14),(14,15),(15,16),(16,17)]
N=18
adj = [0]*N
for i,j in EDGES:
    adj[i] |= 1<<j
    adj[j] |= 1<<i
# Deliberately independently scan all induced vertex degrees on all subsets.
faces_by_size = defaultdict(list)
for s in range(1,1<<N):
    if all((adj[v] & s).bit_count() <= 1
           for v in range(N) if s & (1<<v)):
        faces_by_size[s.bit_count()].append(s)
face_counts = [len(faces_by_size[k]) for k in range(1,11)]
assert face_counts == [18,153,762,2394,4806,6027,4428,1728,308,27]
rank = {0:0}
for k in range(2,11):
    lower_indices = {s:i for i,s in enumerate(faces_by_size[k-1])}
    basis = {}
    for hi in faces_by_size[k]:
        vec=0
        for v in range(N):
            if hi & (1<<v):
                vec ^= 1 << lower_indices[hi ^ (1<<v)]
        while vec:
            pivot=vec.bit_length()-1
            if pivot in basis:
                vec ^= basis[pivot]
            else:
                basis[pivot] = vec
                break
    rank[k-1] = len(basis)
expected_ranks = [17,136,626,1768,3038,2980,1447,281,27]
assert [rank[k] for k in range(1,10)] == expected_ranks
betti = {}
for dim in range(10):
    k = dim+1
    value = face_counts[dim] - rank.get(dim,0) - rank.get(dim+1,0)
    if dim == 0:
        value -= 1  # reduced H0 (connected complex)
    if value:
        betti[dim] = value
assert betti == {5:9,6:1},betti
print('faces=20651 f_vector=' + str(face_counts))
print('boundary_ranks_mod2=' + str(expected_ranks))
print('reduced_mod2_betti=' + str(betti))
print('PASS')
