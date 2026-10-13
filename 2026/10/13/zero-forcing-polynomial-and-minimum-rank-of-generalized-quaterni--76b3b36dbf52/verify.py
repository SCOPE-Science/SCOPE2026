#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import comb

def mul(x,y,n):
    i,e=x; j,f=y
    return ((i + (-j if e else j) + (n if e and f else 0))%(2*n),(e+f)%2)

def generated(gens,n):
    one=(0,0); H={one}; changed=True
    while changed:
        changed=False
        old=list(H)
        for g in gens:
            if g not in H: H.add(g); changed=True
        for x in list(H):
            for y in list(H):
                z=mul(x,y,n)
                if z not in H: H.add(z); changed=True
    return H

def cyclic(H,n):
    one=(0,0)
    for g in H:
        K={one}; x=one
        while True:
            x=mul(x,g,n)
            if x in K: break
            K.add(x)
        if K==H:return True
    return False

def direct_graph(n):
    G=[(i,e) for i in range(2*n) for e in (0,1)]
    N=[set() for _ in G]
    for i,x in enumerate(G):
        for j in range(i+1,len(G)):
            if cyclic(generated((x,G[j]),n),n):
                N[i].add(j);N[j].add(i)
    return G,N

def expected(n):
    G=[(i,e) for i in range(2*n) for e in (0,1)]
    def typ(x):
        i,e=x
        if e==0 and i in (0,n): return 0
        if e==0:return 1
        return 2+i%n
    T=[typ(x) for x in G]
    N=[set() for _ in G]
    for i in range(len(G)):
        for j in range(i+1,len(G)):
            a,b=T[i],T[j]
            if a==0 or b==0 or a==b:
                N[i].add(j);N[j].add(i)
    return G,T,N

def forces(S,N):
    B=set(S)
    while True:
        if len(B)==len(N):return True
        move=None
        for v in sorted(B):
            W=N[v]-B
            if len(W)==1:
                move=next(iter(W));break
        if move is None:return False
        B.add(move)

def poly(N):
    d={}
    for k in range(len(N)+1):
        c=sum(forces(S,N) for S in combinations(range(len(N)),k))
        if c:d[k]=c
    return d

def predicted(n):
    inner={}
    for j in range(n+2):
        c=comb(n+1,j)*2**(n+1-j)
        inner[j+1]=inner.get(j+1,0)+c
        inner[j]=inner.get(j,0)+c*(2*n-2)
    inner[0]-=2**(n+1)*(2*n-2)
    return {3*n-2+k:v for k,v in inner.items() if v}

def rank(M):
    A=[[Fraction(x) for x in row] for row in M]
    r=c=0;m=len(A);n=len(A[0])
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:c+=1;continue
        A[r],A[p]=A[p],A[r]; q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c];A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1;c+=1
    return r

def witness(n,G,T,N):
    V=[]
    for t in T:
        if t==0:V.append([1]*(n+1))
        elif t==1:V.append([1]+[0]*n)
        else:
            v=[0]*(n+1);v[t-1]=1;V.append(v)
    M=[[sum(V[i][k]*V[j][k] for k in range(n+1)) for j in range(len(G))] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(i+1,len(G)):
            assert ((M[i][j]!=0)==(j in N[i]))
    assert rank(M)==n+1

for n in range(2,6):
    G,N=direct_graph(n); G2,T,N2=expected(n)
    assert G==G2 and N==N2
    witness(n,G,T,N)
    if n<=4:
        b=poly(N); p=predicted(n); assert b==p
        assert min(b)==3*n-1 and b[3*n-1]==2**(n+1)*n*n
        print(f"Q_{4*n}: N={4*n}, Z={3*n-1}, min_sets={b[3*n-1]}, polynomial={b}, witness_rank={n+1}")
    else:
        p=predicted(n)
        print(f"Q_{4*n}: N={4*n}, predicted_Z={3*n-1}, min_sets={p[3*n-1]}, witness_rank={n+1}")

for n in range(2,11):
    _,T,N=expected(n)
    classes={t:[i for i,x in enumerate(T) if x==t] for t in set(T)}
    q=n+2
    for mask in range(1<<q):
        white=[classes[t][0] for t in range(q) if (mask>>t)&1]
        ok=forces(set(range(4*n))-set(white),N)
        assert ok==(mask!=(1<<q)-1)
print("PROFILE_CLASSIFICATION_OK")
print("VERIFY_OK")
