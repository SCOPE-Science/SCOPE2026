#!/usr/bin/env python3
"""Independent finite-prime checks for the central-coefficient identities.

The proof in RESULT.md is uniform in p and does not depend on this test.
"""
from math import factorial, comb

PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, 109)


def central(n, p):
    # [t^n](1+a*t+t*t)^n, represented by ascending a coefficients.
    out = [0] * (n + 1)
    for j in range(n // 2 + 1):
        out[n - 2*j] = factorial(n) // (factorial(j)**2 * factorial(n - 2*j)) % p
    return out


def extracted(n, k, p):
    # [t^k](1+a*t+t*t)^n, with exact multinomial integers.
    out = [0] * (k + 1)
    for j in range(k // 2 + 1):
        s = k - 2*j
        z = n - s - j
        if z < 0: continue
        out[s] = factorial(n)//(factorial(j)*factorial(s)*factorial(z)) % p
    return out


def mul(a, b, p):
    out = [0] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return out


def power(a, n, p):
    y = [1]
    for _ in range(n): y = mul(y, a, p)
    return y


def deriv(a,p):
    return [(i*a[i])%p for i in range(1,len(a))]


def strip(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def remainder(a,b,p):
    a=strip(a[:]); b=strip(b[:]); assert b != [0]
    while len(a)>=len(b) and a != [0]:
        fac=a[-1]*pow(b[-1],-1,p)%p
        for i in range(len(b)):
            a[len(a)-len(b)+i]=(a[len(a)-len(b)+i]-fac*b[i])%p
        strip(a)
    return a


def gcd(a,b,p):
    a=strip(a[:]); b=strip(b[:]);
    while b != [0]:a,b=b,remainder(a,b,p)
    return strip(a)


def evalpoly(a,z,p):
    y=0
    for c in a[::-1]:y=(y*z+c)%p
    return y


for p in PRIMES:
    m=(p-1)//6
    r=2*m
    H=central(r,p)
    B=extracted(2*r,r,p)
    C=central(2*r,p)
    delta=power([(-4)%p,0,1],m,p)
    scalar=comb(4*m,2*m)%p
    assert B == [(scalar*c)%p for c in delta], (p,'B identity')
    assert C == mul(delta,H,p), (p,'C identity')
    assert len(strip(H[:]))==r+1 and H[-1]==1
    assert len(strip(gcd(H,deriv(H,p),p)))==1, (p,'multiple roots')
    assert evalpoly(H,2,p)!=0 and evalpoly(H,-2,p)!=0
    roots=[z for z in range(p) if evalpoly(H,z,p)==0]
    assert all(z*z%p != 4 for z in roots)
    print(f'p={p}, exceptional_geom={r}, rational_exceptional={len(roots)}, coefficient_identities=OK')
print('COEFFICIENT_IDENTITIES_OK')
