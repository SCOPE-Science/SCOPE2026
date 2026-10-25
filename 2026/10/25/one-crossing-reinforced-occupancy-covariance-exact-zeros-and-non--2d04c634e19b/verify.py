from fractions import Fraction as F
from math import comb, factorial, prod, gamma
from itertools import combinations

def rise(a,n):
 out=F(1)
 for j in range(n): out*=a+j
 return out

def compositions(n,m):
 if m==1:yield (n,);return
 for a in range(n+1):
  for tail in compositions(n-a,m-1):yield (a,)+tail

def closed(m,n,r,a):
 u=rise((m-1)*a,n)/rise(m*a,n)
 v=F(comb(n,r))*rise(a,r)*rise((m-1)*a,n-r)/rise(m*a,n)
 w=F(comb(n,r))*rise(a,r)*rise((m-2)*a,n-r)/rise(m*a,n)
 return m*(m-1)*w-m*m*u*v

def exact(m,n,r,a):
 den=rise(m*a,n)
 ez=er=ezr=F(0)
 total=F(0)
 for x in compositions(n,m):
  p=F(factorial(n),prod(factorial(k) for k in x))*prod(rise(a,k) for k in x)/den
  z=x.count(0);xr=x.count(r)
  ez+=p*z;er+=p*xr;ezr+=p*z*xr;total+=p
 assert total==1
 return ezr-ez*er

ct=0
for m in (3,4,5):
 for n in range(2,9):
  for a in (F(1,2),F(1),F(2),F(3,2)):
   seq=[]
   for r in range(1,n+1):
    c=closed(m,n,r,a)
    assert c==exact(m,n,r,a),(m,n,r,a,c,exact(m,n,r,a))
    seq.append((c>0)-(c<0))
    if a==1: assert ((c>0)-(c<0))==((m*(r-1)>2*(n-1))-(m*(r-1)<2*(n-1)))
    ct+=1
   assert seq==sorted(seq) and seq[0]==-1 and seq[-1]==1,(m,n,a,seq)
print('EXACT_OCCUPANCY_PASS',ct)
for m in (3,4,5,7):
 for a in (.5,1,2,5,30):
  B=gamma((m-1)*a)**2/(gamma((m-2)*a)*gamma(m*a)) if a<30 else None
  if B:
   theta=1-((m-1)/m*B)**(1/a)
   assert 0<theta<1,(m,a,theta)
  if a==1: assert abs(theta-2/m)<1e-12
print('ASYMPTOTIC_LIMIT_CHECK_PASS')
print('VERIFY_OK')
