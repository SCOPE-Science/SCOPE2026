#!/usr/bin/env python3
"""Reproduce integral Morse certificates for ordinary matching complexes of cycle prisms.
Only elementary combinatorics and Python integers are required.
"""
from collections import defaultdict,Counter,deque
from functools import lru_cache

ORDERS = {
 3:[7,5,1,3,4,2,0,8,6],
 4:[1,9,8,5,10,2,3,7,4,0,11,6],
 5:[14,10,0,13,6,5,3,8,7,11,4,1,12,9,2],
 6:[11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12],
 7:[13,20,10,5,2,11,19,18,17,16,8,6,0,14,1,4,15,12,3,9,7],
 8:[1,9,20,19,2,14,21,4,0,7,6,17,23,13,8,15,22,11,18,5,12,10,16,3],
}

def prism_edges(n):
 return [((i,a),((i+1)%n,a)) for a in range(2) for i in range(n)]+[((i,0),(i,1)) for i in range(n)]

def face_list(n):
 e=prism_edges(n)
 masks=[(1<<(u[0]+n*u[1])) | (1<<(v[0]+n*v[1])) for u,v in e]
 forbid=[sum(1<<j for j,b in enumerate(masks) if b&masks[i]) for i in range(3*n)]
 face=[0]
 for i in range(3*n):face += [f|(1<<i) for f in face if not(f&forbid[i])]
 return sorted(f for f in face if f)

def make_matching(faces,order):
 present=set(faces);lower={};upper={}
 for i in order:
  pairs=[]
  for f in faces:
   if f not in present or f&(1<<i):continue
   g=f|(1<<i)
   if g in present:pairs.append((f,g))
  for f,g in pairs:
   assert f in present and g in present
   present.remove(f);present.remove(g)
   lower[f]=g;upper[g]=f
 return present,lower,upper

def acyclic_certificate(faces,lower):
 present=set(faces)
 indeg=dict.fromkeys(faces,0)
 edges=defaultdict(list)
 count=0
 for f in faces:
  y=f
  while y:
   b=y&-y;y-=b
   g=f^b
   if g not in present:continue
   if lower.get(g)==f:src,dst=g,f
   else:src,dst=f,g
   edges[src].append(dst);indeg[dst]+=1;count+=1
 queue=deque(f for f in faces if indeg[f]==0)
 seen=0
 while queue:
  f=queue.popleft();seen+=1
  for g in edges[f]:
   indeg[g]-=1
   if indeg[g]==0:queue.append(g)
 assert seen==len(faces),(seen,len(faces))
 return count,seen

def boundary(f):
 y=f;j=0
 while y:
  b=y&-y;y-=b
  yield f^b,1 if j%2==0 else -1
  j+=1

def morse_boundary(critical,lower,upper):
 bydim=defaultdict(list)
 for f in critical:bydim[f.bit_count()-1].append(f)
 results={}
 for d in sorted(bydim):
  if d<1 or not bydim.get(d-1):continue
  targets=bydim[d-1]
  index={f:j for j,f in enumerate(targets)}
  @lru_cache(None)
  def projection(s):
   if s in index:return {index[s]:1}
   if s in upper:return {}
   if s not in lower:raise AssertionError(('lost simplex',s))
   u=lower[s]
   coef=next(sign for f,sign in boundary(u) if f==s)
   z=defaultdict(int)
   for f,sgn in boundary(u):
    if f==s:continue
    for j,a in projection(f).items():z[j]-=coef*sgn*a
   return {j:v for j,v in z.items() if v}
  matrix=[]
  for c in bydim[d]:
   z=defaultdict(int)
   for f,sgn in boundary(c):
    for j,a in projection(f).items():z[j]+=sgn*a
   matrix.append([z[j] for j in range(len(targets))])
  results[d]={'rows':len(matrix),'cols':len(targets),'matrix':matrix,'projection_cache':projection.cache_info().currsize}
 return results

def rank_integer(mat):
 if not mat or not mat[0]:return 0
 from fractions import Fraction
 a=[[Fraction(x) for x in row] for row in mat];m=len(a);n=len(a[0]);r=0
 for c in range(n):
  p=next((i for i in range(r,m) if a[i][c]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r]
  t=a[r][c]
  for j in range(c,n):a[r][j]/=t
  for i in range(r+1,m):
   x=a[i][c]
   if x:
    for j in range(c,n):a[i][j]-=x*a[r][j]
  r+=1
  if r==m:break
 return r

def run(n):
 edges=prism_edges(n);assert len(set(tuple(sorted(e)) for e in edges))==3*n
 faces=face_list(n)
 order=ORDERS[n]
 assert sorted(order)==list(range(3*n))
 crit,low,up=make_matching(faces,order)
 assert 2*len(low)+len(crit)==len(faces)
 hasse,visited=acyclic_certificate(faces,low)
 counts=dict(sorted(Counter(f.bit_count()-1 for f in crit).items()))
 matrices=morse_boundary(crit,low,up)
 ranks={d:rank_integer(x['matrix']) for d,x in matrices.items()}
 print('n',n,'faces',len(faces),'Hasse_edges',hasse,'pairs',len(low),'critical',counts);print('order',order)
 print('Morse_matrices',matrices,'rational_ranks',ranks)
 if n==5:
  assert counts=={0:1,2:2,3:2} and ranks.get(3,0)==0
 if n==6:assert counts=={0:1,3:12}
 if n==7:assert counts=={0:1,4:14}
 if n==8:
  assert counts=={0:1,4:4,5:8} and ranks.get(5,0)==1
  coeff=[abs(a) for row in matrices[5]['matrix'] for a in row]
  from math import gcd
  from functools import reduce
  assert reduce(gcd,coeff)==1
  assert any(a in (1,-1) for row in matrices[5]['matrix'] for a in row)
 return counts
if __name__=='__main__':
 for n in [3,4,5,6,7,8]:run(n)
 print('ALL_CERTIFICATES_OK')
