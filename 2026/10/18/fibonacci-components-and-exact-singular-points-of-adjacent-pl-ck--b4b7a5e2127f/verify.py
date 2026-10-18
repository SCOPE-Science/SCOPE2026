"""Finite-field test of Jacobian smoothness criterion for consecutive Plucker sections."""
import itertools,math

def rref_matrices(n,q):
 for i in range(n-1):
  for j in range(i+1,n):
   free=[(0,k) for k in range(i+1,n) if k!=j]+[(1,k) for k in range(j+1,n)]
   for vals in itertools.product(range(q),repeat=len(free)):
    A=[[0]*n for _ in range(2)]
    A[0][i]=1;A[1][j]=1
    for (r,k),val in zip(free,vals):A[r][k]=val
    yield A

def rank(A,q):
 R=[[v%q for v in row] for row in A]; h=len(R); w=len(R[0]) if R else 0; k=0
 for j in range(w):
  pivot=next((i for i in range(k,h) if R[i][j]),None)
  if pivot is None: continue
  R[k],R[pivot]=R[pivot],R[k]
  inv=pow(R[k][j],-1,q); R[k]=[(v*inv)%q for v in R[k]]
  for i in range(h):
   if i==k or not R[i][j]:continue
   fac=R[i][j]
   R[i]=[(u-fac*v)%q for u,v in zip(R[i],R[k])]
  k+=1
  if k==h:break
 return k

def is_in(A,q):
 n=len(A[0]);return all((A[0][j]*A[1][j+1]-A[1][j]*A[0][j+1])%q==0 for j in range(n-1))

def jacobian_rank(A,q):
 n=len(A[0]);J=[]
 for i in range(n-1):
  row=[0]*(2*n)
  row[i]=A[1][i+1];row[i+1]=-A[1][i]
  row[n+i]=-A[0][i+1];row[n+i+1]=A[0][i]
  J.append(row)
 return rank(J,q)

def prediction(A,q):
 n=len(A[0]);nonzero=[(A[0][i]%q or A[1][i]%q)!=0 for i in range(n)]
 if any(not nonzero[i] and not nonzero[i+1] for i in range(n-1)):return False
 for i in range(1,n-1):
  if not nonzero[i]:
   if (A[0][i-1]*A[1][i+1]-A[1][i-1]*A[0][i+1])%q==0:return False
 return True

def independent_subsets(n):
 V=list(range(1,n-1));return [S for m in range(1,len(V)+1) for S in itertools.combinations(V,m) if all(b-a>1 for a,b in zip(S,S[1:]))]

def verify():
 rows=[]
 for n,q in [(4,2),(5,2),(6,2),(7,2),(4,3),(5,3)]:
  total=valid=smooth=0
  for A in rref_matrices(n,q):
   total+=1
   if not is_in(A,q):continue
   valid+=1
   S=jacobian_rank(A,q)==n-1
   P=prediction(A,q)
   assert S==P,(n,q,A,S,P)
   smooth+=S
  subs=independent_subsets(n)
  assert len(subs)==sum(math.comb(n-1-r,r) for r in range(1,(n-1)//2+1))
  rows.append((n,q,total,valid,smooth,len(subs)))
 for row in rows:print('n=%d q=%d GrPoints=%d XPoints=%d Smooth=%d Components=%d'%row)
 print('VERIFY_OK')
if __name__=='__main__':verify()
