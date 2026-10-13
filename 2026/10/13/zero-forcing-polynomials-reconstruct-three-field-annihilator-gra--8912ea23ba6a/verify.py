#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter
from fractions import Fraction
from math import prod, isqrt

ADJ={
    1:{2,3,6}, 2:{1,3,5}, 3:{1,2,4},
    4:{3,5,6}, 5:{2,4,6}, 6:{1,4,5},
}

def profile_forces(white_types):
    W=set(white_types)
    while W:
        move=None
        for t in range(1,7):
            nbr=ADJ[t] & W
            if len(nbr)==1:
                move=next(iter(nbr))
                break
        if move is None:
            return False
        W.remove(move)
    return True

def weights(qs):
    x1,x2,x3=[q-1 for q in qs]
    return [x2*x3,x1*x3,x1*x2,x3,x2,x1]

def weighted_coefficients(qs):
    w=weights(qs)
    N=sum(w)
    out={}
    for k in range(7):
        c=0
        for I in combinations(range(6),k):
            if profile_forces([i+1 for i in I]):
                c += prod(w[i] for i in I)
        if c:
            out[N-k]=c
    return out

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

def blowup_graph(qs):
    w=weights(qs)
    cls=[]
    for t,s in enumerate(w,1):
        cls += [t]*s
    N=[set() for _ in cls]
    for i in range(len(cls)):
        for j in range(i+1,len(cls)):
            if cls[j] in ADJ[cls[i]]:
                N[i].add(j); N[j].add(i)
    return w,cls,N

def brute_polynomial(N):
    n=len(N); out={}
    for k in range(n+1):
        c=0
        for S in combinations(range(n),k):
            if zero_forces(S,N):
                c+=1
        if c: out[k]=c
    return out

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1; continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1; c+=1
    return r

def direct_prime_field_graph(qs):
    # This direct ring-level check is used only for prime q_i.
    elems=list(product(*[range(q) for q in qs]))
    zero=tuple(0 for _ in qs)
    units=[x for x in elems if all(a!=0 for a in x)]
    V=[x for x in elems if x!=zero and x not in units]
    def mul(x,y):
        return tuple((x[i]*y[i])%qs[i] for i in range(3))
    def annihilator(x):
        return frozenset(r for r in elems if mul(r,x)==zero)
    anns={x:annihilator(x) for x in V}
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            xy=mul(x,y)
            annxy=annihilator(xy)
            if annxy != (anns[x] | anns[y]):
                N[i].add(j);N[j].add(i)
    return V,N

def class_type(x):
    nz=tuple(i for i,a in enumerate(x) if a!=0)
    return {
        (1,2):1,(0,2):2,(0,1):3,
        (2,):4,(1,):5,(0,):6,
    }[nz]

def recover(coeff):
    N=max(coeff)
    c2=coeff[N-2]; c4=coeff[N-4]
    D=c2*c2-12*c4
    d=isqrt(D); assert d*d==D
    assert (c2-d)%6==0
    s3=(c2-d)//6
    assert 3*s3*s3-c2*s3+c4==0
    # The other rational root is larger because c2-6*s3>0.
    assert c2-6*s3>0
    E=(N+s3-1)**2-4*(c2-N)
    e=isqrt(E); assert e*e==E
    roots1=[(N+s3-1-e)//2,(N+s3-1+e)//2]
    assert all(t*t-(N+s3-1)*t+(c2-N)==0 for t in roots1)
    s1=min(roots1); s2=N-s1
    vals=[]
    # Exact small integer root recovery from the cubic.
    for x in range(2,s1+1):
        while x**3-s1*x*x+s2*x-s3==0 and len(vals)<3:
            vals.append(x)
            # repeated roots handled below by synthetic division outside this shortcut
            break
    # robust brute multiset search in tested range
    candidates=[]
    for a in range(2,s1+1):
        for b in range(a,s1+1):
            c=s1-a-b
            if c<b: continue
            if a*b+a*c+b*c==s2 and a*b*c==s3:
                candidates.append((a,b,c))
    assert len(candidates)==1,candidates
    return tuple(x+1 for x in candidates[0])

# Exact six-type forcing census.
census=Counter(); bad4=[]
for k in range(7):
    for W in combinations(range(1,7),k):
        if profile_forces(W):
            census[k]+=1
        elif k==4:
            bad4.append(W)
assert census==Counter({0:1,1:6,2:15,3:20,4:12})
assert bad4==[(1,2,5,6),(1,3,4,6),(2,3,4,5)]
print("PROFILE_CENSUS_OK",dict(sorted(census.items())),bad4)

# Equal small case: exhaustive full graph census from scratch.
w,cls,N=blowup_graph((3,3,3))
brute=brute_polynomial(N)
pred=weighted_coefficients((3,3,3))
assert brute==pred,(brute,pred)
assert min(brute)==14
print("FULL_BRUTE_F3_CUBE_OK",brute)

# Direct unequal ring-level adjacency using F_3 x F_3 x F_5.
V,Nd=direct_prime_field_graph((3,3,5))
w,cls,Na=blowup_graph((3,3,5))
types=[class_type(x) for x in V]
assert [types.count(i) for i in range(1,7)]==w
for i in range(len(V)):
    for j in range(i+1,len(V)):
        expected=types[j] in ADJ[types[i]]
        assert ((j in Nd[i])==expected)
print("DIRECT_UNEQUAL_F3_F3_F5_OK",w,len(V))

# Rank four quotient and representative blowups.
B=[[1 if j+1 in ADJ[i+1] else 0 for j in range(6)] for i in range(6)]
assert rank_fraction(B)==4
for qs in [(3,3,3),(3,3,5),(3,5,7)]:
    w,cls,N=blowup_graph(qs)
    A=[[1 if j in N[i] else 0 for j in range(len(N))] for i in range(len(N))]
    assert rank_fraction(A)==4
print("RANK_FOUR_OK")

# Formula identities and reconstruction, including repeated and unequal orders.
for qs in [(3,3,3),(3,3,5),(3,5,7),(4,5,9),(5,7,11)]:
    coeff=weighted_coefficients(qs)
    N=max(coeff); w=weights(qs)
    x=[q-1 for q in qs]
    s1=sum(x); s2=sum(x[i]*x[j] for i in range(3) for j in range(i+1,3)); s3=prod(x)
    assert coeff[N-2]==s1*s2+s1*s3+s2
    assert coeff[N-4]==s3*(coeff[N-2]-3*s3)
    got=recover(coeff)
    assert got==tuple(sorted(qs)),(qs,got)
    print("RECOVER",qs,"->",got,"coeff_min",coeff[N-4])

print("VERIFY_OK")
