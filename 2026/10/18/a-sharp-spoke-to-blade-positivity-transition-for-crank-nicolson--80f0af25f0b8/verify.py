"""Exact and high-precision checks for the generalized-windmill CN threshold.
This finite checker corroborates, but does not prove, the all-size theorem.
Python 3 standard library only.
"""
from fractions import Fraction as F
from math import sqrt

def mat_inverse(A):
    n=len(A)
    B=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if B[k][j])
        B[j],B[k]=B[k],B[j]
        c=B[j][j]
        B[j]=[u/c for u in B[j]]
        for i in range(n):
            if i!=j and B[i][j]:
                a=B[i][j]
                B[i]=[u-a*v for u,v in zip(B[i],B[j])]
    return [row[n:] for row in B]

def laplacian(r,s,a,b):
    n=1+r*s
    A=[[F(0)]*n for _ in range(n)]
    def edge(i,j,w):
        A[i][i]+=w;A[j][j]+=w;A[i][j]-=w;A[j][i]-=w
    for j in range(1,n):edge(0,j,b)
    for k in range(r):
        js=range(1+k*s,1+(k+1)*s)
        for i in js:
            for j in range(i+1,1+(k+1)*s):edge(i,j,a)
    return A

def formulas(r,s,a,b,t):
    m=r*s;n=m+1
    Rh=F(1,n)+F(m,n)/(1+t*n*b)
    Ro=(F(1,n)+F(1,m*n)/(1+t*n*b)+F(r-1,m)/(1+t*b)
        +F(s-1,s)/(1+t*(b+s*a)))
    return Rh,Ro

checks=0
for r in range(2,6):
 for s in range(2,5):
  crit=F(r*(r*s-1),r*(s-2)+1)
  for b in (F(1), F(3,2)):
   for ratio in (F(1,10),F(1),crit/2,crit,2*crit,20*crit):
    a=ratio*b; th=F(1,(r*s-1))*F(1,b)
    Rh,Ro=formulas(r,s,a,b,th)
    assert Rh==F(1,2)
    assert (Ro>F(1,2))==(ratio<crit)
    assert (Ro==F(1,2))==(ratio==crit)
    assert (Ro<F(1,2))==(ratio>crit)
    checks+=4
    # Full matrix inverse at several rational points, for modest sizes.
    if r<=3 and s<=3 and b==1 and ratio in (F(1),crit,2*crit):
     L=laplacian(r,s,a,b)
     for t in (F(1,100),th,F(3,2)*th):
      R=mat_inverse([[F(i==j)+t*L[i][j] for j in range(len(L))] for i in range(len(L))])
      X,Y=formulas(r,s,a,b,t)
      assert R[0][0]==X
      for i in range(1,len(L)):assert R[i][i]==Y
      assert all(R[i][j]>0 for i in range(len(L)) for j in range(len(L)))
      T=[[2*R[i][j]-F(i==j) for j in range(len(L))] for i in range(len(L))]
      assert all(sum(row)==1 for row in T)
      assert all(T[i][j]>=0 for i in range(len(L)) for j in range(len(L)) if i!=j)
      assert all(T[i][i]>=0 for i in range(len(L))) == (X>=F(1,2) and Y>=F(1,2))
      checks+=len(L)*2+5

# Two distinct singular scaling laws for fixed r,s, b=1.
def outer(r,s,a,t):
 m=r*s;n=m+1
 return (1/n + 1/(m*n)/(1+t*n) + (r-1)/m/(1+t) + (s-1)/s/(1+t*(1+s*a)))
def bisect(r,s,a):
 lo=0.; hi=1.
 while outer(r,s,a,hi)>.5:hi*=2.
 for _ in range(150):
  md=(lo+hi)/2
  if outer(r,s,a,md)>.5:lo=md
  else:hi=md
 return (lo+hi)/2
for r in (2,3,5):
 for s in (2,3,4,6):
  a=1e8
  h=2*bisect(r,s,a)
  limit=h*sqrt(a)/sqrt(2) if s==2 else h*a*(s-2)/2
  assert abs(limit-1)<.005, (r,s,limit)
  checks+=1
print('VERIFY_OK',checks,'assertion groups; exact rational matrices and singular-limit probes')
