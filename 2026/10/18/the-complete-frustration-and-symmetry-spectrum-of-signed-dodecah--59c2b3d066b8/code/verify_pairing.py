#!/usr/bin/env python3
"""Independent shortest-path pairing / minimum-T-join verification.

Standalone verification of every face-parity class, via the classical
minimum-weight perfect pairing principle for T-joins.  Uses no external
packages and reads the BFS certificate only after independently calculating
all distances.
"""
from collections import Counter, deque
from functools import lru_cache
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
# Independent adjacency definition: upper/lower pentagons and two poles.
adj = [set() for _ in range(12)]
for i in range(5):
    ui, li = 1+i, 6+i
    adj[0].add(ui); adj[ui].add(0)
    adj[11].add(li); adj[li].add(11)
    for j in ((1+(i+1)%5), (1+(i-1)%5), 6+i, 6+(i-1)%5):
        adj[ui].add(j);adj[j].add(ui)
    for j in (6+(i+1)%5, 6+(i-1)%5):
        adj[li].add(j);adj[j].add(li)
assert all(len(s) == 5 for s in adj)
assert sum(map(len,adj))//2 == 30

# Compute distances on the 12-vertex graph, not on a 2048-state graph.
distance = [[100] * 12 for _ in range(12)]
for a in range(12):
    distance[a][a] = 0
    q = deque([a])
    while q:
        x = q.popleft()
        for y in sorted(adj[x]):
            if distance[a][y] > distance[a][x]+1:
                distance[a][y] = distance[a][x]+1
                q.append(y)
assert all(distance[i][j]==distance[j][i] for i in range(12) for j in range(12))

@lru_cache(None)
def pairing(mask):
    if not mask: return 0
    i = (mask & -mask).bit_length()-1
    rest= mask ^ (1 << i)
    return min(distance[i][j] + pairing(rest ^ (1 << j))
               for j in range(12) if rest & (1 << j))

# Count exact perfect matchings of the induced subgraph on the mask.
@lru_cache(None)
def matching_count(mask):
    if not mask:return 1
    i = (mask & -mask).bit_length()-1
    rest = mask ^ (1 << i)
    return sum(matching_count(rest ^ (1 << j)) for j in adj[i]
               if rest & (1 << j))

H = Counter()
T = {k:Counter() for k in range(0,13,2)}
rows=[]
for m in range(4096):
    if m.bit_count()%2:continue
    x = pairing(m)
    H[x]+=1
    T[m.bit_count()][x]+=1
    rows.append((m,m.bit_count(),x))
assert H == {0:1,1:30,2:315,3:1058,4:577,5:66,6:1}
assert T[0]=={0:1}
assert T[2]=={1:30,2:30,3:6}
assert T[4]=={2:285,3:210}
assert T[6]=={3:842,4:82}
assert T[8]=={4:495} and T[10]=={5:66} and T[12]=={6:1}
assert all((matching_count(m)>0)==(pairing(m)==m.bit_count()//2)
           for m in range(4096) if m.bit_count() in (4,6,8,10,12))
assert matching_count(4095)==125
assert [m for m in range(4096) if m.bit_count()%2==0 and pairing(m)==6] == [4095]

with (ROOT/'data'/'frustration_distances.csv').open(encoding='utf8',newline='') as f:
    it=csv.reader(f)
    assert next(it)==['face_mask_decimal','negative_faces','minimum_negative_edges']
    recorded=[tuple(map(int,line)) for line in it]
assert recorded == rows

print('independent 12-vertex shortest-path pairing recurrence verified')
print('histogram=', sorted(H.items()))
for k in sorted(T):
    print('negative-face count', k, 'frustration counts', sorted(T[k].items()))
print('induced perfect matchings for full face set=',matching_count(4095))
print('all 2048 BFS-certificate rows agree with pairing distances')
