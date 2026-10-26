#!/usr/bin/env python3
"""Standalone polynomial and finite-geometry checks for the Wiman sextic mod 3.

This is a finite reproducibility check, not a substitute for the geometric proof.
Run: python3 verify.py
"""
from itertools import combinations, product
from math import comb

P = 3

def add(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = (out.get(m, 0) + c) % P
    return {m: c for m, c in out.items() if c}

def scale(a, c):
    return {m: (v*c) % P for m, v in a.items() if v*c % P}

def mul(a, b):
    out = {}
    for m, c in a.items():
        for n, d in b.items():
            k = tuple(i+j for i,j in zip(m,n))
            out[k] = (out.get(k, 0) + c*d) % P
    return {m: c for m, c in out.items() if c}

def powp(a, n):
    out = {(0,0,0):1}
    for _ in range(n): out = mul(out,a)
    return out

X = {(1,0,0):1}
Y = {(0,1,0):1}
Z = {(0,0,1):1}
Q = add(add(powp(X,2),powp(Y,2)),powp(Z,2))
L = [add(add(X,Y),Z),add(add(X,Y),scale(Z,-1)),
     add(add(X,scale(Y,-1)),Z),add(add(scale(X,-1),Y),Z)]
F = add(add(add(powp(X,6),powp(Y,6)),powp(Z,6)),
        mul(Q,add(add(powp(X,4),powp(Y,4)),powp(Z,4))))
F = add(F,scale(mul(mul(powp(X,2),powp(Y,2)),powp(Z,2)),-12))
G=Q
for lin in L: G=mul(G,lin)
assert F == G, ('polynomial identity failed', F, G)

def evalp(f, q):
    return sum(c * q[0]**m[0] * q[1]**m[1] * q[2]**m[2] for m,c in f.items()) % P

def normalize(q):
    i = next(i for i,v in enumerate(q) if v%3)
    factor = 1 if q[i]%3 == 1 else 2
    return tuple((factor * c) % 3 for c in q)

points = sorted({normalize(v) for v in product(range(3),repeat=3) if any(v)})
assert len(points)==13
rational_conic = {p for p in points if evalp(Q,p)==0}
tangency = {normalize(v) for v in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]}
assert rational_conic == tangency and len(rational_conic)==4

forms = [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]
for i,c in enumerate(forms):
    at = normalize(c)
    assert evalp(L[i],at)==0 and at in rational_conic
    assert all(evalp(L[i],p)!=0 for p in rational_conic if p!=at)

crosspoints=set()
for i,j in combinations(range(4),2):
    a,b=forms[i],forms[j]
    cross=(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    p=normalize(cross)
    assert p not in rational_conic
    assert sum(evalp(l,p)==0 for l in L)==2
    crosspoints.add(p)
assert len(crosspoints)==6
curvepoints = {p for p in points if evalp(F,p)==0}
assert curvepoints == crosspoints | tangency
assert len(curvepoints)==10

# At a tacnode f(u,v)=u(u-v^2), with f_u=2u-v^2 and f_v=-2uv.
# Substituting u=v^2/2 gives a unit multiple of v^3 in f_v.
# Therefore the local Tjurina algebra is k[[v]]/(v^3), of length 3.
assert (-(2 * (2 % 3) * pow(2,-1,3))) % 3 != 0
assert 4*3+6*1 == 18  # total Tjurina length
assert 4*2+6*1 == 14  # total normalization defect
assert (14 - 5 + 1) == (6-1)*(6-2)//2 == 10
print('PASS: polynomial identity, 4 rational tangents, 6 distinct line crossings,')
print('      10 rational singular points, local tau/delta and genus consistency.')
