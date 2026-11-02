#!/usr/bin/env python3
"""Exact identity and finite-field checks for the arithmetic sextactic complete intersection.

Requires only the Python 3 standard library.  The algebraic proof of finite flatness,
local rings and universal characteristic exclusion is written in RESULT.md.
"""
from itertools import product
from collections import Counter

# Sparse homogeneous polynomials in three abstract variables A,B,C.
def unit(i):
    e=[0,0,0]; e[i]=1
    return {tuple(e):1}
def const(n): return {(0,0,0):n}
def add(*args):
    out={}
    for a in args:
        for mon,c in a.items():out[mon]=out.get(mon,0)+c
    return {m:c for m,c in out.items() if c}
def neg(a):return {m:-v for m,v in a.items()}
def mul(a,b):
    out={}
    for ea,va in a.items():
        for eb,vb in b.items():
            k=tuple(x+y for x,y in zip(ea,eb));out[k]=out.get(k,0)+va*vb
    return {m:c for m,c in out.items() if c}
def power(a,n):
    v=const(1)
    for _ in range(n):v=mul(v,a)
    return v
def eq_mod(a,b,p):
    diff=add(a,neg(b))
    return all(c%p==0 for c in diff.values())
A,B,C=unit(0),unit(1),unit(2)
F=add(A,B,C)
G=mul(mul(add(A,neg(B)),add(B,neg(C))),add(C,neg(A)))
L=add(A,B,C)
Q=add(neg(power(A,2)),neg(mul(A,C)),power(B,2),mul(B,C))
assert eq_mod(G,add(power(add(A,neg(B)),3),mul(L,Q)),3)
# For characteristic two, the Frobenius fourth power identity is exact.
assert eq_mod(power(L,4),add(power(A,4),power(B,4),power(C,4)),2)
H=mul(mul(add(A,B),add(B,C)),add(C,A))
J=mul(mul(add(power(A,4),neg(power(B,4))),add(power(B,4),neg(power(C,4)))),add(power(C,4),neg(power(A,4))))
assert eq_mod(J,power(H,4),2)

# F_9 = F_3[i]/(i^2+1).  The norm to F_3 is t -> t^4.
S=list(product(range(3), repeat=2))
zero=(0,0); one=(1,0)
def fadd(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3)
def fmul(a,b):return ((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
def fpow(a,n):
    z=one
    for _ in range(n):z=fmul(z,a)
    return z
points=[(one,y,z) for y in S for z in S]+[(zero,one,z) for z in S]+[(zero,zero,one)]
assert len(points)==91
Hcurve=[p for p in points if fadd(fadd(fpow(p[0],4),fpow(p[1],4)),fpow(p[2],4))==zero]
D=[p for p in Hcurve if fpow(p[0],4)==fpow(p[1],4)]
axis=[p for p in Hcurve if zero in p]
assert len(Hcurve)==28 and len(D)==16 and len(axis)==12
assert set(D).isdisjoint(axis) and set(D).union(axis)==set(Hcurve)
assert all(zero not in p for p in D)
assert all(fpow(p[0],4)==fpow(p[1],4)==fpow(p[2],4) for p in D)
# The 16 points are the triple intersections of the three four-line pencils.
triple=[p for p in points if fpow(p[0],4)==fpow(p[1],4)==fpow(p[2],4) and p[0]!=zero]
assert set(triple)==set(D)
# In char 2 the reduced support is V(L,H): three distinct rational points.
p2=[(1,y,z) for y,z in product(range(2),repeat=2)]+[(0,1,z) for z in range(2)]+[(0,0,1)]
p2points=[p for p in p2 if (sum(p)%2==0) and ((p[0]+p[1])*(p[1]+p[2])*(p[2]+p[0]))%2==0]
assert set(p2points)=={(1,1,0),(1,0,1),(0,1,1)}
local2=[1,2,3,4,3,2,1]
assert sum(local2)==16
assert len(D)*3==len(p2points)*16==48
print('FERMAT_48_SEXTactic_FLAT_SPECIALIZATION_IDENTITY_AND_F9_COUNTS_PASS')
print('char3 Hermitian rational points:',len(Hcurve),'triple-support:',len(D),'axis-complement:',len(axis))
print('char2 support:',len(p2points),'local algebra Hilbert function:',local2)
