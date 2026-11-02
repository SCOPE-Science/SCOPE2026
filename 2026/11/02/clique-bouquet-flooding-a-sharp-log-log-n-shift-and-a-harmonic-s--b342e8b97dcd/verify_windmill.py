#!/usr/bin/env python3
"""Independent exact and numerical checks for exponential edge-weighted flooding on clique bouquets.
Standard library only.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, comb, exp, log
import itertools
import random
import heapq

checks=0

def check(cond,label):
 global checks
 checks+=1
 if not cond: raise AssertionError(label)

def rates(m):
 return [k*(m+1-k) for k in range(1,m+1)]

def exact_m2_max_mean(n):
 return sum(((-1)**(j+1))*F(comb(n,j),2)*sum(F(comb(j,k)*factorial(k),j**(k+1)) for k in range(j+1)) for j in range(1,n+1))

def exact_m2_extra(q):
 return sum(((-1)**j)*F(comb(q,j),2)*sum(F(comb(j,k)*factorial(k),(j+1)**(k+1)) for k in range(j+1)) for j in range(0,q+1))

def exact_m2_leaf_mean(n):
 return exact_m2_max_mean(n-1)+F(3,4)+F(1,2)*exact_m2_extra(n-1)

def exact_ctmc_mean(n,m,from_leaf):
 N=n*m+1
 adj=[set() for _ in range(N)]
 for i in range(n):
  vs=list(range(1+i*m,1+(i+1)*m))
  for v in vs: adj[0].add(v);adj[v].add(0)
  for u,v in itertools.combinations(vs,2):adj[u].add(v);adj[v].add(u)
 masks=[sum(1<<v for v in adj[u]) for u in range(N)]
 allmask=(1<<N)-1
 @lru_cache(None)
 def E(mask):
  if mask==allmask:return F(0)
  weights=[(u, (mask & masks[u]).bit_count()) for u in range(N) if not ((mask>>u)&1)]
  rate=sum(w for _,w in weights)
  return F(1,rate)+sum(F(w,rate)*E(mask | (1<<u)) for u,w in weights if w)
 return E(2 if from_leaf else 1)

# Exact independent whole-graph CTMC and distinct compartment calculation.
for n in range(1,5):
 hub=exact_ctmc_mean(n,2,False)
 leaf=exact_ctmc_mean(n,2,True)
 check(hub==exact_m2_max_mean(n),f'CTMC hub n={n}: {hub} vs {exact_m2_max_mean(n)}')
 check(leaf==exact_m2_leaf_mean(n),f'CTMC leaf n={n}: {leaf} vs {exact_m2_leaf_mean(n)}')
 print('exact m=2',n,'hub',hub,'leaf',leaf)

# Exact first-hit-to-hub times as independent birth/death recursion.
for m in range(1,61):
 r=rates(m)
 h=F(0)
 for k in range(m,0,-1):
  h=F(1,r[k-1])+F(m-k,m+1-k)*h
 harmonic=sum(F(1,k) for k in range(1,m+1))
 check(h==harmonic/m,f'hub hit mean m={m}')
 # Tail spectral coefficient independent telescoping verification.
 product=F(1)
 for k in range(2,m): product*=F(r[k-1],r[k-1]-m)
 if m>=2: check(product==F((m-1)**2),f'double pole prefactor m={m}')

# Independent numerical survival probabilities via phase-type uniformization.
def survival_uniformized(m,t):
 r=rates(m)
 rate=max(r)
 # If rate*t high, start at 0 Poisson and update until tolerance; used only moderate t.
 z=rate*t
 w=exp(-z)
 probs=[1.0]+[0.0]*m
 survival=0.0
 for k in range(0,max(400,int(z+20*(z+1)**0.5))):
  survival+=w*sum(probs[:-1])
  new=probs[:]
  for j in range(m):
   step=probs[j]*r[j]/rate
   new[j]-=step
   new[j+1]+=step
  probs=new
  w*=z/(k+1) if k+1 else 1
  if k>z+12*(z+1)**0.5 and w<1e-20:break
 return survival
for t in (0.1,0.4,1.0,2.5,5.0,8.0):
 for m in (2,3,4,5,6):
  s=survival_uniformized(m,t)
  check(-1e-12<=s<=1+1e-12,f'phase cdf range m={m},t={t}')
  if m==2: exact=exp(-2*t)*(1+2*t)
  elif m==3: exact=(12*t-8)*exp(-3*t)+9*exp(-4*t)
  else: continue
  check(abs(s-exact)<1e-11,f'phase cdf m={m},t={t}: {s} versus {exact}')
  print('tail',m,t,round(s,10))

# Asymptotic coefficient at t=8..12 for m<=5, numerically stable.
for m in (2,3,4,5):
 for t in (8.,10.,12.):
  s=survival_uniformized(m,t)
  target=m*(m-1)**2*t*exp(-m*t)
  check(0.5<s/target<1.5, f'tail leading m={m},t={t},ratio={s/target}')

# Dijkstra simulations from original edge law to contrast finite compartment formula.
def sample_fpp(n,m,leaf,rng):
 N=n*m+1
 adj=[[] for _ in range(N)]
 for i in range(n):
  vs=list(range(1+i*m,1+(i+1)*m))
  for u,v in [(0,v) for v in vs]+list(itertools.combinations(vs,2)):
   w=rng.expovariate(1.)
   adj[u].append((v,w)); adj[v].append((u,w))
 start=int(bool(leaf))
 d=[float('inf')]*N;d[start]=0.
 pq=[(0.,start)]
 while pq:
  dist,u=heapq.heappop(pq)
  if dist!=d[u]:continue
  for v,w in adj[u]:
   if dist+w<d[v]:d[v]=dist+w;heapq.heappush(pq,(dist+w,v))
 return max(d)

rng=random.Random(314159265)
for n in (2,3,5):
 for leaf in (False,True):
  trials=30000
  samples=[sample_fpp(n,2,leaf,rng) for _ in range(trials)]
  empirical=sum(samples)/trials
  exact=float(exact_m2_leaf_mean(n) if leaf else exact_m2_max_mean(n))
  variance=sum((x-empirical)**2 for x in samples)/trials
  tolerance=6*(variance/trials)**0.5+0.015
  check(abs(empirical-exact)<tolerance,f'dijkstra mean n={n},leaf={leaf}: {empirical}/{exact}, tolerance={tolerance}')
  print('dijkstra',n,'leaf',leaf,'observed',round(empirical,4),'exact',round(exact,4))
print('PASS',checks,'exact/numerical tests')
