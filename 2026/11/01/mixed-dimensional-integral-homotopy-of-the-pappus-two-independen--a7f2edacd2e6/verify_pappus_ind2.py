#!/usr/bin/env python3
"""Exact Pappus-graph two-independence homotopy certificate (stdlib only)."""
from collections import Counter,deque
edges=[(0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),(3,4),(3,10),(4,5),(4,15),(5,6),(6,7),(6,11),(7,8),(7,14),(8,9),(9,10),(9,16),(10,11),(11,12),(12,13),(12,17),(13,14),(14,15),(15,16),(16,17)]
nb=[0]*18
for a,b in edges:nb[a]|=1<<b;nb[b]|=1<<a
faces={0}
for v in range(18):
 bit=1<<v
 for a in tuple(faces):
  b=a|bit
  if (a&nb[v]).bit_count()<=1 and all((b&nb[i]).bit_count()<=1 for i in range(18) if (b>>i)&1):faces.add(b)
assert len(faces)==20652
f=Counter(x.bit_count()-1 for x in faces)
assert dict(f)=={-1:1,0:18,1:153,2:762,3:2394,4:4806,5:6027,6:4428,7:1728,8:308,9:27}
assert len(edges)==27 and all(n.bit_count()==3 for n in nb)
# Independently reconstruct the same graph from the standard Pappus LCF
# notation [5,7,-7,7,-7,-5]^3 on a Hamiltonian eighteen-cycle.
offsets=(5,7,-7,7,-7,-5)*3
cycle={tuple(sorted((i,(i+1)%18))) for i in range(18)}
chords={tuple(sorted((i,(i+offsets[i])%18))) for i in range(18)}
assert cycle | chords == set(edges)

# Independent entire Boolean-cube check of membership (no incremental use).
for mask in range(1<<18):
    assert (mask in faces)==all((mask&nb[v]).bit_count()<=1 for v in range(18) if (mask>>v)&1)
assert all(bool(nb[a] & (1<<b)) == bool(nb[b] & (1<<a)) for a in range(18) for b in range(18))
# Every selected induced component has <=2 vertices iff maximum degree <=1.
U=set(faces);up={};down={}
for v in range(18):
 bit=1<<v
 for a in sorted(U,key=lambda x:(x.bit_count(),x)):
  b=a|bit
  if a in U and b!=a and b in U:
   up[a]=b;down[b]=a;U.remove(a);U.remove(b)
assert len(up)==10321 and dict(Counter(x.bit_count()-1 for x in U))=={5:9,6:1}
assert up.get(0)==1
ind={x:0 for x in faces};adj={x:[] for x in faces};nc=0
for b in faces:
 x=b
 while x:
  bit=x&-x;a=b^bit;x-=bit
  src,dst=(a,b) if up.get(a)==b else (b,a)
  ind[dst]+=1;adj[src].append(dst);nc+=1
q=deque(x for x in ind if not ind[x]);n=0
while q:
 x=q.popleft();n+=1
 for y in adj[x]:
  ind[y]-=1
  if ind[y]==0:q.append(y)
assert n==len(faces) and nc==120240
from functools import lru_cache
crit5=sorted(x for x in U if x.bit_count()==6);crit6=sorted(x for x in U if x.bit_count()==7)
pos={a:i for i,a in enumerate(crit5)}
def bd(a):
 x=a
 while x:
  bit=x&-x;c=a^bit;x^=bit
  yield c, -1 if (c&(bit-1)).bit_count()%2 else 1
@lru_cache(None)
def project(a):
 if a in pos:return {pos[a]:1}
 if a in down:return {}
 b=up[a]
 s=next(t for c,t in bd(b) if c==a)
 out=Counter()
 for c,t in bd(b):
  if c!=a:
   for i,v in project(c).items():out[i]-=s*t*v
 return {i:v for i,v in out.items() if v}
for d in crit6:
 v=Counter()
 for c,t in bd(d):
  for i,value in project(c).items():v[i]+=t*value
 assert all(v.get(i,0)==0 for i in range(len(crit5)))
ranks={}
for d in range(1,10):
 current=sorted(m for m in faces if m.bit_count()==d+1)
 prev={m:i for i,m in enumerate(sorted(m for m in faces if m.bit_count()==d))}
 piv={}
 for b in current:
  val=0
  for a,_ in bd(b):val^=1<<prev[a]
  while val:
   bit=val.bit_length()-1
   if bit not in piv:piv[bit]=val;break
   val^=piv[bit]
 ranks[d]=len(piv)

assert ranks=={1:17,2:136,3:626,4:1768,5:3038,6:2980,7:1447,8:281,9:27}
betti={d:f[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in range(10)}
betti[0]=f[0]-1-ranks[1]
assert betti=={0:0,1:0,2:0,3:0,4:0,5:9,6:1,7:0,8:0,9:0}
assert sum((-1)**d*f[d] for d in range(-1,10))==-8
print('PAPPUS_TWO_INDEPENDENCE_MIXED_WEDGE_OK')
print('vertices=18 edges=27 augmented_faces=20652')
print('fvector=1,18,153,762,2394,4806,6027,4428,1728,308,27')
print('morse_pairs=10321 critical_five=9 critical_six=1')
print('hasse_incidences=120240 acyclic=yes')
print('integral_morse_boundary_C6_to_C5=zero_9_by_1')
print('unreduced_mod2_betti=0,0,0,0,0,9,1,0,0,0')
print('reduced_euler_characteristic=-8')
