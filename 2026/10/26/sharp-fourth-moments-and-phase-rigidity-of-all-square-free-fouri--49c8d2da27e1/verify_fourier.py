#!/usr/bin/env python3
"""Reproducible finite checks for a Fourier fourth-moment extremal identity.
Science-only code: finite examples and algebraic checks, not an infinite proof.
"""
from itertools import combinations, product
from math import comb, isclose
from fractions import Fraction
import random, cmath

count=0

def support(n,k):
    return list(combinations(range(n),k))

def sharp(n,k):
    N=comb(n,k)
    return Fraction(sum(comb(k,r)*comb(n-k,r)*comb(2*r,r)
                        for r in range(k+1) if r<=n-k),N)

def moment(coef,n,k):
    S=support(n,k)
    assert len(coef)==len(S)
    d={}
    for A,a in zip(S,coef):
      for B,b in zip(S,coef):
        u=tuple(int(j in A)+int(j in B) for j in range(n))
        d[u]=d.get(u,0)+a*b
    return sum(abs(v)**2 for v in d.values())

rng=random.Random(241018)
for n in range(2,10):
  for k in range(1,n):
    S=support(n,k);N=len(S)
    if N>100: continue
    ones=[Fraction(1)]*N
    observed=moment(ones,n,k)/N**2
    assert observed==sharp(n,k),(n,k,observed,sharp(n,k))
    count+=1
    for _ in range(6):
      c=[rng.randrange(0,5) for _ in S]
      if not any(c):continue
      val=moment(c,n,k); T=sum(x*x for x in c)
      assert val <= sharp(n,k)*T*T+Fraction(1,10**9), (n,k)
      count+=1
      # Transposition L2-balancing of nonnegative coefficient magnitudes.
      first,second=rng.sample(range(n),2)
      dd={s:i for i,s in enumerate(S)}
      b=list(c)
      for i,s in enumerate(S):
        if first in s and second not in s:
          t=tuple(sorted((set(s)-{first})|{second}));j=dd[t]
          average=(c[i]**2+c[j]**2)/2
          b[i]=b[j]=average**0.5
      assert moment(b,n,k)+1e-7 >= val, (n,k, val,moment(b,n,k))
      count+=1
    # Torus character modulations preserve exact equality, to numerical tolerance.
    phases=[rng.uniform(-2,2) for _ in range(n)]
    coef=[cmath.exp(1j*sum(phases[i] for i in s)) for s in S]
    assert isclose(moment(coef,n,k)/N**2,float(sharp(n,k)),rel_tol=1e-11)
    count+=1

# Pure coefficientwise matrix lemma in three coefficients (no unit tests on old work).
for _ in range(900):
  b=[rng.randrange(0,5) for _ in range(4)]
  c=[rng.randrange(0,5) for _ in range(4)]
  e=[((u*u+v*v)/2)**0.5 for u,v in zip(b,c)]
  def cv(a,d,t):return sum(a[i]*d[t-i] for i in range(len(a)) if 0<=t-i<len(d))
  for t in range(7):
    B2=cv(b,b,t); C2=cv(c,c,t); BC=cv(b,c,t); E2=cv(e,e,t)
    assert B2**2+C2**2+4*BC**2<=6*E2**2+1e-7,(b,c,t)
    count+=1
print('FINITE_CHECKS_PASSED',count)
print('C_8_3',sharp(8,3))
print('C_10_3',sharp(10,3))
