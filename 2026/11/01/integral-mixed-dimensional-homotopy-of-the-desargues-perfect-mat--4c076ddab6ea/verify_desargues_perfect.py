"""Self-contained exact certificate for the perfect-matching complex of GP(10,3).
Uses only the Python standard library; no precomputed scientific output is assumed.
"""
import collections,functools,hashlib,itertools,json,sys,math
N=10;K=3
edges=sorted({tuple(sorted((a,b))) for i in range(N) for a,b in [(i,(i+1)%N),(i,N+i),(N+i,N+(i+K)%N)]})
assert len(edges)==30 and len(set(sum(([a,b] for a,b in edges),[])))==20
inc=[[] for i in range(20)]
for j,(u,v) in enumerate(edges):inc[u].append((j,v));inc[v].append((j,u))
def pm_enum(R,acc,out):
 if not R:out.append(acc);return
 u=min(R,key=lambda x:sum(v in R for _,v in inc[x]))
 for j,v in inc[u]:
  if v in R:pm_enum(R-{u,v},acc | (1<<j),out)
perfect=[];pm_enum(set(range(20)),0,perfect)
assert len(perfect)==60 and len(set(perfect))==60
# Independent bipartite count via the exact 10x10 permanent, rather than edge-set recursion.
neighbor=[set() for _ in range(20)]
for u,v in edges: neighbor[u].add(v);neighbor[v].add(u)
color=[-1]*20
for start in range(20):
 if color[start]<0:
  color[start]=0;Q=collections.deque([start])
  while Q:
   u=Q.popleft()
   for v in neighbor[u]:
    if color[v]<0:color[v]=1-color[u];Q.append(v)
    else:assert color[v]!=color[u]
left=[u for u in range(20) if color[u]==0];right=[u for u in range(20) if color[u]==1]
assert len(left)==len(right)==10
adjm=[sum(1<<j for j,v in enumerate(right) if v in neighbor[u]) for u in left]
permanent=[0]*1024;permanent[0]=1
for mask in range(1,1024):
 i=mask.bit_count()-1
 b=adjm[i]&mask
 while b:
  x=b & -b; b-=x
  permanent[mask]+=permanent[mask^x]
assert permanent[-1]==60
print('independent_bipartite_permanent',permanent[-1],flush=True)
faces={0}
for m in perfect:
 subsets=[0]
 for b in range(30):
  if m>>b&1:subsets += [v|(1<<b) for v in subsets[:]]
 faces.update(subsets)
assert len(faces)==44282
# Independently enumerate *all* ordinary matching faces, accepting exactly
# those with a perfect completion of the uncovered graph by vertex-mask DP.
FULL=(1<<20)-1
@functools.lru_cache(None)
def has_completion(R):
 if not R:return True
 v=(R & -R).bit_length()-1
 return any((R>>w&1) and has_completion(R ^ (1<<v) ^ (1<<w)) for w in neighbor[v])
valid=set();allmatch=[0]
def enumerate_graph_matchings(j,used,chosen):
 if j==len(edges):
  allmatch[0]+=1
  if has_completion(FULL^used):valid.add(chosen)
  return
 enumerate_graph_matchings(j+1,used,chosen)
 u,v=edges[j]
 if not used&(1<<u|1<<v):
  enumerate_graph_matchings(j+1,used|1<<u|1<<v,chosen|1<<j)
enumerate_graph_matchings(0,0,0)
assert valid==faces
assert allmatch[0]==113192
print('ordinary_matchings_including_empty',allmatch[0], 'extendible',len(valid),flush=True)
# Order from an independently obtained bounded-search discrete-Morse experiment.
order=[23,27,18,1,10,9,12,21,6,14,0,11,5,2,15,29,16,26,28,7,13,17,3,8,24,19,4,20,25,22]
assert sorted(order)==list(range(30))
remaining=set(faces);paired={}
for b in order:
 bit=1<<b
 low=[f for f in remaining if not f&bit and f|bit in remaining]
 for a in low:
  u=a|bit
  remaining.remove(a);remaining.remove(u)
  paired[a]=u;paired[u]=a
# Unmatch empty and its paired vertex to get non-reduced CW complex.
base=paired.pop(0);paired.pop(base)
remaining.update((0,base))
# Verify all pairs are codimension one and disjoint.
for a,b in paired.items():assert paired[b]==a and (a^b).bit_count()==1
assert len(paired)+len(remaining)==len(faces)
cc=collections.Counter(f.bit_count()-1 for f in remaining)
print('perfect',len(perfect),'faces',len(faces),'critical',dict(sorted(cc.items())),'basevertex',base,flush=True)
assert cc=={-1:1,0:1,3:31,4:1}
# For the ordinary complex ignore empty; matched/critical partition of nonempty faces unchanged.
def facet_signs(h):
 bits=[j for j in range(30) if h>>j &1]
 for k,j in enumerate(bits):yield h^(1<<j),(-1)**k
indeg={f:0 for f in faces if f}
incidences=0
for h in faces:
 if not h:continue
 for l,sg in facet_signs(h):
  if not l:continue
  incidences+=1
  if paired.get(l)==h:indeg[h]+=1
  else:indeg[l]+=1
from collections import deque
q=deque(f for f,d in indeg.items() if d==0)
processed=0
while q:
 h=q.popleft();processed+=1
 for l,sg in facet_signs(h):
  if not l or paired.get(l)==h:continue
  indeg[l]-=1
  if indeg[l]==0:q.append(l)
 if h in paired and paired[h].bit_count()==h.bit_count()+1:
  u=paired[h]
  indeg[u]-=1
  if indeg[u]==0:q.append(u)
assert processed==len(faces)-1,(processed,len(faces)-1)
print('acyclic',processed,'nonempty cells,',incidences,'incidences',flush=True)
# Chain projection to Morse cells via integral facet expansion.
import sys;sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def proj(f):
 if f not in paired:return {f:1}
 u=paired[f]
 if u.bit_count()<f.bit_count():return {} # upper paired cell
 eps=next(sgn for l,sgn in facet_signs(u) if l==f)
 acc=collections.Counter()
 for l,sign in facet_signs(u):
  if l==f:continue
  t=proj(l)
  factor=-sign*eps
  for z,v in t.items():acc[z]+=factor*v
 return {z:v for z,v in acc.items() if v}
crit3=sorted(f for f in remaining if f.bit_count()==4)
crit4=sorted(f for f in remaining if f.bit_count()==5)
assert len(crit4)==1
print('critical_4_mask',crit4[0],'critical_3_masks',crit3,flush=True)
column=collections.Counter()
for f,s in facet_signs(crit4[0]):
 for z,v in proj(f).items():column[z]+=s*v
B=[column[x] for x in crit3]
print('morse_boundary_4to3',B,flush=True)
assert len(B)==31
# no unit condition, potentially zero
# no gcd condition
assert all(v==0 for v in B)
print('morse_boundary_zero',True,'homotopy_type','wedge_of_31_S3_and_1_S4',flush=True)
# Independent direct mod-2 boundary rank via bit-column elimination.
bydim=collections.defaultdict(list)
for m in faces:
 if m:bydim[m.bit_count()-1].append(m)
def rank2(d):
 cols=bydim.get(d,[]);rows={m:i for i,m in enumerate(bydim.get(d-1,[]))}
 pivots={}
 for c in cols:
  v=0
  for f,_ in facet_signs(c):
   if f in rows:v ^=1<<rows[f]
  while v:
   p=v.bit_length()-1
   if p not in pivots:pivots[p]=v;break
   v^=pivots[p]
 return len(pivots)
ranks={d:rank2(d) for d in range(1,10)}
mod2={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(1,10)}
print('f_vector',dict(sorted((d,len(v)) for d,v in bydim.items())),flush=True)
print('mod2_reduced_high',dict((d,x) for d,x in mod2.items() if x),flush=True)
assert mod2.get(3)==31 and mod2.get(4)==1 and all(x==0 for d,x in mod2.items() if d not in (3,4))
print('DESARGUES_PMC_INTEGRAL_WEDGE_31_S3_1_S4_VERIFIED',flush=True)
