#!/usr/bin/env python3
"""Exact-arithmetic checks for a sharp metric-windmill spline projector theorem.

Requires only Python 3 standard library.  The proof for all parameters is in RESULT.md;
finite enumerations below test independent mass-matrix construction and algebraic identities.
"""
from fractions import Fraction as F
from math import comb

COUNTS = {'identities':0, 'matrices':0, 'thresholds':0}

def check(cond, family):
    assert cond, family
    COUNTS[family] += 1

def I(a,b):
    a,b=F(a),F(b)
    return (abs(a)+abs(b))/2 if a*b>=0 else (a*a+b*b)/(2*(abs(a)+abs(b)))

def parameters(s,k):
    U=F(2*(3*s-1),k*s*(2*s-1))
    H=-F(2,k*s*(2*s-1))
    D=F(2,k*s*(2*s-1)*(3*s-1))
    A=F(6*(3*s-2),(2*s-1)*(3*s-1))+D
    B=-F(6,(2*s-1)*(3*s-1))+D
    return U,H,D,A,B

def closed_norm(s,k):
    U,H,D,A,B=parameters(s,k)
    hub=k*s*I(U,H)+k*comb(s,2)*abs(H)
    outer=(I(A,H)+(s-1)*I(A,B)+(s-1)*I(B,H)
           +comb(s-1,2)*abs(B)+s*(k-1)*I(D,H)
           +(k-1)*comb(s,2)*D)
    return hub,outer

def D_poly(x,y):
    return (x*x*2*(y+2)*(3*y+4)*(9*y**3+51*y*y+96*y+58)
            +x*2*(y+2)*(3*y+5)*(18*y**3+99*y*y+171*y+94)
            +2*(3*y+5)**2*(3*y**3+18*y*y+33*y+19))

def E_poly(x,y):
    return (x**3*(y+3)*(3*y+7)*(9*y**3+51*y*y+78*y+20)
            +x*x*9*(y+2)**2*(y+3)*(3*y+8)*(5*y+13)
            +x*(3*y+8)**2*(21*y**3+159*y*y+401*y+337)
            +(y+3)*(3*y+7)*(3*y+8)**3)

def denominator(s,k):
    return 3*k*k*s*s*(2*s-1)*(3*s-1)**2*(3*k*s-2*k+1)

def exact_inverse(a):
    n=len(a); t=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next(p for p in range(j,n) if t[p][j])
        t[j],t[pivot]=t[pivot],t[j]
        c=t[j][j]; t[j]=[v/c for v in t[j]]
        for i in range(n):
            if i!=j and t[i][j]:
                c=t[i][j]; t[i]=[u-c*v for u,v in zip(t[i],t[j])]
    return [row[n:] for row in t]

def direct(s,k):
    n=1+s*k; edges=[]
    for petal in range(k):
        verts=list(range(1+petal*s,1+(petal+1)*s))
        edges.extend((0,v) for v in verts)
        edges.extend((a,b) for i,a in enumerate(verts) for b in verts[i+1:])
    a=[[F(0) for _ in range(n)] for __ in range(n)]
    for u,v in edges:
        a[u][u]+=2; a[v][v]+=2; a[u][v]+=1; a[v][u]+=1
    inv=exact_inverse(a)
    return [sum(I(6*inv[i][u],6*inv[i][v]) for u,v in edges) for i in range(n)]

# Independent direct nodal Gram inversions and all evaluation rows.
for s in range(2,7):
    for k in range(1,5):
        if 1+s*k>26: continue
        h,r=closed_norm(s,k)
        rows=direct(s,k)
        check(rows[0]==h,'matrices')
        for value in rows[1:]: check(value==r,'matrices')
        check(r>=h,'matrices')

# Rational identity checks for the factored nonnegative-coefficient certificates.
# Their equality as polynomial identities follows by clearing denominators and
# comparing the displayed factorizations in RESULT.md; this loop is a separate test.
for s in range(2,49):
    for k in range(1,53):
        h,r=closed_norm(s,k);den=denominator(s,k)
        check(h==F(12*s*s-9*s+2,3*s*(2*s-1)),'identities')
        check((r-h)*den==(k-1)*D_poly(k-1,s-2),'identities')
        if s>=3:
            check((F(2)-r)*den==E_poly(k-1,s-3),'identities')
            check(r<2,'thresholds')
        if s==2:
            check(r==F(3664*k**3+348*k*k-13*k+1,450*k*k*(4*k+1)),'identities')
            check((r>2)==(k>=9),'thresholds')
        check(r>=h,'thresholds')

print('SUCCESS',COUNTS,'total',sum(COUNTS.values()))
