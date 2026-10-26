from fractions import Fraction as F
from itertools import combinations
from math import comb,sqrt
for n in range(5,11):
 for r in range(3,n-1):
  a=F(2,n-r);b=F(n-r-1,r*(n-r));c=F(r-1,r*(n-r))
  Q=((1-a,a),(b,1-b-c))
  ss=list(combinations(range(n),r));index={S:i for i,S in enumerate(ss)}
  pi0=F((n-r)*(n-r-1),n*(n-1));pi1=F(2*r*(n-r),n*(n-1));pi2=F(r*(r-1),n*(n-1))
  assert pi0+pi1+pi2==1
  target={0,1};vec=[F(1,len(ss)) if len(set(S)&target)!=2 else F(0) for S in ss]
  qvec=[pi0,pi1]
  for t in range(1,8):
   obs=sum(vec)
   assert obs==sum(qvec), (n,r,t,obs,qvec)
   new=[F(0)]*len(ss)
   for i,S in enumerate(ss):
    if vec[i]==0:continue
    for x in S:
     for y in range(n):
      if y in S:continue
      T=tuple(sorted((set(S)-{x})|{y}));j=index[T]
      if len(set(T)&target)!=2:new[j]+=vec[i]/(r*(n-r))
   vec=new
   qvec=[sum(qvec[i]*Q[i][j] for i in range(2)) for j in range(2)]
  assert n*n > 0
  z=float(a+b+c);disc=z*z-4*float(a*c)
  delta=(z-sqrt(disc))/2
  assert 0<delta<float(a) and 0<delta<1
  h=1-delta/float(a)
  assert abs(float(Q[0][0])+float(Q[0][1])*h-(1-delta))<1e-12
  assert abs(float(Q[1][0])+float(Q[1][1])*h-(1-delta)*h)<1e-12
print('VERIFY_OK: exact lumped avoidance recurrences for all 3<=r<=n-2, 5<=n<=10, t<=7; Perron eigenpair')
for r in [3,4,7,10]:
 for n in [1000,10000]:
  A=n+2*r-2
  delta=4*(r-1)/((n-r)*(A+sqrt(A*A-8*r*(r-1))))
  assert abs(delta*n*n/(2*(r-1))-1)<0.08
print('VERIFY_OK: positive Perron root and rate asymptotics')
