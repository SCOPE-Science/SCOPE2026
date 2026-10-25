#!/usr/bin/env python3
"""Independent exact checks for a signed-cycle convex polytope; run with Python 3 and SymPy."""
from fractions import Fraction
from itertools import combinations, product
import sympy as sp

ALPHABET=(-1,0,1)

def generators(n):
    out=[]
    for i in range(n):
        v=[0]*n; v[i]=1
        out.extend([tuple(v),tuple(-z for z in v)])
    for i in range(n):
        v=[0]*n; v[i]=1; v[(i+1)%n]= -1 if i<n-1 else 1
        out.extend([tuple(v),tuple(-z for z in v)])
    return out

def rank(a,n):
    a=[[Fraction(x) for x in row] for row in a]
    r=0
    for col in range(n):
        p=next((i for i in range(r,len(a)) if a[i][col]),None)
        if p is None: continue
        a[p],a[r]=a[r],a[p]
        v=a[r][col]
        for j in range(col,n): a[r][j]/=v
        for i in range(r+1,len(a)):
            fac=a[i][col]
            if fac:
                for j in range(col,n): a[i][j]-=fac*a[r][j]
        r+=1
        if r==n: return r
    return r

def integer_vertices(n):
    gens=generators(n)
    result=[]
    for y in product(ALPHABET,repeat=n):
        if any(sum(a*b for a,b in zip(g,y))>1 for g in gens):continue
        active=[g for g in gens if sum(a*b for a,b in zip(g,y))==1]
        if rank(active,n)==n:result.append(y)
    return result

def declared_vertices(n):
    out=[]
    for y in product(ALPHABET,repeat=n):
        if any(y[i]!=0 and y[i+1]!=0 and y[i]!=y[i+1] for i in range(n-1)):continue
        if y[0]!=0 and y[-1]!=0 and y[0]==y[-1]:continue
        if any(y[(i-1)%n]==y[i]==y[(i+1)%n]==0 for i in range(n)):continue
        out.append(y)
    return out

states=list(product(ALPHABET,repeat=2)); dim=len(states)
T=sp.zeros(dim); S=sp.zeros(dim)
for i,(a,b) in enumerate(states):
    for j,(u,v) in enumerate(states):
        if u==b and abs(b-v)<=1 and (a,b,v)!=(0,0,0):T[i,j]=1
        if (u,v)==(-a,-b):S[i,j]=1
z=sp.symbols('z')
assert T*S==S*T
assert sp.factor(T.charpoly(z).as_expr())==z**5*(z-1)*(z**3-z**2-2*z-2)
assert sp.factor((T*(sp.eye(dim)+S)/2).charpoly(z).as_expr())==z**6*(z**3-z**2-2*z-2)
assert sp.factor((T*(sp.eye(dim)-S)/2).charpoly(z).as_expr())==z**8*(z-1)

p=[3,1,5]
for n in range(3,13):p.append(p[-1]+2*p[-2]+2*p[-3])
# p[n] = sum of n-th powers of the three cubic roots
for n in range(3,10):
    declared=declared_vertices(n)
    assert len(declared)==sp.trace(T**n*S)==p[n]-1
    if n<=8:
        independent=integer_vertices(n)
        assert set(declared)==set(independent)
        half=2 if n%2 else 0
        if half:
            g=generators(n)
            for s in [-1,1]:
                v=tuple(Fraction(s*((-1)**i),2) for i in range(n))
                assert all(sum(a*b for a,b in zip(row,v))<=1 for row in g)
                assert rank([row for row in g if sum(a*b for a,b in zip(row,v))==1],n)==n
        assert len(declared)+half==p[n]-(-1)**n
        print('n=',n, 'integral vertices=',len(declared),'fractional=',half,'facets=',p[n]-(-1)**n)

# Reproduce the six-dimensional cohomology example from the 2026 motivating paper.
source_rows=[
(1,0,0,0,0,0), (0,1,1,0,0,0),(-1,0,0,1,0,0),
(0,-1,0,0,0,0),(0,0,-1,-1,0,0),(0,0,0,0,1,0),
(1,0,0,0,0,1),(0,0,0,0,-1,-1),(0,1,0,0,1,0),
(0,0,1,0,0,0),(0,0,0,0,0,1),(0,0,0,1,0,0)]
order=[0,3,2,1,4,5]
signs=[1,1,-1,1,-1,1]
transform={tuple(signs[j]*row[order[j]] for j in range(6)) for row in source_rows}
canon={tuple(v) for v in generators(6)}
assert {tuple(sign*x for x in row) for row in transform for sign in (-1,1)}==canon
print('Möbius-strip six-coordinate unimodular signed permutation: matched 24 polar inequalities.')
print('Exact transfer characteristic polynomials and ranks: PASS')
