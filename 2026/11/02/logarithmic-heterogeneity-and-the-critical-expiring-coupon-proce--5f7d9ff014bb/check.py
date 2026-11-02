"""Independent finite arithmetic and numerical checks for the critical expiring-coupon law."""
import math
import itertools
import numpy as np
import mpmath as mp
from scipy.linalg import expm

checks=0
for n in range(2,5):
  for M in range(n, min(n+4,8)):
    wins=0
    for w in itertools.product(range(n), repeat=M+1):
      if len(set(w[:M]))<n and len(set(w[1:]))==n:
        wins+=1
    st=[[0]*(n+1) for _ in range(M)]
    st[0][0]=1
    for a in range(1,M):
      for b in range(1,min(a,n)+1):
        st[a][b]=st[a-1][b-1]+b*st[a-1][b]
    predicted=n*(n-1)*math.factorial(n-1)*st[M-1][n-1]
    assert wins==predicted, (n,M,wins,predicted)
    checks+=1
mp.mp.dps=45
for lv in ['0.2','1','2']:
  lam=mp.mpf(lv)
  alpha=mp.quad(lambda y:(mp.exp(lam*y)-1)/y if y else lam,[0,1])
  assert abs(alpha - (mp.ei(lam)-mp.euler-mp.log(lam)))<mp.mpf('1e-40')
  checks+=1
  h=[]
  for k in range(8):
    if k==0:h.append(mp.mpf(0))
    else: h.append(mp.quad(lambda y:mp.exp(lam*y)*(1-(1-y)**k)/y if y else k,[0,1]))
  for k in range(1,7):
    gen=lam*(h[k+1]-h[k])+k*(h[k-1]-h[k]);assert abs(gen+1)<mp.mpf('1e-38')
    checks+=1
  q=mp.mpf('0.7')
  D=mp.quad(lambda y:y**(q-1)*mp.exp(-lam*(1-y)),[0,1])
  f=[mp.quad(lambda y:y**(q-1)*(1-y)**k*mp.exp(-lam*(1-y)),[0,1])/D for k in range(30)]
  assert abs(f[0]-1)<mp.mpf('1e-40');checks+=1
  for k in range(1,5):
    assert 0<f[k]<1;checks+=1
  partial=sum(mp.exp(-lam)*lam**k/mp.factorial(k)*f[k] for k in range(30))
  closed=mp.exp(-lam)*mp.quad(lambda y:y**(q-1)*(1-mp.exp(-lam*(1-y))),[0,1])/D
  assert abs(partial - (mp.exp(-lam)+closed)) <mp.mpf('1e-25');checks+=1
  # Critical-window mean of limit law. At large positive c this tends to Euler constant.
  c=-mp.log(lam)
  m=c-mp.e1(lam)+alpha
  assert mp.isfinite(m);checks+=1

# Direct finite simulation of the one-sided last-M collector and CTMC hitting distribution.
def ctmc_cdf(lam,dt,K=35):
  Q=np.zeros((K+1,K+1),float)
  for j in range(1,K+1):
    Q[j,j-1]=j
    if j<K:Q[j,j+1]=lam
    Q[j,j]=-(j+(lam if j<K else 0))
  probs=np.array([math.exp(-lam)*lam**j/math.factorial(j) for j in range(K+1)],float)
  return probs@expm(Q*dt)[:,0]

rng=np.random.default_rng(41021)
n=350;c=0;M=round(n*math.log(n)+c*n)
rep=900
hit=[]
for r in range(rep):
  last=np.full(n,-1,dtype=int)
  count=0
  finish=None
  max_steps= M+4000
  for k in range(max_steps):
    x=int(rng.integers(n))
    begin=max(0,k-M+1)
    was=(last[x]>=begin)
    # O(1) counter update, using a circular queue
    if k==0: ring=np.empty(M,dtype=np.int32)
    if k>=M:
      old=int(ring[k%M])
      if last[old]==k-M:
        count-=1
    if not was:count+=1
    ring[k%M]=x
    last[x]=k
    if count==n:
      finish=k+1
      break
  hit.append((finish-n*math.log(n))/n if finish is not None else float('inf'))
for s in (0,1,2):
  emp=np.mean(np.asarray(hit)<=s)
  theo=(math.exp(-1) if s==0 else ctmc_cdf(1,s))
  assert abs(emp-theo)<0.095,(s,emp,theo)
  checks+=1
print('PASS assertions:',checks)
print('Finite simulation n=350, reps=900:')
for s in (0,1,2):
 print(' s=',s,'empirical=',np.mean(np.asarray(hit)<=s),'critical law=',math.exp(-1) if s==0 else ctmc_cdf(1,s))
print('Limit mean at c=0:', mp.nstr(-mp.e1(1)+mp.ei(1)-mp.euler,16))

# Heterogeneous logarithmic-tilt regime; exactly normalized plus/minus profile.
a=1.0
kappa=math.cosh(a)
n=350;M=round(n*math.log(n));pplus=(1+a/math.log(n))/2
rng=np.random.default_rng(34134)
he=[]
for rep in range(650):
  last=np.full(n,-1,dtype=int); ring=np.empty(M,dtype=np.int32); count=0;finish=None
  for k in range(M+4500):
    x=int(rng.integers(n//2))+(0 if rng.random()<pplus else n//2)
    begin=max(0,k-M+1)
    was=last[x]>=begin
    if k>=M:
      old=int(ring[k%M])
      if last[old]==k-M:count-=1
    if not was:count+=1
    ring[k%M]=x;last[x]=k
    if count==n:
      finish=k+1;break
  he.append((finish-n*math.log(n))/n if finish is not None else float('inf'))
for s in (0,1,2):
  p=np.mean(np.asarray(he)<=s)
  theory=math.exp(-kappa) if s==0 else ctmc_cdf(kappa,s)
  assert abs(p-theory)<0.11,(s,p,theory)
  checks+=1
print('Heterogeneous critical checks:')
for s in (0,1,2):
 print(' s=',s,'empirical=',np.mean(np.asarray(he)<=s),'critical law=', math.exp(-kappa) if s==0 else ctmc_cdf(kappa,s))
print('kappa cosh(1)=',kappa)
print('PASS assertions total:',checks)
