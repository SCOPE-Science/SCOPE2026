#!/usr/bin/env python3
"""Independently enumerate Pappus induced matchings from its 9-point/9-line incidence.

The search recursively builds compatible edge subsets using bitmasks, independently
of combination-by-combination enumeration or the LCF representation.
Run: python3 check_incidence.py
"""
import json
from collections import Counter,deque
from itertools import combinations

LINES=((0,2,8),(0,1,6),(1,2,7),(2,3,5),(0,3,4),(1,4,5),
       (5,6,8),(3,6,7),(4,7,8))
E=tuple(sorted((p,9+i) for i,line in enumerate(LINES) for p in line))
assert len(E)==27 and len(set(E))==27
neighbors=[set() for _ in range(18)]
for a,b in E:neighbors[a].add(b);neighbors[b].add(a)
assert all(len(a)==3 for a in neighbors)

def compatible(i,j):
    a,b=E[i];c,d=E[j]
    return len({a,b,c,d})==4 and c not in neighbors[a] and d not in neighbors[a] and c not in neighbors[b] and d not in neighbors[b]
C=[0]*27
for i in range(27):
    C[i]=sum(1<<j for j in range(27) if j!=i and compatible(i,j))

families={4:[],5:[],6:[]}
def dfs(prefix,available):
    if len(prefix) in families:families[len(prefix)].append(prefix)
    if len(prefix)==6:return
    while available:
        bit=available&-available;i=bit.bit_length()-1
        available-=bit
        dfs(prefix+(i,),available&C[i])
dfs((),(1<<27)-1)
assert len(families[4])==135 and len(families[5])==27 and not families[6]
S={k:[frozenset(x) for x in families[k]] for k in (4,5)}
assert len(set(S[4]))==135 and len(set(S[5]))==27

positions={s:i for i,s in enumerate(S[4])}
N=[set() for _ in S[4]]
for i,s in enumerate(S[4]):
    for dropped in s:
        remain=s-{dropped}
        for candidate in range(27):
            if candidate not in s:
                j=positions.get(remain|{candidate})
                if j is not None:N[i].add(j)
assert all(i in N[j] for i,row in enumerate(N) for j in row)
assert sum(map(len,N))//2==486

parents=[]
for s in S[4]:
    ps=[i for i,big in enumerate(S[5]) if s<big]
    assert len(ps)==1
    parents.append(ps[0])
Q=[set() for _ in S[5]];counts=Counter()
for i,row in enumerate(N):
    for j in row:
        if i<j and parents[i]!=parents[j]:
            a,b=sorted((parents[i],parents[j]));Q[a].add(b);Q[b].add(a);counts[a,b]+=1
assert set(counts.values())=={4}
assert sum(map(len,Q))//2==54
assert sum(1 for a,b in combinations(range(27),2) if len(S[5][a]&S[5][b])==3)==54

# The maximal triangles of the quotient are the vertices of its cubic line-graph root.
TRI=sorted(tuple(x) for x in combinations(range(27),3) if all(b in Q[a] for a,b in combinations(x,2)))
assert len(TRI)==18
assert all(sum(i in t for t in TRI)==2 for i in range(27))
root=[set() for _ in TRI]
for a,b in combinations(range(18),2):
    if len(set(TRI[a])&set(TRI[b]))==1:root[a].add(b);root[b].add(a)
assert all(len(x)==3 for x in root)
assert sum(map(len,root))//2==27

# Verify a fixed root-isomorphism certificate (triangle indices -> incidence vertices).
CERTIFICATE = (0,9,10,13,2,8,6,15,16,5,3,12,1,11,14,4,7,17)
if CERTIFICATE is not None:
    assert sorted(CERTIFICATE)==list(range(18))
    assert all((CERTIFICATE[b] in neighbors[CERTIFICATE[a]]) == (b in root[a])
               for a,b in combinations(range(18),2))

def bfs(v):
    d={v:0};q=deque([v])
    while q:
        a=q.popleft()
        for b in N[a]:
            if b not in d:d[b]=d[a]+1;q.append(b)
    return d
D=[bfs(i) for i in range(135)]
assert all(len(z)==135 for z in D)
ecc=[max(z.values()) for z in D]
assert min(ecc)==8 and max(ecc)==9
assert Counter(map(len,N))=={4:27,8:108}

print(json.dumps({
 'construction':'9 point/9 line incidence',
 'orders':{'size_4':len(S[4]),'size_5':len(S[5]),'size_6':len(families[6])},
 'exchange':{'edges_4':sum(map(len,N))//2,'edges_5':0,
             'degree_hist':dict(Counter(map(len,N))),
             'eccentricities':dict(Counter(ecc)),
             'distance_9_pairs':sum(D[a][b]==9 for a,b in combinations(range(135),2))},
 'quotient':{'edges':sum(map(len,Q))//2,'edge_multiplicities':dict(Counter(counts.values())),
             'triangles':len(TRI),'root_edge_count':sum(map(len,root))//2},
 'root_triangles':TRI,
 'verified':True},sort_keys=True,indent=2))
