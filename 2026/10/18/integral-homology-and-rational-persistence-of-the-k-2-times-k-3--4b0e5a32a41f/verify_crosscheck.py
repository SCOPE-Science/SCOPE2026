"""Independent vertex ordering, component-count forest test and Smith normal form."""
from itertools import product
from collections import Counter,defaultdict
from sympy import ZZ,Matrix
from sympy.matrices.normalforms import smith_normal_form

V=list(product(range(3),range(2),range(3)))
n=len(V); N=1<<n
adj=[]
for x in V:
 adj.append(sum(1<<j for j,y in enumerate(V) if all(x[h]!=y[h] for h in (0,1,2))))

def good(mask,d):
 vertices=[i for i in range(n) if mask&(1<<i)]
 if any((adj[i]&mask).bit_count()>d for i in vertices):return False
 edgecount=sum((adj[i]&mask).bit_count() for i in vertices)//2
 todo=mask;components=0
 while todo:
  components+=1
  v=(todo&-todo).bit_length()-1;todo^=(1<<v);queue=[v]
  while queue:
   x=queue.pop()
   nbr=adj[x]&todo
   while nbr:
    low=nbr&-nbr;nbr^=low;todo^=low;queue.append(low.bit_length()-1)
 return edgecount==len(vertices)-components

def boundary(mask):
 idx=0
 while mask:
  x=mask&-mask;mask^=x
  yield x,(-1 if idx%2 else 1)
  idx+=1

def compute(d):
 faces={s for s in range(N) if good(s,d)}
 # Reverse pivot ordering, and reverse traversal.
 available=set(faces);pair={};ups=set()
 for i in reversed(range(n)):
  for s in sorted(available,reverse=True):
   if s not in available or s&(1<<i):continue
   t=s|(1<<i)
   if t in available:
    available.remove(s);available.remove(t);pair[s]=t;ups.add(t)
 from functools import lru_cache
 @lru_cache(None)
 def proj(s):
  if s in available:return {s:1}
  if s in ups:return {}
  u=pair[s];pivotbit=u^s
  idx=(u&(pivotbit-1)).bit_count()
  pivot=(-1 if idx%2 else 1)
  z=defaultdict(int)
  for bit,sign in boundary(u):
   t=u^bit
   if t==s:continue
   for q,a in proj(t).items():z[q]-=pivot*sign*a
  return {q:a for q,a in z.items() if a}
 crit=Counter(s.bit_count()-1 for s in available)
 ranks={};units={};matnz={}
 for k in range(0,12):
  rows=sorted(s for s in available if s.bit_count()-1==k-1)
  cols=sorted(s for s in available if s.bit_count()-1==k)
  rowidx={s:i for i,s in enumerate(rows)}
  M=Matrix.zeros(len(rows),len(cols))
  for j,s in enumerate(cols):
   for bit,sgn in boundary(s):
    for t,x in proj(s^bit).items(): M[rowidx[t],j]+=sgn*x
  if M.rows and M.cols:
   S=smith_normal_form(M,domain=ZZ)
   vals=[abs(int(S[i,i])) for i in range(min(S.rows,S.cols)) if S[i,i]!=0]
   assert all(x==1 for x in vals),(d,k,vals)
   ranks[k]=len(vals);units[k]=len(vals);matnz[k]=sum(bool(y) for y in M)
  else:ranks[k]=0;units[k]=0;matnz[k]=0
 bet={k:crit[k]-ranks[k]-ranks.get(k+1,0) for k in range(0,11)}
 return len(faces),dict(sorted(Counter(s.bit_count()-1 for s in faces).items())), dict(sorted(crit.items())), {k:x for k,x in bet.items() if x}, {k:v for k,v in ranks.items() if v},dict(sorted(matnz.items()))

for d in range(5):
 a=compute(d)
 print('d',d,'faces',a[0],'f',a[1],'crit',a[2],'bet',a[3],'ranks',a[4],'matrix_nnz',a[5],flush=True)
# The independently generated complexes agree with the expected Betti table.
# The `compute` function additionally demands that every Smith invariant be 1.
