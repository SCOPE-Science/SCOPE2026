"""Reconstruct discrete-Morse certificate for the Petersen directed-forest complex."""
from collections import Counter,deque
from time import monotonic
from itertools import combinations
import hashlib,json,sys

# Petersen graph: outer pentagon, inner pentagram, five spokes
V=tuple(range(10))
E=sorted({tuple(sorted((i,(i+1)%5))) for i in range(5)}|{tuple(sorted((i,i+5))) for i in range(5)}|{tuple(sorted((i+5,((i+2)%5)+5))) for i in range(5)})
assert len(E)==15
arcs=tuple((u,v,e) for e,(x,y) in enumerate(E) for u,v in ((x,y),(y,x)))
ORDER=(5,0,6,17,12,9,19,2,22,1,4,26,27,14,11,10,8,28,3,25,15,16,24,7,13,18,21,20,29,23)
assert sorted(ORDER)==list(range(30))

# Construct each acyclic outdegree <=1 edge orientation exactly once.
faces={0};out=[-1]*10;cnt=Counter();
def enum(start,mask,used):
 cnt[mask.bit_count()]+=1
 for a in range(start,30):
  u,v,e=arcs[a]
  if out[u]>=0 or (used>>e)&1: continue
  w=v
  while out[w]!=-1 and w!=u:w=out[w]
  if w==u:continue
  out[u]=v;newmask=mask|(1<<a);faces.add(newmask);enum(a+1,newmask,used|(1<<e));out[u]=-1
enum(0,0,0)
assert len(faces)==314928
assert tuple(cnt.get(i,0) for i in range(10))==(1,30,390,2880,13305,39882,77640,94800,66000,20000)
print('FACES_OK',len(faces),flush=True)

# Iterated elementary toggle matchings. Empty face is allowed for reduced check.
remaining=faces.copy();pairs={};upper=set()
for a in ORDER:
 bit=1<<a
 for m in list(remaining):
  if m&bit:continue
  n=m|bit
  if n in remaining:
   remaining.remove(m);remaining.remove(n);pairs[m]=n;upper.add(n)
assert Counter(m.bit_count()-1 for m in remaining)=={7:77,8:333}
assert len(pairs)==(len(faces)-410)//2
assert 0 in pairs
print('MATCHING_OK',len(pairs),'reduced critical',dict(Counter(m.bit_count()-1 for m in remaining)),flush=True)

# Full Hasse graph acyclicity, with lower->upper edges for matched pairs,
# and upper->lower edges for all other cover incidences.
# Note that the empty-face cover relations are included: stricter check.
indeg={m:0 for m in faces}; ninc=0
for m in faces:
 x=m
 while x:
  bit=x&-x;l=m^bit;x-=bit;ninc+=1
  if pairs.get(l)==m: indeg[m]+=1
  else:indeg[l]+=1
Q=deque(m for m in faces if indeg[m]==0)
visited=0
while Q:
 m=Q.popleft();visited+=1
 if m in pairs:
  u=pairs[m];indeg[u]-=1
  if indeg[u]==0:Q.append(u)
 x=m
 while x:
  bit=x&-x;l=m^bit;x-=bit
  if pairs.get(l)!=m:
   indeg[l]-=1
   if indeg[l]==0:Q.append(l)
assert visited==len(faces),('cyclic',visited,len(faces))
print('ACYCLIC_OK',visited,'cover_incidences',ninc,flush=True)

# Dimension 7 chains (8-arc subsets) paired to upper 8-cells or critical.
level7={m for m in faces if m.bit_count()==8}
crit7=sorted(m for m in remaining if m.bit_count()==8)
crit8=sorted(m for m in remaining if m.bit_count()==9)
crit_index={m:i for i,m in enumerate(crit7)}
deps={};inde7={m:0 for m in level7}
for low,up in pairs.items():
 if low.bit_count()!=8:continue
 src=low;entries=[]
 b=up
 while b:
  bit=b&-b;t=up^bit;b-=bit
  if t==src:continue
  entries.append(t);inde7[t]+=1
 deps[src]=entries
assert len(deps)+len(crit7)+sum(m in upper for m in level7)==len(level7)
q=deque(m for m,d in inde7.items() if d==0);topo=[]
while q:
 m=q.popleft();topo.append(m)
 for y in deps.get(m,[]):
  inde7[y]-=1
  if inde7[y]==0:q.append(y)
assert len(topo)==len(level7)

# Simplicial incidence coefficient for upper x, lower obtained by deleting b.
def inc(x,bit):return -1 if ((x&(bit-1)).bit_count()&1) else 1

# Exact critical-chain projection by recurrence along reversed Morse gradient paths.
proj={}
for m in reversed(topo):
 if m in crit_index:
  proj[m]={crit_index[m]:1}
 elif m not in deps:
  proj[m]={}   # upper half of (6,7) matched pair
 else:
  up=pairs[m];u_bit=up^m;s=-inc(up,u_bit)
  z={}
  for t in deps[m]:
   bit=up^t;coeff=s*inc(up,bit)
   for i,v in proj[t].items():
    z[i]=z.get(i,0)+coeff*v
  proj[m]={i:v for i,v in z.items() if v}

# Critical 8-cell attaching degrees onto critical 7-skeleton; every entry exact integer.
M=[[0]*len(crit8) for _ in crit7]
for j,up in enumerate(crit8):
 b=up
 while b:
  bit=b&-b;t=up^bit;b-=bit;sgn=inc(up,bit)
  for i,v in proj[t].items():M[i][j]+=sgn*v
nonzero=sum(x!=0 for row in M for x in row)
maxcoeff=max(abs(x) for row in M for x in row)
print('MORSE_BOUNDARY_OK shape',(len(crit7),len(crit8)),'nonzero',nonzero,'max_abs_coeff',maxcoeff,flush=True)

# Integer unit-pivot elimination: transformations by elementary integral row/column operations.
R=len(M);C=len(M[0]);ranks=0;pivots=[]
for k in range(min(R,C)):
 found=None
 for i in range(k,R):
  for j in range(k,C):
   if abs(M[i][j])==1: found=(i,j);break
  if found:break
 if found is None:break
 i,j=found
 M[k],M[i]=M[i],M[k]
 if j!=k:
  for row in M:row[k],row[j]=row[j],row[k]
 p=M[k][k];assert abs(p)==1
 # clear column via row operations
 for i in range(R):
  if i==k:continue
  mul=M[i][k]*p
  if mul:
   for j in range(C):M[i][j]-=mul*M[k][j]
 # clear row via column operations
 for j in range(C):
  if j==k:continue
  mul=M[k][j]*p
  if mul:
   for i in range(R):M[i][j]-=mul*M[i][k]
 assert all(M[k][j]==0 for j in range(C) if j!=k)
 assert all(M[i][k]==0 for i in range(R) if i!=k)
 pivots.append(p);ranks+=1
residual=[(i,j,M[i][j]) for i in range(ranks,R) for j in range(ranks,C) if M[i][j]]
print('UNIT_PIVOTS',ranks,'residual_nnz',len(residual),'residual_head',residual[:5],flush=True)
if not residual and ranks==39:
 print('PETERSEN_HOMOTOPY_PASS',f'S7_x_{R-ranks}',f'S8_x_{C-ranks}',flush=True)
else:print('NOT_VERIFIED',flush=True);sys.exit(2)
