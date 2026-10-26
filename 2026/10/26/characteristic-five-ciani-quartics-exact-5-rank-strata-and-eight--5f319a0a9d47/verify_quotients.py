#!/usr/bin/env python3
"""Independent census using F5[w]/(w^2+w+1) and elliptic quotients.
No external dependencies. A zero quotient Hasse invariant gives 5-rank 0
for that elliptic quotient. The prime-to-5 Jacobian isogeny adds their ranks.
"""
from collections import Counter
values=range(25)
def pack(a,b=0):return a%5+5*(b%5)
def add(x,y):return pack(x%5+y%5,x//5+y//5)
def neg(x):return pack(-x%5,-(x//5))
def mul(x,y):
 a,b=x%5,x//5;c,d=y%5,y//5
 return pack(a*c-b*d,a*d+b*c-b*d)
def sub(x,y):return add(x,neg(y))
def mul3(a,b,c):return mul(mul(a,b),c)
def quadraticH(x,y,z):
    # Elliptic quotient v^2=(x^2-4)t^4+(2xy-4z)t^2+(y^2-4).
    A=sub(mul(x,x),4); B=sub(mul(2,mul(x,y)),mul(4,z)); C=sub(mul(y,y),4)
    return add(mul(B,B),mul(2,mul(A,C)))
def is_smooth(r,s,t):
    if r in (2,3) or s in (2,3) or t in (2,3):return False
    disc=sub(add(add(mul(r,r),mul(s,s)),mul(t,t)),add(mul3(r,s,t),4))
    return disc!=0
counts=Counter();zeros=[];simple=Counter()
for r in values:
 for s in values:
  for t in values:
   if not is_smooth(r,s,t):continue
   # Involutions changing the signs of x,y,z: quotients are genus one.
   q=(quadraticH(r,t,s),quadraticH(s,r,t),quadraticH(t,s,r))
   rank=sum(h!=0 for h in q)
   counts[rank]+=1
   if rank==0:zeros.append((r,s,t))
   if r<5 and s<5 and t<5:simple[rank]+=1
assert counts==Counter({0:8,1:96,2:1110,3:10469}),counts
assert simple==Counter({1:12,3:11}),simple
assert len(zeros)==8
assert all(any(x//5 for x in z) for z in zeros)
# Every superspecial curve has coefficients of equal squares.
for r,s,t in zeros:
 assert mul(r,r)==mul(s,s)==mul(t,t)
print('QUOTIENT_VERIFY_OK',dict(sorted(counts.items())),'F5',dict(sorted(simple.items())))
