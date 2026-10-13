#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

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
    n=len(N)
    for k in range(n+1):
        c=sum(1 for S in combinations(range(n),k) if zero_forces(S,N))
        if c:
            out[k]=c
    return out

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1
            continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1;c+=1
    return r

def direct_product_model(p,s):
    # R = Z/(p^3) x Z/sZ and I = {0} x Z/sZ.
    mod=p**3
    T=list(range(s))
    I={(0,t) for t in T}
    R=[(x,t) for x in range(mod) for t in T]
    def mul(a,b):
        return ((a[0]*b[0])%mod,(a[1]*b[1])%s if s>1 else 0)
    V=[]
    for x in R:
        if x in I:
            continue
        ok=False
        for y in R:
            if y not in I and mul(x,y) in I:
                ok=True; break
        if ok:
            V.append(x)
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if mul(x,V[j]) in I:
                N[i].add(j);N[j].add(i)
    return V,N

def split_model(q,s):
    a=s*(q-1)
    b=s*q*(q-1)
    n=a+b
    N=[set() for _ in range(n)]
    A=set(range(a))
    B=set(range(a,n))
    for i in range(n):
        for j in range(i+1,n):
            edge=(i in A and j in A) or ((i in A) != (j in A))
            if edge:
                N[i].add(j);N[j].add(i)
    return a,b,N

def predicted(q,s):
    a=s*(q-1); b=s*q*(q-1); N=a+b
    return {N-2:a*b,N-1:N,N:1}

def rank_witness(a,b,N):
    # Bilinear form H=[[0,1],[1,1]], B-vertices use (1,0), A-vertices use (0,1).
    n=a+b
    vec=[(0,1)]*a+[(1,0)]*b
    H=((0,1),(1,1))
    M=[]
    for x in vec:
        row=[]
        for y in vec:
            row.append(sum(x[i]*H[i][j]*y[j] for i in range(2) for j in range(2)))
        M.append(row)
    for i in range(n):
        for j in range(i+1,n):
            assert ((M[i][j]!=0)==(j in N[i]))
    assert rank_fraction(M)==2
    return 2

for p,s in [(2,1),(2,2),(2,3),(3,1)]:
    V,Nd=direct_product_model(p,s)
    a,b,Ns=split_model(p,s)
    assert len(V)==a+b
    # classify by p-adic valuation of the first coordinate
    A=[]; B=[]
    for i,(x,t) in enumerate(V):
        if x%(p*p)==0:
            A.append(i)
        else:
            B.append(i)
    assert len(A)==a and len(B)==b
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            expected=((i in A and j in A) or ((i in A)!=(j in A)))
            assert ((j in Nd[i])==expected)
    brute=polynomial(Nd)
    pred=predicted(p,s)
    assert brute==pred,(p,s,brute,pred)
    mr=rank_witness(a,b,Ns)
    print(f"q={p}, s={s}: a={a}, b={b}, polynomial={brute}, witness_rank={mr}")

# Pure parameter check, including nonprime residue-field orders.
for q in (2,3,4,5,8,9):
    for s in (1,2,5):
        a,b,N=split_model(q,s)
        roots=sorted((a,b))
        rq=roots[1]//roots[0]
        rs=roots[0]//(rq-1)
        assert rq==q and rs==s
print("PARAMETER_RECOVERY_OK")
print("VERIFY_OK")
