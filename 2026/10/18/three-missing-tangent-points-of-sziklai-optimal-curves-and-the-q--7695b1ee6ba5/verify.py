#!/usr/bin/env python3
"""Exact verification for the quartic X^4+Y^4+3Z^4 over F_5.
No external packages needed. Field F_625 = F_5[t]/(t^4-3).
"""
from collections import Counter
from itertools import product

P=5
ZERO=(0,0,0,0)
ONE=(1,0,0,0)
T=(0,1,0,0)

def add(a,b): return tuple((x+y)%P for x,y in zip(a,b))
def neg(a): return tuple(-x%P for x in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    tmp=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b): tmp[i+j]+=x*y
    for i in range(6,3,-1): tmp[i-4]+=3*tmp[i]
    return tuple(x%P for x in tmp[:4])
def powf(a,k):
    out=ONE
    while k:
        if k&1:out=mul(out,a)
        a=mul(a,a);k>>=1
    return out

def val(x): return (x%5,0,0,0)

def eq(a,b): return a==b

def normalize(v):
    first=next(x for x in v if x!=ZERO)
    factor=powf(first,623)
    return tuple(mul(x,factor) for x in v)

def frob(v):return normalize(tuple(powf(x,5) for x in v))

# C's 16 rational points, rational Gauss tangents, and incidence profile.
pts=set()
for x,y,z in product(range(5),repeat=3):
    if (x,y,z)==(0,0,0): continue
    v=(x,y,z)
    a=next(w for w in v if w)
    inv=pow(a,-1,5)
    pts.add(tuple((w*inv)%5 for w in v))
assert len(pts)==31
curve={v for v in pts if (v[0]**4+v[1]**4+3*v[2]**4)%5==0}
assert len(curve)==16 and all(all(x!=0 for x in v) for v in curve)
lines=set()
for x,y,z in curve:
    a=(4*x**3%5,4*y**3%5,12*z**3%5)
    inv=pow(next(w for w in a if w),-1,5)
    lines.add(tuple((w*inv)%5 for w in a))
assert len(lines)==16
incidence=Counter(sum(sum(u*v for u,v in zip(ell,p))%5==0 for ell in lines) for p in pts)
assert incidence=={0:3,3:16,4:12},incidence
assert {p for p in pts if all(sum(u*v for u,v in zip(ell,p))%5 for ell in lines)} == {(1,0,0),(0,1,0),(0,0,1)}

# The geometric bitangent lines in F_625. Let theta^4=3.
assert powf(T,4)==val(3)
assert powf(T,5)==mul(val(3),T)
roots1=[val(i) for i in range(1,5)]
roots3=[mul(val(i),T) for i in range(1,5)]
roots4=[mul(val(i),powf(T,2)) for i in range(1,5)]
roots2=[mul(val(i),powf(T,3)) for i in range(1,5)]
assert all(powf(t,4)==ONE for t in roots1)
assert all(powf(t,4)==val(3) for t in roots3)
assert all(powf(t,4)==val(4) for t in roots4)
assert all(powf(t,4)==val(2) for t in roots2)

ordinary={normalize((ONE,u,v)) for u in roots1 for v in roots3}
hyper_XY={normalize((ONE,neg(s),ZERO)) for s in roots4}
hyper_XZ={normalize((ONE,ZERO,neg(s))) for s in roots2}
hyper_YZ={normalize((ZERO,ONE,neg(s))) for s in roots2}
all_bits=ordinary|hyper_XY|hyper_XZ|hyper_YZ
assert (len(ordinary),len(hyper_XY),len(hyper_XZ),len(hyper_YZ),len(all_bits))==(16,4,4,4,28)

# Direct verify identity F(-uY-vZ,Y,Z)=2*(u^2Y^2+uvYZ+v^2Z^2)^2
# as homogeneous quartics in Y and Z for all 16 ordinary lines.
from math import comb
for ell in ordinary:
    _,u,v=ell
    lhs=[add(add(mul(val(comb(4,j)),mul(powf(u,4-j),powf(v,j))),val(1 if j==0 else 0)),val(3 if j==4 else 0)) for j in range(5)]
    a=powf(u,2);b=mul(u,v);c=powf(v,2)
    sq=[mul(val(2),z) for z in (mul(a,a),mul(val(2),mul(a,b)),add(mul(b,b),mul(val(2),mul(a,c))),mul(val(2),mul(b,c)),mul(c,c))]
    assert lhs==sq,(ell,lhs,sq)

# Hyperflex restriction: e.g. X=sY => (s^4+1)Y^4+3Z^4=3Z^4.
for s in roots4:assert add(powf(s,4),ONE)==ZERO
for s in roots2:assert add(powf(s,4),val(3))==ZERO

# Galois cycles of arithmetic Frobenius on the 28 lines.
assert {frob(ell) for ell in all_bits}==all_bits
left=set(all_bits)
cycles=[]
while left:
    v=next(iter(left));cyc=[]
    while v not in cyc:
        cyc.append(v);left.remove(v);v=frob(v)
    assert v==cyc[0]
    cycles.append(cyc)
cycle_dist=Counter(map(len,cycles))
assert cycle_dist=={2:2,4:6},cycle_dist
assert all(frob(ell)!=ell for ell in all_bits)
assert sum(len(c) for c in cycles)==28
assert len({frob(frob(ell)) for ell in all_bits if frob(frob(ell))==ell})==4

if __name__=='__main__':
    print('curve_rational_points:',len(curve))
    print('distinct_rational_tangent_lines:',len(lines))
    print('rational_incidence_profile:',dict(sorted(incidence.items())))
    print('geometric_bitangents:',len(all_bits))
    print('ordinary_bitangents:',len(ordinary))
    print('hyperflex_lines:',len(hyper_XY|hyper_XZ|hyper_YZ))
    print('frobenius_cycle_lengths:',dict(sorted(cycle_dist.items())))
    print('bitangents_over_F5:',sum(1 for ell in all_bits if frob(ell)==ell))
    print('bitangents_over_F25:',sum(1 for ell in all_bits if frob(frob(ell))==ell))
    print('bitangents_over_F625:',len(all_bits))
    print('ALL_CHECKS_PASS')
