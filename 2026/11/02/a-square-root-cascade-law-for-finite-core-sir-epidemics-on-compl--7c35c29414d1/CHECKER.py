from functools import lru_cache
from fractions import Fraction as F
from math import comb, sqrt, lgamma, exp, log

def direct_core2_probability(n,lam):
 b=lam/(1+lam)
 return F(1)-sum(F(comb(n,k))*b**k*(1-b)**(n-k)/(1+lam*k) for k in range(n+1))

def ctmc_core2(n,lam):
 @lru_cache(None)
 def success(s,i,c):
  if s==i==0 and c==0:return F(0)
  total=lam*i+i+(lam*s+1 if c else 0)
  if total==0:return F(0)
  z=lam*i
  if i:z+=i*success(s,i-1,c)
  if c:
   z+=success(s,i,0)
   if s:z+=lam*s*success(s-1,i+1,1)
  return z/total
 return success(n,0,1)

def direct_expected_periphery(n,lam):
 b=lam/(1+lam)
 return n*b*(1+1/(1+lam)-sum(F(comb(n-1,k))*b**k*(1-b)**(n-1-k)/(1+lam*(k+1)) for k in range(n)))

def ctmc_expected_periphery(n,lam):
 @lru_cache(None)
 def expected(s,i,c1,c2):
  # 0 susceptible, 1 infectious, 2 recovered for second core; c1: 1 infectious, 0 recovered
  active=c1+(c2==1)
  # infected peripheral s+i counts, recovered peripheral n-s-i
  newperiph=lam*s*active
  infect2=lam*i if c2==0 else F(0)
  recoveri=i
  recover1=c1
  recover2=int(c2==1)
  total=newperiph+infect2+recoveri+recover1+recover2
  if total==0:return F(n-s)
  numerator=F(0)
  if newperiph:numerator+=newperiph*expected(s-1,i+1,c1,c2)
  if infect2:numerator+=infect2*expected(s,i,c1,1)
  if recoveri:numerator+=recoveri*expected(s,i-1,c1,c2)
  if recover1:numerator+=expected(s,i,0,c2)
  if recover2:numerator+=expected(s,i,c1,2)
  return numerator/total
 return expected(n,0,1,0)

checks=0
for n in range(1,8):
 for lam in [F(1,4),F(1,2),F(1),F(2),F(3,2)]:
  p=ctmc_core2(n,lam); q=direct_core2_probability(n,lam)
  assert p==q,(n,lam,p,q)
  checks+=1
  a=ctmc_expected_periphery(n,lam); b=direct_expected_periphery(n,lam)
  assert a==b,(n,lam,a,b)
  checks+=1
print('exact checks',checks)
for c in [.5,1,2]:
 for n in [500,2000,10000]:
  lam=c/sqrt(n); b=lam/(1+lam)
  kmax=min(n, int(n*b+15*sqrt(n*b*(1-b))+100))
  kmin=max(0,int(n*b-15*sqrt(n*b*(1-b))-100))
  logs=[lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)+k*log(b)+(n-k)*log(1-b) for k in range(kmin,kmax+1)]
  w=[exp(x) for x in logs]
  norm=sum(w)
  p=1-sum(wj/(1+lam*k) for k,wj in zip(range(kmin,kmax+1),w))/norm
  # calculate n-1 expectation similarly
  n1=n-1
  kmax1=min(n1,int(n1*b+15*sqrt(n1*b*(1-b))+100))
  kmin1=max(0,int(n1*b-15*sqrt(n1*b*(1-b))-100))
  logs1=[lgamma(n1+1)-lgamma(k+1)-lgamma(n1-k+1)+k*log(b)+(n1-k)*log(1-b) for k in range(kmin1,kmax1+1)]
  w1=[exp(x) for x in logs1]
  f=sum(wj/(1+lam*(k+1)) for k,wj in zip(range(kmin1,kmax1+1),w1))/sum(w1)
  mu=n*b*(1+1/(1+lam)-f)/sqrt(n)
  print('c,n,p,p_lim,mu,mu_lim',c,n,round(p,6),round(c*c/(1+c*c),6),round(mu,6),round(c*(1+c*c/(1+c*c)),6))
