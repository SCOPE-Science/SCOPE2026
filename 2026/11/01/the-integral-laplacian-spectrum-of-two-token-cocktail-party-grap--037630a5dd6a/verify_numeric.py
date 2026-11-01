from itertools import combinations
from collections import Counter
from math import comb
import numpy as np
from sympy import Matrix

def table(m):
    vs=list(combinations(range(2*m),2)); index={x:i for i,x in enumerate(vs)}
    adj=[set() for _ in vs]
    for i,(a,b) in enumerate(vs):
      for x in (a,b):
       for y in range(2*m):
        if y!=a and y!=b and y//2!=x//2:
         q=tuple(sorted((y,b if x==a else a)))
         j=index[q]; adj[i].add(j)
    assert all(i in adj[j] for i,z in enumerate(adj) for j in z)
    nn=len(vs)
    L=np.diag([len(z) for z in adj]).astype(int)
    for i,z in enumerate(adj):
     for j in z:L[i,j]=-1
    return L,adj

def spec(m):
    c=comb(m,2)
    ans=Counter({0:1, 2*m:m-1, 2*m-2:m,4*m-4:m*(m-2),4*m-6:c,4*m-2:c})
    for k in list(ans):
     if ans[k]<=0:del ans[k]
    # group equal eigenvalues!
    # Counter constructor does not combine collisions, do manual
    vals=[(0,1),(2*m,m-1),(2*m-2,m),(4*m-4,m*(m-2)),(4*m-6,c),(4*m-2,c)]
    p=Counter()
    for x,y in vals:p[x]+=y
    return p

for m in range(2,10):
 L,adj=table(m)
 pred=spec(m)
 obs=Counter(int(round(x)) for x in np.linalg.eigvalsh(L.astype(float)))
 assert obs==pred,(m,obs,pred)
 deg=Counter(len(z) for z in adj)
 assert deg==Counter({4*m-4:m,4*m-6:2*m*(m-1)})
 print(m, len(adj),sum(map(len,adj))//2,dict(sorted(obs.items())),dict(sorted(deg.items())),flush=True)
 if m<=4:
  t=Matrix(L[:-1,:-1].tolist()).det()
  from functools import reduce
  prod=1
  for x,mult in pred.items():
   if x>0:prod*=x**mult
  assert t==prod//len(adj),(m,t,prod)
  print('tree',m,t,flush=True)
print('PASS_ALL')
