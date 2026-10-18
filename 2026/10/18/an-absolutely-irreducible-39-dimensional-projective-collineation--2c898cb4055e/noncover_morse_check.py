import itertools,collections,time,sys
q=int(sys.argv[1]) if len(sys.argv)>1 else 3
p=(q-1) if q==3 else 1
# field q=3 (or q=2)
def canon(x):
 x=tuple(t%q for t in x)
 for z in x:
  if z:
   r=pow(z,-1,q)
   return tuple((a*r)%q for a in x)
 return None
pts=sorted({canon(x) for x in itertools.product(range(q),repeat=3)}-{None})
L=[frozenset(i for i,p in enumerate(pts) if sum(a*b for a,b in zip(l,p))%q==0) for l in pts]
assert len(set(L))==len(pts)
n=len(pts)
faces={0}
for l in L:
 x=[i for i in range(n) if i not in l]
 for k in range(1,len(x)+1):
  for z in itertools.combinations(x,k):faces.add(sum(1<<i for i in z))
assert n==13 and len(faces)==3862
assert [sum(m.bit_count()==k for m in faces) for k in range(10)]==[1,13,78,286,702,1170,1014,468,117,13]
print('n',n,'size',len(faces),'fvector',sorted(collections.Counter(m.bit_count()-1 for m in faces).items()),flush=True)
# sequential matching
u=faces-{0}; pairs=[]
for v in range(n):
 cur=[]
 for m in sorted(u):
  if m&(1<<v):continue
  t=m|(1<<v)
  if t in u:cur.append((m,t))
 for a,b in cur:
  u.remove(a);u.remove(b);pairs.append((a,b))
 print('pivot',v,'pairs',len(cur),'remaining',len(u),flush=True)
crit=collections.Counter(m.bit_count()-1 for m in u)
print('critical',crit,'total matched pairs',len(pairs))
# full directed poset verify acyclic (unmatched edge high -> low, matched edge low->high)
from collections import deque
indeg={m:0 for m in faces if m}; edges={m:[] for m in faces if m}
matched_up={a:b for a,b in pairs}
for m in faces:
 if m==0:continue
 for v in range(n):
  bit=1<<v
  if not m&bit:continue
  z=m^bit
  if z==0:continue
  if matched_up.get(z)==m:
   edges[z].append(m);indeg[m]+=1
  else:
   edges[m].append(z);indeg[z]+=1
ready=deque(m for m,d in indeg.items() if d==0)
c=0
while ready:
 m=ready.popleft();c+=1
 for z in edges[m]:
  indeg[z]-=1
  if indeg[z]==0:ready.append(z)
assert c==len(indeg) and sum(map(len,edges.values()))==20085
assert crit=={0:1,4:39,5:1} and len(pairs)==1910
print('acyclic',c==len(indeg),'vis',c,'needed',len(indeg),'incidences',sum(map(len,edges.values())))
from functools import lru_cache
critfaces={m for m in u if m}
lower_up={a:b for a,b in pairs}
upper_set={b for a,b in pairs}
upper5={b for b in upper_set if b.bit_count()==6}
print('critical dims/ids',[(m.bit_count()-1,m) for m in sorted(critfaces,key=lambda x:(x.bit_count(),x))][:50])
def oriented_boundary(m):
 inds=[i for i in range(n) if m&(1<<i)]
 for idx,i in enumerate(inds):yield m^(1<<i), (-1)**idx
@lru_cache(None)
def proj4(m):
 if m in critfaces:
  return {m:1} if m.bit_count()==5 else {}
 if m in upper_set:return {}
 if m in lower_up:
  top=lower_up[m]
  bd=dict(oriented_boundary(top)); den=bd[m]
  d=collections.Counter()
  for f,c in bd.items():
   if f==m:continue
   for z,v in proj4(f).items():d[z]-=c*den*v
  return {z:v for z,v in d.items() if v}
 raise ValueError('unknown simplex')
crit5=[m for m in critfaces if m.bit_count()==6]
for m in crit5:
 d=collections.Counter()
 for f,c in oriented_boundary(m):
  for z,v in proj4(f).items():d[z]+=c*v
 assert all(v==0 for v in d.values())
 print('crit5',m,'boundary',[(k,v) for k,v in d.items() if v],'all coeffs',len(d))
print('PASS: integral Morse complex has one 0-cell, thirty-nine 4-cells, one 5-cell, and all boundaries vanish')
