#!/usr/bin/env python3
"""Independent exact small-digit census and finite spectral check."""
from math import gcd
from cmath import exp,pi
A=set(range(10))-{1}
expected={
 2:(31,13,7,3,1,7),
 3:(260,122,48,21,11,58),
 4:(2130,1111,383,169,87,380),
 5:(17626,9999,3073,1363,691,2500),
 6:(147446,89987,24575,10942,5476,16466),
}
def classify(n):
 ds=set(map(int,str(n)))
 if any(d in ds and n%d==0 for d in range(1,10)):
  return None
 if gcd(n,210)==1:return 0
 if 2 not in ds and n%2==0 and n%4!=0 and gcd(n,105)==1:return 1
 if 3 not in ds and n%3==0 and n%9!=0 and gcd(n,70)==1:return 2
 if 7 not in ds and n%7==0 and gcd(n,30)==1:return 3
 assert 1 not in ds
 assert len(({2,3,4,5,6,7,8,9}-ds))>=2,(n,ds)
 return 4
for k,expct in expected.items():
 cnt=[0]*5
 for n in range(10**(k-1),10**k):
  c=classify(n)
  if c is not None:cnt[c]+=1
 got=(sum(cnt),)+tuple(cnt)
 assert got==expct,(k,got,expct)
 print('k',k,'U,E,F2,F3,F7,R',got)
for B,q in [(A,21),(A-{2},21),(A-{3},63),(A-{7},21)]:
 theta=max(abs(sum(exp(2j*pi*t*d/q) for d in B)) for t in range(1,q))
 assert theta<8-1e-7, (B,q,theta)
 print('alphabet', ''.join(str(x) for x in sorted(B)), 'modulus',q, 'theta',round(theta,8))
print('VERIFY_OK')
