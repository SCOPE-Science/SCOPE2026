#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

def mul(x,y,n):
    # x=(i,e) represents r^i s^e
    i,e=x; j,f=y
    return ((i + (j if e==0 else -j)) % n, (e+f)%2)

def commute(x,y,n):
    return mul(x,y,n)==mul(y,x,n)

def center(n):
    G=[(i,e) for i in range(n) for e in (0,1)]
    return {x for x in G if all(commute(x,y,n) for y in G)}

def graph(n):
    G=[(i,e) for i in range(n) for e in (0,1)]
    Z=center(n)
    V=[x for x in G if x not in Z]
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if not commute(x,V[j],n):
                N[i].add(j);N[j].add(i)
    return V,N

def zero_forces(C,N):
    blue=set(C); trace=[]
    while True:
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=(v,next(iter(W)));break
        if move is None:
            return len(blue)==len(N),trace
        v,u=move; blue.add(u); trace.append((v,u))

def brute_z_counts(N):
    n=len(N); out={}
    for k in range(n+1):
        c=0
        for C in combinations(range(n),k):
            ok,_=zero_forces(C,N)
            if ok:c+=1
        if c: out[k]=c
    return out

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=0;c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1;continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1;c+=1
    return r

H=((0,1),(1,0))

def bil(u,v):
    return u[0]*v[1]+u[1]*v[0]

def witness(n,V,N):
    coords=[]
    if n%2:
        # noncentral rotations: (1,0); reflections: (1,1)
        for i,e in V:
            coords.append((1,0) if e==0 else (1,1))
    else:
        # rotations: (1,0). Pair reflections i and i+n/2 using slopes +/- 2^i.
        half=n//2
        for i,e in V:
            if e==0:
                coords.append((1,0))
            else:
                if i<half:
                    coords.append((1,2**i))
                else:
                    coords.append((1,-(2**(i-half))))
    A=[[bil(coords[i],coords[j]) for j in range(len(V))] for i in range(len(V))]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            assert ((A[i][j]!=0)==(j in N[i])), (n,V[i],V[j],A[i][j])
    assert rank_fraction(A)==2
    return A

for n in range(3,9):
    V,N=graph(n)
    Nvert=len(V)
    A=witness(n,V,N)
    counts=brute_z_counts(N) if Nvert<=14 else None
    if n%2:
        assert Nvert==2*n-1
        expected_min=Nvert-2
        expected_count=n*(n-1)
    else:
        assert Nvert==2*n-2
        expected_min=Nvert-2
        expected_count=3*n*(n-2)//2
    if counts is not None:
        assert min(counts)==expected_min,(n,counts)
        assert counts[expected_min]==expected_count,(n,counts[expected_min],expected_count)
        assert counts[Nvert-1]==Nvert
        assert counts[Nvert]==1
        assert set(counts)=={Nvert-2,Nvert-1,Nvert}
        print(f"n={n}: |V|={Nvert}, Z={expected_min}, min_sets={expected_count}, polynomial_terms={counts}, rank_witness=2")
    else:
        print(f"n={n}: |V|={Nvert}, structural Z={expected_min}, min_sets={expected_count}, rank_witness=2")

print("VERIFY_OK")
