"""Independent exact and numerical checks of cyclic conservative Active Flux feasibility."""
from fractions import Fraction as F
from itertools import product
from random import Random
from scipy.optimize import linprog
import numpy as np

STATES=(-1,0,1)

def bounds(y):
 n=len(y)
 return [min(y[i-1],y[i]) for i in range(n)], [max(y[i-1],y[i]) for i in range(n)]

def reward(s,a,l,u):
 return (l-a) if s==-1 else ((a-u) if s==1 else F(0))

def dp_dual(y,a,lam,cap):
 n=len(a);l,u=bounds(y)
 opt=None
 for start in STATES:
  d={s:None for s in STATES};d[start]=reward(start,a[0],l[0],u[0])
  for i in range(1,n):
   nd={}
   for s in STATES:
    nd[s]=reward(s,a[i],l[i],u[i])+max(d[t]-lam*cap*abs(t-s) for t in STATES if d[t] is not None)
   d=nd
  v=max(d[s]-lam*cap*abs(s-start) for s in STATES)
  opt=v if opt is None else max(v,opt)
 return sum(abs(y[i]-y[i-1]) for i in range(n))+2*opt

def brute_dual(y,a,lam,cap):
 n=len(a);l,u=bounds(y)
 return sum(abs(y[i]-y[i-1]) for i in range(n))+2*max(
  sum(reward(s,a[i],l[i],u[i]) for i,s in enumerate(p))-lam*cap*sum(abs(p[i-1]-p[i]) for i in range(n))
  for p in product(STATES,repeat=n))

def cut_cap(y,a,lam):
 n=len(a);l,u=bounds(y)
 if not sum(l)<=sum(a)<=sum(u):return None
 cap=F(0)
 for start in range(n):
  sl=su=F(0)
  for k in range(1,n):
   i=(start+k-1)%n
   sl+=l[i]-a[i];su+=a[i]-u[i]
   cap=max(cap,sl/(2*lam),su/(2*lam))
 return cap

def brute_cap(y,a,lam):
 n=len(a);l,u=bounds(y)
 if not sum(l)<=sum(a)<=sum(u):return None
 val=F(0)
 for p in product(STATES,repeat=n):
  cost=sum(abs(p[i-1]-p[i]) for i in range(n))
  r=sum(reward(s,a[i],l[i],u[i]) for i,s in enumerate(p))
  if cost:val=max(val,r/(lam*cost))
  elif r>0: return None
 return val

def primal_lp(y,a,lam,cap):
 n=len(a);l,u=bounds(y)
 # Optimize 2 distance outside bounds through upper/lower hinge auxiliaries p_i and q_i
 # m_i = a_i + lam(f_{i-1}-f_i)
 c=np.array([0.]*n+[1.]*(2*n))
 A=[];bb=[]
 for i in range(n):
  row=np.zeros(3*n)
  row[i]=-lam;row[i-1 if i>0 else n-1]+=lam
  row[n+i]=-1
  A.append(row);bb.append(float(u[i]-a[i]))
  row=np.zeros(3*n)
  row[i]=lam;row[i-1 if i>0 else n-1]-=lam
  row[2*n+i]=-1
  A.append(row);bb.append(float(a[i]-l[i]))
 out=linprog(c,A_ub=A,b_ub=bb,bounds=[(-float(cap),float(cap))]*n+[(0,None)]*(2*n),method='highs')
 assert out.success,out.message
 return float(sum(abs(y[i]-y[i-1]) for i in range(n))+2*out.fun)

rng=Random(457812)
ct=0
for n in range(2,9):
 for trial in range(72):
  y=[F(rng.randint(-3,4)) for _ in range(n)]
  a=[F(rng.randint(-4,5)) for _ in range(n)]
  lam=F(rng.randint(1,5),rng.randint(1,5))
  cap=F(rng.randint(0,7),rng.randint(1,5))
  v=dp_dual(y,a,lam,cap)
  assert v==brute_dual(y,a,lam,cap)
  w=primal_lp(y,a,lam,cap)
  assert abs(float(v)-w)<1e-7,(n,y,a,lam,cap,v,w)
  assert cut_cap(y,a,lam)==brute_cap(y,a,lam)
  ct+=1
print('PASS exact cyclic ternary DP vs exhaustive 3^n dual and numerical primal LP:',ct,'cases (n=2..8)')
print('PASS exact cyclic interval cap vs exhaustive ternary dual:',ct,'cases')
for m in (1,2,3,4,6,9):
 n=2*m;y=[F(i%2) for i in range(n)];a=[F(2) if i<m else F(-1) for i in range(n)]
 assert cut_cap(y,a,F(1))==F(m,2),(n,cut_cap(y,a,F(1)))
print('PASS sharp collective-bottleneck family, n=2m, lambda=1, delta*=m/2, m=1,2,3,4,6,9')
