from collections import Counter,defaultdict
from itertools import product,combinations
q=3
# Matrices modulo scalar identity choose a00=0, other 8 coordinates [a01,a02,a10,a11,a12,a20,a21,a22]
ix=[(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
vecs=[]; ids={}
for tail in product(range(3),repeat=8):
 if not any(tail):continue
 first=next(x for x in tail if x)
 if first!=1:continue
 v=tuple(tail)
 ids[v]=len(vecs);vecs.append(v)
assert len(vecs)==3280

def norm(v):
 v=tuple(x%3 for x in v)
 for x in v:
  if x:return tuple(y*(1 if x==1 else 2)%3 for y in v)
 return None

def full(v):
 A=[[0]*3 for _ in range(3)]
 for (i,j),x in zip(ix,v):A[i][j]=x
 return A

def matvec(A,p):return tuple(sum(A[i][j]*p[j] for j in range(3))%3 for i in range(3))
P=[norm(p) for p in product(range(3),repeat=3) if norm(p) is not None]
P=list(dict.fromkeys(P));assert len(P)==13
# smooth iff A has no rational eigenvectors, proven by Tallini + irreducible polynomial
smooth=[]
for v in vecs:
 A=full(v)
 if all(matvec(A,p)!=p and matvec(A,p)!=tuple(2*x%3 for x in p) and matvec(A,p)!=(0,0,0) for p in P): smooth.append(v)
assert len(smooth)==576,len(smooth)
S=set(smooth)
lines={}
for ai,a in enumerate(smooth):
 for b in smooth[ai+1:]:
  # for projective pencil over F3 all 4 F3 points must smooth
  c=norm(tuple(x+y for x,y in zip(a,b)));d=norm(tuple(x-y for x,y in zip(a,b)))
  if c in S and d in S:
   pen=frozenset((a,b,c,d));assert len(pen)==4
   lines[pen]=None
print('smooth',len(smooth),'pencils',len(lines))
# tangent coincidences at rational pts. For each p tangent A gives line span(p,Ap), normalize line cross product

def tangent(A,p):
 v=matvec(A,p)
 return norm((p[1]*v[2]-p[2]*v[1],p[2]*v[0]-p[0]*v[2],p[0]*v[1]-p[1]*v[0]))
T={v:tuple(tangent(full(v),p) for p in P) for v in smooth}
# common tangent at p for every curve in pencil; then base is nontransverse at p
count=Counter()
for pen in lines:
 a,b=tuple(pen)[:2]
 t=sum(T[a][j]==T[b][j] for j in range(13))
 count[t]+=1
print('shared tangents',count)
# generate matrices GL3(3); group PGL3 5616
from itertools import product

def det(A):
 a,b,c=A
 return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))%3
GL=[]
for entries in product(range(3),repeat=9):
 if entries[0:3] ==(0,0,0):continue
 A=[entries[:3],entries[3:6],entries[6:]]
 if det(A):
  # mod scalar group
  if next(x for x in entries if x)==1:GL.append(A)
print('PGL order',len(GL))

def adjugate(M):
 a,b,c=M
 return [[(b[1]*c[2]-b[2]*c[1])%3,(a[2]*c[1]-a[1]*c[2])%3,(a[1]*b[2]-a[2]*b[1])%3],[(b[2]*c[0]-b[0]*c[2])%3,(a[0]*c[2]-a[2]*c[0])%3,(a[2]*b[0]-a[0]*b[2])%3],[(b[0]*c[1]-b[1]*c[0])%3,(a[1]*c[0]-a[0]*c[1])%3,(a[0]*b[1]-a[1]*b[0])%3]]
def prod(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3))%3 for j in range(3)] for i in range(3)]
def trans(M,v):
 A=prod(prod(M,full(v)),adjugate(M))
 # quotient subtract scalar a00
 x=A[0][0];A=[[ (A[i][j] - (x if i==j else 0))%3 for j in range(3)] for i in range(3)]
 return norm(tuple(A[i][j] for i,j in ix))
# group orbits of pencil using small generating matrices sufficient (swap coords, 3-cycle, shear)
gens=[[[0,1,0],[1,0,0],[0,0,1]],[[0,1,0],[0,0,1],[1,0,0]],[[1,1,0],[0,1,0],[0,0,1]],[[2,0,0],[0,1,0],[0,0,1]]]
seen=set(); orbits=[]
for seed in lines:
 if seed in seen:continue
 orbit={seed}; stack=[seed]
 while stack:
  pen=stack.pop()
  for M in gens:
   pp=frozenset(trans(M,v) for v in pen)
   if pp not in lines: raise RuntimeError(('out',pen,pp))
   if pp not in orbit: orbit.add(pp);stack.append(pp)
 seen.update(orbit);orbits.append((seed,len(orbit),sum(T[tuple(seed)[0]][j]==T[tuple(seed)[1]][j] for j in range(13))))
print('pencil orbits',len(orbits), Counter((o[1],o[2]) for o in orbits));print('orbits',orbits)
