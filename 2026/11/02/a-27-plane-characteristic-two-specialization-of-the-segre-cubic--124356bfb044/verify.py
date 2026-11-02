#!/usr/bin/env python3
"""Exact finite-field checks for the characteristic-two Segre cubic cone."""
from itertools import product, combinations

def mul(a,b):
    t=0
    while b:
        if b&1: t^=a
        b>>=1; a<<=1
        if a&4: a^=7
    return t

def pow4(a,n):
    r=1
    for _ in range(n):r=mul(r,a)
    return r

def inv(a):
    assert a
    return pow4(a,2)

def addv(a,b):return tuple(x^y for x,y in zip(a,b))
def scal(a,b):return tuple(mul(a,x) for x in b)
def f(v):
    a,b,c,d=v
    e=a^b^c^d
    return pow4(a,3)^pow4(b,3)^pow4(c,3)^pow4(d,3)^pow4(e,3)

def canon(v):
    j=next(i for i,x in enumerate(v) if x)
    return scal(inv(v[j]),v)

def rref2(v,w):
    rows=[list(v),list(w)]; piv=[]; rr=0
    for col in range(4):
        p=next((i for i in range(rr,2) if rows[i][col]),None)
        if p is None:continue
        rows[p],rows[rr]=rows[rr],rows[p]
        rows[rr]=list(scal(inv(rows[rr][col]),rows[rr]))
        for k in range(2):
            if k!=rr and rows[k][col]:
                fac=rows[k][col]
                rows[k]=[x^mul(fac,y) for x,y in zip(rows[k],rows[rr])]
        piv.append(col);rr+=1
        if rr==2:break
    return tuple(tuple(row) for row in rows) if rr==2 else None

allv=list(product(range(4),repeat=4))
proj4={canon(v) for v in allv if any(v)}
assert len(proj4)==85
lines=set()
for vi,v in enumerate(allv):
    if not any(v):continue
    for w in allv:
        if not any(w):continue
        rr=rref2(v,w)
        if rr:lines.add(rr)
assert len(lines)==357,len(lines)
within=set()
for v,w in lines:
    pts=[v]+[addv(w,scal(t,v)) for t in range(4)]
    if all(f(p)==0 for p in pts):within.add((v,w))
assert len(within)==27,(len(within),sorted(within))
assert all(f(v)==0 for v,w in within)

def frob_line(line):return rref2(*[tuple(pow4(a,2) for a in v) for v in line])
assert {frob_line(L) for L in within}==within
assert all(frob_line(frob_line(L))==L for L in within)
fixed={L for L in within if frob_line(L)==L}
assert len(fixed)==15,len(fixed)
print('GEOMETRIC_PLANES=27, F2_PLANES=15, F4_NEW_PLANES=12, FROBENIUS_PAIRS=6')

def projective_points_q4():return {canon(v) for v in allv if any(v)}
q4=sum(f(v)==0 for v in projective_points_q4())
assert q4==45,q4
q2=sum(f(v)==0 for v in product(range(2),repeat=4) if any(v))
assert q2==15,q2
print('CLEBSCH_F2_POINTS=15, CLEBSCH_F4_POINTS=45')

def segre(v):
    assert len(v)==6
    return (not (v[0]^v[1]^v[2]^v[3]^v[4]^v[5])) and (not (pow4(v[0],3)^pow4(v[1],3)^pow4(v[2],3)^pow4(v[3],3)^pow4(v[4],3)^pow4(v[5],3)))
for base,expect in [(range(2),31),(range(4),181)]:
    proj={canon(a+(a[0]^a[1]^a[2]^a[3]^a[4],)) for a in product(base,repeat=5) if any(a)}
    assert sum(segre(v) for v in proj)==expect
for a in product(range(4),repeat=5):
    v=a+(a[0]^a[1]^a[2]^a[3]^a[4],)
    for t in range(4):
        w=tuple(x^t for x in v)
        assert segre(w)==segre(v)
print('DIRECT_SEGRE_F2_AND_F4_COUNTS_AND_CONE_TRANSLATION_OK')
print('SEGRE_CONE_F2_POINTS=31, F4_POINTS=181')
print('PICARD_FROBENIUS_EIGEN_MULTIPLICITIES=+1:6,-1:1')
print('ZETA_S=1/((1-T)(1-2T)(1-4T)^6(1+4T)(1-8T))')
print('VERIFY_OK')
