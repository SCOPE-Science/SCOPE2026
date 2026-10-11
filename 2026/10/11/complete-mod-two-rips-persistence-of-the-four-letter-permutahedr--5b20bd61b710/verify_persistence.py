"""Independent direct GF(2) persistent-boundary reduction for the 4-permutation metric up to scale 4."""
from itertools import permutations
from collections import Counter
v=list(permutations(range(4)))
N=len(v)
D=[[0]*N for _ in range(N)]
for i,p in enumerate(v):
 for j,q in enumerate(v):
  x=[q.index(a) for a in p]
  D[i][j]=sum(x[u]>x[w] for u in range(4) for w in range(u+1,4))

def collect():
 c=Counter()
 nbr=[sum(1<<j for j in range(i+1,N) if D[i][j]<=4) for i in range(N)]
 faces=[]
 def dfs(tail,allowed,birth):
  faces.append((birth, len(tail)-1,tail))
  while allowed:
   bit=allowed&-allowed;allowed^=bit;z=bit.bit_length()-1
   newbirth=max(birth,*(D[z][w] for w in tail))
   dfs(tail+(z,),allowed&nbr[z],newbirth)
 for i in range(N):dfs((i,),nbr[i],0)
 return sorted(faces)
F=collect()
print('simplices',len(F),flush=True)
index={s[2]:i for i,s in enumerate(F)}
pivots={};pairs=[];born=set()
for j,(birth,dim,tup) in enumerate(F):
 b=0
 for k in range(len(tup)):
  sub=tup[:k]+tup[k+1:]
  if sub:b^=1<<index[sub]
 while b:
  p=b.bit_length()-1
  if p not in pivots:
   pivots[p]=b
   pairs.append((p,j))
   break
  b ^= pivots[p]
 if not b:born.add(j)
print('paired',len(pairs),'birth',len(born),flush=True)
positive=Counter()
death_pivot=set()
for p,j in pairs:
 death_pivot.add(p)
 a,birth=F[p][0],F[j][0]
 if a<birth: positive[(F[p][1],a,birth)]+=1
for i in born-death_pivot:positive[(F[i][1],F[i][0],None)]+=1
print('positive bars in truncated filtration up to r4',dict(positive))
expect={(0,0,1):23,(0,0,None):1,(1,1,2):13,(2,2,3):8,(2,2,4):1,(4,4,None):5,(5,4,None):2}
assert positive==expect, (positive, expect)
print('PERSISTENCE_OK')
