from itertools import combinations
from prism_core import graph,char

def rank_sparse_mod(cols, p):
 pivots={}
 for col in cols:
  a={k:(v%p) for k,v in col.items() if v%p}
  while a:
   k=max(a)
   if k not in pivots:
    inv=pow(a[k],-1,p)
    pivots[k]={i:(v*inv)%p for i,v in a.items() if (v*inv)%p}
    break
   c=a[k];q=pivots[k]
   for j,v in q.items():
    nv=(a.get(j,0)-c*v)%p
    if nv:a[j]=nv
    else:a.pop(j,None)
 return len(pivots)

def complexes(n):
 V,E=graph(n)
 c0=list(combinations(V,2));d0={z:i for i,z in enumerate(c0)}
 c1=[(ei,v) for ei,e in enumerate(E) for v in V if v not in e];d1={z:i for i,z in enumerate(c1)}
 c2=[(i,j) for i,j in combinations(range(len(E)),2) if not(set(E[i])&set(E[j]))]
 b1=[]
 for ei,v in c1:
  u,w=E[ei]
  b1.append({d0[tuple(sorted((u,v)))]:-1,d0[tuple(sorted((w,v)))]:1})
 b2=[]
 for i,j in c2:
  u,v=E[i];w,z=E[j]
  b2.append({d1[(j,v)]:1,d1[(j,u)]:-1,d1[(i,z)]:-1,d1[(i,w)]:1})
 return len(c0),len(c1),len(c2),b1,b2

if __name__=='__main__':
 for n in range(5,13):
  c0,c1,c2,b1,b2=complexes(n)
  ranks=[(p,rank_sparse_mod(b1,p),rank_sparse_mod(b2,p)) for p in (2,3,5)]
  assert all(d1==c0-1 and d2==c1-c0+1-(n+2) for _,d1,d2 in ranks),(n,ranks)
  assert c2-ranks[0][2]==(n-1)*(n-2)//2
  print(n, (c0,c1,c2), ranks)
 print('PRISM_TOPOLOGY_CHECK_OK')
