from itertools import product,combinations
from fractions import Fraction
from math import gcd
from collections import Counter
from functools import reduce

vertices=list(product((0,1),repeat=3))
edges=[(i,j) for i,a in enumerate(vertices) for j,b in enumerate(vertices) if i<j and sum(x!=y for x,y in zip(a,b))==1]
black=[i for i,v in enumerate(vertices) if sum(v)%2==0]
white=[i for i,v in enumerate(vertices) if sum(v)%2==1]
retain=[v for v in range(8) if v not in (black[-1],white[-1])]
P=[tuple(int(t in e) for t in retain) for e in edges]

def det(a):
 n=len(a)
 if not n:return 1
 b=[list(map(int,r)) for r in a]
 sign=1; prev=1
 for k in range(n-1):
  if b[k][k]==0:
   sw=next((j for j in range(k+1,n) if b[j][k]),None)
   if sw is None:return 0
   b[k],b[sw]=b[sw],b[k];sign=-sign
  pivot=b[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    z=b[i][j]*pivot-b[i][k]*b[k][j]
    assert z%prev==0
    b[i][j]=z//prev
   b[i][k]=0
  prev=pivot
 return sign*b[n-1][n-1]

def rank(a):
 if not a:return 0
 b=[list(map(Fraction,r)) for r in a]
 m=len(b);n=len(b[0]);r=0
 for j in range(n):
  k=next((i for i in range(r,m) if b[i][j]),None)
  if k is None:continue
  b[r],b[k]=b[k],b[r]
  z=b[r][j]
  for t in range(j,n):b[r][t]/=z
  for i in range(r+1,m):
   z=b[i][j]
   for t in range(j,n):b[i][t]-=z*b[r][t]
  r+=1
  if r==m:break
 return r

# The edge differences span the ambient rank-six character lattice.
differences=[[p[j]-P[0][j] for j in range(6)] for p in P[1:]]
assert rank(differences)==6
assert reduce(gcd,(abs(det([differences[i] for i in cols])) for cols in combinations(range(11),6)),0)==1

facets={}
for select in combinations(range(12),6):
 rows=[list(P[i])+[1] for i in select]
 vec=[(-1)**j*det([row[:j]+row[j+1:] for row in rows]) for j in range(7)]
 if vec==[0]*7:continue
 g=reduce(gcd,vec)
 vec=tuple(v//g for v in vec)
 values=[sum(a*b for a,b in zip(vec,list(x)+[1])) for x in P]
 if max(values)>0 and min(values)<0:continue
 if max(values)==0:vec=tuple(-v for v in vec);values=[-v for v in values]
 eq=frozenset(i for i,v in enumerate(values) if v==0)
 assert len(eq)>=6 and rank([list(P[i])+[1] for i in eq])==6
 assert eq not in facets or facets[eq]==vec
 facets[eq]=vec
assert len(facets)==12, len(facets)
full=frozenset(range(12))
faces={full};stack=[full]
while stack:
 F=stack.pop()
 for facet in facets:
  B=F & facet
  if B and B not in faces:
   faces.add(B);stack.append(B)
assert len(faces)==349, len(faces)
facedim={F:rank([list(P[i])+[1] for i in F])-1 for F in faces}
assert dict(Counter(facedim.values()))=={6:1,5:12,4:52,3:108,2:110,1:54,0:12}, Counter(facedim.values())

bad=[]; nonsimple=[]
for F in faces:
 dim=facedim[F]
 if dim==6:continue
 r=6-dim
 rays=[normal[:6] for facet,normal in facets.items() if F<=facet]
 assert rank(rays)==r
 if len(rays)>r:
  bad.append(F);nonsimple.append(F)
 else:
  assert len(rays)==r
  index=reduce(gcd,(abs(det([[u[j] for j in cols] for u in rays])) for cols in combinations(range(6),r)),0)
  if index!=1:bad.append(F)
assert bad==nonsimple or set(bad)==set(nonsimple)
assert Counter(facedim[f] for f in bad)=={0:12,1:30,2:8}
max_bad=[f for f in bad if not any(f<g for g in bad)]
star_faces={frozenset(i for i,e in enumerate(edges) if v in e) for v in range(8)}
opposite={frozenset((i,next(j for j,e2 in enumerate(edges) if e2==tuple(sorted((edges[i][0]^7,edges[i][1]^7))))) ) for i in range(12)}
assert len(opposite)==6
assert set(max_bad)==star_faces|opposite, (len(max_bad),star_faces,opposite)
assert len([f for f in max_bad if facedim[f]==2])==8
assert len([f for f in max_bad if facedim[f]==1])==6
assert all(len(f)==3 for f in star_faces)
assert all(len(f)==2 for f in opposite)
# f vector for coordinate union of P2 and P1 components (simplicial complex facets above)
complex_faces=set()
for facet in max_bad:
 for i in range(1,len(facet)+1):
  complex_faces.update(frozenset(x) for x in combinations(facet,i))
assert Counter(map(len,complex_faces))=={1:12,2:30,3:8}
print('VERIFY_OK polytope_dimension=6 facets=12 faces=349 singular_faces=(12,30,8) maximal=(8_P2,6_P1) f_complex=(12,30,8)')
