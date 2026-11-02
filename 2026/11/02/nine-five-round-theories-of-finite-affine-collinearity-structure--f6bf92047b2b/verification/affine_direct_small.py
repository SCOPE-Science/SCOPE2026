"""Direct vertex-tuple rank-five recursion (no affine-orbit normalization)."""
from itertools import product, combinations
from affine_rank5_probe import FF, run

def direct(q,d):
 F=FF(q);pts=list(product(range(q),repeat=d)); n=len(pts)
 tri={}
 for i,j,k in combinations(range(n),3):
  a,b,c=pts[i],pts[j],pts[k]
  u=tuple(F.sub(y,x) for x,y in zip(a,b));v=tuple(F.sub(y,x) for x,y in zip(a,c))
  if d==2:
   col=F.times(u[0],v[1])==F.times(u[1],v[0])
  else: col=all(F.times(u[a],v[b])==F.times(u[b],v[a]) for a in range(d) for b in range(a+1,d))
  tri[i,j,k]=int(col)
 def atom(t):
  return (tuple(int(t[i]==t[j]) for i in range(len(t)) for j in range(i+1,len(t))), tuple(1 if len(set((t[i],t[j],t[k])))<3 else tri[tuple(sorted((t[i],t[j],t[k])))] for i,j,k in combinations(range(len(t)),3)))
 intern={}
 def canon(obj):
  if obj not in intern:intern[obj]=len(intern)+1
  return intern[obj]
 # Compute on all tuples bottom-up, keeping only one layer.
 # 4tuple signature requires 5th atomic diagrams.
 types={t:canon((4,atom(t),frozenset(atom(t+(j,)) for j in range(n)))) for t in product(range(n),repeat=4)}
 for k in range(3,-1,-1):
  types={t:canon((k,atom(t),frozenset(types[t+(j,)] for j in range(n)))) for t in product(range(n),repeat=k)}
 return types[()],len(intern)
if __name__=='__main__':
 for q,d in [(2,2),(3,2),(4,2)]:
  print('DIRECT',q,d,'root',direct(q,d),flush=True)
 print('DIRECT_VERIFY_OK')
