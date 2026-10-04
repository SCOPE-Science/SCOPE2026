#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction


def graph(p,f):
    s=(p-1)*f
    k=p+1
    # vertices 0..f-2 are Frattini isolates; then k parts of size s
    iso=list(range(max(0,f-1)))
    parts=[]
    cur=len(iso)
    for _ in range(k):
        part=list(range(cur,cur+s)); parts.append(part); cur+=s
    N=[set() for _ in range(cur)]
    for a in range(k):
        for b in range(a+1,k):
            for x in parts[a]:
                for y in parts[b]:
                    N[x].add(y);N[y].add(x)
    return N,iso,parts


def zero_forces(C,N):
    blue=set(C)
    trace=[]
    while True:
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=(v,next(iter(W)));break
        if move is None:
            return len(blue)==len(N),trace
        v,u=move; blue.add(u); trace.append((v,u))


def counts(N):
    n=len(N); out={}
    for k in range(n+1):
        c=0
        for C in combinations(range(n),k):
            ok,_=zero_forces(C,N)
            if ok:c+=1
        if c:out[k]=c
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


def witness(p,f,N,iso,parts):
    s=(p-1)*f
    n=len(N)
    A=[[0]*n for _ in range(n)]
    if s==1:
        # only p=2,f=1: K3
        for i in range(n):
            for j in range(n):
                A[i][j]=1
        expected=1
    elif s==2:
        # 2D hyperbolic form <(a,b),(c,d)>=ad+bc.
        vec={}
        for i,part in enumerate(parts):
            a=2**i
            vec[part[0]]=(1,a)
            vec[part[1]]=(1,-a)
        for i in range(n):
            for j in range(n):
                if i in iso or j in iso: continue
                u,v=vec[i],vec[j]
                A[i][j]=u[0]*v[1]+u[1]*v[0]
        expected=2
    else:
        # Lorentz form diag(-1,1,1) with rational isotropic parametrization.
        # One vector is repeated on each multipartite part.
        vec={}
        for i,part in enumerate(parts):
            t=i+1
            v=(1+t*t,1-t*t,2*t)
            for x in part: vec[x]=v
        for i in range(n):
            for j in range(n):
                if i in iso or j in iso: continue
                u,v=vec[i],vec[j]
                A[i][j]=-u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
        expected=3
    for i in range(n):
        for j in range(i+1,n):
            assert ((A[i][j]!=0)==(j in N[i])), (p,f,i,j,A[i][j])
    assert rank_fraction(A)==expected,(p,f,rank_fraction(A),expected)
    return expected


def predicted(p,f):
    s=(p-1)*f; k=p+1
    m=k*s
    N=p*p*f-1
    A=k*(k-1)//2*s*s
    if s==1:
        poly={2:3,3:1}
        Z=2; mr=1
    else:
        poly={N-2:A,N-1:m,N:1}
        Z=N-2; mr=(2 if s==2 else 3)
    return N,m,A,Z,mr,poly

cases=[(2,1),(2,2),(2,4),(3,1),(3,2),(5,1)]
for p,f in cases:
    N,iso,parts=graph(p,f)
    n,m,A,Z,mr,poly=predicted(p,f)
    assert len(N)==n
    gotmr=witness(p,f,N,iso,parts)
    assert gotmr==mr
    # The theorem's degree-(n-2) characterization: omitted pair is forcing
    # exactly when it lies in distinct multipartite parts. Isolates are never omitted.
    if (p-1)*f>1:
        c=0
        allv=set(range(n))
        for u,v in combinations(range(n),2):
            ok,_=zero_forces(allv-{u,v},N)
            same_part=any(u in P and v in P for P in parts)
            desired=(u not in iso and v not in iso and not same_part)
            assert ok==desired,(p,f,u,v,ok,desired)
            c+=ok
        assert c==A,(p,f,c,A)
    if n<=8:
        got=counts(N)
        assert got==poly,(p,f,got,poly)
        print(f'p={p}, f={f}: n={n}, exhaustive polynomial={got}, mr={mr}')
    else:
        # Check constructed minimum forcing sets and predicted high coefficients.
        if (p-1)*f>1:
            white=(parts[0][0],parts[1][0])
            C=set(range(n))-set(white)
            ok,tr=zero_forces(C,N)
            assert ok and len(C)==Z
            assert len(tr)==2
        print(f'p={p}, f={f}: n={n}, structural Z={Z}, min_sets={A}, mr={mr}')

print('VERIFY_OK')
