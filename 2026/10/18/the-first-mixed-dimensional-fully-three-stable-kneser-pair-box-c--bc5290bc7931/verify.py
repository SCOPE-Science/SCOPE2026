#!/usr/bin/env python3
"""Exact combinatorial certificate for stable-Kneser neighborhood complexes."""
from itertools import combinations
from collections import defaultdict,Counter,deque
from functools import lru_cache

N=8; GAP=3
vertices=tuple((i,j) for i in range(N) for j in range(i+1,N) if min(j-i,N-(j-i))>=GAP)
assert len(vertices)==12
neighbors=tuple(tuple(j for j,q in enumerate(vertices) if not (set(p)&set(q))) for p in vertices)
assert set(map(len,neighbors))=={7}
faces=set()
for neighborhood in neighbors:
    for subset in range(1,1<<len(neighborhood)):
        faces.add(sum(1<<neighborhood[i] for i in range(len(neighborhood)) if subset>>i & 1))
assert len(faces)==910
v_order=(7,0,1,5,3,9,2,8,4,11,10,6)
unmatched=set(faces)
matching={}
for v in v_order:
    for f in sorted(faces):
        f_plus=f|(1<<v)
        if f in unmatched and not(f&(1<<v)) and f_plus in unmatched:
            unmatched.remove(f);unmatched.remove(f_plus)
            matching[f]=f_plus
assert len(matching)==453
assert len(unmatched)==4
critical=tuple(sorted(unmatched,key=lambda a:(a.bit_count(),a)))
critical_dims=Counter(f.bit_count()-1 for f in critical)
assert critical_dims=={0:1,2:2,3:1},critical_dims
print('critical_faces',tuple(tuple(i for i in range(len(vertices)) if f>>i&1) for f in critical))
print('critical_dims',dict(critical_dims),'matching_pairs',len(matching))
# Verify gradient DAG: unmatched incidence arrows from larger to smaller;
# each matching arrow points from smaller to larger.
indegree={f:0 for f in faces}
out=defaultdict(list)
for higher in faces:
    bits=higher
    while bits:
        bit=bits&-bits;bits-=bit
        lower=higher^bit
        if lower not in faces:continue
        if matching.get(lower)==higher:
            out[lower].append(higher);indegree[higher]+=1
        else:
            out[higher].append(lower);indegree[lower]+=1
Q=deque(f for f in faces if indegree[f]==0)
processed=0
while Q:
    f=Q.popleft();processed+=1
    for g in out[f]:
        indegree[g]-=1
        if indegree[g]==0:Q.append(g)
assert processed==len(faces)
print('acyclic_hasse_orientation',processed)
# Signed Morse boundary using path elimination on matched lower faces.
upper_to_lower={u:l for l,u in matching.items()}
def simplex_boundary(f):
    items=[i for i in range(len(vertices)) if f>>i&1]
    return [(f^(1<<v), -1 if i%2 else 1) for i,v in enumerate(items)]

@lru_cache(maxsize=None)
def projection(f):
    # projection to surviving critical generators in fixed chain degree
    if f in unmatched:return {f:1}
    if f in upper_to_lower:return {}
    assert f in matching
    high=matching[f]
    cf=next(c for lower,c in simplex_boundary(high) if lower==f)
    res=defaultdict(int)
    for low,c in simplex_boundary(high):
        if low!=f:
            for crit,coef in projection(low).items():res[crit]-=cf*c*coef
    return {k:v for k,v in res.items() if v}

M={}
for f in critical:
    d=defaultdict(int)
    if f.bit_count()>1:
        for low,c in simplex_boundary(f):
            for crit,coef in projection(low).items():d[crit]+=c*coef
    M[f]={k:v for k,v in d.items() if v}
    print('morse_boundary',tuple(i for i in range(len(vertices)) if f>>i&1),M[f])
assert all(not x for x in M.values())
print('verified_wedge:S2+S2+S3')

# Earlier natural sizes: one critical vertex plus one critical edge.
for n,steps in ((6,(2,1,0)),(7,(3,0,1,2,6,4,5))):
    smaller_vertices=tuple((i,j) for i in range(n) for j in range(i+1,n)
                          if min(j-i,n-(j-i))>=3)
    cn=tuple(tuple(j for j,q in enumerate(smaller_vertices)
                   if not(set(p)&set(q))) for p in smaller_vertices)
    sf=set()
    for neighborhood in cn:
        for subset in range(1,1<<len(neighborhood)):
            sf.add(sum(1<<neighborhood[i] for i in range(len(neighborhood)) if subset>>i & 1))
    sm=set(sf); pairs={}
    for v in steps:
        for f in sorted(sf):
            h=f|(1<<v)
            if f in sm and not(f & (1<<v)) and h in sm:
                pairs[f]=h;sm.remove(f);sm.remove(h)
    assert Counter(f.bit_count()-1 for f in sm)=={0:1,1:1}
    din={f:0 for f in sf}; arrows=defaultdict(list)
    for h in sf:
        x=h
        while x:
            bit=x&-x;x-=bit;l=h^bit
            if l not in sf:continue
            a,b=(l,h) if pairs.get(l)==h else (h,l)
            arrows[a].append(b);din[b]+=1
    q=deque(f for f in sf if din[f]==0);count=0
    while q:
        f=q.popleft();count+=1
        for g in arrows[f]:
            din[g]-=1
            if not din[g]:q.append(g)
    assert count==len(sf)
    print('size',n,'faces',len(sf),'pairs',len(pairs),'remaining_dims',
          dict(Counter(f.bit_count()-1 for f in sm)),'acyclic',count)
print('integral_homotopy_certificates_OK')
