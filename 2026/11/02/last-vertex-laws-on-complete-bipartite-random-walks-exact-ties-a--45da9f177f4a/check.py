"""Standalone exact checks of last-cover law and asymptotic diagnostics."""
from fractions import Fraction as F
from math import comb, log, exp
from functools import lru_cache

checks=0

def assert_eq(x,y):
 global checks
 assert x==y,(x,y)
 checks+=1

def last_by_markov(a,b):
 @lru_cache(None)
 def solve(i,j):
  if i==a:return (F(1),F(1))
  if j==b:return (F(0),F(0))
  q=F(j,b);p=F(i,a)
  HB=solve(i,j+1)[1]
  HA=solve(i+1,j)[0]
  x=(q*(1-p)*HA+(1-q)*HB)/(1-q*p)
  y=p*x+(1-p)*HA
  return x,y
 return solve(1,0)[0]

def coupon_pgf_a_minus1(a,z):
 v=F(1)
 for s in range(1,a):v*=F(s)*z/(a-(a-s)*z)
 return v

def last_by_coupon(a,b):
 return sum(((-1)**(j+1)*comb(b,j)*coupon_pgf_a_minus1(a,F(b-j,b)) for j in range(1,b+1)),F(0))

for a in range(1,9):
 for b in range(1,9):
  x=last_by_markov(a,b); y=last_by_coupon(a,b)
  assert_eq(x,y)
  assert_eq(F(0)<=x<=F(1),True)
  if a==1:assert_eq(x,F(1))
  if b==1 and a>1:assert_eq(x,F(0))

# Independent coupon completion law via exact finite Markov occupancy recursion.
def finish_dist(n,steps=300):
 p=[F(0)]*(n+1);p[0]=F(1)
 out=[]
 for t in range(steps):
  q=[F(0)]*(n+1)
  for k in range(n+1):
   q[k]+=p[k]*F(k,n)
   if k<n:q[k+1]+=p[k]*F(n-k,n)
  out.append(q[n]-p[n]);p=q
 return out,p[n]
for n in range(1,5):
 d,mass=finish_dist(n,steps=60)
 fromsum=sum((x*x for x in d),F(0))
 b=last_by_coupon(n,n)
 err=(F(1)-mass*mass)/2 # bounds on missing finite tail, not used for exact equality
 assert_eq(abs(b-(F(1)+fromsum)/2)<F(1,10**9), True)

# Check Gumbel-window and balanced bias with stable float dynamic forward recursion.
def last_float(a,b):
 A=[0.0]*a; B=[0.0]*(b+1);A[0]=B[0]=1.0
 result=0.0
 for t in range(int(max(a,b)*(log(max(a,b))+25))):
  Q=[0.0]*(b+1)
  for k,v in enumerate(B):
   Q[k]+=v*(k/b)
   if k<b:Q[k+1]+=v*(b-k)/b
  result+=A[-1]*(Q[-1]-B[-1]);B=Q
  P=[0.0]*a
  for k,v in enumerate(A):
   P[k]+=v*(k+1)/a
   if k<a-1:P[k+1]+=v*(a-1-k)/a
  A=P
 return result
for n in (25,50,100,200,400):
 ans=last_float(n,n)
 assert 0.10<n*(ans-0.5)<0.15
 checks+=1
for n in (100,200):
 for delta in (-1,0,1):
  b=max(1,n+round(delta*n/log(n)))
  value=last_float(n,b)
  target=1/(1+exp(-delta))
  assert abs(value-target)<0.15,(n,delta,value,target)
  checks+=1
print('PASS',checks,'exact and numerical assertions')
print('balanced_n_200',last_float(200,200),'scaled_bias',200*(last_float(200,200)-.5))
