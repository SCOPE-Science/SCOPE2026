#!/usr/bin/env python3
"""Independent backtracking and edge-involution verification of the order-four Latin flip graph."""
from itertools import permutations, combinations
from hashlib import sha256
from collections import Counter, deque

PERMS=sorted(permutations(range(4)))
latin=[]
def extend(rows, used):
    if len(rows)==4:
        latin.append(tuple(rows)); return
    for row in PERMS:
        if all(not (used[c] & (1<<row[c])) for c in range(4)):
            extend(rows+[row], [used[c] | (1<<row[c]) for c in range(4)])
extend([], [0]*4)
latin.sort()
assert len(latin)==576
lookup={sq:i for i,sq in enumerate(latin)}
graph=[set() for sq in latin]
# Generate neighbors from pairs of rows and two-symbol transpositions. A
# transposition is legal exactly if each changed row contains the two symbols
# in the same two columns, and in reversed order.
for k,sq in enumerate(latin):
    for a,b in combinations(range(4),2):
        for x,y in combinations(range(4),2):
            cols_a={j for j in range(4) if sq[a][j] in (x,y)}
            cols_b={j for j in range(4) if sq[b][j] in (x,y)}
            if cols_a != cols_b: continue
            u=[list(row) for row in sq]
            for row in (a,b):
                for j in cols_a:
                    u[row][j]=x+y-u[row][j]
            state=tuple(map(tuple,u))
            if state not in lookup: continue
            graph[k].add(lookup[state])
assert all(k in graph[j] for k in range(576) for j in graph[k])
assert Counter(map(len,graph)) == {4:432,12:144}
assert sum(map(len,graph))//2==1728
# Evaluate all-pairs distances without relying on graph transitivity.
diameter=0
for src in range(576):
    distance={src:0}; queue=deque([src])
    while queue:
        u=queue.popleft()
        for v in graph[u]:
            if v not in distance:
                distance[v]=distance[u]+1; queue.append(v)
    assert len(distance)==576
    diameter=max(diameter,max(distance.values()))
assert diameter==6
encoded=';'.join(','.join(map(str,sorted(neigh))) for neigh in graph).encode()
digest=sha256(encoded).hexdigest()
assert digest=='07a20876e896ecc727c6a58253c4a4580fe3282b1d5262760b06bb940dbe113b'
print('backtracking_latin_squares=576; edges=1728; degrees={4:432,12:144}; diameter=6')
print('adjacency_sha256=',digest)
print('INDEPENDENT_GRAPH_OK')
