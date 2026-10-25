from fractions import Fraction as F
import itertools, math, random

def expected_exact(k,m):
 q=k-m
 H=sum((F(1,i) for i in range(m+1,k+1)),F(0))
 return (F(q*(q+1),m)+2*q-2*(k+1)*H)/(2*k*(k+1))

def direct_nearest(lam,m):
 k=len(lam)
 vals=[]
 for S in itertools.combinations(range(k),m):
  T=[i for i in range(k) if i not in S]
  tail=sum(lam[j] for j in T)
  err=sum(lam[j]**2 for j in T)+tail**2/m
  vals.append((err,S))
 return min(vals)

def nearest_sorted(lam,m):
 tail=sorted(lam,reverse=True)[m:]
 return sum(a*a for a in tail)+sum(tail)**2/m

def exact_integral_via_dirichlet(k,m):
 vals=[]
 for r in range(m+1,k+1):
  for s in range(m+1,k+1):
   c=F(1,m)-F(1,min(r,s))
   vals.append(c*(2 if r==s else 1))
 return sum(vals,F(0))/F(2*k*(k+1))

random.seed(71655)
for k in range(2,13):
 for m in range(1,k):
  e=expected_exact(k,m)
  assert e==exact_integral_via_dirichlet(k,m), (k,m,e)
  for rep in range(30):
   raw=[random.expovariate(1) for _ in range(k)]
   lam=[v/sum(raw) for v in raw]
   expect=nearest_sorted(lam,m)
   if k<=7:
    value,which=direct_nearest(lam,m)
    assert abs(value-expect)<1e-12,(k,m,expect,value,which)
  if k<=5:
   print(k,m,str(e),float(e))
print('Exact matrix-moment identity and all finite nearest-face comparisons passed.')
# Monte Carlo independent of ordered-gaps formula.
for k,m in [(3,1),(3,2),(4,1),(4,2),(4,3),(8,2),(10,5)]:
 v=0.;N=120000
 for _ in range(N):
  raw=[random.expovariate(1) for _ in range(k)];t=sum(raw)
  v+=nearest_sorted([x/t for x in raw],m)/2
 empirical=v/N;truth=float(expected_exact(k,m))
 assert abs(empirical-truth)<0.006,(k,m,empirical,truth)
 print('MC',k,m,round(empirical,6),round(truth,6))
