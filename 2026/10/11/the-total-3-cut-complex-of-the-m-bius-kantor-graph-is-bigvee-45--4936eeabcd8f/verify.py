#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque
import json

N = 16

def edge_set():
    e=set()
    def add(a,b):
        if a>b: a,b=b,a
        e.add((a,b))
    for i in range(8):
        add(i,(i+1)%8)
        add(i,8+i)
        add(8+i,8+((i+3)%8))
    return e

def build_complex():
    E=edge_set()
    adj=[[False]*N for _ in range(N)]
    for a,b in E:
        adj[a][b]=adj[b][a]=True
    independent=[]
    for t in combinations(range(N),3):
        if all(not adj[a][b] for a,b in combinations(t,2)):
            independent.append(sum(1<<v for v in t))
    full=(1<<N)-1
    facets=[full^m for m in independent]
    faces=set()
    for f in facets:
        s=f
        while True:
            faces.add(s)
            if s==0: break
            s=(s-1)&f
    return E,independent,facets,faces

def element_matching(faces):
    unmatched=set(faces)
    pairs=[]
    for v in range(N):
        b=1<<v
        for x in list(unmatched):
            if x&b: continue
            y=x|b
            if y in unmatched:
                unmatched.remove(x)
                unmatched.remove(y)
                pairs.append((x,y))
    return unmatched,pairs

def direct_acyclicity(faces,pairs):
    fs=list(faces)
    index={x:i for i,x in enumerate(fs)}
    matched=set(pairs)
    out=[[] for _ in fs]
    indeg=[0]*len(fs)
    arrows=0
    for upper in fs:
        bits=upper
        while bits:
            bit=bits & -bits
            lower=upper^bit
            i=index[lower]; j=index[upper]
            if (lower,upper) in matched:
                out[j].append(i); indeg[i]+=1
            else:
                out[i].append(j); indeg[j]+=1
            arrows+=1
            bits-=bit
    q=deque(i for i,d in enumerate(indeg) if d==0)
    seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return seen==len(fs), seen, arrows

def vertices(mask):
    return [i for i in range(N) if mask>>i & 1]

E, independent, facets, faces = build_complex()
unmatched,pairs = element_matching(faces)
acyclic,visited,arrows = direct_acyclicity(faces,pairs)
fvec=Counter(m.bit_count()-1 for m in faces if m)
critical=sorted(unmatched)
critical_dims=Counter(m.bit_count()-1 for m in critical)
chi=sum(((-1)**d)*c for d,c in fvec.items())

expected_fvec={0:16,1:120,2:560,3:1820,4:4368,5:8008,6:11440,7:12870,8:11440,9:8008,10:4368,11:1592,12:272}
assert len(E)==24
assert len(independent)==272
assert len(facets)==272 and len(set(facets))==272
assert len(faces)==64883
assert dict(sorted(fvec.items()))==expected_fvec
assert len(pairs)==32419
assert critical_dims==Counter({10:45})
assert 0 not in critical
assert acyclic and visited==len(faces) and arrows==515872
assert chi==46

out={
  "graph":{"vertices":N,"edges":len(E),"model":"generalized Petersen G(8,3)"},
  "independent_triples":len(independent),
  "facets":len(facets),
  "faces_including_empty":len(faces),
  "f_vector":expected_fvec,
  "euler_characteristic":chi,
  "element_matching_order":list(range(N)),
  "matched_pairs":len(pairs),
  "critical_cell_dimensions":dict(critical_dims),
  "critical_faces":[vertices(m) for m in critical],
  "hasse_arrows_checked":arrows,
  "hasse_vertices_checked":visited,
  "acyclic":acyclic,
  "conclusion":"Delta_3^t(G(8,3)) is homotopy equivalent to a wedge of 45 ten-spheres."
}
print(json.dumps(out,sort_keys=True,separators=(",",":")))
