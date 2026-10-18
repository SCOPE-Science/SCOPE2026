#!/usr/bin/env python3
"""Independent lexicographic census of the optimal Clebsch recoloring graph.

Graph construction uses antipodal pairs of the ordinary five-cube,
not the XOR generator list from the other verifier.
"""
from collections import Counter,deque

n=16
# Each five-bit word is identified with its bitwise complement.
# A vertex is the representative of its antipodal pair with leading bit 0.
rep=lambda x:min(x,x ^ 31)
links=[set() for _ in range(n)]
for a in range(16):
    for d in (1,2,4,8,16):
        b=rep(a^d)
        assert b!=a
        links[a].add(b)
assert all(len(q)==5 for q in links)
assert all(a in links[b] for a in range(n) for b in links[a])

# Different search ordering from the dynamic saturation-based enumeration.
# Recursively assign colors to vertices in increasing numerical order.
assign=[-1]*n
all_colorings=[]
def fill(pos):
    if pos==n:
        all_colorings.append(tuple(assign))
        return
    used={assign[j] for j in links[pos] if j<pos}
    for col in (0,1,2,3):
        if col not in used:
            assign[pos]=col
            fill(pos+1)
    assign[pos]=-1
fill(0)
assert len(all_colorings)==28560
labels={tuple(s):i for i,s in enumerate(all_colorings)}

# Edges obtained by direct Hamming distance 1 among valid colorings:
# generate single-position substitutions and check membership of valid states.
# This deliberately does not use neighbor-color availability tests.
R=[set() for _ in all_colorings]
for i,s in enumerate(all_colorings):
    for j in range(n):
        for col in range(4):
            if s[j]==col:continue
            candidate=list(s)
            candidate[j]=col
            k=labels.get(tuple(candidate))
            if k is not None:
                R[i].add(k)
assert all(i in R[j] for i in range(len(R)) for j in R[i])
assert sum(map(len,R))//2==57600
assert Counter(map(len,R))=={0:1680,2:3840,4:11520,5:7680,6:3840}

visited=[False]*len(R)
comp=Counter(); diam=Counter(); internal_edges=Counter()
for root in range(len(R)):
    if visited[root]:continue
    Q=deque([root]); visited[root]=True; group=[]
    while Q:
        v=Q.popleft();group.append(v)
        for w in R[v]:
            if not visited[w]: visited[w]=True;Q.append(w)
    comp[len(group)]+=1
    internal_edges[(len(group),sum(len(R[v]) for v in group)//2)]+=1
    if len(group)>1:
        dmax=0
        for source in group:
            dist={source:0};B=deque([source])
            while B:
                v=B.popleft()
                for w in R[v]:
                    if w not in dist:
                        dist[w]=dist[v]+1
                        B.append(w)
            assert len(dist)==len(group)
            dmax=max(dmax,max(dist.values()))
        diam[dmax]+=1
assert comp=={1:1680,28:960}
assert internal_edges=={(1,0):1680,(28,60):960}
assert diam=={6:960}
print('VERIFY_OK ALT')
print('vertices=28560 edges=57600')
print('component_sizes={1:1680,28:960} nontrivial_diameter=6 edges_per_nontrivial=60')
print('degree_histogram={0:1680,2:3840,4:11520,5:7680,6:3840}')
