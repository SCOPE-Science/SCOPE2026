from itertools import permutations
from collections import Counter

def inv(p):
 a=[0]*len(p)
 for i,j in enumerate(p):a[j]=i
 return tuple(a)
for n in range(1,6):
 perms=list(permutations(range(n))); seen=set(); reps=[]
 for p in perms:
  for q in perms:
   if (p,q) in seen:continue
   reps.append((p,q))
   for s in perms:
    t=inv(s)
    seen.add((tuple(s[p[t[i]]] for i in range(n)),tuple(s[q[t[i]]] for i in range(n))))
 atoms=[]
 for p,q in reps:
  atoms.append([[(int(x==y),int(p[x]==y),int(p[y]==x),int(q[x]==y),int(q[y]==x),int(p[x]==x),int(q[x]==x),int(p[y]==y),int(q[y]==y)) for y in range(n)] for x in range(n)])
 d={a:i for i,a in enumerate(sorted({v for g in atoms for row in g for v in row}))}
 cols=[[[d[v] for v in row] for row in g] for g in atoms]
 for it in range(n+3):
  sig=[]
  for a in cols:
   sig.append([[(a[x][y],tuple(sorted(Counter((a[x][z],a[z][y]) for z in range(n)).items()))) for y in range(n)]for x in range(n)])
  d={a:i for i,a in enumerate(sorted({v for g in sig for row in g for v in row}))}
  nxt=[[[d[v] for v in row] for row in g] for g in sig]
  if nxt==cols:break
  cols=nxt
 keys=[tuple(sorted(Counter(v for row in g for v in row).items())) for g in cols]
 assert len(keys)==len(set(keys)),(n,len(reps),len(set(keys)))
 print(n,'pairs',len(perms)**2,'isotypes',len(reps),'c3_classes',len(set(keys)),'iterations',it,'PASS',flush=True)
