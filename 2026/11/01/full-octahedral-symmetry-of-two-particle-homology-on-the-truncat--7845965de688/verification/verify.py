#!/usr/bin/env python3
"""Reproduce homology characters for two unordered particles on the truncated-octahedral graph.

Uses integer cells, boundary incidence, and all signed coordinate permutations.
Requirements: Python 3.9+ standard library only.
"""
from itertools import permutations, product, combinations
from collections import defaultdict
import json, hashlib

V=sorted({tuple(t*a for t,a in zip(s,p)) for p in set(permutations((0,1,2))) for s in product((-1,1),repeat=3)})
assert len(V)==24
vi={v:i for i,v in enumerate(V)}
E=sorted((i,j) for i,j in combinations(range(24),2) if sum((V[i][k]-V[j][k])**2 for k in range(3))==2)
assert len(E)==36
ed={e:i for i,e in enumerate(E)}
adj=[set() for _ in V]
for a,b in E:adj[a].add(b);adj[b].add(a)
assert all(len(n)==3 for n in adj)
# Every graph four-cycle is one of the six square facets.  At each vertex
# precisely two incident edges lie on a four-cycle.  Therefore a vertex
# stabilizer has size <=2, giving |Aut(T)|<=24*2=48.  The explicit signed
# coordinate symmetries attain that bound.
cycles4=set()
for quad in combinations(range(24),4):
 for a,b,c,d in ((quad[0],quad[1],quad[2],quad[3]),(quad[0],quad[1],quad[3],quad[2]),(quad[0],quad[2],quad[1],quad[3])):
  if b in adj[a] and c in adj[b] and d in adj[c] and a in adj[d]:
   cycles4.add(frozenset(quad))
assert len(cycles4)==6
# Contracting each unique square yields an octahedral graph K_{2,2,2}.
# Every original vertex is determined by its square and the square at
# the other endpoint of its unique non-square incident edge.
squares=list(cycles4)
sq_of={v:i for i,f in enumerate(squares) for v in f}
assert len(sq_of)==24
cross_edges=[(a,b) for a,b in E if sq_of[a]!=sq_of[b]]
assert len(cross_edges)==12
square_pairs={tuple(sorted((sq_of[a],sq_of[b]))) for a,b in cross_edges}
assert len(square_pairs)==12
sq_neighbors=[set() for _ in squares]
for a,b in square_pairs:sq_neighbors[a].add(b);sq_neighbors[b].add(a)
assert all(len(neighbors)==4 for neighbors in sq_neighbors)
assert len({tuple(sorted((i,j))) for i,j in combinations(range(6),2) if j not in sq_neighbors[i]})==3
for f in squares:
 assert len({sq_of[b] for a in f for b in adj[a] if sq_of[b]!=sq_of[a]})==4
for v in range(24):
 containing=[f for f in cycles4 if v in f]
 assert len(containing)==1
 assert len(adj[v]&containing[0])==2

# The convex hull facets are six square coordinate facets and eight signed-sum hexagons.
face_spec=[]
for k in range(3):
 for s in (-1,1):face_spec.append(((k,s),frozenset(i for i,v in enumerate(V) if v[k]==2*s)))
for s in product((-1,1),repeat=3):face_spec.append((('hex',)+s,frozenset(i for i,v in enumerate(V) if sum(s[k]*v[k] for k in range(3))==3)))
faces=[f for _,f in face_spec]
assert len(set(faces))==14
assert sorted(map(len,faces))==[4]*6+[6]*8
fi={f:i for i,f in enumerate(faces)}

def cross(u,v):
 return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))

def orient(f,n):
 a=min(f);nb=sorted(adj[a]&f)
 assert len(nb)==2
 order=[a,nb[0]]
 while len(order)<len(f):
  nxt=(adj[order[-1]]&f)-{order[-2]}
  assert len(nxt)==1
  v=next(iter(nxt)); assert v not in order
  order.append(v)
 assert order[0] in adj[order[-1]]
 for v in f:assert len(adj[v]&f)==2
 if dot(cross(sub(V[order[1]],V[order[0]]),sub(V[order[2]],V[order[1]])),n)<0:
  order=[order[0]]+list(reversed(order[1:]))
 assert dot(cross(sub(V[order[1]],V[order[0]]),sub(V[order[2]],V[order[1]])),n)>0
 return order

oriented=[]
for spec,f in face_spec:
 if spec[0]=='hex':normal=spec[1:]
 else:
  k,s=spec;normal=tuple(s if i==k else 0 for i in range(3))
 oriented.append(orient(f,normal))

edgecyc=[]
for cyc in oriented:
 d={}
 for a,b in zip(cyc,cyc[1:]+cyc[:1]):
  e=tuple(sorted((a,b)));idx=ed[e]
  d[idx]=1 if a<b else -1
 edgecyc.append(d)
pairs=[(i,j) for i,j in combinations(range(14),2) if not faces[i]&faces[j]]
assert len(pairs)==55
pairindex={x:i for i,x in enumerate(pairs)}

C0=list(combinations(range(24),2)); c0idx={z:i for i,z in enumerate(C0)}
C1=[(v,i) for i,(a,b) in enumerate(E) for v in range(24) if v not in (a,b)]
c1idx={z:i for i,z in enumerate(C1)}
C2=[(i,j) for i,j in combinations(range(36),2) if not set(E[i])&set(E[j])]
c2idx={z:i for i,z in enumerate(C2)}
assert (len(C0),len(C1),len(C2))==(276,792,558)

def boundary1(v,i):
 a,b=E[i]
 return {c0idx[tuple(sorted((v,b)))]:1,c0idx[tuple(sorted((v,a)))]:-1}

def boundary2(i,j):
 a,b=E[i];c,d=E[j]
 return {c1idx[(b,j)]:1,c1idx[(a,j)]:-1,c1idx[(d,i)]:-1,c1idx[(c,i)]:1}

# Boundary^2=0 and bitset rank over F_2, independent of literature.
for e in C2:
 s={}
 for idx,c in boundary2(*e).items():
  for v,t in boundary1(*C1[idx]).items():s[v]=s.get(v,0)+c*t
 assert all(v==0 for v in s.values())

def rank_mod2(columns):
 pivots={}
 for col in columns:
  while col:
   p=col.bit_length()-1
   if p not in pivots:pivots[p]=col;break
   col^=pivots[p]
 return len(pivots)
b2rank=rank_mod2(sum(1<<idx for idx in boundary2(*z)) for z in C2)
assert b2rank==503

# Integral top cycles from pairs of vertex-disjoint oriented facial boundaries.
tori=[]
for f,h in pairs:
 z={}
 for i,ci in edgecyc[f].items():
  for j,cj in edgecyc[h].items():
   key=tuple(sorted((i,j)))
   assert key in c2idx
   col=c2idx[key]
   z[col]=z.get(col,0)+ci*cj*(1 if i<j else -1)
 assert z and all(a in (-1,1) for a in z.values())
 bd={}
 for col,a in z.items():
  for row,v in boundary2(*C2[col]).items():bd[row]=bd.get(row,0)+a*v
 assert all(x==0 for x in bd.values())
 tori.append(z)
assert rank_mod2(sum(1<<i for i in z) for z in tori)==55

# All 48 signed-permutation symmetries, induced on each cellular chain degree.
def parity(p):return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def s4class(p,s):
 diags=[(1,*r) for r in product((-1,1),repeat=2)]
 dsets=[frozenset((d,tuple(-x for x in d))) for d in diags]
 didx={d:i for i,d in enumerate(dsets)}
 perm=[]
 for d in diags:
  y=tuple(s[k]*d[p[k]] for k in range(3))
  perm.append(didx[frozenset((y,tuple(-x for x in y)))])
 cyc=[];seen=set()
 for i in range(4):
  if i in seen:continue
  l=0;j=i
  while j not in seen:seen.add(j);l+=1;j=perm[j]
  cyc.append(l)
 return tuple(sorted(cyc,reverse=True)),s[0]*s[1]*s[2]

classes=defaultdict(list)
actions_on_faces=[]
so3=[]; central=[]; classcheck=[]
for p in permutations(range(3)):
 for s in product((-1,1),repeat=3):
  vp=[vi[tuple(s[k]*v[p[k]] for k in range(3))] for v in V]
  epi=[];esign=[]
  for a,b in E:
   x,y=vp[a],vp[b];epi.append(ed[tuple(sorted((x,y)))]);esign.append(1 if x<y else -1)
  assert len(set(epi))==36
  fp=[fi[frozenset(vp[v] for v in f)] for f in faces]
  assert len(set(fp))==14
  actions_on_faces.append(tuple(fp))
  # Check action on every oriented face cycle: det of signed orthogonal matrix.
  det=parity(p)*s[0]*s[1]*s[2]
  for idx,d in enumerate(edgecyc):
   image={epi[k]:v*esign[k] for k,v in d.items()}
   assert image=={k:det*v for k,v in edgecyc[fp[idx]].items()}
  # Action on the cell bases.
  def on1(row):
   v,i=C1[row]
   return c1idx[(vp[v],epi[i])],esign[i]
  def on2(row):
   i,j=C2[row];x,y=epi[i],epi[j]
   return c2idx[tuple(sorted((x,y)))],esign[i]*esign[j]*(1 if x<y else -1)
  for j,(v,i) in enumerate(C1):
   # Boundary of the image equals image of the boundary.
   ni,sg=on1(j)
   left={k:sg*a for k,a in boundary1(*C1[ni]).items()}
   right={c0idx[tuple(sorted((vp[C0[k][0]],vp[C0[k][1]])))]:a for k,a in boundary1(v,i).items()}
   assert left==right
  for j,(i,k) in enumerate(C2):
   ni,sg=on2(j)
   left={v:sg*a for v,a in boundary2(*C2[ni]).items()}
   right={}
   for row,a in boundary2(i,k).items():
    target,t=on1(row)
    right[target]=right.get(target,0)+a*t
   assert left==right
  # Independently reconstruct top-degree action using complete integral cycles.
  for (f,h),z in zip(pairs,tori):
   a,b=fp[f],fp[h];key=tuple(sorted((a,b)))
   sg=1 if a<b else -1
   target=tori[pairindex[key]]
   image={}
   for row,co in z.items():
    idx,t=on2(row);image[idx]=image.get(idx,0)+co*t
   assert image=={idx:sg*co for idx,co in target.items()}
  chi2=sum(1 if fp[f]==f and fp[h]==h else (-1 if fp[f]==h and fp[h]==f else 0) for f,h in pairs)
  tr0=sum(tuple(sorted((vp[a],vp[b])))==(a,b) for a,b in C0)
  tr1=sum(on1(idx)[1] for idx,(v,i) in enumerate(C1) if on1(idx)[0]==idx)
  tr2=sum(on2(idx)[1] for idx,z in enumerate(C2) if on2(idx)[0]==idx)
  chi1=1+chi2-tr0+tr1-tr2
  cls=s4class(p,s)
  classes[cls].append((chi1,chi2,tr0,tr1,tr2))
  if det==1:so3.append((chi1,chi2))
  if p==(0,1,2) and s in ((1,1,1),(-1,-1,-1)):central.append((chi1,chi2))
assert len(classes)==10 and sum(map(len,classes.values()))==48
for cls,v in classes.items():assert len(set(v))==1
assert classes[((1,1,1,1),1)][0][:2]==(14,55)
assert sum(len(a)*a[0][0] for a in classes.values())==0
assert sum(len(a)*a[0][1] for a in classes.values())==48
assert sum(z[0] for z in so3)==48 and sum(z[1] for z in so3)==24
assert sum(z[0] for z in central)==14 and sum(z[1] for z in central)==48

# Signed permutation orbit decomposition of the integral face-torus basis.
# A pair interchange inside the stabilizer makes that orbit's invariant zero.
notseen=set(pairs)
face_orbits=[]
while notseen:
 pair=min(notseen)
 orbit={tuple(sorted((g[pair[0]],g[pair[1]]))) for g in actions_on_faces}
 assert orbit<=notseen
 notseen-=orbit
 swaps=any(g[pair[0]]==pair[1] and g[pair[1]]==pair[0] for g in actions_on_faces)
 typ=('square-square' if pair[0]<6 and pair[1]<6 else 'hexagon-hexagon' if pair[0]>=6 else 'square-hexagon')
 face_orbits.append({'face_types':typ,'size':len(orbit),'pair_interchange_in_stabilizer':swaps})
assert sorted((x['face_types'],x['size'],x['pair_interchange_in_stabilizer']) for x in face_orbits)==sorted([
 ('square-square',3,True),('square-square',12,True),('hexagon-hexagon',4,True),('hexagon-hexagon',12,True),('square-hexagon',24,False)])
# Character decomposition for S_4 x C_2; irreducible representations rational over Q.
labels=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
s4chars={'1':(1,1,1,1,1),'sgn':(1,-1,1,1,-1),'V3':(3,1,-1,0,-1),'V3sgn':(3,-1,-1,0,1),'V2':(2,0,2,-1,0)}
decomps={1:[],2:[]}
for h in (1,2):
 for name,ch in s4chars.items():
  for eps in (1,-1):
   num=sum(len(entries)*entries[0][h-1]*ch[labels.index(part)]*(eps if sign==-1 else 1) for (part,sign),entries in classes.items())
   assert num%48==0
   mult=num//48
   assert mult>=0
   if mult:decomps[h].append({'irreducible':name,'central_sign':eps,'multiplicity':mult})
 assert sum(s4chars[x['irreducible']][0]*x['multiplicity'] for x in decomps[h])==(14 if h==1 else 55)

summary={'graph':{'vertices':len(V),'edges':len(E),'square_faces':6,'hexagonal_faces':8,'disjoint_face_pairs':len(pairs)},'cells':[len(C0),len(C1),len(C2)],'mod2_boundary2_rank':b2rank,'mod2_top_torus_rank':55,'automorphisms':48,'face_pair_orbits':sorted(face_orbits,key=lambda x:(x['face_types'],x['size'])),'all_four_cycles':len(cycles4),'square_contraction_graph':'K_2,2,2','automorphism_order_upper_bound':48,'classes':[{'S4_cycle_type':list(part),'central_sign':sgn,'count':len(entries),'H1_trace':entries[0][0],'H2_trace':entries[0][1],'cell_traces':list(entries[0][2:])} for (part,sgn),entries in sorted(classes.items())],'decompositions':decomps,'quotient_positive_betti':{'full':[0,1],'SO3':[2,1],'central_inversion':[7,24]},'checks':['all_boundary_squares_zero','all_55_integral_tori_closed','all_55_tori_linearly_independent_mod_2','all_48_automorphisms_chain_maps','all_48_torus_actions_verified','all_irreducible_inner_products_exact']}
print(json.dumps(summary,indent=2,sort_keys=True))
