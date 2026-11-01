import networkx as nx,collections,functools
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from sympy import Matrix
G=nx.chvatal_graph();E=tuple(sorted(tuple(sorted(e)) for e in G.edges))
masks=[(1<<u)|(1<<v) for u,v in E]
F=[]
def rec(pos,vertices,chosen):
 if chosen:F.append(chosen)
 for j in range(pos,len(E)):
  if masks[j]&vertices==0:rec(j+1,vertices|masks[j],chosen|(1<<j))
rec(0,0,0)
F=set(F)
order=(1,2,22,11,5,9,8,6,23,18,10,21,16,13,20,17,19,4,3,14,12,0,7,15)
alive=F.copy();lo_to_hi={};hi_to_lo={}
for v in order:
 bit=1<<v
 for m in sorted(alive):
  if m&bit:continue
  if (m|bit) in alive:
   lo_to_hi[m]=m|bit;hi_to_lo[m|bit]=m
   alive.remove(m);alive.remove(m|bit)
crit=collections.defaultdict(list)
for m in sorted(alive):crit[m.bit_count()-1].append(m)
print('crit', {i:len(x) for i,x in crit.items()},'pairs',len(lo_to_hi))
# exhaustive acyclicity of oriented Hasse diagram: matched edge up, others down.
indeg={m:0 for m in F};adj=collections.defaultdict(list); incidences=0
for upper in F:
 if upper.bit_count()<=1:continue
 for j in range(24):
  b=1<<j
  if not upper&b:continue
  lower=upper^b
  if lower not in F:continue
  incidences+=1
  a,c=(lower,upper) if lo_to_hi.get(lower)==upper else (upper,lower)
  adj[a].append(c);indeg[c]+=1
queue=collections.deque(x for x in F if indeg[x]==0);seen=0
while queue:
 x=queue.popleft();seen+=1
 for y in adj[x]:
  indeg[y]-=1
  if indeg[y]==0:queue.append(y)
print('acyclic',seen,len(F),'incidences',incidences); assert seen==len(F)
# gradient-path critical boundary coefficients
@functools.lru_cache(None)
def expand(low):
 if low in hi_to_lo:return {}
 if low not in lo_to_hi:return {low:1}
 hi=lo_to_hi[low]
 lowitems=[j for j in range(24) if low&(1<<j)];hitems=[j for j in range(24) if hi&(1<<j)]
 pivot=hitems.index(next(j for j in hitems if not (low>>j)&1))
 sgnpivot=(-1)**pivot
 out=collections.defaultdict(int)
 for pos,j in enumerate(hitems):
  child=hi^(1<<j)
  if child==low:continue
  coeff=-((-1)**pos)*sgnpivot
  for m,v in expand(child).items():out[m]+=coeff*v
 return {m:v for m,v in out.items() if v}
C3=crit[3];C4=crit[4]; idx={m:i for i,m in enumerate(C3)}
M=[[0 for hi in C4] for lo in C3]
for j,hi in enumerate(C4):
 items=[e for e in range(24) if (hi>>e)&1]
 for i,e in enumerate(items):
  for lower,c in expand(hi^(1<<e)).items():
   assert lower in idx,(hi,lower)
   M[idx[lower]][j]+=(-1)**i*c
A=Matrix(M);SNF=smith_normal_form(A,domain=ZZ)
D=collections.Counter(abs(int(SNF[i,i])) for i in range(min(SNF.shape)))
print('morse integral boundary',A.shape,'Smith',D,'Euler',sum((-1)**j*len(crit[j]) for j in crit))
print('all nonzeros',[(i,j,int(A[i,j])) for i in range(A.rows) for j in range(A.cols) if A[i,j]])
# Independent simplicial homology over distinct characteristic fields.
def rank_columns_mod(columns,p):
 pivot={}
 for col in columns:
  x={i:c%p for i,c in col if c%p}
  while x:
   t=min(x)
   if t not in pivot:
    v=pow(x[t],-1,p);pivot[t]={k:(a*v)%p for k,a in x.items() if (a*v)%p};break
   c=x[t];old=pivot[t]
   for k,v in old.items():
    z=(x.get(k,0)-c*v)%p
    if z:x[k]=z
    elif k in x:del x[k]
 return len(pivot)
bydim=collections.defaultdict(list)
for mask in sorted(F,key=lambda m:(m.bit_count(),m)):
 bydim[mask.bit_count()-1].append(mask)
for p in (2,3,5):
 ranks={}
 for dim in range(1,6):
  loindex={m:i for i,m in enumerate(bydim[dim-1])}
  col=[]
  for m in bydim[dim]:
   edges=[e for e in range(24) if m>>e&1]
   col.append([(loindex[m^(1<<e)], (-1)**i) for i,e in enumerate(edges)])
  ranks[dim]=rank_columns_mod(col,p)
 betti={dim:len(bydim[dim])-ranks.get(dim,0)-ranks.get(dim+1,0) for dim in range(6)}
 betti[0]-=1
 print('independent simplicial field',p,'ranks',ranks,'reduced betti',betti)
 assert (betti[3],betti[4])==((29,1) if p==3 else (28,0))
 assert all(v==0 for d,v in betti.items() if d not in (3,4))
print('CHVATAL_MATCHING_THREE_TORSION_VERIFIED')
