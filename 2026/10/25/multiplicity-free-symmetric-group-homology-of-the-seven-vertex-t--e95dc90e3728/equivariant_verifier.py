import itertools,collections,functools,heapq,time,json
import sympy as sp
from sympy.polys.domains import QQ
T=time.time();n=7
E=list(itertools.combinations(range(n),2));em={e:i for i,e in enumerate(E)};tri=[sum(1<<em[e] for e in itertools.combinations(t,2)) for t in itertools.combinations(range(n),3)]
faces={u for u in range(1<<len(E)) if all(u&t!=t for t in tri)}
R=faces.copy();mat={}
for j in range(len(E)):
 bit=1<<j
 for s in tuple(R):
  if s&bit==0 and s|bit in R:R.remove(s);R.remove(s|bit);mat[s]=s|bit
upper=set(mat.values());crit=R

def bd(s):
  ans=[];p=0
  while s:
   b=s&-s;s^=b
   ans.append((b,1 if p%2==0 else -1));p+=1
  return ans

def boundary(s):
 return [(s^b,v) for b,v in bd(s)]
@functools.lru_cache(None)
def P(s):
 if s in crit:return {s:1}
 if s in upper:return {}
 u=mat[s]; epsilon=next(v for t,v in boundary(u) if t==s)
 res={}
 for t,coef in boundary(u):
  if t==s:continue
  for q,v in P(t).items():
   z=res.get(q,0)-epsilon*coef*v
   if z:res[q]=z
   elif q in res:del res[q]
 return res
# Topological order of directed Hasse arrows, with reversed pairs
idx={s:i for i,s in enumerate(sorted(faces))};m=len(idx)
adj=[[] for _ in range(m)];indeg=[0]*m
for s in faces:
 for t,_ in boundary(s):
  if mat.get(t)==s:src,dst=t,s
  else:src,dst=s,t
  x,y=idx[src],idx[dst]; adj[x].append(y);indeg[y]+=1
Q=collections.deque(i for i,v in enumerate(indeg) if not v);order={}
while Q:
 i=Q.popleft();order[i]=len(order)
 for j in adj[i]:
  indeg[j]-=1
  if not indeg[j]:Q.append(j)
assert len(order)==m
pos={s:order[i] for s,i in idx.items()}

def lift(c):
 chain={c:1}; b={}
 for t,v in boundary(c):b[t]=b.get(t,0)+v
 todo=[(pos[t],t) for t in b if t in mat];heapq.heapify(todo)
 while todo:
  _,t=heapq.heappop(todo)
  a=b.get(t,0)
  if not a:continue
  if t not in mat:continue
  u=mat[t]
  epsilon=next(v for ss,v in boundary(u) if ss==t)
  change=-a*epsilon
  v=chain.get(u,0)+change
  if v:chain[u]=v
  elif u in chain:del chain[u]
  for ss,coeff in boundary(u):
   new=b.get(ss,0)+change*coeff
   if new:b[ss]=new
   elif ss in b:del b[ss]
   if ss in mat and new:heapq.heappush(todo,(pos[ss],ss))
 assert not any(b.get(t) for t in mat if t.bit_count()==c.bit_count()-1)
 return chain,b

bydim={d:sorted(s for s in R if s.bit_count()-1==d) for d in range(5,10)}
L={};bds={}
for d,cs in bydim.items():
 for c in cs:L[c],bds[c]=lift(c)
 print('LIFTS',d,len(cs),'maxterms',max([len(L[c]) for c in cs],default=0),'maxbd',max([len(bds[c]) for c in cs],default=0),flush=True)

def D(d):
 rows=bydim.get(d-1,[]);cols=bydim.get(d,[])
 out=[]
 for c in cols:
  coeff=collections.Counter()
  for t,v in boundary(c):
   for q,a in P(t).items():coeff[q]+=v*a
  out.append([coeff.get(r,0) for r in rows])
 return sp.Matrix(out).T if rows and cols else sp.zeros(len(rows),len(cols))
Ds={d:D(d) for d in range(6,10)}
# test inclusion chain map by comparing boundary of each lift with linear combination lifts of differential
for d in range(6,10):
 for j,c in enumerate(bydim[d]):
  rhs=collections.Counter()
  for i,t in enumerate(bydim[d-1]):
   a=int(Ds[d][i,j])
   if a:
    for ss,v in L[t].items():rhs[ss]+=a*v
  lhs=collections.Counter(bds[c])
  assert {k:v for k,v in lhs.items() if v}=={k:v for k,v in rhs.items() if v},('lift not chain map',d,j)
print('lift-time',time.time()-T,flush=True)

def partitions(n,maximum=None):
 if n==0:yield ()
 else:
  for first in range(min(n,maximum or n),0,-1):
   for rest in partitions(n-first,first):yield (first,)+rest

def cycleperm(lens):
 p=list(range(n));k=0
 for ln in lens:
  for j in range(ln):p[k+j]=k+(j+1)%ln
  k+=ln
 return p

def act(s,pi):
 old=[bit.bit_length()-1 for bit,sign in bd(s)]
 newer=[em[tuple(sorted((pi[E[j][0]],pi[E[j][1]])))] for j in old]
 inversions=sum(a>b for i,a in enumerate(newer) for b in newer[i+1:])
 return sum(1<<j for j in newer),(-1 if inversions%2 else 1)

def action(d,pi):
 rows=bydim[d];cols=rows
 out=sp.zeros(len(rows),len(cols));ix={r:i for i,r in enumerate(rows)}
 for j,c in enumerate(cols):
  cf=collections.Counter()
  for s,v in L[c].items():
   ss,sgn=act(s,pi)
   for q,a in P(ss).items():cf[q]+=v*sgn*a
  for q,a in cf.items():
   if a:out[ix[q],j]=a
 return out

def basis(d):
 b=Ds.get(d+1,sp.zeros(len(bydim[d]),0))
 pivots=list(b.rref()[1])
 return b[:,pivots]
Bs={d:basis(d) for d in range(5,9)}
selected={}
for d,b in Bs.items():
 rows=list(b.T.rref()[1]);selected[d]=(rows,b[rows,:].inv()) if rows else ([],None)
print('BASIS_RANKS',{d:b.cols for d,b in Bs.items()},flush=True)

def bt(d,g):
 b=Bs.get(d)
 if b is None or b.cols==0:return 0
 rows,inv=selected[d]
 return sp.trace(inv*(g*b)[rows,:])

results=[]
for lam in partitions(n):
 pi=cycleperm(lam)
 acts={d:action(d,pi) for d in range(5,9)}
 for d in (6,7,8):assert acts[d-1]*Ds[d]==Ds[d]*acts[d],('not equivariant',lam,d)
 traces={d:int(sp.trace(acts[d])-bt(d,acts[d])-bt(d-1,acts[d-1]) if d>5 else sp.trace(acts[d])-bt(d,acts[d])) for d in range(5,9)}
 assert traces[5]==((-1)**(n-len(lam)))*sum(x==1 for x in lam),('low-degree sign point character',lam)
 results.append((lam,traces))

 expected=sum((-1)**d * v for d,v in traces.items())
 fixed_euler=-1
 for face in faces:
  if not face:continue
  img,sgn=act(face,pi)
  if img==face:fixed_euler+=((-1)**(face.bit_count()-1))*sgn
 assert fixed_euler==expected,('Lefschetz',lam,fixed_euler,expected)
 print('CHARACTER',lam,traces,'LEFSCHETZ',fixed_euler,flush=True)
print('ACTION_TIME',time.time()-T,flush=True)
