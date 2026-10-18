"""Exact finite-cycle coalescence and collective-reset correlation checks.

Requires Python 3 and sympy; numpy/scipy optional for independent numerical checks.
"""
from itertools import combinations
import sympy as sp

r=sp.symbols('r', positive=True)
D=r*r+8*r+8
f=r/(r+8)
t=8*f/(r+4)
a=2*t*(r+8)/D
o=2*t*(r+6)/D
s=2*a/r
assert sp.factor(f+t+a+o+s-1)==0
m=sp.factor(f+sp.Rational(3,4)*t+(a+o)/2+s/4)
C_near=sp.factor(f+t/2+a/4-m*m)
C_far=sp.factor(f+t/2+o/2-m*m)
assert C_near== -64/((r+4)**2*D**2)
P=r**5+16*r**4+88*r**3+192*r**2+112*r-128
assert sp.factor(C_far-4*P/((r+4)**2*(r+8)*D**2))==0
assert sp.factor(m-(r**3+10*r**2+24*r+8)/((r+4)*D))==0
assert sp.limit(C_far,r,0)==-sp.Rational(1,16)
assert sp.limit(r*r*C_far,r,sp.oo)==4

# Independently check all 15 individual Markov balance equations, in exact rational arithmetic.
N=4
states=[sum(1<<i for i in I) for k in range(1,N+1) for I in combinations(range(N),k)]
S=set(states); assert len(states)==15
orbit={}
for st in states:
 n=st.bit_count()
 if n==4: cat='f'; div=1
 elif n==3: cat='t'; div=4
 elif n==1: cat='s'; div=4
 else:
  ids=[i for i in range(N) if st>>i&1]
  if (ids[0]-ids[1])%N in (1,N-1):cat='a';div=4
  else:cat='o';div=2
 orbit[st]=(cat,div)
weights={'f':f,'t':t,'a':a,'o':o,'s':s}
pi={st:weights[orbit[st][0]]/orbit[st][1] for st in states}
flows={st:0 for st in states}
for st in states:
 p=pi[st]
 for i in range(N):
  if not (st>>i&1): continue
  for j in ((i-1)%N,(i+1)%N):
   dst=(st&~(1<<i))|(1<<j)
   if dst==st:continue
   flows[st]-=p
   flows[dst]+=p
 if st != (1<<N)-1:
  flows[st]-=r*p
  flows[(1<<N)-1]+=r*p
assert all(sp.factor(flows[st])==0 for st in states)
assert sp.factor(sum(pi.values())-1)==0
for x in range(N):
 ex=sp.factor(sum(p for st,p in pi.items() if st>>x&1))
 assert sp.factor(ex-m)==0
 for y in range(x+1,N):
  joint=sp.factor(sum(p for st,p in pi.items() if (st>>x&1) and (st>>y&1)))
  target=C_far if abs(x-y)==2 else C_near
  assert sp.factor(joint-m*m-target)==0
print('PASS: exact 15-state generator and all covariances for every positive rate')
print('Opposite covariance numerator:',P)
print('Unique positive root approximately:',sp.nroots(P)[2])

# Independent full finite-state stationary solutions at several rates.
try:
 import numpy as np
 from scipy.linalg import solve
 for n in (4,5,6,7):
  states=list(range(1,1<<n)); index={st:i for i,st in enumerate(states)}; msize=len(states)
  for rate in (.01,.5,1.,20.):
   Q=np.zeros((msize,msize))
   for k,st in enumerate(states):
    for i in range(n):
     if not (st>>i&1):continue
     for j in ((i-1)%n,(i+1)%n):
      dst=(st&~(1<<i))|(1<<j)
      if dst!=st:
       Q[index[dst],k]+=1;Q[k,k]-=1
    if st != (1<<n)-1:
     Q[index[(1<<n)-1],k]+=rate;Q[k,k]-=rate
   Q[-1,:]=1
   target=np.zeros(msize);target[-1]=1
   p=solve(Q,target,assume_a='gen')
   assert min(p)>-1e-9 and abs(sum(p)-1)<1e-8
   E=lambda ix:sum(p[k] for k,st in enumerate(states) if all(st>>i&1 for i in ix))
   d2=E((0,2))-E((0,))*E((2,))
   if n==4:
    assert abs(d2-float(C_far.subs(r,rate)))<1e-10
    d1=E((0,1))-E((0,))*E((1,))
    assert abs(d1-float(C_near.subs(r,rate)))<1e-10
   if rate==.01:assert d2<0
   if rate==20:assert d2>0
 print('PASS: independent stationary chains N=4..7 and four reset rates')
except ImportError:
 print('Independent finite-state numerical checks skipped (scipy/numpy not installed).')
