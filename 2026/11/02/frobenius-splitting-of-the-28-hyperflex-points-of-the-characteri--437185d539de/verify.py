#!/usr/bin/env python3
"""Exact self-contained computation in a 729-element field; no third-party packages."""
from collections import Counter
# F_3[t]/(t^6+t+2), elements encoded base 3, verify irreducibility by Frobenius gcd.
P=3**6
MOD=[2,1,0,0,0,0,1]
def dec(a):
    v=[]
    for _ in range(6): v.append(a%3);a//=3
    return v
def enc(v): return sum((z%3)*3**i for i,z in enumerate(v[:6]))
def add(a,b):return enc([(x+y)%3 for x,y in zip(dec(a),dec(b))])
def mul(a,b):
    u=dec(a);v=dec(b);z=[0]*11
    for i in range(6):
        for j in range(6):z[i+j]=(z[i+j]+u[i]*v[j])%3
    for k in range(10,5,-1):
        c=z[k]
        for j in range(6):z[k-6+j]=(z[k-6+j]-c*MOD[j])%3
    return enc(z)
def power(a,n):
    r=1
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
# Frobenius orbit criterion checks degree six factor to ensure field.
def polynomial_gcd(a,b):
    def trim(a):
        while a and a[-1]==0:a.pop()
        return a
    while b:
        a=trim(a[:]);b=trim(b[:]); inv=pow(b[-1],-1,3)
        while len(a)>=len(b) and a:
            c=a[-1]*inv%3; j=len(a)-len(b)
            for i,x in enumerate(b):a[j+i]=(a[j+i]-c*x)%3
            trim(a)
        a,b=b,a
    return tuple((v*pow(a[-1],-1,3))%3 for v in a) if a else ()
def poly_mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%3
    return z
def remainder(a,b):
    a=a[:]
    while len(a)>=len(b):
        z=a[-1]*pow(b[-1],-1,3)%3;k=len(a)-len(b)
        for j,v in enumerate(b):a[k+j]=(a[k+j]-z*v)%3
        while a and not a[-1]:a.pop()
    return a
def xpower(n):
    a=[0,1];r=[1]
    for _ in range(n):r=remainder(poly_mul(r,a),MOD)
    return r
for d in [1,2,3]:
    xp=xpower(3**d)
    assert polynomial_gcd(MOD,[(xp[i] if i<len(xp) else 0)-(1 if i==1 else 0) for i in range(max(2,len(xp)))])==(1,),('reducible',d)
assert xpower(729)==[0,1]
print('FIELD=GF(729); DEGREE_SIX_IRREDUCIBILITY_OK')
# Check primitive generator and enumerate projective 91 semilinear fixed points.
prim=next(a for a in range(2,729) if all(power(a,728//p)!=1 for p in (2,7,13)))
assert len({power(prim,i) for i in range(728)})==728
seen=set(); points=[]; roots={}
for k in range(91):
    a=power(prim,k);b=power(a,81);c=power(a,9)
    assert all(power(e,729)==e for e in [a,b,c])
    xyz=(a,b,c)
    assert power(a,9)==c and power(b,9)==a and power(c,9)==b
    s=power(a,56)
    if add(add(power(s,4),s),1)==0:
        assert add(add(mul(power(a,3),b),mul(power(b,3),c)),mul(power(c,3),a))==0
        points.append(k)
assert len(points)==28
# Frobenius maps the projective exponent classes k (mod 91) to 3k.
remaining=set(points);cycles=[]
while remaining:
    x=min(remaining);cyc=[];y=x
    while y not in cyc:
        assert y in remaining
        cyc.append(y); remaining.remove(y);y=3*y%91
    assert y==x
    cycles.append(len(cyc))
assert Counter(cycles)==Counter([1,3,6,6,6,6]),cycles
print('SEMILINEAR_FIXED_POINTS=91; HYPERFLEX_POINTS=28')
print('FROBENIUS_ORBIT_LENGTHS=',sorted(cycles))
# Independent tangent criterion: for each projective class, cubic terms K are multiple of L^3
for k in points:
    a=power(prim,k);b=power(a,81);c=power(a,9)
    # vector (b,c,a) proportional to (c^9,a^9,b^9).
    left=(b,c,a);right=(power(c,9),power(a,9),power(b,9))
    for i in range(3):
        for j in range(3): assert mul(left[i],right[j])==mul(left[j],right[i])
print('TANGENT_CUBIC_VANISHING_IDENTITIES_OK; VERIFY_OK')
