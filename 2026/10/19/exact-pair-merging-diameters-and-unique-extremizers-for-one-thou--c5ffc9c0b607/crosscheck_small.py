"""Independent explicit reverse-adjacency oracle for small Dzyga--Szykula automata."""
from collections import deque
from itertools import combinations
import csv
import sys


def transitions(k):
    n = 3*k+6
    edge = [[None,None] for _ in range(n)]
    edge[0] = [0,1]
    for i in range(1,2*k+4):
        edge[i] = [i+1 if i%2 else i-1, i+1 if not i%2 else i-1]
    edge[2*k+4] = [2*k+5,2]
    edge[2*k+5] = [3,2*k+6]
    for i in range(2*k+6,n-1):
        edge[i] = [i+1 if not i%2 else i-1,
                   i+1 if i%2 else i-1]
    edge[-1] = [n-1 if (n-1)%2==0 else n-2,
                n-1 if (n-1)%2==1 else n-2]
    assert all(0 <= z < n for ab in edge for z in ab)
    return edge


def compute(k):
    edge=transitions(k)
    n=len(edge)
    nodes=list(combinations(range(n),2))
    nodes+= [(i,i) for i in range(n)]
    incoming={p:[] for p in nodes}
    for pair in nodes:
        for letter in (0,1):
            x,y=sorted((edge[pair[0]][letter],edge[pair[1]][letter]))
            incoming[(x,y)].append(pair)
    dist={(i,i):0 for i in range(n)}
    queue=deque((i,i) for i in range(n))
    while queue:
        cur=queue.popleft()
        for p in incoming[cur]:
            if p not in dist:
                dist[p]=dist[cur]+1
                queue.append(p)
    assert len(dist)==n*(n+1)//2
    mx=max(dist[p] for p in nodes)
    return mx,[p for p in nodes if dist[p]==mx]

with open(sys.argv[1],newline='',encoding='utf-8') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
for k in range(1,41):
    row=rows[k-1]
    D,pairs=compute(k)
    assert k==int(row['k'])
    assert D==int(row['diameter'])
    assert pairs==[(int(row['farthest_p']),int(row['farthest_q']))]
print('CROSSCHECK_SMALL_OK k=1..40; exact reverse-adjacency BFS agrees on every pairwise merging diameter and unique farthest pair')
