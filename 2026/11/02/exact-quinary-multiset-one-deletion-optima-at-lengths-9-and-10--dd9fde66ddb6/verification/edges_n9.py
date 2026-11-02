import numpy as np, time, os
from itertools import combinations
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix

def compositions(n,q):
 if q==1: yield (n,)
 else:
  for j in range(n+1):
   for y in compositions(n-j,q-1): yield (j,)+y
n,q=9,5
xs=list(compositions(n,q)); assert len(xs)==715
idx={v:i for i,v in enumerate(xs)}
pairs=[]
for a,x in enumerate(xs):
 for i in range(q):
  if x[i]==0: continue
  for j in range(q):
   if j==i:continue
   v=list(x);v[i]-=1;v[j]+=1
   b=idx[tuple(v)]
   if a<b:pairs.append((a,b))
assert len(pairs)==sum(sum(xi>0 for xi in x)*4 for x in xs)//2
rows=np.repeat(np.arange(len(pairs)),2)
cols=np.array(pairs,dtype=int).ravel()
E=coo_matrix((np.ones(len(cols)),(rows,cols)),shape=(len(pairs),len(xs))).tocsr()
t=time.monotonic()
r=milp(c=-np.ones(len(xs)),integrality=np.ones(len(xs)),bounds=Bounds(0,1),constraints=LinearConstraint(E,0,1),options={'time_limit':140,'mip_rel_gap':0.0})
print('Independent edge formulation',len(xs),'vertices',len(pairs),'edges',time.monotonic()-t,'sec','status',r.status,'max',-r.fun if r.fun is not None else None,'certified upper',-r.mip_dual_bound if r.mip_dual_bound is not None else None,flush=True)
assert r.status==0 and -r.mip_dual_bound<143.9999 and -r.fun>142.999
print('Q5N9_EDGE_MILP_OK',flush=True)
os._exit(0)
