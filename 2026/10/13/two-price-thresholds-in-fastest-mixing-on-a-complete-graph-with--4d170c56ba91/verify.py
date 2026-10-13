from fractions import Fraction as F
from math import isclose
from random import Random

def plus(x):return max(F(0),x)
def cost(s,r,t,b):
 return s*r*b + t*F(s-1,2)*plus(1-r*b)+F(r-1,2)*plus(1-s*b)
def optimum(s,r,t):
 n=s+r
 t1=F(s*(r+1),r*(s-1))
 t2=F(2*s,s-1)
 if t<t1: b=F(1,n)
 elif t>t1:
  if s<=r:b=F(1,r)
  elif t<t2:b=F(1,s)
  elif t>t2:b=F(1,r)
  else:b=F(1,r)
 else: b=F(1,n)
 a=plus(1-r*b)/s
 c=plus(1-s*b)/r
 C=cost(s,r,t,b)
 return a/C,b/C,c/C,F(1,C),b,C

def full_lap(s,r,a,b,c):
 n=s+r
 L=[[F(0) for _ in range(n)] for i in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   w=a if i<s and j<s else c if i>=s and j>=s else b
   L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
 return L

def test(s,r,t):
 a,b,c,lam,b0,C=optimum(s,r,t)
 n=s+r
 assert t*F(s*(s-1),2)*a + s*r*b+F(r*(r-1),2)*c==1
 lam1=s*a+r*b; lam2=s*b+r*c; lam3=n*b
 assert lam == min(lam1,lam2,lam3)
 assert all(C<=cost(s,r,t,v) for v in {F(1,n), F(1,s),F(1,r),F(1),F(2,1)})
 L=full_lap(s,r,a,b,c)
 vecs=[]
 for i in range(s-1):vecs.append(([F(1) if j==i else F(-1) if j==s-1 else F(0) for j in range(n)],lam1))
 for i in range(r-1):vecs.append(([F(1) if j==s+i else F(-1) if j==n-1 else F(0) for j in range(n)],lam2))
 vecs.append(([F(r) for _ in range(s)]+[F(-s) for _ in range(r)],lam3))
 vecs.append(([F(1)]*n,F(0)))
 for x,ev in vecs:
  assert all(sum(L[i][j]*x[j] for j in range(n))==ev*x[i] for i in range(n))
 return C
if __name__=='__main__':
 rng=Random(307)
 total=0
 for s in range(2,11):
  for r in range(2,11):
   t1=F(s*(r+1),r*(s-1));t2=F(2*s,s-1)
   ts={t1,t1/F(2),t1+F(1,100),max(F(1,1000),t1-F(1,100)),t2,t2+F(1,100),max(F(1,1000),t2-F(1,100)),F(1),F(3,2),F(3),F(7),F(11,4)}
   for t in ts: test(s,r,t);total+=1
 print('VERIFY_OK',total,'exact rational two-block Laplacian eigenvector, budget and global breakpoint tests')
