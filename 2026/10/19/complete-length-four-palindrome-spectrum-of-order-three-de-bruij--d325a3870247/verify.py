from collections import Counter
from itertools import permutations

def construct(q,perms):
 V=[(a,b) for a in range(q) for b in range(q) if a!=b]
 edges={v:[] for v in V}
 for a,b in V:
  for c in range(q):
   if c!=b:edges[a,b].append(((b,c),[(a,b,c)]))
  sigma=perms[b]
  inv=sigma.index(b)
  assert sigma[b]!=b and inv!=b
  if a==inv:
   c=sigma[b]
   path=[(a,b,b),(b,b,b),(b,b,c)]
  else:
   c=sigma[a]
   path=[(a,b,b),(b,b,c)]
  assert c!=b
  edges[a,b].append(((b,c),path))
 vertex=V[0];tour=[];stack=[(vertex,None)]
 while stack:
  v,_=stack[-1]
  if edges[v]:
   u,p=edges[v].pop()
   stack.append((u,p))
  else:
   _,p=stack.pop()
   if p is not None:tour.append(p)
 tour.reverse()
 path=sum(tour,[])
 assert len(path)==q**3
 assert len(set(path))==q**3
 for i in range(len(path)):
  a,b,c=path[i];d,e,f=path[(i+1)%len(path)]
  assert (b,c)==(d,e)
 pals=sum((a==path[(i+1)%len(path)][2] and b==c) for i,(a,b,c) in enumerate(path))
 predicted=sum(sum(perms[b][a]==a for a in range(q)) for b in range(q))
 assert pals==predicted
 w=tuple(p[0] for p in path)
 assert len({tuple(w[(i+j)%len(w)] for j in range(3)) for i in range(len(w))})==q**3
 literal=sum(w[i]==w[(i+3)%len(w)] and w[(i+1)%len(w)]==w[(i+2)%len(w)] for i in range(len(w)))
 assert literal==pals
 return w,pals

def perm_for(q,b,f):
 keep=[a for a in range(q) if a!=b][:f]
 rest=[a for a in range(q) if a not in keep]
 p=list(range(q))
 for a,z in zip(rest,rest[1:]+rest[:1]):p[a]=z
 assert p[b]!=b and sum(p[a]==a for a in range(q))==f
 return p

for q in range(2,9):
 for K in range(q*(q-2)+1):
  val=K;plist=[]
  for b in range(q):
   f=min(q-2,val);val-=f;plist.append(perm_for(q,b,f))
  w,c=construct(q,plist)
  assert c==K
 print(q,'q^3',q**3,'achieved',list(range(q*(q-2)+1)))
# all diagonal assignments q=3, compare exhaustive local possibilities
q=3
P=list(permutations(range(q)))
A=[[p for p in P if p[b]!=b] for b in range(q)]
from itertools import product
counts=Counter()
for ps in product(*A):
 w,c=construct(q,ps);counts[c]+=1
print('q3 assignments by palindrome count',dict(sorted(counts.items())))
print('ALL_CONSTRUCTED_DEBRUIJN_PALINDROME_SPECTRA_PASSED')
