#!/usr/bin/env python3
"""Independent exact-rational and asymptotic checks for a Poisson partial-reset gas."""
from fractions import Fraction as Q
from math import comb
from itertools import product

def phi(N,m,k,a):
    return 1-sum((Q(comb(k,h)*comb(N-k,m-h),comb(N,m)) * a**(2*h)
                  for h in range(max(0,m-(N-k)),min(k,m)+1)), Q(0))

def phi_direct(N,m,k,a):
    # Independent enumeration of subsets, not the hypergeometric formula.
    from itertools import combinations
    return sum((1-a**(2*len(set(S)&set(range(k))))
                for S in combinations(range(N),m)),Q(0))/comb(N,m)

def products(N,m,k,a,r,gamma,D):
    ds=[r*phi(N,m,j,a)-2*j*gamma for j in range(1,k+1)]
    if min(ds)<=0: return None
    out=Q(1)
    for j,d in enumerate(ds,1):out*=2*D*j/d
    return out

def pure(N,m,k,a,r,gamma,D):
    p=Q(m,N)
    ds=[r*p*(1-a**(2*j))-2*j*gamma for j in range(1,k+1)]
    if min(ds)<=0: return None
    out=Q(1)
    for j,d in enumerate(ds,1):out*=2*D*j/d
    odd=1
    for j in range(1,k+1):odd*=2*j-1
    return out*odd

num=0
for N in range(2,9):
 for m in range(1,N+1):
  for k in range(1,N+1):
   for a in (Q(1,4),Q(1,2),Q(3,4)):
    p=Q(m,N)
    assert phi(N,m,k,a)==phi_direct(N,m,k,a)
    F=[phi(N,m,j,a) for j in range(1,k+1)]
    assert all(F[j-1]/j >= F[j]/(j+1) for j in range(1,k))
    if k>1 and m<N:
      assert F[-1]>p*(1-a**(2*k))
    # Test stationary generator identity and pure-marginal recurrence.
    r=Q(5,3); D=Q(7,5); gam=Q(1,10)
    T=Q(1)
    S=Q(1)
    for j in range(1,k+1):
     tm=products(N,m,j,a,r,gam,D)
     if tm is not None:
      assert (r*phi(N,m,j,a)-2*j*gam)*tm ==2*D*j*T
      T=tm
     sm=pure(N,m,j,a,r,gam,D)
     if sm is not None:
      assert (r*p*(1-a**(2*j))-2*j*gam)*sm == (2*j)*(2*j-1)*D*S
      S=sm
    num+=1

# Exact positive band for distinct mixed moment finite but pure same-degree infinite.
for N in range(2,10):
 for m in range(1,N):
  for k in range(2,N+1):
   a=Q(3,5);r=Q(7,4);D=Q(1)
   p=Q(m,N)
   lower=r*p*(1-a**(2*k))/(2*k)
   upper=r*phi(N,m,k,a)/(2*k)
   assert upper>lower
   gamma=(lower+upper)/2
   assert products(N,m,k,a,r,gamma,D) is not None
   assert pure(N,m,k,a,r,gamma,D) is None
   assert r*p*(1-a**2)>2*gamma
   num+=1

# Critical-window limits and strict thresholds away from boundaries.
for N,m,k in [(4,1,3),(5,2,4),(6,3,4),(6,6,3)]:
 p=Q(m,N);q=Q(m*(m-1),N*(N-1));u=q/p
 lam=Q(3,2);D=Q(2)
 K=Q(1,2)+(k-1)*u+Q(2)
 target=(2*D/lam)**k
 for j in range(1,k+1):target/=2*K-1-2*(j-1)*u
 vals=[]
 for denom in [100,1000,10000,100000]:
  s=Q(1,denom); a=1-s;r=lam/(p*s);gamma=lam*(1-K*s)
  vals.append(float(s**k*products(N,m,k,a,r,gamma,D)))
 assert abs(vals[-1]/float(target)-1)<2e-4,(N,m,k,vals,target)
 num+=1
print('PASS:',num,'exact-combinatorial/recurrence/strict-moment-gap cases and four critical-window checks')
