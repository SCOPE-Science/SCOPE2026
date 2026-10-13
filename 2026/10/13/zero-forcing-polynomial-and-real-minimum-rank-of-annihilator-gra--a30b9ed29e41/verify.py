#!/usr/bin/env python3
from itertools import combinations, product
from fractions import Fraction
from math import comb

# Class graph A1,...,A6 from the published product-of-three-fields decomposition.
TYPE_N=[{1,2,5},{0,2,4},{0,1,3},{2,4,5},{1,3,5},{0,3,4}]

def zero_forces(C,N):
    blue=set(C)
    while True:
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=next(iter(W)); break
        if move is None:
            return len(blue)==len(N)
        blue.add(move)

def polynomial(N):
    n=len(N); out={}
    for k in range(n+1):
        c=0
        for C in combinations(range(n),k):
            if zero_forces(C,N): c+=1
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
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1; c+=1
    return r

def type_peels(S):
    W=set(S)
    while W:
        target=None
        for c in range(6):
            x=TYPE_N[c]&W
            if len(x)==1:
                target=next(iter(x)); break
        if target is None: return False
        W.remove(target)
    return True

def predicted(q):
    a=(q-1)**2; b=q-1; N=3*a+3*b
    if q==2:
        return {3:14,4:15,5:6,6:1}
    e2=3*a*a+9*a*b+3*b*b
    e3=a**3+9*a*a*b+9*a*b*b+b**3
    c4=3*a*b*(a+b)**2
    return {N-4:c4,N-3:e3,N-2:e2,N-1:N,N:1}

def blown_graph(q):
    a=(q-1)**2; b=q-1
    sizes=[a,a,a,b,b,b]
    typ=[]
    for c,s in enumerate(sizes): typ += [c]*s
    N=[set() for _ in typ]
    for i in range(len(typ)):
        for j in range(i+1,len(typ)):
            if typ[j] in TYPE_N[typ[i]]:
                N[i].add(j); N[j].add(i)
    return sizes,typ,N

def base_adjacency():
    B=[[0]*6 for _ in range(6)]
    for i in range(6):
        for j in TYPE_N[i]: B[i][j]=1
    return B

def blowup_rank_witness(q):
    sizes,typ,N=blown_graph(q)
    n=len(typ)
    if q==2:
        rawvec=[(1,0,0),(0,1,0),(1,0,1),(1,1,-1),(1,2,3),(0,3,-2)]
        perm=(0,2,4,1,5,3)
        vec=[rawvec[i] for i in perm]
        A=[[sum(x*y for x,y in zip(vec[i],vec[j])) for j in range(6)] for i in range(6)]
        expected=3
    else:
        B=base_adjacency()
        assert rank_fraction(B)==4
        A=[[B[typ[i]][typ[j]] for j in range(n)] for i in range(n)]
        expected=4
    for i in range(n):
        for j in range(i+1,n):
            assert ((A[i][j]!=0)==(j in N[i]))
    assert rank_fraction(A)==expected
    return expected

def ann_direct(x,q):
    elems=list(product(range(q),repeat=3))
    return frozenset(r for r in elems if all((r[i]*x[i])%q==0 for i in range(3)))

def direct_annihilator_graph(q):
    elems=list(product(range(q),repeat=3)); zero=(0,0,0)
    V=[x for x in elems if x!=zero and 0 in x]
    anns={x:ann_direct(x,q) for x in V}
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            xy=tuple((x[k]*y[k])%q for k in range(3))
            if ann_direct(xy,q)!=(anns[x]|anns[y]):
                N[i].add(j);N[j].add(i)
    def typ(x):
        Z=frozenset(i for i,v in enumerate(x) if v==0)
        mapping={frozenset({0}):0,frozenset({1}):1,frozenset({2}):2,
                 frozenset({0,1}):3,frozenset({0,2}):4,frozenset({1,2}):5}
        return mapping[Z]
    T=[typ(x) for x in V]
    return V,T,N

# Type-profile theorem: all subsets through size 3 peel, exactly 12 of 15 size-4 subsets peel, none larger.
counts={k:sum(type_peels(S) for S in combinations(range(6),k)) for k in range(7)}
assert counts=={0:1,1:6,2:15,3:20,4:12,5:0,6:0}
cat={r:0 for r in range(5)}
for S in combinations(range(6),4):
    if type_peels(S): cat[sum(i<3 for i in S)]+=1
assert (cat[1],cat[2],cat[3])==(3,6,3)
print('type_profile_counts=',counts,'size4_Aclass_distribution=',(cat[1],cat[2],cat[3]))

# Direct Badawi-definition checks over F_2^3 and F_3^3.
for q in (2,3):
    V,T,N=direct_annihilator_graph(q)
    sizes=[T.count(i) for i in range(6)]
    a=(q-1)**2; b=q-1
    assert sizes==[a,a,a,b,b,b]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            assert ((j in N[i])==(T[j] in TYPE_N[T[i]]))
    brute=polynomial(N)
    assert brute==predicted(q),(q,brute,predicted(q))
    mr=blowup_rank_witness(q)
    print(f'q={q}: N={len(V)}, class_sizes={sizes}, polynomial={brute}, witness_rank={mr}')

# Larger class-level instances and rank witnesses.
for q in (4,5,7):
    sizes,T,N=blown_graph(q)
    mr=blowup_rank_witness(q)
    print(f'q={q}: N={len(T)}, class_sizes={sizes}, predicted_polynomial={predicted(q)}, witness_rank={mr}')

print('VERIFY_OK')
