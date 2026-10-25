#!/usr/bin/env python3
"""Quotient four-state ordered binary transition tables by S_4 x S_2."""
from itertools import permutations
from collections import defaultdict,Counter
n=4
perms=list(permutations(range(n)))
functions=[]
for k in range(n**n):
 q=k;t=[]
 for _ in range(n):t.append(q%n);q//=n
 functions.append(tuple(t))
remaps=[]
for perm in perms:
 inv=[perm.index(x) for x in range(n)]
 out=[]
 for f in functions:
  v=0
  for i in reversed(range(n)):
   v=v*n + perm[f[inv[i]]]
  out.append(v)
 remaps.append(out)
print('symmetry transformed table sample',remaps[0][:5])
classes=defaultdict(list)
for a in range(256):
 for b in range(256):
  c=min(min(row[a]+256*row[b],row[b]+256*row[a]) for row in remaps)
  classes[c].append(a+256*b)
print('total orbits:',len(classes), 'orbit sizes:', dict(sorted(Counter(map(len,classes.values())).items())))
# Independent set construction on pair product, classify only canonical reps.
pairs=list(__import__('itertools').combinations(range(n),2)); pos={p:i for i,p in enumerate(pairs)};m=len(pairs)
def level(key):
 a=functions[key%256];b=functions[key//256]
 maps=[]
 for f in (a,b):
  maps.append(tuple(m if f[i]==f[j] else pos[tuple(sorted((f[i],f[j])))] for i,j in pairs)+(m,))
 # Bob-first with k=1,2,3 only. 4-state binary collapse verified independently over all labels in earlier run.
 for k in (3,2,1):
  reachable=[{p} for p in range(m+1)]
  for _ in range(k-1):
   reachable=[z|reachable[maps[0][p]]|reachable[maps[1][p]] for p,z in enumerate(reachable)]
  W={m}
  while True:
   W2=W|{p for p in range(m) if all(maps[0][q] in W or maps[1][q] in W for q in reachable[p])}
   if W2==W:break
   W=W2
  if len(W)==m+1:return k
 return 0
by_class=Counter();by_label=Counter();shown={}
for key,orbit in classes.items():
 cat=level(key)
 by_class[cat]+=1;by_label[cat]+=len(orbit)
 shown.setdefault(cat,(key,functions[key%256],functions[key//256],len(orbit)))
print('orbit counts for categories non-sync=0, A1-only=1, A2-only=2, Aomega=3:',dict(sorted(by_class.items())))
print('labeled counts:',dict(sorted(by_label.items())))
print('representatives:',shown)
assert by_label=={0:14016,1:26160,2:2976,3:22384}
print('ORBIT_CHECK_OK')
