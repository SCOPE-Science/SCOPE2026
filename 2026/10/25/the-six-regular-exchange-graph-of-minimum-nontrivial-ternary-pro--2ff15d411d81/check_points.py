"""Exhaustive six-subset checker for the projective order-three blocking-set exchange graph.
Requires Python 3 standard library only. All point coordinates are normalized over F_3.
"""
from itertools import product, combinations
from collections import Counter, deque
import hashlib

q=3

def norm(x):
    t=next(a for a in x if a)
    return tuple(a*pow(t,-1,3)%3 for a in x)

P=sorted({norm(x) for x in product(range(3),repeat=3) if any(x)})
assert len(P)==13
lines=[frozenset(i for i,p in enumerate(P) if sum(a*b for a,b in zip(p,v))%3==0) for v in P]
assert len(set(lines))==13 and all(len(L)==4 for L in lines)

by_size={}
for k in range(1,7):
    goods=[]
    for S in combinations(range(13),k):
        Z=set(S)
        if all(Z&L for L in lines) and all(not L<=Z for L in lines):
            goods.append(frozenset(S))
    by_size[k]=len(goods)
    if k==6: states=sorted(goods,key=lambda s:tuple(sorted(s)))
assert by_size=={1:0,2:0,3:0,4:0,5:0,6:234},by_size
idx={s:i for i,s in enumerate(states)}
adj=[set() for s in states]
for i,S in enumerate(states):
    for x in S:
        for y in range(13):
            if y not in S:
                T=frozenset((S-{x})|{y})
                if T in idx: adj[i].add(idx[T])
assert all(len(a)==6 for a in adj)
assert all(i in adj[j] for i,a in enumerate(adj) for j in a)
assert sum(map(len,adj))//2==702

def distances(start):
    D={start:0}; queue=deque([start])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if v not in D:D[v]=D[u]+1;queue.append(v)
    return D

profiles={tuple(sorted(Counter(distances(i).values()).items())) for i in range(len(states))}
assert profiles=={((0,1),(1,6),(2,24),(3,72),(4,116),(5,12),(6,3))},profiles
# An invariant canonical fingerprint for the sorted point-set indexing.
edges=sorted((i,j) for i,ns in enumerate(adj) for j in ns if i<j)
fingerprint=hashlib.sha256('\n'.join(f'{i}-{j}' for i,j in edges).encode()).hexdigest()
print('POINT_CHECK_PASS')
print('counts',by_size)
print('vertices',len(states),'edges',len(edges),'degree',6)
print('distance_layers',(1,6,24,72,116,12,3),'radius',6,'diameter',6)
print('edge_sha256',fingerprint)
