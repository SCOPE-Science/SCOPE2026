#!/usr/bin/env python3
"""Exact finite verification of the ordinary 4-cut complex of the Mycielski five-cycle."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N=11
EDGES=set()
def add(a,b):EDGES.add(tuple(sorted((a,b))))
for i in range(5):
    add(i,(i+1)%5)
    add(5+i,(i+1)%5)
    add(5+i,(i-1)%5)
    add(10,5+i)
assert len(EDGES)==20

def disconnected(s):
    verts=[i for i in range(N) if s&(1<<i)]
    reached={verts[0]}; pending=[verts[0]]
    while pending:
        x=pending.pop()
        for y in verts:
            if y not in reached and tuple(sorted((x,y))) in EDGES:
                reached.add(y);pending.append(y)
    return len(reached)!=len(verts)

ALL=(1<<N)-1
facets={ALL^sum(1<<i for i in choice) for choice in combinations(range(N),4)
        if disconnected(sum(1<<i for i in choice))}
assert len(facets)==180
faces={0}
for facet in facets:
    s=facet
    while s:
        faces.add(s);s=(s-1)&facet
face_order=sorted(faces,key=lambda s:(s.bit_count(),s))
face_by_degree={degree:sorted(f for f in faces if f.bit_count()==degree+1)
                for degree in range(7)}
assert [len(face_by_degree[i]) for i in range(7)]==[11,55,165,330,462,431,180]
assert len(faces)==1635

@lru_cache(None)
def boundary(s):
    bits=[i for i in range(N) if s&(1<<i)]
    return [(s^(1<<j), 1 if r%2==0 else -1) for r,j in enumerate(bits)]

# Element matchings on the augmented face poset. Remove the empty-face pair
# afterwards, leaving one critical vertex in the usual CW Morse complex.
pivot_order=(0,3,8,4,9,5,7,6,2,10,1)
remaining=set(faces);up={}
for i in pivot_order:
    bit=1<<i
    for s in face_order:
        if s&bit or s not in remaining:continue
        t=s|bit
        if t in remaining:
            remaining.remove(s);remaining.remove(t);up[s]=t
assert up.get(0)==1
assert len(up)==813
critical=Counter(s.bit_count()-1 for s in remaining)
assert critical=={5:4,6:5}
# Unaugmented matching pairs, and critical ordinary vertex.
del up[0]
assert len(up)==812
criticals=set(remaining)|{1}
assert Counter(s.bit_count()-1 for s in criticals)=={0:1,5:4,6:5}

# Verify the entire directed Hasse graph is a DAG.
# For each unmatched incidence, arrow large -> small; matched arrow small -> large.
node_set=set(faces)-{0}
succ={s:[] for s in node_set};indegree={s:0 for s in node_set};covers=0
for large in node_set:
    for small,_ in boundary(large):
        if small==0:continue
        covers+=1
        a,b=(small,large) if up.get(small)==large else (large,small)
        succ[a].append(b);indegree[b]+=1
queue=deque(s for s in node_set if indegree[s]==0)
visited=0
while queue:
    s=queue.popleft();visited+=1
    for t in succ[s]:
        indegree[t]-=1
        if indegree[t]==0:queue.append(t)
assert visited==len(node_set)==1634
assert covers==8081

# Exact integral gradient-path coefficients in degree 6 -> 5.
critical5=sorted(s for s in criticals if s.bit_count()==6)
critical6=sorted(s for s in criticals if s.bit_count()==7)
up56={a:b for a,b in up.items() if a.bit_count()==6}
@lru_cache(None)
def reduction(s):
    if s in critical5:return {s:1}
    if s not in up56:return {}
    high=up56[s]
    sign=dict(boundary(high))[s]
    out=Counter()
    for low,eps in boundary(high):
        if low==s:continue
        for v,c in reduction(low).items():out[v]-=sign*eps*c
    return {x:y for x,y in out.items() if y}
M=[]
for high in critical6:
    out=Counter()
    for low,eps in boundary(high):
        for v,c in reduction(low).items():out[v]+=eps*c
    M.append([out.get(v,0) for v in critical5])
assert M==[[0]*4 for _ in range(5)]

# Independently compute all boundary ranks over GF(2).
def rank_binary(degree):
    lower={s:i for i,s in enumerate(face_by_degree[degree-1])}
    pivots={}
    for high in face_by_degree[degree]:
        w=sum(1<<lower[low] for low,_ in boundary(high))
        while w:
            p=w.bit_length()-1
            if p not in pivots:
                pivots[p]=w;break
            w^=pivots[p]
    return len(pivots)
ranks=[rank_binary(k) for k in range(1,7)]
assert ranks==[10,45,120,210,252,175]
assert [len(face_by_degree[k])-(ranks[k-1] if k else 0)-(ranks[k] if k<6 else 0)
        for k in range(7)]==[1,0,0,0,0,4,5]

# Independent Euler characteristic from face counts and critical counts.
assert sum((-1)**k*len(face_by_degree[k]) for k in range(7))==2
assert 1-4+5==2
print('GROETZSCH_4CUT_180_FACETS_1635_FACES_812_ACYCLIC_PAIRS_4S5_5S6_EXACT_OK')
print('faces=',[len(face_by_degree[k]) for k in range(7)],
      'Hasse=',covers,'matching=',len(up),'acyclic_nodes=',visited)
print('Morse integer differential=',M,'mod2 ranks=',ranks)
