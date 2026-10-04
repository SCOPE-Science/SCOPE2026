#!/usr/bin/env python3
"""Exact algebra replay for the equilibrium-index theorem."""

from fractions import Fraction
from itertools import permutations

# Sparse polynomials in variables (L,a,b,c,s): monomial tuple -> Fraction.
N = 5
ZERO = {}

def const(q):
    q = Fraction(q)
    return {} if q == 0 else {(0,0,0,0,0): q}

def var(i):
    e=[0]*N
    e[i]=1
    return {tuple(e): Fraction(1)}

def add(p,q):
    r=dict(p)
    for m,v in q.items():
        r[m]=r.get(m,Fraction(0))+v
        if r[m]==0:
            del r[m]
    return r

def neg(p):
    return {m:-v for m,v in p.items()}

def sub(p,q):
    return add(p,neg(q))

def mul(p,q):
    r={}
    for m,v in p.items():
        for n,w in q.items():
            k=tuple(m[i]+n[i] for i in range(N))
            r[k]=r.get(k,Fraction(0))+v*w
    return {m:v for m,v in r.items() if v}

def powp(p,n):
    r=const(1)
    for _ in range(n):
        r=mul(r,p)
    return r

def scale(p,q):
    return mul(const(q),p)

def parity(perm):
    inv=sum(1 for i in range(len(perm)) for j in range(i+1,len(perm)) if perm[i]>perm[j])
    return -1 if inv%2 else 1

def det4(M):
    out={}
    for p in permutations(range(4)):
        term=const(parity(p))
        for i,j in enumerate(p):
            term=mul(term,M[i][j])
        out=add(out,term)
    return out

L,a,b,c,s = [var(i) for i in range(N)]

# J_s = [[-a,a,0,0],[0,0,s,1],[-s,-s,0,0],[0,0,s,-c]]
M = [
    [add(L,a), neg(a), ZERO, ZERO],
    [ZERO, L, neg(s), const(-1)],
    [s, s, L, ZERO],
    [ZERO, ZERO, neg(s), add(L,c)],
]
raw=det4(M)

# Reduce s^2=b. The determinant has only even powers of s.
reduced={}
for mon,coef in raw.items():
    eL,ea,eb,ec,es=mon
    assert es%2==0
    mon2=(eL,ea,eb+es//2,ec,0)
    reduced[mon2]=reduced.get(mon2,Fraction(0))+coef
reduced={m:v for m,v in reduced.items() if v}

A1=add(a,c)
A2=add(mul(a,c),b)
A3=mul(b,add(add(scale(a,2),c),const(1)))
A4=scale(mul(mul(a,b),add(c,const(1))),2)
expected=add(
    powp(L,4),
    add(mul(A1,powp(L,3)),
        add(mul(A2,powp(L,2)),
            add(mul(A3,L),A4)))
)
assert reduced == expected, (reduced,expected)

D2=sub(mul(A1,A2),A3)
D3=sub(sub(mul(mul(A1,A2),A3),powp(A3,2)),mul(powp(A1,2),A4))

P = add(
    scale(powp(a,3),2),
    add(scale(mul(powp(a,2),b),2),
    add(mul(mul(powp(a,2),powp(c,2)),const(1)),
    add(scale(mul(powp(a,2),c),3),
    add(mul(mul(a,b),c),
    add(scale(mul(a,b),3),
    add(mul(a,powp(c,3)),
    add(mul(a,powp(c,2)),
    add(mul(b,c),b)))))))))
target=neg(mul(b,P))
assert D3 == target, (D3,target)

def evalp(p,Lv,av,bv,cv,sv=0):
    vals=(Fraction(Lv),Fraction(av),Fraction(bv),Fraction(cv),Fraction(sv))
    out=Fraction(0)
    for mon,coef in p.items():
        term=coef
        for e,v in zip(mon,vals):
            term*=v**e
        out+=term
    return out

# Exact Routh sample (a,b,c)=(1,1,2):
A1s=Fraction(3)
A2s=Fraction(3)
A3s=Fraction(5)
A4s=Fraction(6)
D2s=A1s*A2s-A3s
D3s=A1s*A2s*A3s-A3s*A3s-A1s*A1s*A4s
assert D2s == 4
assert D3s == -34
first_column=[Fraction(1),A1s,D2s/A1s,D3s/D2s,A4s]
signs=[1 if x>0 else -1 if x<0 else 0 for x in first_column]
assert signs == [1,1,1,-1,1]
changes=sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
assert changes == 2

# Positivity certificate: every coefficient of P is positive and b>0,
# hence D3=-b*P<0 on a,b,c>0.
assert all(v>0 for v in P.values())
print("VERIFY_OK")
