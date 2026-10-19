from itertools import product
from math import comb

def mul(A,B,n,p):
 return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%p for i in range(n) for j in range(n))
def inv(A,n,p):
 X=[[A[i*n+j]%p for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
 for c in range(n):
  cand=next((i for i in range(c,n) if X[i][c]%p),None)
  if cand is None:return None
  X[c],X[cand]=X[cand],X[c]
  z=pow(X[c][c],-1,p)
  X[c]=[(x*z)%p for x in X[c]]
  for i in range(n):
   if i!=c:
    z=X[i][c]; X[i]=[(u-z*v)%p for u,v in zip(X[i],X[c])]
 return tuple(X[i][n+j] for i in range(n) for j in range(n))
def b0(X,n,p):
 Y=[0]*(n*n)
 for i in range(n):
  for j in range(n):
   x=X[i*n+j]
   if i<=j:
    for r in range(n):
     if i+r<n and j+r+1<n: Y[(i+r)*n+j+r+1]=(Y[(i+r)*n+j+r+1]+x)%p
   else:
    for r in range(1,n):
     if i-r>=0 and j-r+1>=0: Y[(i-r)*n+j-r+1]=(Y[(i-r)*n+j-r+1]-x)%p
 return tuple(Y)
def P(t,n,p):return tuple(comb(j,i)*pow(t,j-i,p)%p if i<=j else 0 for i in range(n) for j in range(n))
def test(n,p):
 E=[tuple(int(k==i*n+j) for k in range(n*n)) for i in range(n) for j in range(n)]
 for X in E:
  for Y in E:
   RX=b0(X,n,p); RY=b0(Y,n,p)
   if mul(RX,RY,n,p)!=b0(tuple((a+b)%p for a,b in zip(mul(RX,Y,n,p),mul(X,RY,n,p))),n,p):raise ValueError('RB fails')
 for t in range(p):
  U=P(t,n,p);V=inv(U,n,p)
  for X in E:
   a=b0(mul(mul(U,X,n,p),V,n,p),n,p)
   b=mul(mul(U,b0(X,n,p),n,p),V,n,p)
   if a!=b:raise ValueError(('pascal fails',n,p,t))
 I=tuple(int(i==j) for i in range(n) for j in range(n))
 stabilizers=[]; group=0
 for vals in product(range(p),repeat=n*n):
  V=inv(vals,n,p)
  if V is None:continue
  group+=1
  if all(b0(mul(mul(vals,X,n,p),V,n,p),n,p)==mul(mul(vals,b0(X,n,p),n,p),V,n,p) for X in E):stabilizers.append(vals)
 target={tuple(c*x%p for x in P(t,n,p)) for c in range(1,p) for t in range(p)}
 assert set(stabilizers)==target,(n,p,len(stabilizers),len(target),set(stabilizers)-target)
 print('OK',n,p,'GL',group,'stabilizers',len(stabilizers),'inner orbit',group//len(stabilizers))
for n,p in [(2,2),(3,2),(2,3),(3,3)]:test(n,p)
for n in range(2,6):
 for p in (2,3,5):
  E=[tuple(int(k==i*n+j) for k in range(n*n)) for i in range(n) for j in range(n)]
  for X in E:
   for Y in E:
    bx=b0(X,n,p);by=b0(Y,n,p)
    assert mul(bx,by,n,p)==b0(tuple((u+v)%p for u,v in zip(mul(bx,Y,n,p),mul(X,by,n,p))),n,p)
  for t in range(p):
   U=P(t,n,p); V=inv(U,n,p)
   for X in E:
    assert b0(mul(mul(U,X,n,p),V,n,p),n,p)==mul(mul(U,b0(X,n,p),n,p),V,n,p)
  for c in range(1,p):
   D=tuple(pow(c,i,p) if i==j else 0 for i in range(n) for j in range(n))
   Di=inv(D,n,p)
   for X in E:
    assert mul(mul(D,b0(mul(mul(Di,X,n,p),D,n,p),n,p),n,p),Di,n,p)==tuple(pow(c,-1,p)*v%p for v in b0(X,n,p))
  e=E[(n-1)*n+0]; assert any(e)
  for _ in range(2*n-2): e=b0(e,n,p)
  assert e[0*n+n-1] == ((-1)**(n-1))%p
  assert all(v==0 for v in b0(e,n,p))
print('VERIFY_OK: RB identities, Pascal stabilizers, finite-field inner stabilizer exhaustions, scalar conjugacies, nilpotence witnesses')

