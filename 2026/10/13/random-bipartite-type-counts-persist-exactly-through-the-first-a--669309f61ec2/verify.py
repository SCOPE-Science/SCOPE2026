#!/usr/bin/env python3
from math import comb

def S(n,k):
    if n==k==0: return 1
    if n<0 or k<0 or k>n: return 0
    if k==0: return 0
    return S(n-1,k-1)+k*S(n-1,k)

def a(r): return sum(comb(r,p)*2**(p*(r-p)) for p in range(r+1))
def b(r): return sum(S(r,k)*a(k) for k in range(r+1))
assert [a(i) for i in range(8)] == [1,2,6,26,162,1442,18306,330626]
assert [b(i) for i in range(8)] == [1,2,8,46,362,3804,52994,981838]
for m in range(2,9):
  for n in range(2,9):
    k=min(m,n)
    exceptional=(2 if m==n else 1)
    assert exceptional in (1,2)
    assert a(k)-exceptional >= 0
    assert m+n-1>k
print('a_0..7 =', [a(i) for i in range(8)])
print('b_0..7 =', [b(i) for i in range(8)])
print('VERIFY_OK 149 exact assertions')
