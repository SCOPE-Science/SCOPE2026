#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import prod

def layer_sizes(q,ell):
    return [q**(ell-i-1)*(q-1) for i in range(1,ell)]

def abstract_graph(q,ell):
    sizes=layer_sizes(q,ell)
    cls=[]
    for i,s in enumerate(sizes, start=1):
        cls += [i]*s
    N=[set() for _ in cls]
    for a in range(len(cls)):
        for b in range(a+1,len(cls)):
            if cls[a]+cls[b]>=ell:
                N[a].add(b); N[b].add(a)
    return sizes,cls,N

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

def brute_poly(N):
    out={}
    n=len(N)
    for k in range(n+1):
        c=sum(1 for S in combinations(range(n),k) if zero_forces(S,N))
        if c:
            out[k]=c
    return out

def predicted(q,ell):
    sizes=layer_sizes(q,ell)
    N=sum(sizes)
    if q==2 and ell==2:
        return {1:1}
    P={0:1}
    for s in sizes:
        Q={}
        for d,c in P.items():
            Q[d+1]=Q.get(d+1,0)+c
            Q[d]=Q.get(d,0)+c*s
        P=Q
    shift=N-(ell-1)
    return {shift+d:c for d,c in P.items() if c}

def profile_forces(q,ell,W):
    W=set(W)
    sizes={i:q**(ell-i-1)*(q-1) for i in range(1,ell)}
    while W:
        t=max(W)
        s=ell-t
        # Need a blue representative in source layer s.
        if sizes[s]==1 and s in W:
            return False
        # Source sees exactly white layers j with s+j>=ell, i.e. j>=t.
        seen=[j for j in W if s+j>=ell]
        assert seen==[t],(q,ell,W,s,seen)
        W.remove(t)
    return True

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
        r+=1; c+=1
    return r

def quotient(ell):
    m=ell-1
    return [[1 if (i+1)+(j+1)>=ell else 0 for j in range(m)] for i in range(m)]

def direct_Zpn(p,ell):
    mod=p**ell
    V=[x for x in range(1,mod) if x%p==0]
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if (x*V[j])%mod==0:
                N[i].add(j);N[j].add(i)
    return V,N

# Exact profile theorem through substantial lengths.
for q in (2,3,4,5):
    for ell in range(2,11):
        m=ell-1
        bad=[]
        for mask in range(1<<m):
            W=[i+1 for i in range(m) if (mask>>i)&1]
            ok=profile_forces(q,ell,W)
            if not ok:
                bad.append(tuple(W))
        expected=[(1,)] if (q,ell)==(2,2) else []
        assert bad==expected,(q,ell,bad)
print("PROFILE_THEOREM_OK")

# Quotient rank is ell-1.
for ell in range(2,13):
    Q=quotient(ell)
    assert rank_fraction(Q)==ell-1
print("QUOTIENT_RANK_OK")

# Exhaustive full-polynomial checks where feasible.
for q,ell in [(2,2),(3,2),(2,3),(3,3),(2,4),(2,5)]:
    sizes,cls,N=abstract_graph(q,ell)
    b=brute_poly(N)
    p=predicted(q,ell)
    assert b==p,(q,ell,b,p)
    print(f"(q,ell)=({q},{ell}): sizes={sizes}, N={len(N)}, polynomial={b}")

# Direct ring multiplication checks for Z/(p^ell).
for p,ell in [(2,2),(2,3),(2,4),(3,2),(3,3)]:
    V,Nd=direct_Zpn(p,ell)
    sizes,cls,Na=abstract_graph(p,ell)
    assert len(V)==len(Na)
    # Order direct vertices by p-adic valuation and compare all edges.
    def val(x):
        i=0
        while x%p==0:
            x//=p; i+=1
        return i
    vals=[val(x) for x in V]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            expected=vals[i]+vals[j]>=ell
            assert ((j in Nd[i])==expected)
    print(f"Z/{p**ell}Z direct graph OK: N={len(V)}")

# Parameter recovery from polynomial roots.
for q,ell in [(2,3),(3,2),(3,5),(4,4),(5,6)]:
    roots=sorted(layer_sizes(q,ell))
    rq=min(roots)+1
    rell=len(roots)+1
    assert (rq,rell)==(q,ell)
print("PARAMETER_RECOVERY_OK")
print("VERIFY_OK")
