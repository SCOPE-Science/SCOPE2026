#!/usr/bin/env python3
"""Exact GF(25) census for the characteristic-five Ciani family.

Arithmetic uses F5[v]/(v*v-2). No external packages.
"""
from collections import Counter
P=5
E=range(25)
def elem(a,b=0):return (a%5)+5*(b%5)
def add(x,y):return elem((x%5)+(y%5),x//5+y//5)
def neg(x):return elem(-(x%5),-(x//5))
def mul(x,y):
    a,b=x%5,x//5;c,d=y%5,y//5
    return elem(a*c+2*b*d,a*d+b*c)
def sub(x,y):return add(x,neg(y))
def power(x,n):
    z=1
    while n:
        if n&1:z=mul(z,x)
        x=mul(x,x);n//=2
    return z
TWO=2;FOUR=4
def smooth(r,s,t):
    if any(v in (2,3) for v in (r,s,t)):return False
    D=sub(sub(add(add(mul(r,r),mul(s,s)),mul(t,t)),mul(mul(r,s),t)),FOUR)
    return D!=0
def hw(r,s,t):
    R=mul(r,r);S=mul(s,s);T=mul(t,t);z=mul(mul(r,s),t)
    # Coefficients of x^8 y^4 z^4, x^4 y^8 z^4, x^4 y^4 z^8 in F^4.
    a=add(add(add(add(mul(R,T),mul(TWO,R)),sub(S,z)),mul(TWO,T)),TWO)
    b=add(add(add(add(mul(R,S),mul(TWO,R)),sub(T,z)),mul(TWO,S)),TWO)
    c=add(add(add(add(mul(S,T),mul(TWO,S)),sub(R,z)),mul(TWO,T)),TWO)
    return a,b,c
counts=Counter();bad=0;S=[]
for r in E:
 for s in E:
  for t in E:
   if not smooth(r,s,t):bad+=1;continue
   z=sum(a!=0 for a in hw(r,s,t))
   counts[z]+=1
   if z==0:S.append((r,s,t))
assert bad==3942, (bad,counts)
assert counts==Counter({0:8,1:96,2:1110,3:10469}),counts
roots=[a for a in E if sub(add(sub(power(a,4),power(a,3)),TWO),0)==0 and a not in (2,3)]
assert len(roots)==2, roots
expected=set()
for a in roots:
 for signs in [(1,1,1),(1,4,4),(4,1,4),(4,4,1)]:
  expected.add(tuple(mul(a,e) for e in signs))
assert set(S)==expected,(S,expected)
assert all(a//5!=0 for a in roots)
assert len(S)==8
# Quotient elliptic Hasse polynomial (r²-4)Y^4+(2rt-4s)Y²+(t²-4).
for r in E:
 for s in E:
  for t in E:
   A=sub(mul(r,r),4);B=sub(mul(2,mul(r,t)),mul(4,s));C=sub(mul(t,t),4)
   hq=add(mul(B,B),mul(2,mul(A,C)))
   assert hq==hw(r,s,t)[0]
print('VERIFY_OK',dict(sorted(counts.items())),'smooth',sum(counts.values()),'singular',bad,'roots',roots)
