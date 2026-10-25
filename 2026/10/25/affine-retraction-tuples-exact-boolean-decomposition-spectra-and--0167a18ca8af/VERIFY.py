#!/usr/bin/env python3
"""Exhaustive small-field checks of affine retraction tuple counts.

Run: python3 verify_affine11.py
No third-party dependencies. GF(4) uses the irreducible polynomial t^2+t+1.
"""
from itertools import product
from math import prod

def add(a, b, q):
    return a ^ b if q == 4 else (a+b) % q

def mul(a, b, q):
    if q != 4:
        return (a*b) % q
    w=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1: w ^= 1<<(i+j)
    if w&4: w ^= 7 # t^2=t+1
    return w

def compose(f, g):
    return tuple(f[g[x]] for x in range(len(f)))

def affine_map(matrix, b, n, q, pts, lookup):
    return tuple(lookup[tuple(
        add(b[i], sum_field((mul(matrix[i][j],x[j],q) for j in range(n)), q), q)
        for i in range(n))] for x in pts)

def sum_field(vals,q):
    z=0
    for a in vals: z=add(z,a,q)
    return z

def enumeration(n,q):
    pts=list(product(range(q),repeat=n))
    lookup={x:i for i,x in enumerate(pts)}
    out=[]
    for vals in product(range(q),repeat=n*n):
        matrix=tuple(tuple(vals[i*n:(i+1)*n]) for i in range(n))
        for b in product(range(q),repeat=n):
            f=affine_map(matrix,b,n,q,pts,lookup)
            if compose(f,f)==f:
                out.append((matrix,b,f))
    return out

def GL(n,q):
    return prod(q**n-q**j for j in range(n))

def compositions(n,m):
    if m==1:yield (n,)
    else:
        for a in range(n+1):
            for tail in compositions(n-a,m-1):yield (a,)+tail

def predicted(n,q,k):
    m=1<<k
    total=0
    g=GL(n,q)
    for a in compositions(n,m):
        d=prod(GL(z,q) for z in a)
        assert g%d==0
        total+=(g//d)*q**(n-a[-1])
    return total

def direct(n,q,k):
    fs=enumeration(n,q)
    if k==1:return len(fs),len(fs)
    N=len(fs)
    # The verifier uses the full transformation tables, not matrix identities.
    commute=[[compose(fs[i][2],fs[j][2])==compose(fs[j][2],fs[i][2])
              for j in range(N)] for i in range(N)]
    if k==2: return sum(sum(row) for row in commute),N
    if k==3:
        return sum(1 for i in range(N) for j in range(N) if commute[i][j]
                   for h in range(N) if commute[i][h] and commute[j][h]),N
    raise ValueError('Only k up to three is exhaustively checked')

cases=[(2,1,1),(2,2,1),(2,3,1),(2,1,2),(2,2,2),
       (2,3,2),(2,2,3),(3,1,2),(3,2,2),(4,1,2),(4,2,2)]
for q,n,k in cases:
    count,size=direct(n,q,k)
    formula=predicted(n,q,k)
    assert count==formula,(q,n,k,count,formula)
    print(f'GF({q}), dimension={n}, arity={k}: idempotents={size}, commuting={count}')
print('VERIFY_OK: affine idempotent tuple formula; all 11 cases')
