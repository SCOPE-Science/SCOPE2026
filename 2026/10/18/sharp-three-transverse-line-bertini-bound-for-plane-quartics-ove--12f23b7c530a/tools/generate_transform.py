from pathlib import Path
import json
T=json.load(open(Path(__file__).resolve().parent.parent/'data/quartic_tab.json'));monos=[tuple(x) for x in T['monos']];idx={v:i for i,v in enumerate(monos)}
subs=[[[0,1,0],[1,0,0],[0,0,1]], [[1,0,0],[0,0,1],[0,1,0]], [[2,0,0],[0,1,0],[0,0,1]], [[1,1,0],[0,1,0],[0,0,1]], [[1,0,0],[0,1,1],[0,0,1]]]
def mult(p,q):
 ans={}
 for m,a in p.items():
  for n,b in q.items():
   s=tuple(i+j for i,j in zip(m,n));ans[s]=(ans.get(s,0)+a*b)%3
 return ans
mats=[]
for sm in subs:
 A=[[0]*15 for _ in range(15)]
 for j,m in enumerate(monos):
  p={(0,0,0):1}
  for k,v in enumerate(m):
   for _ in range(v):p=mult(p,{tuple(1 if z==u else 0 for z in range(3)):sm[k][u] for u in range(3) if sm[k][u]})
  for ex,c in p.items(): A[idx[ex]][j]=c
 mats.append(A)
open(Path(__file__).resolve().parent.parent/'data/qgenmat.json','w').write(json.dumps(mats))
print('generated',len(mats))
