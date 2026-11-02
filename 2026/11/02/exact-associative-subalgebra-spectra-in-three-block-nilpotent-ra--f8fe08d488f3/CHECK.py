from itertools import product
from math import prod

def gbin(n,k,q):
 if k<0 or k>n:return 0
 if k==0 or k==n:return 1
 return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))
def gl(n,q):return prod(q**n-q**i for i in range(n))
def pred(r,q):
 out=[0]*(2*r+2)
 for d in range(2*r+2):
  out[d]=gbin(2*r,d-1,q)
  if d<=r:
   for a in range(r+1):
    for b in range(r-a+1):
     t=a+b-d
     if 0<=t<=min(a,b):
      out[d]+=q**d*gbin(r,a,q)*gbin(r-a,b,q)*gbin(a,t,q)*gbin(b,t,q)*gl(t,q)
 return out

def rrref(n,q):
 # generate all reduced row echelon bases over F_q
 for d in range(n+1):
  from itertools import combinations
  for piv in combinations(range(n),d):
   free=[]
   for i,p in enumerate(piv):
    for c in range(p+1,n):
     if c not in piv:free.append((i,c))
   for coeff in product(range(q),repeat=len(free)):
    mat=[[0]*n for _ in range(d)]
    for i,p in enumerate(piv):mat[i][p]=1
    for (i,c),v in zip(free,coeff):mat[i][c]=v
    yield mat

def mul(x,y,q):
 if q!=4:return (x*y)%q
 v=0
 for i in range(2):
  for j in range(2):
   if (x>>i)&1 and (y>>j)&1:v^=1<<(i+j)
 if v&4:v^=7  # x^2 = x+1 in GF(4)
 return v

def add(x,y,q):
 return x^y if q==4 else (x+y)%q

def observed(r,q):
 n=2*r+1;out=[0]*(n+1)
 for rows in rrref(n,q):
  d=len(rows)
  valid=True
  for x in rows:
   for y in rows:
    c=0
    for i in range(r):c=add(c,mul(x[i],y[r+i],q),q)
    contains_z=bool(rows and rows[-1]==[0]*(2*r)+[1])
    if c and not contains_z:
     valid=False;break
   if not valid:break
  out[d]+=valid
 return out

if __name__=='__main__':
 for r,q in ((1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(3,2)):
  p=pred(r,q);v=observed(r,q)
  print('r,q',r,q,'formula',p,'actual',v,'PASS',p==v,flush=True)
  assert p==v
 print('GENERALIZED_HEISENBERG_SUBALGEBRA_OK')
