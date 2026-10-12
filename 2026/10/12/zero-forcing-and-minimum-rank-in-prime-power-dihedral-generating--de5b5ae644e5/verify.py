#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import gcd

def graph_direct(n):
    # Vertices 0,...,n-1 are rotations r^i; n+j is the reflection s r^j.
    # Adjacency is evaluated from the exact two-generator criterion in D_{2n}.
    N=[set() for _ in range(2*n)]
    for i in range(2*n):
        for j in range(i+1,2*n):
            if i<n and j<n:
                edge=False
            elif i<n and j>=n:
                edge=(gcd(i,n)==1)
            else:
                edge=(gcd((i-n)-(j-n),n)==1)
            if edge:
                N[i].add(j);N[j].add(i)
    return N

def zero_forces(S,N):
    blue=set(S)
    while True:
        if len(blue)==len(N):
            return True
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=next(iter(W))
                break
        if move is None:
            return False
        blue.add(move)

def polynomial(N):
    out={}
    for k in range(len(N)+1):
        c=sum(1 for S in combinations(range(len(N)),k) if zero_forces(S,N))
        if c:
            out[k]=c
    return out

def predicted(p,k):
    n=p**k
    m=p**(k-1)
    active=(2*p-1)*m
    if k==1:
        c=p*(p-1)
    else:
        c=3*p*(p-1)*m*m//2
    return {2*n-2:c,2*n-1:active,2*n:1}

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    rows=len(A); cols=len(A[0]) if A else 0
    r=c=0
    while r<rows and c<cols:
        piv=next((i for i in range(r,rows) if A[i][c]),None)
        if piv is None:
            c+=1
            continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(rows):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(cols)]
        r+=1;c+=1
    return r

def witness(p,k):
    n=p**k
    # type -1: isolated rotation; 0: generating rotation; 1..p: reflection residue mod p.
    types=[]
    for i in range(n):
        types.append(-1 if gcd(i,n)>1 else 0)
    for j in range(n):
        types.append(1+(j%p))
    if k==1:
        vec={0:(1,0)}
        for t in range(1,p+1):
            vec[t]=(1,1)
        def ip(x,y):
            return x[0]*y[1]+x[1]*y[0]
    else:
        vec={}
        for t in range(p+1):
            vec[t]=(1-t*t,2*t,1+t*t)
        def ip(x,y):
            return x[0]*y[0]+x[1]*y[1]-x[2]*y[2]
    M=[]
    for a in types:
        row=[]
        for b in types:
            row.append(0 if a==-1 or b==-1 else ip(vec[a],vec[b]))
        M.append(row)
    N=graph_direct(n)
    for i in range(2*n):
        for j in range(i+1,2*n):
            assert ((M[i][j]!=0)==(j in N[i]))
    return rank_fraction(M)

# Exhaustive complete polynomial checks.
for p,k in [(3,1),(5,1),(3,2)]:
    n=p**k
    N=graph_direct(n)
    brute=polynomial(N)
    pred=predicted(p,k)
    assert brute==pred,(p,k,brute,pred)
    r=witness(p,k)
    assert r==(2 if k==1 else 3)
    print(f"p={p}, k={k}, order={2*n}, polynomial={brute}, witness_rank={r}")

# Structural profile checks beyond exhaustive subset sizes.
for p,k in [(3,3),(5,2),(7,2)]:
    n=p**k
    m=p**(k-1)
    phi=(p-1)*m
    N=graph_direct(n)
    isolates=[i for i in range(n) if gcd(i,n)>1]
    A=[i for i in range(n) if gcd(i,n)==1]
    parts=[A]+[[n+j for j in range(n) if j%p==t] for t in range(p)]
    assert len(isolates)==m and len(A)==phi
    assert all(len(P)==m for P in parts[1:])
    # Any one-white active profile forces.
    for P in parts:
        w=P[0]
        S=set(range(2*n))-{w}
        assert zero_forces(S,N)
    # Two whites from distinct parts force because every part has size >= 2.
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            S=set(range(2*n))-{parts[i][0],parts[j][0]}
            assert zero_forces(S,N)
    # Three whites from distinct parts stall.
    S=set(range(2*n))-{parts[0][0],parts[1][0],parts[2][0]}
    assert not zero_forces(S,N)
    # Omitting an isolate always fails.
    S=set(range(2*n))-{isolates[0]}
    assert not zero_forces(S,N)
    r=witness(p,k)
    assert r==3
    print(f"p={p}, k={k}, structural_profiles_ok, witness_rank={r}")

print("VERIFY_OK")
