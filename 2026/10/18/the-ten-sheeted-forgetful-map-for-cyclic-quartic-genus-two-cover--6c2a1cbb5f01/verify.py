#!/usr/bin/env python3
"""Independent finite-characteristic checks for the cyclic-quartic genus-two parameter map.

Pure Python (standard library only). Polynomial calculations are exact over F_2.
The finite-field tests corroborate, but do not replace, the all-field proof.
"""
from collections import Counter, defaultdict

# A bivariate polynomial over F_2, monomial (power_of_r, power_of_u).
def add(*polys):
    s=set()
    for p in polys:
        s.symmetric_difference_update(p)
    return s

def mul(a,b):
    o=set()
    for i,j in a:
        for m,n in b:
            e=(i+m,j+n)
            if e in o: o.remove(e)
            else: o.add(e)
    return o

def power(a,n):
    o={(0,0)}
    while n:
        if n&1: o=mul(o,a)
        a=mul(a,a)
        n >>=1
    return o

R={(1,0)}; U={(0,1)}; ONE={(0,0)}
x=add(power(U,2),U)
lam=power(R,4)
H=add(mul(power(R,2),power(U,3)),mul(power(R,2),power(U,2)),mul(add(ONE,R),U))
F=add(mul(lam,power(U,5)),mul(add(lam,power(R,2),ONE),power(U,3)),mul(add(ONE,R),U))
# Y_1^2+Y_1= lambda*x^3+u^2+u^3;
# substituting Y_1=v+H, v^2+v=F makes both sides equal.
assert add(F,power(H,2),H) == add(mul(lam,power(x,3)),power(U,2),power(U,3))
print('WITT_TO_ARTIN_SCHREIER_IDENTITY_OK')

# GF(256), AES irreducible polynomial z^8+z^4+z^3+z+1.
def gmul(a,b):
    r=0
    while b:
        if b&1: r ^= a
        a <<= 1
        if a&256: a ^= 0x11b
        b >>= 1
    return r

def gpow(a,n):
    o=1
    while n:
        if n&1: o=gmul(o,a)
        a=gmul(a,a)
        n >>=1
    return o

squares=defaultdict(list)
for l in range(1,256):
    r=gpow(l,64) # fourth root
    assert gpow(r,4)==l
    a=l
    b=l ^ gpow(r,2) ^ 1
    c=r ^ 1
    q=gpow(l,2)^l^1
    assert gpow(b,2)==q
    j=gmul(gpow(q,5),gpow(l,255-6))
    i=gmul(gpow(b,5),gpow(l,255-3))
    assert gpow(i,2)==j
    squares[j].append((l,a,b,c))
assert len(squares[0])==2
assert all(gpow(l,2)^l^1==0 for l,*_ in squares[0])

# For equal nonzero j, explicitly reconstruct scaling between quintic models.
comparison_count=0
for j,objs in squares.items():
    if not j: continue
    for l,a,b,c in objs:
        for m,a2,b2,c2 in objs:
            z=gmul(gpow(gmul(b,gpow(b2,254)),2), gmul(a2,gpow(a,254)))
            # This candidate is (b/b2)^2 /(a/a2), since z^3=b/b2, z^5=a/a2.
            assert gmul(a2,gpow(z,5))==a
            assert gmul(b2,gpow(z,3))==b
            comparison_count+=1
print('F256_PARAMETER_VALUES_OK',len(squares),len(squares[0]),comparison_count)

# Characteristic-two polynomial arithmetic represented by coefficient bitmask.
def pmul(a,b):
    r=0
    while b:
        if b&1: r ^= a
        a <<=1; b >>=1
    return r

def ppow(a,n):
    r=1
    while n:
        if n&1: r=pmul(r,a)
        a=pmul(a,a); n>>=1
    return r

def deriv(a):
    return sum(1<<(i-1) for i in range(1,a.bit_length(),2) if (a>>i)&1)
q=0b111
N=ppow(q,5)
assert N.bit_length()-1==10
assert deriv(N)==ppow(q,4)
assert (q&1)==1
assert deriv(1<<6)==0
print('DEGREE_TEN_AND_RAMIFICATION_IDENTITY_OK')
print('VERIFY_OK')
