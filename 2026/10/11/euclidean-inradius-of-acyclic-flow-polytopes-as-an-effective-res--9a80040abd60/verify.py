#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import sqrt, isclose

def inv(A):
    n=len(A)
    M=[list(map(Fraction,row))+[Fraction(i==j) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c])
        M[c],M[p]=M[p],M[c]
        z=M[c][c]; M[c]=[x/z for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                z=M[r][c]; M[r]=[M[r][j]-z*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def effective_resistances(n,edges):
    L=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    for u,v in edges:
        L[u][u]+=1; L[v][v]+=1; L[u][v]-=1; L[v][u]-=1
    R=inv([row[:-1] for row in L[:-1]])
    out=[]
    for u,v in edges:
        b=[Fraction(0) for _ in range(n-1)]
        if u<n-1:b[u]+=1
        if v<n-1:b[v]-=1
        q=sum(b[i]*R[i][j]*b[j] for i in range(n-1) for j in range(n-1))
        out.append(q)
    return out

def lower_ideals(n,edges):
    ans=[]
    for mask in range(1,(1<<n)-1):
        S={i for i in range(n) if mask>>i & 1}
        if all(not (u not in S and v in S) for u,v in edges):
            ans.append(S)
    return ans

def cut_radius(n,edges,a,facets):
    R=effective_resistances(n,edges)
    c=[sqrt(float(1-r)) for r in R]
    vals=[]
    for S in lower_ideals(n,edges):
        den=sum(c[k] for k,(u,v) in enumerate(edges) if k in facets and u in S and v not in S)
        if den>1e-12:
            num=sum(a[i] for i in S)
            vals.append(num/den)
    return min(vals),R

# Diamond: endpoints are the two s-t paths; Euclidean length is 2.
edges=[(0,1),(0,2),(1,3),(2,3)]
r,R=cut_radius(4,edges,[1,0,0,-1],set(range(4)))
assert all(x==Fraction(3,4) for x in R)
assert isclose(r,1.0,rel_tol=1e-12,abs_tol=1e-12)

# Transitive triangle with unit source-sink flow: segment length sqrt(3).
edges=[(0,1),(0,2),(1,2)]
r,R=cut_radius(3,edges,[1,0,-1],{0,1,2})
assert all(x==Fraction(2,3) for x in R)
assert isclose(r,sqrt(3)/2,rel_tol=1e-12,abs_tol=1e-12)

# Same triangle with netflow (1,1,-2). Edge 1->2 is never zero, so F={0,1}.
r,R=cut_radius(3,edges,[1,1,-2],{0,1})
assert all(x==Fraction(2,3) for x in R)
assert isclose(r,sqrt(3)/2,rel_tol=1e-12,abs_tol=1e-12)
wrong,_=cut_radius(3,edges,[1,1,-2],{0,1,2})
assert wrong <= r + 1e-12

print('VERIFY_OK flow-inradius examples=3 resistance_exact=yes nonfacet_guard=yes')
