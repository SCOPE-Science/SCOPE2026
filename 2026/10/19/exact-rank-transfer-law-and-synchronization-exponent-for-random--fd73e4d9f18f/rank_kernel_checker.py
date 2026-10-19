#!/usr/bin/env python3
"""Exact transfer-kernel verification for random products of finite-set retractions."""
from math import comb
from itertools import product
from collections import Counter
from fractions import Fraction

def cov(m,c,k):
    return sum((-1)**j*comb(k,j)*(c+k-j)**m for j in range(k+1))

def kernel(n):
    K=[[0]*(n+1) for _ in range(n+1)]
    for r in range(1,n+1):
        for u in range(1,n+1):
            for c in range(max(0,r+u-n),min(r,u)+1):
                for v in range(1,r+1):
                    k=v-c
                    if 0<=k<=min(r-c,u-c):
                        K[r][v]+=comb(r,c)*comb(n-r,u-c)*u**(n-r-u+c)*comb(u-c,k)*cov(r-c,c,k)
    return K

def get_direct(n):
    E=[]
    for f in product(range(n),repeat=n):
        if all(f[f[i]]==f[i] for i in range(n)):
            E.append(f)
    return E

def times(K,n,m):
    p=[0]*(n+1);p[n]=1
    for _ in range(m):
        p=[sum(p[r]*K[r][v] for r in range(1,n+1)) for v in range(n+1)]
    return p

def expected_time(K,n):
    E=sum(K[1]); T=[Fraction(0)]*(n+1)
    for r in range(2,n+1):
       T[r]=(E+sum(K[r][v]*T[v] for v in range(1,r)))/(E-K[r][r])
    return T[n]

if __name__=='__main__':
  for n in range(1,7):
    K=kernel(n); E=get_direct(n);N=len(E)
    for r in range(1,n+1):
        expected=Counter(len({f[i] for i in range(r)}) for f in E)
        assert {v:K[r][v] for v in range(1,n+1) if K[r][v]}==expected, (n,r,expected,K[r])
        assert sum(K[r])==N
    assert all(K[r][r]>K[r+1][r+1] for r in range(1,n))
    expected_rank=Counter(len(set(f)) for f in E)
    assert {v:times(K,n,1)[v] for v in range(1,n+1) if times(K,n,1)[v]}==expected_rank
    if n<=4:
      # Independent exhaustive pairs; the two-step distribution must agree.
      ct=Counter(len({f[g[i]] for i in range(n)}) for f in E for g in E)
      assert dict(ct)=={v:times(K,n,2)[v] for v in range(1,n+1) if times(K,n,2)[v]}
      trip=Counter((len(set(g)),len(set(f)),len({f[g[i]] for i in range(n)})) for f in E for g in E)
      assert sum(trip.values())==N*N
      if n==4:
        assert trip[2,3,1]==48 and trip[3,2,1]==36
        assert trip[2,3,2]==240 and trip[3,2,2]==252
        print('FIRST_DIRECTIONAL_ASYMMETRY',trip[2,3,1],trip[3,2,1])
    if n>=2:
      print('PASS',n,'#idempotents',N,'kernel_diagonal',[K[r][r] for r in range(1,n+1)],
            'lambda',Fraction(K[2][2],N),'E_tau',expected_time(K,n))
    else:print('PASS',n,'absorbed initially')
  for n in (7,9,12):
    K=kernel(n); N=sum(K[1]);
    assert all(sum(K[r])==N for r in range(1,n+1))
    assert all(K[r][r]>K[r+1][r+1] for r in range(1,n))
    print('SYMBOLIC',n,'lambda',Fraction(K[2][2],N),'two-step ranks',times(K,n,2))
  print('ALL_EXACT_CHECKS_PASSED')
