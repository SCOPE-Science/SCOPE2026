#!/usr/bin/env python3
"""Exhaustive, dependency-free 24-state certificate for Fano matching exchanges."""
import itertools, json, sys
from collections import Counter, deque

LINES = tuple(tuple(sorted({i,(i+1)%7,(i+3)%7})) for i in range(7))
assert len(set(LINES))==7 and all(len(x)==3 for x in LINES)
assert all(sum(a in line and b in line for line in LINES)==1
           for a,b in itertools.combinations(range(7),2))
matchings = sorted(p for p in itertools.permutations(range(7))
                   if all(i in LINES[p[i]] for i in range(7)))
assert len(matchings)==24
# A pair of size-seven perfect matchings has a six-edge alternating-cycle
# symmetric difference iff exactly three points change their partners.
N=len(matchings)
adj=[[] for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        moved=sum(a!=b for a,b in zip(matchings[i],matchings[j]))
        if moved==3:
            adj[i].append(j);adj[j].append(i)
assert all(len(v)==7 for v in adj)
assert sum(map(len,adj))//2==84
D=[]
for root in range(N):
    row=[-1]*N; row[root]=0
    q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if row[v]<0:
                row[v]=row[u]+1;q.append(v)
    assert Counter(row)==Counter({0:1,1:7,2:14,3:2})
    D.append(row)
array=[]
for distance in (0,1,2,3):
    values=set()
    for r in range(N):
        for u in range(N):
            if D[r][u]==distance:
                values.add(tuple(sum(D[r][v]==d for v in adj[u])
                                 for d in (distance-1,distance,distance+1)))
    assert len(values)==1,(distance,values)
    array.append(next(iter(values)))
assert array==[(0,0,7),(1,2,4),(2,4,1),(7,0,0)],array
pair=Counter()
for i in range(N):
    for j in range(i+1,N):
        moved=sum(a!=b for a,b in zip(matchings[i],matchings[j]))
        pair[(moved,D[i][j])]+=1
assert pair=={(3,1):84,(5,2):84,(6,2):84,(7,3):24},pair
# Dist=3 along each antipodal triple; each other triple has exactly one neighbor.
fibers=[];seen=set()
for i in range(N):
    if i not in seen:
        fiber=tuple([i]+[j for j in range(N) if D[i][j]==3])
        assert len(fiber)==3
        assert all(D[u][v]==3 for u,v in itertools.combinations(fiber,2))
        fibers.append(tuple(sorted(fiber)));seen.update(fiber)
assert len(fibers)==8 and len(seen)==N
for i in range(N):
    assert all(sum(j in adj[i] for j in f)==1 for f in fibers if i not in f)

certificate={
    'definition':'Fano lines i,i+1,i+3 modulo 7; matching tuple records the line matched to point 0,...,6',
    'lines':[list(x) for x in LINES],
    'matchings':[list(p) for p in matchings],
    'six_flip_adjacency':[sorted(v) for v in adj],
    'distance_matrix':D,
    'intersection_by_distance':{'0':[0,0,7],'1':[1,2,4],'2':[2,4,1],'3':[7,0,0]},
    'antipodal_triples':[list(f) for f in sorted(fibers)],
    'pair_differences':{'3_changed_distance_1':84,'5_changed_distance_2':84,'6_changed_distance_2':84,'7_changed_distance_3':24},
    'vertices':24,'edges':84,'diameter':3,
    'intersection_array':{'b':[7,4,1],'c':[1,2,7]}
}
if len(sys.argv)>1 and sys.argv[1]!='--write':
    with open(sys.argv[1],encoding='utf-8') as f: old=json.load(f)
    assert old==certificate
print('FANO_PERMANENT_PASS matchings=24 six_flips=84 array=[7,4,1;1,2,7] antipodal=8 triples')
if '--write' in sys.argv:
    with open('certificate.json','w',encoding='utf-8') as f:json.dump(certificate,f,sort_keys=True,indent=2);f.write('\n')
