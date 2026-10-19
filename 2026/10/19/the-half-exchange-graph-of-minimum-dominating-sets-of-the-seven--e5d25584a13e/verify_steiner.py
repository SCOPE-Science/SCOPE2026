#!/usr/bin/env python3
"""Exact 7-cube efficient-domination exchange census by Steiner triples."""
from collections import Counter,deque
from itertools import combinations
import json,sys,hashlib

N=7
triples=[sum(1<<i for i in xyz) for xyz in combinations(range(N),3)]
pairs=list(combinations(range(N),2))
coverage={t:sum(1<<j for j,p in enumerate(pairs) if all((t>>i)&1 for i in p)) for t in triples}
by_pair=[[t for t in triples if (coverage[t]>>j)&1] for j in range(21)]
solutions=[]
def rec(lines,unused):
    if not unused:
        assert len(lines)==7
        solutions.append(tuple(sorted(lines)));return
    j=min(unused,key=lambda z:sum((coverage[t] & sum(1<<w for w in unused))==coverage[t] for t in by_pair[z]))
    allowed_mask=sum(1<<w for w in unused)
    for t in by_pair[j]:
        mask=coverage[t]
        if mask & allowed_mask == mask:
            rec(lines+[t],unused-set(k for k in unused if (mask>>k)&1))
rec([],set(range(21)))
assert len(solutions)==30 and len(set(solutions))==30
codes=set()
for lines in solutions:
    H={0,127,*lines,*(127^t for t in lines)}
    assert len(H)==16
    assert all((a^b) in H for a in H for b in H)
    cosets={tuple(sorted(a^shift for a in H)) for shift in range(128)}
    assert len(cosets)==8
    codes|=cosets
codes=sorted(codes)
assert len(codes)==240
for c in codes:
    assert len(c)==16
    cover=[0]*128
    for x in c:
        for y in (x,*(x^(1<<i) for i in range(7))):cover[y]+=1
    assert all(v==1 for v in cover)

graph=[set() for _ in codes]; intersection=Counter()
for i,C in enumerate(codes):
    A=set(C)
    for j in range(i+1,len(codes)):
        overlap=len(A.intersection(codes[j]));intersection[overlap]+=1
        if overlap==8:graph[i].add(j);graph[j].add(i)
assert dict(intersection)=={0:12600,2:7680,4:6720,8:1680}
assert set(map(len,graph))=={14}
profiles=[]
for k in range(len(codes)):
    distances={k:0};queue=deque([k])
    while queue:
        u=queue.popleft()
        for v in graph[u]:
            if v not in distances:distances[v]=distances[u]+1;queue.append(v)
    assert len(distances)==240
    profiles.append([sum(v==j for v in distances.values()) for j in range(5)])
assert set(map(tuple,profiles))=={(1,14,63,106,56)}
triangles=sum(len(graph[i]&graph[j]) for i in range(240) for j in graph[i])//6
assert triangles==0
edges=sorted([ [i,j] for i in range(240) for j in graph[i] if i<j])
assert len(edges)==1680
out={'schema_version':1,'definition':'7-cube efficient dominating sets, edge iff eight elements replaced',
     'steiner_system_count':30,'codes':[list(c) for c in codes],
     'edges':edges,'pair_intersection_counts':{str(k):v for k,v in sorted(intersection.items())},
     'distance_profile_per_vertex':[1,14,63,106,56], 'triangle_count':triangles}
raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')
if len(sys.argv)!=2:raise SystemExit('usage verify_steiner.py certificate.json')
with open(sys.argv[1],'wb') as f:f.write(raw)
print('STEINER_OK 30_STS7 240_CODES 1680_EDGES 14_REGULAR TRIANGLE_FREE DIAMETER_4')
print('INTERSECTIONS 0:12600 2:7680 4:6720 8:1680')
print('DISTANCE_SPHERES 1 14 63 106 56')
print('CERTIFICATE_SHA256',hashlib.sha256(raw).hexdigest())
