#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import comb

# Type order:
# C1,C2,C3 are the singleton Boolean types {1},{2},{3}.
# L1,L2,L3 are the opposite doubleton types {2,3},{1,3},{1,2}.
TYPE_NEIGHBORS = [
    {1,2,3},
    {0,2,4},
    {0,1,5},
    {0},
    {1},
    {2},
]

def weights(l1,l2,l3):
    return [l1,l2,l3,l2*l3,l1*l3,l1*l2]

def blowup_graph(ls):
    w=weights(*ls)
    cls=[]
    for t,s in enumerate(w):
        cls += [t]*s
    N=[set() for _ in cls]
    for i in range(len(cls)):
        for j in range(i+1,len(cls)):
            if cls[j] in TYPE_NEIGHBORS[cls[i]]:
                N[i].add(j);N[j].add(i)
    return w,cls,N

def direct_chain_product_graph(ls):
    # Models Z/(p^ell_1) x Z/(q^ell_2) x Z/(r^ell_3) at the ideal level.
    # In a length-ell chain ring, ideals are indexed by 0..ell,
    # with 0=whole ring and positive exponents proper.
    a,b,c=ls
    V=[]
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                # proper, and not contained in the Jacobson radical
                if (i,j,k)!=(0,0,0) and 0 in (i,j,k):
                    V.append((i,j,k))
    N=[set() for _ in V]
    for x in range(len(V)):
        for y in range(x+1,len(V)):
            # Sum is whole ring iff in each coordinate one ideal is whole.
            if all(V[x][r]==0 or V[y][r]==0 for r in range(3)):
                N[x].add(y);N[y].add(x)
    return V,N

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

def brute_polynomial(N):
    n=len(N); out={}
    for k in range(n+1):
        c=0
        for S in combinations(range(n),k):
            if zero_forces(S,N):
                c+=1
        if c:
            out[k]=c
    return out

def factorized_polynomial(ls):
    w=weights(*ls)
    N=sum(w)
    # u^(N-6) product_i (u+w_i)
    coeff={N-6:1}
    # Easier: expand product in local degree then shift.
    q={0:1}
    for s in w:
        nq={}
        for d,c in q.items():
            nq[d+1]=nq.get(d+1,0)+c
            nq[d]=nq.get(d,0)+c*s
        q=nq
    return {N-6+d:c for d,c in q.items() if c}

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=0; c=0
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

def adjacency_matrix(N):
    n=len(N)
    return [[1 if j in N[i] else 0 for j in range(n)] for i in range(n)]

def recover_triple_from_roots(root_abs):
    vals=sorted(root_abs)
    a,b=vals[0],vals[1]
    prod=1
    for x in vals:
        prod*=x
    # Exact integer cube root in tested range.
    P=round(prod**(1/3))
    while (P+1)**3<=prod: P+=1
    while P**3>prod: P-=1
    assert P**3==prod
    c=P//(a*b)
    assert a*b*c==P
    return tuple(sorted((a,b,c)))

# Quotient B3 adjacency is invertible.
HQ=[[0]*6 for _ in range(6)]
for i in range(6):
    for j in TYPE_NEIGHBORS[i]:
        HQ[i][j]=1
assert rank_fraction(HQ)==6

# Direct ring-level structure and full polynomial checks.
for ls in [(1,1,2),(1,2,2),(2,2,2)]:
    w,cls,N=blowup_graph(ls)
    Vd,Nd=direct_chain_product_graph(ls)
    assert len(Vd)==len(N)
    # Identify direct vertices by their positive-coordinate support and compare
    # the resulting type-level pattern.
    dtypes=[]
    for v in Vd:
        S={i for i,x in enumerate(v) if x>0}
        if S=={0}: t=0
        elif S=={1}: t=1
        elif S=={2}: t=2
        elif S=={1,2}: t=3
        elif S=={0,2}: t=4
        elif S=={0,1}: t=5
        else: raise AssertionError(v)
        dtypes.append(t)
    assert [dtypes.count(t) for t in range(6)]==w
    for i in range(len(Vd)):
        for j in range(i+1,len(Vd)):
            expected=dtypes[j] in TYPE_NEIGHBORS[dtypes[i]]
            assert ((j in Nd[i])==expected)
    brute=brute_polynomial(N)
    pred=factorized_polynomial(ls)
    assert brute==pred,(ls,brute,pred)
    Z=min(brute)
    assert Z==len(N)-6
    assert brute[Z]==(ls[0]*ls[1]*ls[2])**3
    A=adjacency_matrix(N)
    assert rank_fraction(A)==6
    print(f"l={ls}: weights={w}, N={len(N)}, Z={Z}, min_sets={brute[Z]}, adjacency_rank=6")

# Parameter recovery from the six nonzero roots.
for a in range(1,9):
    for b in range(a,9):
        for c in range(b,9):
            if (a,b,c)==(1,1,1):
                continue
            roots=weights(a,b,c)
            assert recover_triple_from_roots(roots)==(a,b,c)
print("RECOVERY_CENSUS_OK")

# Check that every at-most-one-white-per-type profile forces in a boundary
# case with two field factors; this is the least redundant regime.
ls=(1,1,3)
w,cls,N=blowup_graph(ls)
classes=[set(i for i,t in enumerate(cls) if t==c) for c in range(6)]
for mask in range(1<<6):
    white=[]
    ways=1
    for c in range(6):
        if (mask>>c)&1:
            # use a fixed representative; twins make the choice immaterial
            white.append(min(classes[c]))
    blue=set(range(len(N)))-set(white)
    assert zero_forces(blue,N),mask
print("ALL_64_PROFILES_FORCE_OK")
print("VERIFY_OK")
