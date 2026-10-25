"""Exact finite verification of the five-cut complex of the Fano-incidence graph.
Requires Python 3 and networkx; prints a completion marker only after all checks."""
from itertools import combinations
from collections import defaultdict, Counter, deque
import networkx as nx

N=14
ALL=(1<<N)-1
lines=[{(j+d)%7 for d in (0,1,3)} for j in range(7)]
adj=[0]*N
for i in range(7):
 for j,line in enumerate(lines):
  if i in line:
   adj[i]|=1<<(7+j);adj[7+j]|=1<<i
assert sum(x.bit_count() for x in adj)==42

def connected(mask):
 seen=mask&-mask
 while True:
  new=seen
  for v in range(N):
   if seen>>v&1:new|=adj[v]&mask
  if new==seen:return seen==mask
  seen=new

facets=[]
for T in combinations(range(N),5):
 s=sum(1<<i for i in T)
 if not connected(s):facets.append(ALL^s)
assert len(facets)==1750
faces={0}
for facet in facets:
 sub=facet
 while sub:
  faces.add(sub)
  sub=(sub-1)&facet
assert len(faces)==14633
fv=Counter(m.bit_count()-1 for m in faces if m)
assert tuple(fv[d] for d in range(9))==(14,91,364,1001,2002,3003,3432,2975,1750)

# Simultaneous element matchings at successive vertices.
unmatched=set(faces)
partner={}
for v in range(N):
 bit=1<<v
 for a in list(unmatched):
  b=a|bit
  if not a&bit and b in unmatched:
   unmatched.remove(a);unmatched.remove(b)
   partner[a]=b;partner[b]=a
assert len(partner)==2*7071
assert Counter(m.bit_count()-1 for m in unmatched)==Counter({8:491})
assert partner[0] in faces

# Directed Hasse graph: matched edges point upwards; remaining edges downwards.
indeg={m:0 for m in faces}
cover_count=0
for hi in faces:
 t=hi
 while t:
  bit=t&-t;t-=bit;lo=hi-bit
  if partner.get(lo)==hi:indeg[hi]+=1
  else:indeg[lo]+=1
  cover_count+=1
q=deque(m for m,d in indeg.items() if d==0)
seen_count=0
while q:
 u=q.popleft();seen_count+=1
 # Outgoing unmatched downward edges only.
 t=u
 while t:
  bit=t&-t;t-=bit;lo=u-bit
  if partner.get(lo)!=u:
   indeg[lo]-=1
   if indeg[lo]==0:q.append(lo)
 # One possible upward matched edge.
 dst=partner.get(u)
 if dst is not None and (u&dst)==u:
  indeg[dst]-=1
  if indeg[dst]==0:q.append(dst)
assert seen_count==len(faces),(seen_count,len(faces))

# Independent mod-two boundary rank calculation.
face_by_dim={d:sorted(m for m in faces if m and m.bit_count()==d+1) for d in range(9)}
def f2_rank(cols):
 pivots={}
 for col in cols:
  while col:
   lead=col.bit_length()-1
   if lead in pivots:col^=pivots[lead]
   else:pivots[lead]=col;break
 return len(pivots)
ranks={}
for dim in range(1,9):
 loidx={m:i for i,m in enumerate(face_by_dim[dim-1])}
 cols=[]
 for m in face_by_dim[dim]:
  boundary=0;t=m
  while t:
   bit=t&-t;t-=bit
   boundary^=1<<loidx[m-bit]
  cols.append(boundary)
 ranks[dim]=f2_rank(cols)
assert tuple(ranks[k] for k in range(1,9))==(13,78,286,715,1287,1716,1716,1259)
assert {k:len(face_by_dim[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(9)}=={0:1,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:491}

# Full automorphism group, signed traces and character on cycle types.
G=nx.Graph();G.add_nodes_from(range(N))
G.add_edges_from((i,j) for i in range(N) for j in range(i+1,N) if adj[i]&(1<<j))
from networkx.algorithms.isomorphism import GraphMatcher
perms=[tuple(d[i] for i in range(N)) for d in GraphMatcher(G,G).isomorphisms_iter()]
assert len(perms)==336

def cycle_type(p):
 unseen=set(range(N));sizes=[]
 while unseen:
  first=min(unseen);x=first;d=0
  while x in unseen:
   unseen.remove(x);x=p[x];d+=1
  sizes.append(d)
 return tuple(sorted(sizes))

def signed_fixed(m,p):
 image=[]
 for i in range(N):
  if m&(1<<i):image.append(p[i])
 if sum(1<<i for i in image)!=m:return 0
 inv=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
 return -1 if inv%2 else 1

types=defaultdict(list)
for p in perms:
 trace=-1
 for m in faces:
  if m:trace+=(-1 if m.bit_count()%2==0 else 1)*signed_fixed(m,p)
 types[cycle_type(p)].append(trace)
expected={
 (1,)*14:(1,491),
 (1,)*6+(2,)*4:(21,-29),
 (1,)*2+(2,)*2+(4,)*2:(42,-1),
 (1,)*2+(3,)*4:(56,5),
 (2,)*7:(28,-11),
 (2,4,8):(84,1),
 (2,6,6):(56,1),
 (7,7):(48,1),
}
assert {t:(len(v),v[0]) for t,v in types.items()}==expected
assert all(len(set(v))==1 for v in types.values())
assert sum(len(v)*v[0] for v in types.values())==0
print('HEAWOOD_FIVE_CUT_COMPLETE_EXACT_CHECKS_PASSED',len(faces)-1,cover_count,len(partner)//2,seen_count,len(perms))
