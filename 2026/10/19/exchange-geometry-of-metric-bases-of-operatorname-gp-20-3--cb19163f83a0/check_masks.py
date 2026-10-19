"""Independent finite check via pair-separation bitsets. Python 3 standard library."""
from itertools import combinations
from collections import Counter, deque

n=20
vertices=range(2*n)
neighbor=[set() for _ in vertices]
for i in range(n):
    for a,b in ((i,(i+1)%n),(i,i+n),(i+n,(i+3)%n+n)):
        neighbor[a].add(b)
        neighbor[b].add(a)
assert all(len(v)==3 for v in neighbor)

def distance(source):
    ds=[-1]*(2*n)
    ds[source]=0
    queue=deque([source])
    while queue:
        u=queue.popleft()
        for v in neighbor[u]:
            if ds[v]<0:
                ds[v]=ds[u]+1
                queue.append(v)
    assert all(t>=0 for t in ds)
    return ds

all_d=[distance(v) for v in vertices]
all_pairs=list(combinations(vertices,2))
full=(1<<len(all_pairs))-1
separators=[]
for landmark in vertices:
    mask=0
    for j,(v,w) in enumerate(all_pairs):
        if all_d[landmark][v]!=all_d[landmark][w]:
            mask|=1<<j
    separators.append(mask)

four_tested=0
for a,b,c,d in combinations(vertices,4):
    four_tested+=1
    assert separators[a]|separators[b]|separators[c]|separators[d]!=full
assert four_tested==91390

basis=set()
profile=Counter()
for x in combinations(vertices,5):
    a,b,c,d,e=x
    if separators[a]|separators[b]|separators[c]|separators[d]|separators[e]==full:
        bitset=sum(1<<j for j in x)
        basis.add(bitset)
        profile[sum(j<n for j in x)]+=1
assert len(basis)==41040

adj={}
for x in basis:
    own=[i for i in vertices if x>>i&1]
    free=[i for i in vertices if not (x>>i&1)]
    moves=set()
    for i in own:
        remove=x^(1<<i)
        for j in free:
            y=remove|(1<<j)
            if y in basis:
                moves.add(y)
    adj[x]=moves
assert all(x in adj[y] for x, nbrs in adj.items() for y in nbrs)
num_edges=sum(map(len,adj.values()))//2
assert num_edges==670930

# BFS can establish connectivity, and cross-check two extreme eccentricities.
def bfs(start):
    distances={start:0}
    queue=deque([start])
    while queue:
        x=queue.popleft()
        for y in adj[x]:
            if y not in distances:
                distances[y]=distances[x]+1
                queue.append(y)
    return distances

d0=bfs(0x10000087)
d1=bfs(0x40000903)
assert len(d0)==len(d1)==len(basis)
assert max(d0.values())==6
assert max(d1.values())==7
assert profile=={1:1720,2:13400,3:20520,4:5300,5:100}
print('metric_dimension=5')
print('four_set_candidates=',four_tested,sep='')
print('bases=',len(basis),' exchange_edges=',num_edges,sep='')
print('outer_profile=',dict(sorted(profile.items())),sep='')
print('connected=yes diameter_at_witness=7 radius_at_witness=6')
print('radius_witness=',[i for i in vertices if 0x10000087>>i&1],sep='')
print('diameter_witness=',[i for i in vertices if 0x40000903>>i&1], ' to ',[i for i in vertices if min(k for k,t in d1.items() if t==7)>>i&1],sep='')
print('VERIFY_OK')
