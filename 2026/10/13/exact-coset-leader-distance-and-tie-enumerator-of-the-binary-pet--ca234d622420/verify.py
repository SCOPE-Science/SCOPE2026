#!/usr/bin/env python3
"""Exact syndrome-geometry check for the Petersen binary cycle code.

Two independent shortest-distance calculations are performed: a full edge-subset
census and a breadth-first search in the 512-syndrome graph. The latter also
counts shortest paths and hence shortest error supports.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from math import factorial

V = list(combinations(range(5), 2))
E = [(i, j) for i in range(10) for j in range(i+1, 10)
     if set(V[i]).isdisjoint(V[j])]
assert len(V) == 10 and len(E) == 15
edge_syndromes = [(1 << i) | (1 << j) for i, j in E]

# Census of every binary error pattern, not merely a sample.
size = 1 << len(E)
syn = [0] * size
min_weight = [99] * (1 << len(V))
leader_count = [0] * (1 << len(V))
weight_of_zero_syndrome = Counter()
for word in range(size):
    if word:
        low = word & -word
        syn[word] = syn[word ^ low] ^ edge_syndromes[low.bit_length()-1]
    s = syn[word]
    w = word.bit_count()
    if w < min_weight[s]:
        min_weight[s] = w
        leader_count[s] = 1
    elif w == min_weight[s]:
        leader_count[s] += 1
    if s == 0:
        weight_of_zero_syndrome[w] += 1
assert sum(weight_of_zero_syndrome.values()) == 64
assert min(k for k in weight_of_zero_syndrome if k > 0) == 5
assert weight_of_zero_syndrome == {0:1, 5:12, 6:10, 8:15, 9:20, 10:6}

# An independent BFS on syndromes, recording shortest-path counts. Every
# shortest path uses distinct edge types, so each minimum support corresponds
# to exactly factorial(distance) shortest ordered paths.
D = [-1] * (1 << len(V))
P = [0] * (1 << len(V))
D[0] = 0
P[0] = 1
Q = deque([0])
while Q:
    s = Q.popleft()
    for v in edge_syndromes:
        u = s ^ v
        if D[u] < 0:
            D[u] = D[s] + 1
            P[u] = P[s]
            Q.append(u)
        elif D[u] == D[s] + 1:
            P[u] += P[s]
for s in range(1 << len(V)):
    if s.bit_count() % 2:
        assert D[s] == -1 and min_weight[s] == 99
    else:
        assert D[s] == min_weight[s]
        assert P[s] == leader_count[s] * factorial(D[s])

# Sym(5) naturally permutes the ten two-element subsets and preserves E.
vertex_index = {frozenset(v):i for i,v in enumerate(V)}
actions = []
for p in permutations(range(5)):
    a = tuple(vertex_index[frozenset((p[i], p[j]))] for i,j in V)
    actions.append(a)
assert len(set(actions)) == 120

def moved(s, action):
    return sum(1 << action[i] for i in range(10) if s & (1 << i))

unseen = {s for s in range(1024) if s.bit_count() % 2 == 0}
rows = []
while unseen:
    s = min(unseen)
    orbit = {moved(s,a) for a in actions}
    assert orbit <= unseen
    assert all((D[t], leader_count[t]) == (D[s],leader_count[s]) for t in orbit)
    unseen -= orbit
    rows.append((s, len(orbit), D[s], leader_count[s]))
rows.sort(key=lambda x: (x[0].bit_count(), x[1], x[2], x[3], x[0]))
expected_rows = [
    (0,1,0,1), (20,15,1,1), (3,30,2,1),
    (15,5,4,3), (184,10,3,1), (54,15,2,1),
    (58,60,2,1), (23,60,3,1), (29,60,3,2),
    (183,5,3,1), (126,10,3,2), (207,15,4,4),
    (187,60,3,1), (221,60,3,1), (63,60,4,3),
    (495,15,4,2), (255,30,4,2), (1023,1,5,6),
]
assert rows == expected_rows, (rows, expected_rows)

radius_counts = Counter(D[s] for s in range(1024) if D[s] >= 0)
tie_counts = Counter((D[s], leader_count[s]) for s in range(1024) if D[s]>=0)
assert radius_counts == {0:1, 1:15, 2:105, 3:265, 4:125, 5:1}
assert tie_counts == {
    (0,1):1, (1,1):15, (2,1):105,
    (3,1):195, (3,2):70,
    (4,2):45, (4,3):65, (4,4):15, (5,6):1}
assert {s for s in range(1024) if D[s] == 5} == {1023}
assert sum(w == 5 and syn[word] == 1023 for word, w in
           ((i,i.bit_count()) for i in range(size))) == 6

print('Petersen edge index:',E)
print('Coset radius histogram:', dict(sorted(radius_counts.items())))
print('Coset tie histogram:', dict(sorted(tie_counts.items())))
print('Automorphism orbits:', len(rows))
for mask, orb, distance, multiplicity in rows:
    print('ORBIT',mask,orb,distance,multiplicity)
print('VERIFY_OK')
