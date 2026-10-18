import itertools
from collections import defaultdict
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def faces(q):
  result=[]
  for k in range(1,4):
    for I in itertools.combinations(range(6),k):
      if any((i+1)%6 in I for i in I):continue
      result +=[tuple(i*q+c for i,c in zip(I,C)) for C in itertools.product(range(q),repeat=k)]
  return result

def rot(face,q,t):return tuple(sorted(((v//q+t)%6)*q+v%q for v in face))
def can(chain,q):return min(tuple(rot(f,q,t) for f in chain) for t in range(6))
def chain(q):
  fs=faces(q); arrays=[]
  for k in range(1,4):
    arrays.append(sorted({can((f,),q) for f in fs if len(f)==k}))
  # all chains of length=2,3: ordered dimensions increase
  c2=[];c3=[]
  for f in fs:
    if len(f)>=2:
      for j in range(1,len(f)):
        for a in itertools.combinations(f,j):c2.append((a,f))
    if len(f)==3:
      for a in itertools.combinations(f,1):
        for b in itertools.combinations(f,2):
          if set(a).issubset(b):c3.append((a,b,f))
  C=[sorted({can((f,),q) for f in fs}),sorted({can(t,q) for t in c2}),sorted({can(t,q) for t in c3})]
  B=[]
  for d in [1,2]:
    index={s:i for i,s in enumerate(C[d-1])}
    M=[[0]*len(C[d]) for _ in range(len(C[d-1]))]
    for col,x in enumerate(C[d]):
      for i in range(d+1): M[index[can(x[:i]+x[i+1:],q)]][col]+=(-1)**i
    B.append(M)
  return C,B

def rankmod(M,p):
  if not M:return 0
  rows=len(M); cols=len(M[0]); a=[[x%p for x in row] for row in M];rank=0
  for j in range(cols):
    r=next((k for k in range(rank,rows) if a[k][j]),None)
    if r is None:continue
    a[rank],a[r]=a[r],a[rank]; z=pow(a[rank][j],-1,p)
    a[rank]=[x*z%p for x in a[rank]]
    for k in range(rank+1,rows):
      if a[k][j]:
        c=a[k][j];a[k]=[(x-c*y)%p for x,y in zip(a[k],a[rank])]
    rank+=1
    if rank==rows:break
  return rank

for q in (1,2,3,4):
  C,B=chain(q); print('q',q,'quot cell counts',list(map(len,C)))
  for k in range(len(C[2])):
    for j in range(len(C[0])):
      assert sum(B[0][j][i]*B[1][i][k] for i in range(len(C[1])))==0, (q,j,k)
  for p in (2,3,5,7):
    ranks=[rankmod(x,p) for x in B]
    hom=[len(C[0])-1-ranks[0],len(C[1])-ranks[0]-ranks[1],len(C[2])-ranks[1]]
    print(' mod',p,'ranks',ranks,'reduced b',hom)
    assert hom == [0,q*(q-1)//2,((q-1)**3+2*(q-1))//3], (q,p,hom)
  if q<=2:
    for i,M in enumerate(B):
      S=smith_normal_form(Matrix(M),domain=ZZ)
      diag=[int(S[j,j]) for j in range(min(S.rows,S.cols)) if S[j,j]!=0]
      print(' SNF boundary',i+1,'nonunits',[(j,x) for j,x in enumerate(diag) if abs(x)!=1])
      assert all(abs(x)==1 for x in diag)

print("VERIFIED quotient homology, finite fields, Smith invariants")
