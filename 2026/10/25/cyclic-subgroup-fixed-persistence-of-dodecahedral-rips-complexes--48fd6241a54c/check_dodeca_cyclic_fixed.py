#!/usr/bin/env python3
"""Exact finite verification of cyclic geometric-fixed Rips persistence on the dodecahedral graph.
No external packages are needed. All graph searches are exhaustive and integer-valued.
"""
from itertools import permutations, combinations
from collections import Counter, defaultdict

N=20
V=tuple(range(N))
E=set()
def edge(a,b):E.add(frozenset((a,b)))
for i in range(10):
 edge(i,(i+1)%10)                 # outer decagon
 edge(i,10+i)                     # spoke
 edge(10+i,10+((i+2)%10))        # two inner pentagons
assert len(E)==30
adj=[set() for _ in V]
for a,b in (tuple(x) for x in E): adj[a].add(b);adj[b].add(a)
assert all(len(a)==3 for a in adj)
dist=[]
for v in V:
 d={v:0};q=[v]
 for x in q:
  for y in adj[x]:
   if y not in d:d[y]=d[x]+1;q.append(y)
 assert len(d)==N
 dist.append(tuple(d[x] for x in V))
assert max(max(x) for x in dist)==5
identity=tuple(V)
def mul(p,q):return tuple(p[q[i]] for i in V)
def inv(p):
 res=[None]*N
 for i,j in enumerate(p):res[j]=i
 return tuple(res)
def power_subgroup(p):
 a=identity;out=[]
 while a not in out:
  out.append(a);a=mul(p,a)
 assert a==identity
 return frozenset(out)

# An automorphism is determined by its images of a chosen vertex and three neighbors
# plus a completion. Enumerating ALL compatible assignments avoids hidden assumptions.
def automorphisms():
 result=set();root=0;near=tuple(sorted(adj[root])); attempts=0
 def extend(fwd):
  if len(fwd)==N:
   p=tuple(fwd[i] for i in V)
   assert all(dist[i][j]==dist[p[i]][p[j]] for i in V for j in V)
   result.add(p)
   return
  used=set(fwd.values());opts=[]
  for v in V:
   if v in fwd:continue
   candidates=[w for w in V if w not in used and all(dist[v][x]==dist[w][fwd[x]] for x in fwd)]
   if not candidates:return
   opts.append((len(candidates),-len(adj[v].intersection(fwd)),v,candidates))
  _,__,v,candidates=min(opts)
  for w in candidates:
   fwd[v]=w;extend(fwd);del fwd[v]
 for target in V:
  for images in permutations(sorted(adj[target])):
   attempts+=1
   a={root:target}
   a.update(dict(zip(near,images)))
   extend(a)
 assert attempts==120
 return result

autos=automorphisms()
assert len(autos)==120
assert identity in autos
assert all(mul(p,q) in autos for p in autos for q in (identity,))
subgroups={power_subgroup(p) for p in autos if p!=identity}
assert len(subgroups)==63
anti=next(p for p in autos if all(dist[i][p[i]]==5 for i in V))
assert len(power_subgroup(anti))==2

def typ(H):
 order=len(H);a=next(x for x in H if x!=identity)
 if order==2:
  if all(dist[i][a[i]]==5 for i in V):return 'inversion-C2'
  if sum(a[i]==i for i in V)==4:return 'reflection-C2'
  assert all(a[i]!=i for i in V)
  return 'rotation-C2'
 return {3:'rotation-C3',5:'rotation-C5',6:'rotatory-C6',10:'rotatory-C10'}[order]
classes=defaultdict(list)
for H in subgroups:classes[typ(H)].append(H)
assert dict((k,len(v)) for k,v in classes.items())=={
 'rotation-C2':15,'inversion-C2':1,'reflection-C2':15,'rotation-C3':10,
 'rotation-C5':6,'rotatory-C6':10,'rotatory-C10':6}
# Confirm each of the seven types forms a single conjugacy class of cyclic subgroups.
for kind,sub in classes.items():
 H=sub[0]; all_conj=set()
 for g in autos:
  gi=inv(g); all_conj.add(frozenset(mul(mul(g,h),gi) for h in H))
 assert all_conj==set(sub),(kind,len(all_conj),len(sub))

# An invariant barycentric point corresponds to a convex combination of uniform
# probability measures on admissible vertex orbits. Its simplex is their union.
def orbits(H):
 remaining=set(V);result=[]
 while remaining:
  v=min(remaining);orbit=frozenset(h[v] for h in H)
  assert orbit<=remaining
  result.append(orbit);remaining-=orbit
 return result

def complex_at(H,r):
 orbitlist=[o for o in orbits(H) if all(dist[x][y]<=r for x in o for y in o)]
 n=len(orbitlist)
 adjacent={(i,j) for i in range(n) for j in range(i+1,n)
           if all(dist[x][y]<=r for x in orbitlist[i] for y in orbitlist[j])}
 # Exhaustive flag-face enumeration; empty face excluded.
 faces=set()
 for mask in range(1,1<<n):
  vs=frozenset(i for i in range(n) if mask>>i&1)
  if all((min(i,j),max(i,j)) in adjacent for i,j in combinations(vs,2)):
   faces.add(vs)
 assert all(f-{v} in faces for f in faces if len(f)>1 for v in f)
 return orbitlist,faces

def elementary_collapse(faces):
 faces=set(faces);steps=[]
 while True:
  free=None
  for z in sorted(faces,key=lambda x:(-len(x),tuple(sorted(x)))):
   if len(z)<2:continue
   for v in sorted(z):
    f=z-{v}
    if sum(1 for w in faces if len(w)==len(z) and f<w)==1:
     free=(f,z);break
   if free:break
  if free is None:break
  f,z=free
  assert f in faces and z in faces
  assert not any(f<w and w!=z for w in faces),('invalid elementary collapse',f,z)
  faces.remove(f);faces.remove(z);steps.append((f,z))
 return faces,steps

def components_graph(faces):
 vertices=set(v for f in faces for v in f)
 edges={frozenset(x) for x in faces if len(x)==2}
 comps=[]
 while vertices:
  x=min(vertices);C={x};todo=[x]
  for u in todo:
   for e in edges:
    if u in e:
     v=next(iter(e-{u}))
     if v not in C:C.add(v);todo.append(v)
  vertices-=C;comps.append(C)
 return len(comps),len(edges),sum(len(c) for c in comps)

EXPECTED={
 'rotation-C2':['empty','2pts','2pts','S1','S3','point'],
 'inversion-C2':['empty','empty','empty','empty','empty','point'],
 'reflection-C2':['4pts','4pts','S1','S1','S5','point'],
 'rotation-C3':['2pts','2pts','2pts','wedge3S1','S3','point'],
 'rotation-C5':['empty','empty','2pts','2pts','S1','point'],
 'rotatory-C6':['empty','empty','empty','empty','empty','point'],
 'rotatory-C10':['empty','empty','empty','empty','empty','point']
}
def classify(faces):
 if not faces:return 'empty'
 nv=sum(len(s)==1 for s in faces)
 if len(faces)==(1<<nv)-1:return 'point'
 # complete multipartite 2x...x2 => join of S^0, hence S^(k-1)
 graph={frozenset(f) for f in faces if len(f)==2}
 if nv==2 and not graph:return '2pts'
 missing={frozenset((i,j)) for i in range(nv) for j in range(i+1,nv) if frozenset((i,j)) not in graph}
 if nv%2==0 and len(missing)==nv//2 and all(sum(v in x for x in missing)==1 for v in range(nv)):
  return 'S'+str(nv//2-1)
 res,pairs=elementary_collapse(faces)
 assert all(len(x)<=2 for x in res)
 nc,ne,nvr=components_graph(res)
 beta1=ne-nvr+nc
 assert beta1>=0
 if beta1==0:return 'point' if nc==1 else str(nc)+'pts'
 assert nc==1
 return 'S1' if beta1==1 else 'wedge'+str(beta1)+'S1'

representatives={};tables={};allchecked=0
for kind in EXPECTED:
 rep=min(classes[kind],key=lambda x:sorted(x))
 representatives[kind]=rep
 data=[]
 for r in range(6):
  orbitlist,faces=complex_at(rep,r)
  t=classify(faces)
  # A sole forest with several components reduces to a set of components.
  if t not in EXPECTED[kind][r:r+1]:
   if len(faces)>0:
    rem,_=elementary_collapse(faces)
    nc,ne,nv=components_graph(rem)
    if ne==0:t=str(nc)+'pts'
  assert t==EXPECTED[kind][r],(kind,r,t,EXPECTED[kind][r])
  data.append((len(orbitlist),tuple(Counter(len(x) for x in faces)[i] for i in range(1,max(map(len,faces),default=0)+1)),t))
 tables[kind]=data
 for H in classes[kind]:
  for r in range(6):
   assert classify(complex_at(H,r)[1])==EXPECTED[kind][r],(kind,r)
   allchecked+=1

# Validate the exact critical face vectors and elementary-collapse certificate sizes.
CRITICAL_FACES={
 ('rotation-C2',3):(6,8,2),('rotation-C2',4):(8,24,32,16),
 ('reflection-C2',2):(10,18,8),('reflection-C2',3):(10,30,30,10),
 ('reflection-C2',4):(12,60,160,240,192,64),
 ('rotation-C3',3):(8,14,4),('rotation-C3',4):(8,24,32,16),
 ('rotation-C5',4):(4,4)}
CRITICAL_COLLAPSES={('rotation-C2',3):3,('reflection-C2',2):11,
                    ('reflection-C2',3):33,('rotation-C3',3):5}
for (kind,r),fvector in CRITICAL_FACES.items():
 _,faces=complex_at(representatives[kind],r)
 assert tuple(Counter(map(len,faces))[i] for i in range(1,len(fvector)+1))==fvector
for (kind,r),numpairs in CRITICAL_COLLAPSES.items():
 _,faces=complex_at(representatives[kind],r)
 rest,pairs=elementary_collapse(faces)
 assert len(pairs)==numpairs,(kind,r,len(pairs))
 assert all(len(x)<=2 for x in rest)

# Test the nontrivial persistence connecting map in integral H_1 for reflection-C2.
H=representatives['reflection-C2']
orb2,fac2=complex_at(H,2)
orb3,fac3=complex_at(H,3)
assert orb2==orb3
res2,seq2=elementary_collapse(fac2)
res3,seq3=elementary_collapse(fac3)
def fundamental_cycle(faces):
 ed={tuple(sorted(f)) for f in faces if len(f)==2}
 vv={next(iter(f)) for f in faces if len(f)==1}
 # Find a shortest lexicographic simple cycle in a connected graph.
 for size in range(3,len(vv)+1):
  for c in combinations(sorted(vv),size):
   start=c[0]
   for path in permutations(c[1:]):
    seq=(start,)+path
    if all(tuple(sorted((a,b))) in ed for a,b in zip(seq,seq[1:]+seq[:1])):
     return seq
 raise AssertionError('no cycle')
cycle2=fundamental_cycle(res2)
cycle3=fundamental_cycle(res3)
chain=Counter()
def add(a,b,n):
 x=tuple(sorted((a,b)))
 chain[x]+=n*(1 if a<b else -1)
 if not chain[x]:del chain[x]
for a,b in zip(cycle2,cycle2[1:]+cycle2[:1]):add(a,b,1)
for small,big in seq3:
 if len(small)==2 and len(big)==3:
  u,v=sorted(small);coef=chain.pop((u,v),0)
  if coef:
   T=sorted(big)
   facets=[T[:j]+T[j+1:] for j in range(3)]
   k=next(j for j,x in enumerate(facets) if set(x)==set(small))
   for j,x in enumerate(facets):
    if j!=k:add(x[0],x[1],coef*((-1)**(k+j+1)))
 elif len(small)==1 and len(big)==2:
  assert chain.get(tuple(sorted(big)),0)==0
# Check the image is exactly the primitive cycle of the surviving graph up to sign.
ref=Counter()
for a,b in zip(cycle3,cycle3[1:]+cycle3[:1]):
 k=tuple(sorted((a,b)));ref[k]+=(1 if a<b else -1)
assert chain==ref or all(chain.get(e,0)==-ref.get(e,0) for e in set(chain)|set(ref))

for kind in EXPECTED:
 print(kind,'subgroups',len(classes[kind]),'stage-data',tables[kind])
print('DODECAHEDRAL_CYCLIC_FIXED_PERSISTENCE_VERIFIED',len(autos),len(subgroups),allchecked)
print('REFLECTION_INTEGRAL_H1_PERSISTENCE_ISOMORPHISM_VERIFIED',cycle2,cycle3)
