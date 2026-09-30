#!/usr/bin/env python3
from itertools import combinations
from math import comb


def bad_triple_masks(n,m):
    # 0 hub; petal index for outer vertex v is (v-1)//m
    N=1+n*m
    bad=[]
    for a,b,c in combinations(range(N),3):
        triple=(a,b,c)
        # A triple fails GP iff hub and vertices from two different petals are all selected.
        if 0 in triple:
            ou=[v for v in triple if v]
            if (ou[0]-1)//m != (ou[1]-1)//m:
                bad.append((1<<a)|(1<<b)|(1<<c))
    return N,bad


def formula(n,m):
    N=n*m
    a=[comb(N,k) for k in range(N+1)]
    a[1]+=1
    for j in range(1,m+1):
        a[j+1]+=n*comb(m,j)
    return a


def unimodal(a):
    i=0
    while i+1<len(a) and a[i]<=a[i+1]: i+=1
    while i+1<len(a) and a[i]>=a[i+1]: i+=1
    return i==len(a)-1

checked=0
for n in range(2,4):
    for m in range(1,3):
        N,bad=bad_triple_masks(n,m)
        counts=[0]*N
        for mask in range(1<<N):
            ok=True
            for b in bad:
                if mask & b == b:
                    ok=False; break
            if ok: counts[mask.bit_count()]+=1
        f=formula(n,m)
        assert counts==f,(n,m,counts,f)
        checked+=1

for n in range(2,31):
  for m in range(1,31):
    a=formula(n,m); assert unimodal(a),(n,m)
    N=n*m
    if m>=2 and n>=3:
      for k in range(2,m+1):
        if 2*k>m+1:
          L=n**(k-1)*(N-2*k-1)*(m-k+1)
          R=(k+1)*(2*k-m-1)
          assert L>=R,(n,m,k,L,R)
      k=m+1
      if k < N//2:
        assert comb(N,k+1)-comb(N,k)>=n,(n,m,'boundary')
    if m>=2 and n==2:
      for k in range(2,m):
        if 2*k>m+1:
          L=2**(k-1)*(2*m-2*k-1)*(m-k+1)
          R=(k+1)*(2*k-m-1)
          assert L>=R,(m,k,L,R)
print('VERIFY_OK')
print('exhaustive_parameter_pairs=',checked)
print('arithmetic_sweep_n=2..30_m=1..30')
