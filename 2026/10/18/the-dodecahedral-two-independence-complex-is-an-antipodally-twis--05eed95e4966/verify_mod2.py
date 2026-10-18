"""Independent direct full mod-two boundary rank calculation for the dodecahedral 2-independence complex."""
from collections import defaultdict
N=20
E=set()
for i in range(10):
 for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
  E.add(tuple(sorted((a,b))))
assert len(E)==30
adj=[0]*N
for a,b in E:adj[a]|=1<<b;adj[b]|=1<<a
faces=defaultdict(list)
for s in range(1<<N):
 for u in range(N):
  if s>>u&1 and (adj[u]&s).bit_count()>1:break
 else:faces[s.bit_count()-1].append(s)
counts={d:len(v) for d,v in sorted(faces.items())}
assert sum(counts.values())==63143
print('face_counts',counts,flush=True)
rank={-1:0}
for k in range(1,max(faces)+1):
 rows={s:i for i,s in enumerate(faces[k-1])}
 pivots={};r=0
 for t in faces[k]:
  column=0
  bits=t
  while bits:
   b=bits&-bits;bits-=b
   column^=1<<rows[t^b]
  while column:
   p=column.bit_length()-1
   if p in pivots:column^=pivots[p]
   else:
    pivots[p]=column;r+=1;break
 rank[k]=r
 print('rank_boundary',k,r,flush=True)
rank[0]=1
homology={k:counts[k]-rank.get(k,0)-rank.get(k+1,0) for k in range(max(faces)+1)}
print('reduced_mod2_betti',homology,flush=True)
assert homology[6]==1 and all(x==0 for k,x in homology.items() if k!=6)
