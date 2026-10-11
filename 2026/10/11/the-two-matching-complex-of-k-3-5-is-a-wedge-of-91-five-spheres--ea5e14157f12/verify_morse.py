#!/usr/bin/env python3
"""Reproducible discrete-Morse proof for the 2-matching complex of K_{3,5}."""
from collections import defaultdict, deque

N_ROWS,N_COLS=3,5
EDGES=tuple((i,j) for i in range(N_ROWS) for j in range(N_COLS))

def admissible(mask):
    rd=[0]*N_ROWS;cd=[0]*N_COLS
    for k,(i,j) in enumerate(EDGES):
        if mask & (1<<k):
            rd[i]+=1;cd[j]+=1
            if rd[i]>2 or cd[j]>2:return False
    return True

cells={mask for mask in range(1,1<<(N_ROWS*N_COLS)) if admissible(mask)}
faces=defaultdict(int)
for mask in cells: faces[mask.bit_count()-1]+=1
assert [faces[d] for d in range(6)]==[15,105,420,990,1260,690]
assert not any(d>=6 for d in faces)

# Priority-toggle matching on the not-yet-paired collection.
remaining=set(cells);pairs=[]
for pivot in range(len(EDGES)):
    bit=1<<pivot
    low=[mask for mask in remaining if not (mask & bit) and (mask|bit) in remaining]
    for mask in low:
        hi=mask|bit
        remaining.remove(mask);remaining.remove(hi)
        pairs.append((mask,hi))
assert len(pairs)==1694,len(pairs)
assert sorted(mask.bit_count()-1 for mask in remaining)==[0]+[5]*91

# For each facet-cofacet incidence, reverse its Hasse direction iff matched.
matched={(lo,hi) for lo,hi in pairs}
indegree={v:0 for v in cells}; adj={v:[] for v in cells};hcount=0
for hi in cells:
    for k in range(15):
        if not (hi>>k)&1:continue
        lo=hi^(1<<k)
        if not lo: continue
        hcount+=1
        a,b=(lo,hi) if (lo,hi) in matched else (hi,lo)
        adj[a].append(b);indegree[b]+=1
queue=deque(v for v in cells if indegree[v]==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in adj[u]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert visited==len(cells),(visited,len(cells))
print({'nonempty_cells':len(cells),'fvector':[faces[d] for d in range(6)],'matched_pairs':len(pairs),'critical_0':1,'critical_5':91,'hasse_arcs':hcount,'toposort_vertices':visited})
