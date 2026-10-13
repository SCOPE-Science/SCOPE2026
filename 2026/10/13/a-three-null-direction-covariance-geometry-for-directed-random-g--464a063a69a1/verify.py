from fractions import Fraction
from itertools import product
from math import comb
for n in (2,3,4):
 for p in (Fraction(1,3),Fraction(2,3)):
  arcs=[(i,j) for i in range(n) for j in range(n) if i!=j]
  b=[Fraction(comb(n-1,k))*p**k*(1-p)**(n-1-k) for k in range(n)]
  Z=[Fraction(0) for _ in range(2*n)]; G=[[Fraction(0) for _ in range(2*n)] for _ in range(2*n)]
  for mask in range(1<<len(arcs)):
   degin=[0]*n;degout=[0]*n; e=0
   for a,(i,j) in enumerate(arcs):
    if mask>>a&1:degin[j]+=1;degout[i]+=1;e+=1
   w=p**e*(1-p)**(len(arcs)-e)
   v=[degin.count(k) for k in range(n)]+[degout.count(k) for k in range(n)]
   for i in range(2*n):
    Z[i]+=w*v[i]
    for j in range(2*n):G[i][j]+=w*v[i]*v[j]
  assert Z==[n*x for x in b]*2
  for i in range(2*n):
   for j in range(2*n):
    k=i%n;l=j%n
    delta=n*b[k]*(int(k==l)-b[l]) if (i<n)==(j<n) else b[k]*b[l]*(k-(n-1)*p)*(l-(n-1)*p)*n/((n-1)*p*(1-p))
    assert G[i][j]-Z[i]*Z[j]==delta,(n,p,i,j,G[i][j]-Z[i]*Z[j],delta)
  Ediff=sum((G[k][k]+G[n+k][n+k]-2*G[k][n+k])/(2*n*b[k]) for k in range(n))
  assert Ediff==n-2,(n,p,Ediff)
  print('PASS',n,p,'case count',1<<len(arcs),'Pearson difference expectation',Ediff)
print('VERIFY_OK')
