#!/usr/bin/env python3
"""Independent exact combinatorial checks for the truncated-cube graph-metric Rips action."""
import itertools, math, collections, networkx as nx
import numpy as np
import sympy as sp
from functools import lru_cache

SIGNS=list(itertools.product((-1,1),repeat=3))
V=sorted((axis,signs) for axis in range(3) for signs in SIGNS)
idx={x:i for i,x in enumerate(V)}
G=nx.Graph();G.add_nodes_from(range(24))
for i,(a,s) in enumerate(V):
 for j,(b,t) in enumerate(V):
  if i>=j: continue
  if (a==b and sum(x!=y for x,y in zip(s,t))==1 and s[a]!=t[a]) or (a!=b and s==t): G.add_edge(i,j)
assert sorted(dict(G.degree()).values())==[3]*24
assert nx.is_isomorphic(G,nx.truncated_cube_graph())
dist=dict(nx.all_pairs_shortest_path_length(G))
assert max(max(u.values()) for u in dist.values())==6
H=nx.Graph(); H.add_nodes_from(G); H.add_edges_from((u,v) for u in G for v in G if u<v and dist[u][v]<=3)
F={}
for clique in nx.enumerate_all_cliques(H):
 q=tuple(sorted(clique)); F.setdefault(len(q),[]).append(q)
assert {k:len(v) for k,v in F.items()}=={1:24,2:156,3:376,4:372,5:144,6:20}
S={k:set(lst) for k,lst in F.items()}

# Geometric surface representing original polyhedral boundary.
big=1+2**.5
def xyz(i):
 axis,s=V[i]
 return np.array([s[j]*(1 if j==axis else big) for j in range(3)],dtype=float)
FACES=[]
for s in SIGNS:
 face=[idx[(a,s)] for a in range(3)]
 FACES.append((face,np.array(s,dtype=float)))
for fixed in range(3):
 for sign in (-1,1):
  face=[i for i,(a,s) in enumerate(V) if a!=fixed and s[fixed]==sign]
  assert len(face)==8
  sub=G.subgraph(face)
  assert all(d==2 for d in dict(sub.degree()).values())
  cycle=[min(face)];prev=None;cur=cycle[0]
  for _ in range(7):
   nxv=next(t for t in sorted(sub[cur]) if t!=prev)
   cycle.append(nxv);prev,cur=cur,nxv
  assert cycle[0] in sub[cycle[-1]] and set(cycle)==set(face)
  norm=np.zeros(3);norm[fixed]=sign
  FACES.append((cycle,norm))

def triangulate(cycle):
 n=len(cycle)
 @lru_cache(None)
 def sol(i,j):
  if j<=i+2:return [] if j==i+1 else [(cycle[i],cycle[i+1],cycle[j])]
  for k in range(i+1,j):
   a=cycle[i];b=cycle[k];c=cycle[j]
   if all(dist[x][y]<=3 for x,y in ((a,b),(b,c),(a,c))):
    left=sol(i,k);right=sol(k,j)
    if left is not None and right is not None:return left+right+[(a,b,c)]
  return None
 return sol(0,n-1)
z=collections.defaultdict(int)
for cycle,norm in FACES:
 tri=triangulate(cycle)
 assert tri is not None and len(tri)==len(cycle)-2
 for q in tri:
  a,b,c=map(xyz,q)
  orient=np.dot(np.cross(b-a,c-a),norm)
  assert abs(orient)>0.0001,(q,orient)
  s=1 if orient>0 else -1
  p=sorted(q)
  inversions=sum(q[i]>q[j] for i in range(3) for j in range(i+1,3))
  z[tuple(p)]+=s*(-1)**inversions
z={q:k for q,k in z.items() if k}
assert len(z)>0
bz=collections.Counter()
for q,k in z.items():
 for i in range(3):bz[q[:i]+q[i+1:]]+=(-1)**i*k
assert all(v==0 for v in bz.values()),'polygon triangulation chain is not a cycle'

# Modulo a prime, perform exact elimination to check the homological class.
prime=101
q2=sorted(F[3]);q3=sorted(F[4]);iq2={q:i for i,q in enumerate(q2)}
def sign_sort(seq):
 return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1
basis={}
def reduce_vec(vec,build=False):
 v=np.array(vec,dtype=np.int64)%prime
 for p in sorted(basis,reverse=True):
  t=int(v[p]);
  if t:v=(v-t*basis[p])%prime
 if build:
  if np.any(v):
   p=int(np.flatnonzero(v)[-1]);v=(v*pow(int(v[p]),-1,prime))%prime;basis[p]=v
 return v
for q in q3:
 v=np.zeros(len(q2),dtype=np.int64)
 for i in range(4):v[iq2[q[:i]+q[i+1:]]]=(-1)**i
 reduce_vec(v,True)
assert len(basis)==242,len(basis)
zv=np.zeros(len(q2),dtype=np.int64)
for q,c in z.items():zv[iq2[q]]=c
assert np.any(reduce_vec(zv)),'boundary sphere did not survive in H2 mod 101'

# Octahedral group coordinates: first a coordinate permutation, then coordinate signs.
perms=list(itertools.permutations(range(3)))
GROUP=[]
for perm in perms:
 for signs in SIGNS:
  maps=[]
  for axis,ss in V:
   na=perm.index(axis) # new coordinate i receives old perm[i]
   ns=tuple(signs[i]*ss[perm[i]] for i in range(3))
   maps.append(idx[(na,ns)])
  assert len(set(maps))==24
  pp=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
  det=pp*math.prod(signs)
  GROUP.append((perm,signs,det,tuple(maps)))
assert len({g[3] for g in GROUP})==48

def action_on_cycle(g,v):
 out=np.zeros(len(q2),dtype=np.int64)
 for q,c in z.items():
  im=tuple(g[x] for x in q)
  out[iq2[tuple(sorted(im))]]+=c*sign_sort(im)
 return out
for _,_,det,g in GROUP:
 assert not np.any(reduce_vec(action_on_cycle(g,zv)-det*zv)),('bad orientation character',g)

# Rotate body diagonals of parent cube to label the rotational subgroup S4.
DIAGS=sorted({min(ss,tuple(-x for x in ss)) for ss in SIGNS})
assert len(DIAGS)==4
DIDX={s:i for i,s in enumerate(DIAGS)}
def type_s4(perm,signs,det):
 rot_signs=tuple(t*(1 if det==1 else -1) for t in signs)
 im=[]
 for ss in DIAGS:
  out=tuple(rot_signs[i]*ss[perm[i]] for i in range(3))
  im.append(DIDX[min(out,tuple(-x for x in out))])
 assert sorted(im)==list(range(4))
 remain=set(range(4));lens=[]
 while remain:
  x=min(remain);cur=x;n=0
  while cur in remain:
   remain.remove(cur);n+=1;cur=im[cur]
  lens.append(n)
 return tuple(sorted(lens,reverse=True))

char={}
for perm,signs,det,g in GROUP:
 L=0
 for dim,cs in F.items():
  for q in cs:
   im=tuple(g[x] for x in q)
   if tuple(sorted(im))==q: L+=(-1)**(dim-1)*sign_sort(im)
 h3=1+det-L
 cls=(type_s4(perm,signs,det), 0 if det==1 else 1)
 assert cls not in char or char[cls]==(det,h3,L), ('character not class constant',cls)
 char[cls]=(det,h3,L)

sizes={(1,1,1,1):1,(2,1,1):6,(2,2):3,(3,1):8,(4,):6}
chars={(4,):[1,1,1,1,1],(3,1):[3,1,-1,0,-1],(2,2):[2,0,2,-1,0],(2,1,1):[3,-1,-1,0,1],(1,1,1,1):[1,-1,1,1,-1]}
types=list(sizes)
for cl in types:
 print('class',cl,'size',sizes[cl],'H2/H3/L positive',char[(cl,0)],'negative',char[(cl,1)])
print('H3 multiplicities:')
for part,values in chars.items():
 for parity in (0,1):
  numerator=sum(sizes[cl]*char[(cl,e)][1]*values[types.index(cl)]*((-1)**(parity*e)) for cl in types for e in (0,1))
  assert numerator%48==0,(part,parity,numerator)
  m=numerator//48
  if m:print(part,'central parity',parity,'multiplicity',m)
assert sum(char[(cl,e)][1]*sizes[cl] for cl in types for e in (0,1))%48==0
# Independently determine all rational boundary ranks (not just ranks modulo 101).
ranks = {}
for dim in range(2,7):
    low=sorted(F[dim-1]); high=sorted(F[dim]); ir={x:j for j,x in enumerate(low)}
    mat=sp.MutableSparseMatrix(len(low),len(high),{})
    for j,q in enumerate(high):
        for i in range(dim): mat[ir[q[:i]+q[i+1:]],j]=(-1)**i
    ranks[dim-1]=mat.rank()
assert ranks=={1:23,2:133,3:242,4:124,5:20},ranks
# Confirm no rank drops at the prime used for the orientation class.
mod_ranks={}
for dim in range(2,7):
    low=sorted(F[dim-1]); high=sorted(F[dim]); ir={x:j for j,x in enumerate(low)}
    mbase={}
    for q in high:
        vec=np.zeros(len(low),dtype=np.int64)
        for i in range(dim):vec[ir[q[:i]+q[i+1:]]]=(-1)**i
        vec%=prime
        for p in sorted(mbase,reverse=True):
            if vec[p]:vec=(vec-int(vec[p])*mbase[p])%prime
        if np.any(vec):
            pivot=int(np.flatnonzero(vec)[-1])
            mbase[pivot]=(vec*pow(int(vec[pivot]),-1,prime))%prime
    mod_ranks[dim-1]=len(mbase)
assert mod_ranks==ranks,mod_ranks
assert [len(F[k])-ranks.get(k-1,0)-ranks.get(k,0) for k in range(1,7)]==[1,0,1,6,0,0]
print('RESULT PASS; faces',sum(len(x) for x in F.values()),'boundary_ranks_Q',ranks,'rank d3 mod101',len(basis),'surface triangles',len(z),'Rips diam',6)
