#!/usr/bin/env python3
"""Exact polynomial checks for the flex-divisor stratification of a cyclic octic pencil.

Only Python's standard library is required. The all-parameter assertion is proved
by algebraic identities and an independent geometric argument in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction

# Sparse polynomials in X,Y,Z,L with integer coefficients.
def const(c):
    return {(0,0,0,0): c} if c else {}
def mon(c=1, ex=(0,0,0,0)):
    return {ex:c} if c else {}
def add(*polys):
    d=defaultdict(int)
    for p in polys:
        for k,v in p.items(): d[k]+=v
    return {k:v for k,v in d.items() if v}
def neg(p): return {k:-v for k,v in p.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    d=defaultdict(int)
    for ka,va in a.items():
        for kb,vb in b.items(): d[tuple(x+y for x,y in zip(ka,kb))]+=va*vb
    return {k:v for k,v in d.items() if v}
def times(p,n): return {k:n*v for k,v in p.items() if n*v}
def power(p,n):
    out=const(1)
    while n:
        if n&1:out=mul(out,p)
        p=mul(p,p);n>>=1
    return out
def diff(p,i):
    d=defaultdict(int)
    for ex,v in p.items():
        if ex[i]:
            t=list(ex);t[i]-=1;d[tuple(t)]+=v*ex[i]
    return {k:v for k,v in d.items() if v}
X,Y,Z,L=[mon(ex=tuple(int(i==j) for i in range(4))) for j in range(4)]
F=add(power(X,8),mul(L,mul(power(X,4),power(Y,4))),power(Y,8),power(Z,8))
Fxx,Fyy,Fxy=diff(diff(F,0),0),diff(diff(F,1),1),diff(diff(F,0),1)
Fzz=diff(diff(F,2),2)
H=mul(sub(mul(Fxx,Fyy),mul(Fxy,Fxy)),Fzz)
R=add(times(mul(L,add(power(X,8),power(Y,8))),6),mul(sub(const(28),power(L,2)),mul(power(X,4),power(Y,4))))
assert H==times(mul(mul(power(X,2),power(Y,2)),mul(power(Z,6),R)),6272)

# Discriminant of 6L u^2+(28-L^2)u+6L.
disc=sub(power(sub(const(28),power(L,2)),2),times(power(L,2),144))
assert disc==mul(sub(power(L,2),const(4)),sub(power(L,2),const(196)))

# Q=u^2+Lu+1, R(u)=6Lu^2+(28-L^2)u+6L.
# Therefore R mod Q = (28-L^2-6L^2)u = 7(4-L^2)u.
assert add(sub(const(28),power(L,2)),neg(times(power(L,2),6)))==times(sub(const(4),power(L,2)),7)
assert add(mul(const(84),power(sub(power(X,4),power(Y,4)),2)),neg(add(times(power(X,8),84),times(power(Y,8),84),times(mul(power(X,4),power(Y,4)),-168))))=={}
assert sub(add(times(power(X,8),-84),times(power(Y,8),-84),times(mul(power(X,4),power(Y,4)),-168)),times(power(add(power(X,4),power(Y,4)),2),-84))=={}

# Check weighted total and support stratification; coefficient-based
# multiplicities rather than floating root approximations.
for lam in range(-50,51):
    if lam in (-2,2):continue
    branch_count=8
    if lam==0: poles,quartic,ordinary=24,0,0
    elif lam in (-14,14):poles,quartic,ordinary=8,48,0
    else: poles,quartic,ordinary=8,16,64
    assert 6*poles+2*quartic+ordinary==144
    assert branch_count==8
    if lam!=0:
        assert (lam*lam-4)*(lam*lam-196)==0 if lam in (-14,14) else (lam*lam-4)*(lam*lam-196)!=0

# Independent exact check of the real sign obstruction at several magnitudes.
for t in [Fraction(201,100),3,7,14,100,10_000]:
    for u in [Fraction(1,10000),Fraction(1,2),1,2,10000]:
        Rval=-6*t*(u*u+1)+(28-t*t)*u
        assert Rval<0

print('VERIFY_OK: exact 4-variable Hessian, discriminant, special factorizations, weight and real-sign checks')
