#!/usr/bin/env python3
"""Exact finite polynomial certificate for five-term truncated two-block partition positivity."""
from math import lcm,comb
import hashlib

N=5
L=lcm(*(2*j for j in range(1,11)))
S=((3,1),(6,-1),(10,-3),(15,3),(21,6))

# Method I: direct polynomial products.
a=[1]
for j in range(1,11):
    e=2*j; deg=len(a)-1
    b=[0]*(deg+L-e+1)
    for k in range(len(b)):
        b[k]=(a[k] if k<=deg else 0)+(b[k-e] if k>=e else 0)-(a[k-L] if 0<=k-L<=deg else 0)
    o=2*j-1
    a=[(b[k] if k<len(b) else 0)+(b[k-o] if 0<=k-o<len(b) else 0) for k in range(len(b)+o)]
h=[0]*(len(a)+21)
for e,c in S:
    for k,v in enumerate(a):h[k+e]+=c*v
assert len(h)==50412
assert min(h)==0
assert [i for i,x in enumerate(h) if x==0]==[0,1,2,26,30]

# Method II: partition dynamic programming + period-step finite difference.
D=len(h)-1
f=[0]*(D+1);f[0]=1
for j in range(1,11):
    odd=2*j-1;even=2*j
    for n in range(D,odd-1,-1): f[n]+=f[n-odd]
    for n in range(even,D+1): f[n]+=f[n-even]
b=[sum(c*f[n-e] for e,c in S if n>=e) for n in range(D+1)]
h2=[sum((-1)**k*comb(10,k)*b[n-k*L] for k in range(11) if n>=k*L) for n in range(D+1)]
assert h==h2
assert [i for i,z in enumerate(b[:5041]) if z==0]==[0,1,2,26,30]
# Infinite P/P10 has nonnegative coefficients and contains q^21, so its
# coefficient at n=26 and 30 is positive via b_5 and b_9 respectively.
assert b[5]>0 and b[9]>0
for n in range(3,21):
    # Cross-check signed combinatorial definition with the finite product.
    v=0
    for x in range(1,n):
        for y in range(x+1,n):
            for r in range((n//x+1)//2):
                for s in range((n//y+1)//2):
                    if (2*r+1)*x+(2*s+1)*y==n:v+=(-1)**(r+s)
    # Only when n<=20, unrepresented factors start at 21.
    assert v==b[n],(n,v,b[n])
print('CERTIFICATE_PASS N=5 L=',L,'degree=',D,'nonzero=',sum(bool(x) for x in h),
    'zero_indices=',[i for i,x in enumerate(h) if x==0],
    'initial=',b[:40], 'max_digits=',len(str(max(h))))
print('H_SHA256',hashlib.sha256(','.join(map(str,h)).encode()).hexdigest())
