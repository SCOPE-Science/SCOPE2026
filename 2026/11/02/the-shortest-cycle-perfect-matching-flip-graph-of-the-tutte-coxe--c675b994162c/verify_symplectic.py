"""Exhaustive independent verification using the 15 point, 15 line W(2) model.
Run: python3 verify_symplectic.py
"""
from collections import Counter, deque
from itertools import combinations

def omega(x,y):
    return (((x&1) and (y&2)) != 0) ^ (((x&2) and (y&1)) != 0) ^ (((x&4) and (y&8)) != 0) ^ (((x&8) and (y&4)) != 0)

points=list(range(1,16))
lines=sorted({frozenset((x,y,x^y)) for x in points for y in points if x!=y and not omega(x,y)})
assert len(lines)==15 and all(len(x)==3 for x in lines)
adj=[set() for _ in range(30)]
for i,x in enumerate(points):
    for j,L in enumerate(lines):
        if x in L:adj[i].add(15+j);adj[15+j].add(i)
assert all(len(x)==3 for x in adj)
edge_list=sorted((x,y) for x in range(30) for y in adj[x] if x<y)
assert len(edge_list)==45
idx={e:i for i,e in enumerate(edge_list)}
# Enumerate all perfect matchings of the 30-vertex graph using recursive covering.
matchings=[]
def rec(uncovered,mask):
    if uncovered==0:matchings.append(mask);return
    i=(uncovered & -uncovered).bit_length()-1
    for j in sorted(adj[i]):
        if uncovered>>j & 1:
            rec(uncovered ^ (1<<i) ^ (1<<j),mask|(1<<idx[min(i,j),max(i,j)]))
rec((1<<30)-1,0)
assert len(matchings)==288 and len(set(matchings))==288
# DFS all simple 4-, 6-, and 8-cycles, quotienting rotations and reversals.
cycle_sets={}
def trace(path,target,found):
    if len(path)==target:
        if path[0] in adj[path[-1]]:
            arr=path+[path[0]]
            mask=sum(1<<idx[min(arr[i],arr[i+1]),max(arr[i],arr[i+1])] for i in range(target))
            found.add(mask)
        return
    for j in adj[path[-1]]:
        if j not in path:trace(path+[j],target,found)
for target in (4,6,8):
    found=set()
    for i in range(30):trace([i],target,found)
    cycle_sets[target]=found
assert len(cycle_sets[4])==len(cycle_sets[6])==0
assert len(cycle_sets[8])==90
cycles=sorted(cycle_sets[8])
cyc_counts=Counter(sum((m&C).bit_count()==4 for m in matchings) for C in cycles)
M_index={m:i for i,m in enumerate(matchings)}
G=[set() for _ in matchings]
for k,m in enumerate(matchings):
    for C in cycles:
        if (m&C).bit_count()==4:
            n=m^C
            assert n in M_index
            G[k].add(M_index[n])
assert all(len(q)==10 for q in G)
assert all(k in G[j] for k,q in enumerate(G) for j in q)
assert sum(map(len,G))//2==1440
profiles=Counter()
for root in range(len(G)):
    dist=[-1]*len(G);dist[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        for v in G[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1;q.append(v)
    assert -1 not in dist
    profile=tuple(Counter(dist)[j] for j in range(max(dist)+1))
    profiles[profile]+=1
assert profiles==Counter({(1,10,45,97,96,37,2):144,(1,10,42,97,101,37):144}),profiles
assert cyc_counts==Counter({32:90})
# bipartition via BFS colouring
color={0:0};q=deque([0])
while q:
    u=q.popleft()
    for v in G[u]:
        if v not in color:color[v]=1-color[u];q.append(v)
        else:assert color[v]!=color[u]
assert Counter(color.values())==Counter({0:144,1:144})
# All even squares counted by common-neighbor pairs, each square counted twice.
common=Counter()
square_double=0
for a in range(len(G)):
    for b in range(a+1,len(G)):
        t=len(G[a].intersection(G[b]))
        square_double+=t*(t-1)//2
assert square_double//2==4320
# Diagonal of same colour classes, ecc counts.
assert max(len(p)-1 for p in profiles)==6
print('SYMPLECTIC_EXHAUSTIVE_PASS points=15 lines=15 incidence_edges=45 perfect_matchings=288 eight_cycles='+str(len(cycles)))
print('FLIP_METRIC_PASS edges=1440 degree=10 connected=1 bipartite=1 radius=5 diameter=6 squares=4320')
print('DISTANCE_PROFILES_PASS '+repr(sorted(profiles.items())))
