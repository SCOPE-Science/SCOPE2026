from fractions import Fraction as F
from itertools import combinations
from math import comb
import sympy as s

def claimed(a,b,k):
 N=a+b
 m=F(2*a*b*k*(N-k),N*(N-1))
 first=F((a-b)**2*(N-2*k)**2,N*N*(N-2)**2)
 second=F(4*(a-1)*(b-1)*(k-1)*(N-k-1),(N-3)*(N-2)**2*(N-1)**2)
 return m,1+first+second

def actual(a,b,k):
 N=a+b
 states=[tuple(c) for c in combinations(range(N),k)]
 idx={st:i for i,st in enumerate(states)}
 Q=s.zeros(len(states)); lam=[]
 for i,x in enumerate(states):
  xx=set(x)
  for p in range(a):
   for q in range(a,N):
    if (p in xx) != (q in xx):
     y=tuple(sorted((xx-{p})|{q})) if p in xx else tuple(sorted((xx-{q})|{p}))
     Q[i,idx[y]]+=1
  Q[i,i]=-sum(Q[i,j] for j in range(len(states)) if j!=i)
  lam.append(-Q[i,i])
 mu=sum(lam)/len(states)
 lamv=s.Matrix([v-mu for v in lam]); Mat=-Q
 # fix row of Poisson equation by sum zero constraint
 Mat[0,:]=s.ones(1,len(states));lamv[0]=0
 h=Mat.inv()*lamv
 vv=mu+2*sum(lam[i]*h[i] for i in range(len(states)))/len(states)
 return F(int(mu.p),int(mu.q)),F(int(vv.p),int(vv.q))/F(int(mu.p),int(mu.q))

ct=0
for a in range(1,5):
 for b in range(1,5):
  if a+b<4:continue
  for k in range(1,a+b):
   v=actual(a,b,k);c=claimed(a,b,k)
   if v!=c: raise AssertionError((a,b,k,v,c))
   ct+=1
print('PASS',ct,'exact full configuration tests')
for a,b,k in [(2,2,2),(5,5,5),(6,4,5),(1,5,3),(6,7,4)]:print(a,b,k,claimed(a,b,k))

# Verify the hypergeometric variance decomposition as a rational polynomial identity.
from sympy.functions.combinatorial.numbers import stirling
A,B,K=s.symbols('A B K',integer=True,positive=True)
NN=A+B
fall=s.ff
raw=[]
for p in range(5):
 raw.append(s.factor(sum(stirling(p,r,kind=2)*fall(A,r)*fall(K,r)/fall(NN,r) for r in range(1,p+1))) if p else s.Integer(1))
mm=raw[1]
v=s.factor(raw[2]-mm**2)
m3=s.factor(raw[3]-3*mm*raw[2]+2*mm**3)
m4=s.factor(raw[4]-4*mm*raw[3]+6*mm**2*raw[2]-3*mm**4)
H=s.factor(m4-v**2-m3**2/v)
expected=2*A*B*K*(A-1)*(B-1)*(K-1)*(NN-K)*(NN-K-1)/(NN*(NN-3)*(NN-2)**2*(NN-1)**2)
assert s.cancel(H-expected)==0
print('PASS symbolic hypergeometric degree-two norm identity')

# Verify the critical joint balance window against exact rational Fano values.
for n in [256,1296,4096,10000,65536]:
 # a/N = 1/2 + approximately 0.5 n^(-1/4); k/N = 1/2 + 0.75 n^(-1/4)
 delta1=round(0.5*n**0.75)
 delta2=round(0.75*n**0.75)
 aa=n//2+delta1;kk=n//2+delta2
 f=claimed(aa,n-aa,kk)[1]
 val=n*(f-1)
 assert val>0
 print('asymptotic check N=',n,' N(F-1)=',float(val),'limit=',16*(0.5**2)*(0.75**2)+0.25)
