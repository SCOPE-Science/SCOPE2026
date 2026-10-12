#!/usr/bin/env python3
from math import gcd
from itertools import combinations
from fractions import Fraction

def direct_graph(p,q):
    n=p*p*q
    V=[x for x in range(1,n) if gcd(x,n)>1]
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if (x*V[j])%n==0:
                N[i].add(j); N[j].add(i)
    return V,N

def typ(x,p,q):
    g=gcd(x,p*p*q)
    if g==p: return 0  # A
    if g==p*q: return 1  # B
    if g==p*p: return 2  # C
    if g==q: return 3  # D
    raise AssertionError((x,g,p,q))

def expected_sizes(p,q):
    return [(p-1)*(q-1), p-1, q-1, p*(p-1)]

def expected_type_edge(t,u):
    if t==u:
        return t==1
    return frozenset((t,u)) in {frozenset((0,1)),frozenset((1,2)),frozenset((2,3))}

def zero_forces(S,N):
    blue=set(S)
    while True:
        if len(blue)==len(N):
            return True
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=next(iter(W)); break
        if move is None:
            return False
        blue.add(move)

def brute_poly(N):
    out={}
    n=len(N)
    for k in range(n+1):
        c=0
        for S in combinations(range(n),k):
            if zero_forces(S,N):
                c+=1
        if c:
            out[k]=c
    return out

def mul_poly(P,Q):
    out={}
    for i,a in P.items():
        for j,b in Q.items():
            out[i+j]=out.get(i+j,0)+a*b
    return out

def predicted_poly(p,q):
    a,b,c,d=expected_sizes(p,q)
    N=a+b+c+d
    P={N-4:1}
    for w in (a,b,c,d):
        P=mul_poly(P,{1:1,0:w})
    return {k:v for k,v in P.items() if v}

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=c=0
    while r<m and c<n:
        pivot=next((i for i in range(r,m) if A[i][c]),None)
        if pivot is None:
            c+=1; continue
        A[r],A[pivot]=A[pivot],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1; c+=1
    return r

def rank_witness(V,N,p,q):
    T=[typ(x,p,q) for x in V]
    Q=[
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,1],
        [0,0,1,0],
    ]
    M=[[Q[T[i]][T[j]] for j in range(len(V))] for i in range(len(V))]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            assert ((M[i][j]!=0)==(j in N[i]))
    assert rank_fraction(M)==4
    return 4

def check_pair(p,q, exhaustive):
    assert p!=q
    V,N=direct_graph(p,q)
    T=[typ(x,p,q) for x in V]
    sz=[T.count(t) for t in range(4)]
    assert sz==expected_sizes(p,q),(p,q,sz,expected_sizes(p,q))
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            assert ((j in N[i])==expected_type_edge(T[i],T[j])),(p,q,V[i],V[j],T[i],T[j])
    r=rank_witness(V,N,p,q)
    pred=predicted_poly(p,q)
    z=min(pred)
    assert z==len(V)-4
    assert pred[z]==p*(p-1)**3*(q-1)**2
    if exhaustive:
        brute=brute_poly(N)
        assert brute==pred,(p,q,brute,pred)
        print(f"p={p}, q={q}: N={len(V)}, polynomial={brute}, witness_rank={r}")
    else:
        print(f"p={p}, q={q}: N={len(V)}, predicted_polynomial={pred}, witness_rank={r}")
    # Type-profile sufficiency: leave <=1 representative per class.
    classes=[[i for i,t in enumerate(T) if t==c] for c in range(4)]
    for mask in range(1<<4):
        white=[]
        for c in range(4):
            if (mask>>c)&1:
                white.append(classes[c][0])
        blue=set(range(len(V)))-set(white)
        assert zero_forces(blue,N),(p,q,mask)
    return True

for p,q,ex in [(2,3,True),(3,2,True),(2,5,True),(3,5,False),(5,2,False)]:
    check_pair(p,q,ex)

print("ALL_16_TYPE_PROFILES_FORCE_OK")
print("VERIFY_OK")
