#!/usr/bin/env python3
"""Exact checks for the genus-five Howe plane-sextic zeta correction."""
from itertools import product
from math import gcd

A = (0, 1, 2, 5)
B = (3, 4, 6, 7)

def phi(x, roots):
    z = 1
    for a in roots:
        z *= x - a
    return z

def poly_add(f, g):
    return [ (f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0) for i in range(max(len(f),len(g))) ]

def poly_mul(f,g):
    r=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):
            r[i+j]+=a*b
    return r

def from_roots(roots):
    out=[1]
    for r in roots:
        out=poly_mul(out,[-r,1])
    return out

p1=from_roots(A)
p2=from_roots(B)
h=[a-b for a,b in zip(p1,p2)]
assert p1==[0,-10,17,-8,1]
assert p2==[504,-450,145,-20,1]
assert h==[-504,440,-128,12,0]
g=[v//4 for v in h[:4]]
assert g==[-126,110,-32,3]

# Cubic discriminant, exact integer arithmetic.
a,b,c,d=g[3],g[2],g[1],g[0]
discriminant = b*b*c*c - 4*a*c**3 -4*b**3*d-27*a*a*d*d+18*a*b*c*d
assert discriminant == -4460
assert all(sum(g[j]*x**j for j in range(4)) % 13 != 0 for x in range(13))

# Independent finite-field point counts for the singular sextic C and its smooth normalization H.
# H has four points at infinity, C has three, and affine y-solutions are enumerated directly.
for p in [11,13,17,19,23,29,31,37,41]:
    if p in set(A)|set(B):
        # Integer branch-coordinate coincidences are irrelevant modulo a good prime.
        pass
    if len({a%p for a in A+B}) != 8 or 12%p ==0:
        continue
    squares={v*v%p for v in range(p)}
    chi=lambda z: 0 if z%p==0 else (1 if z%p in squares else -1)
    hcount=4
    ccount=3
    for x in range(p):
        v1,v2=phi(x,A)%p,phi(x,B)%p
        hcount+=(1+chi(v1))*(1+chi(v2))
        ccount+=sum(((y**4-2*(v1+v2)*y*y+(v1-v2)**2)%p==0) for y in range(p))
    correction= -1-sum(chi(phi(x,A)) for x in range(p) if phi(x,A)%p==phi(x,B)%p)
    assert ccount-hcount == correction,(p,ccount,hcount,correction)
print('VERIFY_OK: quartics, cubic discriminant, irreducibility mod13, zeta point-count corrections at 9 small odd primes')
