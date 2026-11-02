#!/usr/bin/env python3
"""Exact standalone finite checker of Paley-11 directed flag triangulation.
Uses standard Python only; tests rational ranks by lower bounds over F_3 and chain exactness.
"""
from itertools import combinations
from collections import defaultdict, deque, Counter
from math import gcd

p=11; R={1,3,4,5,9}
def edge(u,v): return ((v-u)%p in R)
def transitive_order(v):
    out={u:sum(edge(u,w) for w in v if u!=w) for u in v}
    if len(set(out.values()))!=len(v): return None
    order=tuple(sorted(v,key=lambda u:-out[u]))
    assert all(edge(order[i],order[j]) for i in range(len(v)) for j in range(i+1,len(v)))
    return order
S={k:[tuple(c) for c in combinations(range(p),k+1) if transitive_order(c) is not None] for k in range(4)}
assert list(map(lambda d:len(S[d]),range(4)))==[11,55,110,55]
assert all(transitive_order(c) is None for c in combinations(range(p),5))
T=S[3]; edges=S[1]; tris=S[2]
# codimension-one degree
count=Counter(t for tetra in T for t in combinations(tetra,3))
assert set(count)==set(tris) and set(count.values())=={2}
# adjacency of top tetrahedra
te=defaultdict(list)
for i,tetra in enumerate(T):
 for face in combinations(tetra,3): te[face].append(i)
adj=[set() for _ in T]
for e,(i,j) in te.items(): adj[i].add(j);adj[j].add(i)
def cc(graph):
 seen={0};queue=[0]
 while queue:
  i=queue.pop()
  for j in graph[i]:
   if j not in seen: seen.add(j);queue.append(j)
 return len(seen)
assert cc(adj)==len(T)

def link_check(v):
  lvert=[u for u in range(p) if u!=v and (min(u,v),max(u,v)) in S[1]]
  ledges=[tuple(u for u in t if u!=v) for t in tris if v in t]
  ltris=[tuple(u for u in t if u!=v) for t in T if v in t]
  assert (len(lvert),len(ledges),len(ltris))==(10,30,20)
  ef=defaultdict(list)
  for i,t in enumerate(ltris):
   for j in range(3): ef[t[:j]+t[j+1:]].append((i,j))
  assert set(ef)==set(ledges) and all(len(x)==2 for x in ef.values())
  nbr={u:set() for u in lvert}
  for a,b in ledges:nbr[a].add(b);nbr[b].add(a)
  assert all(len(nbr[u])==6 for u in lvert)
  for u in lvert:
   graph={w:set() for w in nbr[u]}
   for t in ltris:
    if u in t:
      a,b=(x for x in t if x!=u)
      graph[a].add(b);graph[b].add(a)
   assert all(len(graph[a])==2 for a in graph)
   assert cc([{list(graph).index(b) for b in graph[a]} for a in graph])==6
  dual=[set() for _ in ltris]
  orient_adj=[[] for _ in ltris]
  for ed,((i,ji),(j,jj)) in ef.items():
   dual[i].add(j);dual[j].add(i)
   # constraint: sign_j=(-1)^(ji+jj+1)sign_i in sorted orientation, because boundary incidence of sorted triangle
   relation=(-1)**(ji+jj+1)
   orient_adj[i].append((j,relation)); orient_adj[j].append((i,relation))
  assert cc(dual)==len(ltris)
  sign={0:1}; parent={0:None}; stack=[0]; contradiction=None
  while stack and contradiction is None:
   i=stack.pop()
   for j,rel in orient_adj[i]:
    desired=sign[i]*rel
    if j not in sign: sign[j]=desired;parent[j]=i;stack.append(j)
    elif sign[j]!=desired:
     contradiction=(i,j,rel);break
  assert contradiction is not None
  return (lvert,ledges,ltris,contradiction)
for v in range(11): link_check(v)

# Standard simplicial signed boundaries of sorted faces.
def rank_mod3(k):
    if k==0:return 0
    lower=S[k-1]; idx={v:i for i,v in enumerate(lower)}
    rows=[{} for _ in lower]
    for j,face in enumerate(S[k]):
      for i in range(len(face)):
        v=face[:i]+face[i+1:]; rr=rows[idx[v]]; rr[j]=(-1 if i%2 else 1)%3
    # sparse row elimination over F3
    pivots={};rank=0
    for r in rows:
      d={j:x for j,x in r.items() if x}
      while d:
        c=min(d)
        if c not in pivots:
          inv=pow(d[c],-1,3)
          pivots[c]={j:(v*inv)%3 for j,v in d.items() if v%3}
          rank+=1;break
        f=d[c]
        for j,v in pivots[c].items():
          z=(d.get(j,0)-f*v)%3
          if z:d[j]=z
          elif j in d:del d[j]
    return rank
ranks={k:rank_mod3(k) for k in range(1,4)}
assert ranks=={1:10,2:45,3:55},ranks
# first differential upper bound 10 via augmentation, d2<= 55-rank(d1)=45, d3<= 55.
# So exact mod3 = rational ranks and rational Betti in all degrees = (1,0,10,0).

# All affine permutations are simplicial automorphisms, affine fixed sets with first simplex trace.
G=[(a,b) for a in sorted(R) for b in range(11)]
assert len(G)==55
assert all(sum(edge(u,w) and edge(v,w) for w in range(11) if w!=u and w!=v)==2 for u in range(11) for v in range(u+1,11))
for a,b in G:
    mapping={x:(a*x+b)%11 for x in range(11)}
    assert all(edge(mapping[u],mapping[v])==edge(u,v) for u in range(11) for v in range(11) if u!=v)
    fs=[x for x in range(11) if mapping[x]==x]
    # fixed simplices are pointwise fixed because no transitive tournament has a nontrivial automorphism
    lf=sum((-1)**k * sum(set(face).issubset(fs) for face in S[k]) for k in range(4))
    perm=sum(mapping[x]==x for x in range(11))
    h2=lf-1
    assert h2==perm-1,(a,b,h2,perm-1)
    if a==1 and b==0:assert (len(fs),lf,h2)==(11,11,10)
    elif a==1:assert (len(fs),lf,h2)==(0,0,-1)
    else:assert (len(fs),lf,h2)==(1,1,0)

# 55-element affine character: 0 invariant; 11-translation group:0 invariant; 5-dilation group:2 invariant.
def avg(subgroup):return sum(sum(1 for x in range(11) if (a*x+b)%11==x)-1 for a,b in subgroup)//len(subgroup)
assert avg(G)==0
assert avg([(1,b) for b in range(11)])==0
assert avg([(a,0) for a in R])==2
print('PALEY11_LINK_AND_AFFINE_CHARACTER_EXACT_OK')
print('f_vector 11 55 110 55; top_dual_connected 55')
print('each_link f_vector 10 30 20, edge_degree_2, links_6_cycles, dual_connected, orientation_conflict')
print('boundary_mod3_ranks 10 45 55; rational_betti 1 0 10 0')
print('G_order 55; H2_character 10 -1 0; invariants_G_C11_C5 0 0 2')
