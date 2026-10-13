from itertools import product
from math import prod

def matmul(A,B,q):
  return [[sum(x*y for x,y in zip(row,col))%q for col in zip(*B)] for row in A]

def rank(A,q):
  A=[list(map(lambda x:x%q,row)) for row in A]; m=len(A); n=len(A[0]) if m else 0; rr=0
  for j in range(n):
    ii=next((i for i in range(rr,m) if A[i][j]),None)
    if ii is None:continue
    A[rr],A[ii]=A[ii],A[rr]
    inv=pow(A[rr][j],-1,q)
    A[rr]=[(u*inv)%q for u in A[rr]]
    for i in range(m):
      if i!=rr and A[i][j]:
        t=A[i][j];A[i]=[(u-t*v)%q for u,v in zip(A[i],A[rr])]
    rr+=1
  return rr

def sym2(P,q):
  r=len(P); pair=[(i,j) for i in range(r) for j in range(i,r)]; W=len(pair)
  A=[]
  for i,j in pair:
    # polynomial product of f(x_i), f(x_j)
    col=[]
    for a,b in pair:
      v=P[a][i]*P[b][j]
      if a!=b:v+=P[b][i]*P[a][j]
      col.append(v%q)
    A.append(col)
  return list(map(list,zip(*A)))

def constraints(P,q):
  r=len(P); W=r*(r+1)//2; S=sym2(P,q)
  # Endomorphism f determined by f(x_i) = P x_i + Q x_i; f^2 on V gives P^2 and QP+S Q
  # Constraint entry (a,i) in Q - QP - S Q =0
  rows=[]
  for a in range(W):
    for i in range(r):
      row=[]
      for b in range(W):
        for j in range(r):
          val=int(a==b and i==j) - (int(a==b)*P[j][i]) - S[a][b]*int(i==j)
          row.append(val%q)
      rows.append(row)
  return rows

def count_all(r,q):
  W=r*(r+1)//2; strata={k:0 for k in range(r+1)}; distribution={}
  for a in product(range(q),repeat=r*r):
    P=[list(a[i*r:(i+1)*r]) for i in range(r)]
    if matmul(P,P,q)!=P:continue
    k=rank(P,q)
    h=W*r-rank(constraints(P,q),q)
    strata[k]+=q**h
    distribution[(k,h)]=distribution.get((k,h),0)+1
  return strata,distribution

def gauss(n,k,q):
  if k<0 or k>n:return 0
  aa=prod(q**(n-j)-1 for j in range(k));bb=prod(q**(k-j)-1 for j in range(k));return aa//bb

def theory(r,q):
  W=r*(r+1)//2;out={}
  for k in range(r+1):
    S=k*(k+1)//2
    d=k*(W-S)+(r-k)*S
    out[k]=gauss(r,k,q)*q**(k*(r-k)+d)
  return out

if __name__=='__main__':
 for r,q in [(1,2),(2,2),(2,3),(2,5),(3,2),(3,3)]:
  a,dist=count_all(r,q)
  print(r,q,a,theory(r,q),dist,flush=True)
  assert a==theory(r,q)
 print('VERIFY_OK')

# Separate exhaustive test of idempotence and image subspaces, using full degree-two
# multiplication rather than the constraint-matrix count.
def rref_key(A,q):
  A=[list(row) for row in A if any(z%q for z in row)]
  if not A:return ()
  n=len(A[0]); pivotrow=0
  for j in range(n):
    ii=next((i for i in range(pivotrow,len(A)) if A[i][j]%q),None)
    if ii is None:continue
    A[pivotrow],A[ii]=A[ii],A[pivotrow]
    u=pow(A[pivotrow][j],-1,q)
    A[pivotrow]=[(z*u)%q for z in A[pivotrow]]
    for i in range(len(A)):
      if i!=pivotrow and A[i][j]:
        z=A[i][j];A[i]=[(a-z*b)%q for a,b in zip(A[i],A[pivotrow])]
    pivotrow+=1
    if pivotrow==len(A):break
  return tuple(tuple(row) for row in A[:pivotrow])

def enumerate_direct(r,q):
  s=r*(r+1)//2; images={k:set() for k in range(r+1)}; counts={k:0 for k in range(r+1)}
  for pp in product(range(q),repeat=r*r):
    P=[list(pp[i*r:(i+1)*r]) for i in range(r)]
    S=sym2(P,q)
    for qq in product(range(q),repeat=s*r):
      Q=[list(qq[i*r:(i+1)*r]) for i in range(s)]
      # On generators: the full endomorphism matrix has block rows [P 0;Q S].
      # Compare each full column against the corresponding column of its square.
      if any(sum(P[i][j]*P[j][h] for j in range(r))%q!=P[i][h] for i in range(r) for h in range(r)):continue
      if any((sum(Q[a][j]*P[j][h] for j in range(r))+sum(S[a][b]*Q[b][h] for b in range(s)))%q!=Q[a][h] for a in range(s) for h in range(r)):continue
      k=rank(P,q);counts[k]+=1
      rows=[]
      for i in range(r):rows.append(tuple(P[a][i] for a in range(r))+tuple(Q[b][i] for b in range(s)))
      for j in range(s):rows.append((0,)*r+tuple(S[a][j] for a in range(s)))
      images[k].add(rref_key(rows,q))
  return counts,{k:len(v) for k,v in images.items()}

def retract_theory(r,q):
  s=r*(r+1)//2
  return {k:gauss(r,k,q)*q**(k*(s-k*(k+1)//2)) for k in range(r+1)}

if __name__=='__main__':
 for r,q in [(2,2),(2,3)]:
  actual,retracts=enumerate_direct(r,q)
  print('direct',r,q,actual,retracts,flush=True)
  assert actual==theory(r,q)
  assert retracts==retract_theory(r,q)
 print('DIRECT_VERIFY_OK')
