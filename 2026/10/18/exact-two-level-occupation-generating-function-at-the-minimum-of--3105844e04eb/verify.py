from fractions import Fraction as F
from math import comb
from collections import defaultdict, Counter
from itertools import product

def prod(A,B,nmax):
 C=defaultdict(F)
 for (t,a,b),v in A.items():
  for (s,c,d),w in B.items():
   if t+s<=nmax:C[t+s,a+c,b+d]+=v*w
 return dict(C)

def paths_direct(nmax):
 joint=defaultdict(F);Q=defaultdict(F);E=defaultdict(F)
 for n in range(nmax+1):
  for steps in product((-1,1),repeat=n):
   s=[0]
   for st in steps:s.append(s[-1]+st)
   mi=min(s); N0=sum(x==mi for x in s);N1=sum(x==mi+1 for x in s)
   wt=F(1,2**n)
   joint[n,N0,N1]+=wt
   if n==0 or min(s[1:])>0: Q[n,0,sum(x==1 for x in s[1:])]+=wt
   if n>=2 and s[-1]==0 and min(s[1:-1])>0:E[n,0,sum(x==1 for x in s[1:])]+=wt
 return joint, Q,E
joint,Q,E=paths_direct(10)
# Coefficient factorization
B=prod(Q,Q,10)
all_cf=defaultdict(F);power={(0,0,0): F(1)}
for k in range(1,12):
 layer=prod(B,power,10)
 for (n,u,v),a in layer.items():all_cf[n,k,v]+=a
 power=prod(power,E,10)
for key in set(joint)|set(all_cf): assert joint[key]==all_cf[key],(key,joint[key],all_cf[key])
print('factorization passed',len(joint),'direct masses',len(all_cf),'composed masses')
# exact E_v vs z^2 v/(4(1-v E)) at selected v, using univariate series
for v in [F(0),F(1,2),F(1),F(2),F(3)]:
 e=[F(0)]*11
 for m in range(1,6):e[2*m]=F(comb(2*m-2,m-1),m*4**m)
 # rhs denom invert coeff
 den=[F(1)] +[-v*e[i] for i in range(1,11)]
 inv=[F(0)]*11;inv[0]=F(1)
 for i in range(1,11): inv[i]=-sum(den[j]*inv[i-j] for j in range(1,i+1))
 for n in range(11):
  from_path=sum(c*v**b for (t,a,b),c in E.items() if t==n)
  from_formula=F(0) if n<2 else F(v,4)*inv[n-2]
  assert from_path==from_formula,(n,v,from_path,from_formula)
 print('E closed form confirmed for v=',v)
# Test Q_v against explicit GF for rational v using bounded formal power series
L=11
e=[F(0)]*L
for m in range(1,L//2+1):
 if 2*m<L:e[2*m]=F(comb(2*m-2,m-1),m*4**m)
def inv(a):
 out=[F(0)]*L;out[0]=1/a[0]
 for n in range(1,L):out[n]=-sum(a[j]*out[n-j] for j in range(1,n+1))/a[0]
 return out
def mul(a,b):return [sum(a[i]*b[j-i] for i in range(j+1)) for j in range(L)]
def add(a,b):return [a[i]+b[i] for i in range(L)]
one=[F(1)]+[F(0)]*(L-1)
D=[one[i]-e[i] for i in range(L)]
D2=[one[i]-2*e[i] for i in range(L)]
N=[one[i]-e[i]+(F(1,2) if i==1 else 0) for i in range(L)]
q=mul(N,inv(D2)); h=mul(q,inv(D))
for v in [F(0),F(1,2),F(1),F(2),F(3)]:
 vD=[one[i]-v*e[i] for i in range(L)]
 numer=[one[i]+(h[i-1]/2 if i>=1 else 0) for i in range(L)]
 term=mul(numer,inv(vD))
 pred=add(one,[F(0)]+[v*term[i]/2 for i in range(L-1)])
 for n in range(L):
  actual=sum(c*v**b for (t,a,b),c in Q.items() if t==n)
  assert pred[n]==actual,(n,v,pred[n],actual)
 print('Q closed form confirmed for v=',v)
print('all tested')

# Rare joint event exact binomial survival formula.
for n in range(2,11):
    predicted = F(comb(n-2,(n-2)//2), 2**(n-1))
    assert joint[n,1,1] == predicted, (n,joint[n,1,1],predicted)
print('rare joint cell verified for horizons 2 through 10')
