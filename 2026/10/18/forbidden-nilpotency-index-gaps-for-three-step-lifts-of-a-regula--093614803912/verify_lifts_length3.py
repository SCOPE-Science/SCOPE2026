"""Finite checks for nilpotency-index counts of 3-step lifts.
All operations use integer arithmetic modulo a prime. No external packages.
"""
from collections import Counter
from itertools import product

def expected(n,q):
 c=(n+1)//2; T=q**(2*n*n)
 d={}
 for r in range(c):d[3*n-2*r]=(q-1)*T//q**(r+1)
 for t in range(c):d[2*n-t]=(q-1)*T//q**(c+t+1)
 for t in range(c,n):d[2*n-t]=T//q**(2*t)-T//q**(2*t+2)
 d[n]=T//q**(2*n)
 assert sum(d.values())==T
 return d

def nilindex(A,q):
 n=len(A); V=[[int(i==j) for j in range(n)] for i in range(n)]
 for power in range(1,n+1):
  W=[[sum(A[i][k]*V[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]
  if not any(any(row) for row in W):return power
  V=W
 raise AssertionError('not nilpotent')

def lift(C,D,q):
 n=len(C);m=3*n; A=[[0]*m for _ in range(m)]
 for j in range(3):
  for i in range(n-1):A[j*n+i][j*n+i+1]=1
 for i in range(n):
  for j in range(n):
   A[n+i][j]=C[i][j]
   A[2*n+i][n+j]=C[i][j]
   A[2*n+i][j]=D[i][j]
 return A

def enumeration(n,q):
 count=Counter()
 for co in product(range(q),repeat=n*n):
  C=[co[i*n:(i+1)*n] for i in range(n)]
  for do in product(range(q),repeat=n*n):
   D=[do[i*n:(i+1)*n] for i in range(n)]
   count[nilindex(lift(C,D,q),q)]+=1
 prediction=expected(n,q)
 assert dict(count)==prediction,(count,prediction)
 print('exhaustive',n,q,sorted(count.items()))

def polynomial(n,q):
 # Directly work with the quotient R[t]/(t^n-eps*g-eps^2*h).
 # Store polynomials as array of n coefficient triples.
 count=Counter()
 for gt in product(range(q),repeat=n):
  for ht in product(range(q),repeat=n):
   vec=[[0,0,0] for i in range(n)]; vec[0][0]=1
   for k in range(1,3*n+1):
    ans=[[0,0,0] for i in range(n)]
    for i in range(1,n):ans[i]=vec[i-1][:]
    top=vec[-1]
    for i in range(n):
     ans[i][1]=(ans[i][1]+top[0]*gt[i])%q
     ans[i][2]=(ans[i][2]+top[0]*ht[i]+top[1]*gt[i])%q
    vec=ans
    if not any(any(z) for z in vec):
     count[k]+=1;break
   else:raise AssertionError('nilpotency bound')
 pred={k:v//(q**(2*n*n-2*n)) for k,v in expected(n,q).items()}
 assert dict(count)==pred,(count,pred)
 print('companion',n,q,sorted(count.items()))

if __name__=='__main__':
 for n,q in ((1,2),(2,2),(2,3)):
  enumeration(n,q)
 for n,q in ((2,5),(3,2),(3,3),(4,2),(5,2)):
  polynomial(n,q)
 print('VERIFY_OK')

# Extra extension-field check for reproducibility if imported and executed.
def gf4_mul(x,y):
 z=0
 if y&1:z^=x
 if y&2:z^=x<<1
 if z&8:z^=0b1100  # x^3=x*(x+1)=x^2+x (adjust via polynomial)
 if z&4:z^=0b111    # x^2=x+1
 return z

def polynomial_gf4(n):
 count=Counter();q=4
 for gt in product(range(q),repeat=n):
  for ht in product(range(q),repeat=n):
   vec=[[0,0,0] for _ in range(n)];vec[0][0]=1
   for k in range(1,3*n+1):
    ans=[[0,0,0] for _ in range(n)]
    for i in range(1,n):ans[i]=vec[i-1][:]
    top=vec[-1]
    for i in range(n):
     ans[i][1]^=gf4_mul(top[0],gt[i])
     ans[i][2]^=gf4_mul(top[0],ht[i])^gf4_mul(top[1],gt[i])
    vec=ans
    if not any(any(z) for z in vec):
     count[k]+=1;break
   else:raise AssertionError('not nilpotent')
 factor=q**(2*n*n-2*n)
 pred={k:v//factor for k,v in expected(n,q).items()}
 assert dict(count)==pred,(count,pred)
 print('companion GF4',n,sorted(count.items()))

if __name__=='__main__':
 for n in (2,3):polynomial_gf4(n)
 print('VERIFY_GF4_OK')
