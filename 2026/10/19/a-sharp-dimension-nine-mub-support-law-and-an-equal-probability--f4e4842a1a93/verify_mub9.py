#!/usr/bin/env python3
"""Exact support and probability check for a nine-dimensional finite-field MUB."""
from collections import Counter
P=3
ELTS=[(a,b) for a in range(P) for b in range(P)]
def add(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def mul(x,y): return ((x[0]*y[0]-x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def neg(x): return ((-x[0])%P,(-x[1])%P)
def tr(x): return (2*x[0])%P
# An amplitude zeta^e belongs to Q(zeta); pair coefficients use basis 1,zeta with zeta^2=-1-zeta.
def phase(e): return [(1,0),(0,1),(-1,-1)][e%3]
def norm2(z): return z[0]*z[0]-z[0]*z[1]+z[1]*z[1]
def coordinate(x):
    return 1 if x==(0,0) else (-1 if x in ((1,0),(2,0),(0,1),(0,2)) else 0)
assert sum(coordinate(x)**2 for x in ELTS)==5
by_basis={}
for a in ELTS:
    norms=[]
    for b in ELTS:
        r=(0,0)
        for x in ELTS:
            c=coordinate(x)
            if c:
                e=tr(add(mul(a,mul(x,x)),mul(b,x)))
                p=phase(e)
                r=(r[0]+c*p[0],r[1]+c*p[1])
        norms.append(norm2(r))
    by_basis[a]=Counter(norms)
    assert by_basis[a]==Counter({0:4,9:5}),(a,by_basis[a])
assert sum(1 for x in ELTS if coordinate(x))==5
assert sum(sum(c[k] for k in c if k) for c in by_basis.values())+5==50
# Coordinate inner products in B_a are (1/sqrt(45))*r, norm2(r)=9 => probability=1/5.
assert 5*10==50 and 4*9==36
print('PASS: all nine finite bases have exactly four zero amplitudes, five with squared norm 9.')
print('PASS: computational basis has five amplitudes; total MUB support=50 and all positive probabilities=1/5.')
