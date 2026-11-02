from itertools import combinations
from fractions import Fraction as F
from math import comb
count=0
for N in range(3,12):
 for a in range(1,N):
  b=N-a; sm1=sm2=sm3=0
  for S in combinations(range(1,N+1),a):
   V=sum(i for i in S); W2=F((2*V-a*(N+1))**2,4); R=1+sum(((i in S)!=(i+1 in S)) for i in range(1,N))
   sm1+=W2; sm2+=R; sm3+=W2*R
  total=F(comb(N,a));cov=sm3/total-(sm1/total)*(sm2/total)
  ans=-F(a*b*(a*b-1),3*N)
  if cov!=ans:print('FAIL',N,a,cov,ans);exit(1)
  count+=1
print('PASS',count,'(N,a) exact exhaustive cases, N<=11')

# Independently verify the position-resolved transition covariance formula.
for N in range(4,11):
    for a in range(1,N):
        b=N-a
        k=F(N*(N+1)-6*a*b,(N-2)*(N-3))
        mu=F(N*(N-2),12)
        pred_avg=-F(a*b-1,6)
        for t in range(1,N):
            z=F(2*t-N,2)
            predicted=F(2*a*b,N*(N-1))*(pred_avg+k*(z*z-mu))
            words=list(combinations(range(1,N+1),a))
            val=F(0)
            for S in words:
                W=F(2*sum(S)-a*(N+1),2)
                val+=W*W*((t in S)!=(t+1 in S))
            Ew2=F(a*b*(N+1),12)
            cov=val/len(words)-Ew2*F(2*a*b,N*(N-1))
            assert cov==predicted, (N,a,t,cov,predicted)
print('PASS local covariance for all N=4..10, a=1..N-1 and t=1..N-1')
