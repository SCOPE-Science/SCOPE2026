"""Finite check of proposed primitive necklace invariant for C2 of finite total functions."""
from itertools import product
from collections import defaultdict

def primitive_key(f):
 n=len(f); pred=[[] for _ in f]
 for i,j in enumerate(f):pred[j].append(i)
 seen=set(); accum=defaultdict(int)
 def subtree(v, cyclic):
  return '('+''.join(sorted(subtree(u,cyclic) for u in pred[v] if u not in cyclic))+')'
 for start in range(n):
  if start in seen:continue
  path=[]; idx={}; v=start
  while v not in seen and v not in idx:
   idx[v]=len(path);path.append(v);v=f[v]
  if v in idx:
   cyc=path[idx[v]:]; cycset=set(cyc)
  else:
   # This component was already processed; no new contribution.
   seen.update(path);continue
  # Mark all preimages belonging to the component to prevent duplicate processing.
  stack=list(cyc); seen.update(stack)
  while stack:
   w=stack.pop()
   for u in pred[w]:
    if u not in seen:seen.add(u);stack.append(u)
  word=tuple(subtree(v,cycset) for v in cyc)
  m=len(word)
  if m<=2:
   # A self-loop and reciprocal 2-cycle are visible atomically to C2.
   key=('short',m,min(word[i:]+word[:i] for i in range(m)))
   accum[key]+=1
  else:
   d=next(k for k in range(1,m+1) if m%k==0 and all(word[i]==word[i%k] for i in range(m)))
   p=word[:d];key=('long',min(p[i:]+p[:i] for i in range(d)))
   accum[key]+=m//d
 return tuple(sorted(accum.items()))

def refine_all(fs,n):
 preds=[];cols=[]
 for f in fs:
  pd=[[] for _ in f]
  for i,j in enumerate(f):pd[j].append(i)
  preds.append(pd)
  cols.append(tuple((int(f[i]==i),int(f[i]!=i and f[f[i]]==i)) for i in range(n)))
 for rnd in range(3*n+3):
  interns={};new=[]
  for f,pd,c in zip(fs,preds,cols):
   x=[]
   for i in range(n):
    key=(c[i],c[f[i]],tuple(sorted(c[v] for v in pd[i])))
    if key not in interns:interns[key]=len(interns)
    x.append(interns[key])
   new.append(tuple(x))
  cols=new
 return [tuple(sorted(c)) for c in cols]

for n in range(1,7):
 fs=list(product(range(n),repeat=n))
 wls=refine_all(fs,n)
 from_wl=defaultdict(set);from_p=defaultdict(set)
 for f,w in zip(fs,wls):
  p=primitive_key(f)
  from_wl[w].add(p);from_p[p].add(w)
 bad1=[(w,ps) for w,ps in from_wl.items() if len(ps)>1]
 bad2=[(p,ws) for p,ws in from_p.items() if len(ws)>1]
 print(f'n={n} maps={len(fs)} c2_classes={len(from_wl)} necklace_classes={len(from_p)} disagreement={len(bad1)+len(bad2)}',flush=True)
 assert not bad1 and not bad2,(n,bad1[:1],bad2[:1])

def isomorphism_key(f):
 """Multiset of entire cycle necklaces decorated by exact rooted feeding trees."""
 n=len(f); pred=[[] for _ in f]
 for i,j in enumerate(f):pred[j].append(i)
 seen=set();components=[]
 def tree(v,cyc):return '('+''.join(sorted(tree(u,cyc) for u in pred[v] if u not in cyc))+')'
 for start in range(n):
  if start in seen:continue
  v=start;idx={};path=[]
  while v not in idx:
   idx[v]=len(path);path.append(v);v=f[v]
  cyc=path[idx[v]:]; cycset=set(cyc)
  stack=list(cycset);seen.update(cycset)
  while stack:
   for u in pred[stack.pop()]:
    if u not in seen:seen.add(u);stack.append(u)
  word=tuple(tree(v,cycset) for v in cyc)
  components.append(min(word[i:]+word[:i] for i in range(len(word))))
 return tuple(sorted(components))

n=6;fibres=defaultdict(set)
for f in product(range(n),repeat=n):
 fibres[primitive_key(f)].add(isomorphism_key(f))
collision=[v for v in fibres.values() if len(v)>1]
print(f'n=6 isomorphism_types={sum(map(len,fibres.values()))} distinct_C2_classes={len(fibres)} nontrivial_C2_classes={len(collision)}')
assert len(collision)==1 and len(collision[0])==2
assert collision[0]=={(('()', '()', '()'),('()', '()', '()')),(('()',)*6,)}
