"""Exact independent enumeration of branch-free cyclic vertices in uniform random mappings."""
from collections import Counter
from itertools import product
from math import comb,exp, sqrt,pi
from fractions import Fraction as F

checks=0

def ck(z,label):
 global checks
 checks+=1
 if not z:raise AssertionError(label)

def cyclic_set(f):
 n=len(f);cyc=set();visited=set()
 for i in range(n):
  path=[];ix={};j=i
  while j not in visited and j not in ix:
   ix[j]=len(path);path.append(j);j=f[j]
  if j in ix:cyc.update(path[ix[j]:])
  visited.update(path)
 return cyc

def probs(n,r):
 if r==n:return [F(int(k==n)) for k in range(n+1)]
 m=r-1;L=n-r-1
 return [F(comb(m,k)*sum((-1)**j*comb(m-k,j)*(n-k-j)**L for j in range(m-k+1)),n**L) for k in range(m+1)]

for n in range(2,7):
 out={r:Counter() for r in range(1,n+1)}
 for f in product(range(n),repeat=n):
  roots=cyclic_set(f);ind=Counter(f)
  out[len(roots)][sum(ind[i]==1 for i in roots)]+=1
 for r in range(1,n+1):
  tot=sum(out[r].values());pv=probs(n,r)
  ck(sum(pv)==1,f'norm n={n},r={r}')
  for k,v in enumerate(pv):ck(v==F(out[r][k],tot),f'enum n={n},r={r},k={k}')
  if r<n:
   L=n-r-1
   for j in range(r+1):
    exact=F(1) if j==0 else (F(0) if j==r else F(r-j,r)*F((n-j)**L,n**L))
    lhs=sum(F(__import__('math').factorial(k),__import__('math').factorial(k-j))*pv[k] for k in range(j,r)) / F(__import__('math').factorial(r),__import__('math').factorial(r-j))
    ck(exact==lhs,f'joint void n={n},r={r},j={j}')

# Direct exact comparison with the compulsory-one-root multinomial representation.
for n in range(2,22):
 for r in range(1,n):
  m=r-1;L=n-r-1
  exact=probs(n,r)
  occ=[F(comb(m,k)*sum((-1)**j*comb(m-k,j)*(n-k-j)**L for j in range(m-k+1)),n**L) for k in range(m+1)]
  for a,b in zip(exact,occ):ck(a==b,f'occupancy n={n},r={r}')

# Normalization and mean-scale predictions do not constitute the infinite-limit proof.
for n in [100,1000,10000]:
 for x in [0.25,0.7,1.4,2.8]:
  r=max(1,round(x*sqrt(n)));L=n-r-1
  mu=(r-1)*(1-1/n)**L
  ck(abs(mu-r/exp(1)) < 1+20*x*x,f'mean n={n},r={r}')
print('PASS',checks,'exact mapping enumerations, moments and occupancy comparisons')
