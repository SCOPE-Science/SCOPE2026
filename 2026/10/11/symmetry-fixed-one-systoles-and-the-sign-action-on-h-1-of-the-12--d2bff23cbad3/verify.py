#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

FACETS = [
(1,2,3,4),(1,2,3,10),(1,2,4,9),(1,2,5,6),(1,2,5,9),(1,2,6,11),(1,2,10,11),
(1,3,4,7),(1,3,7,8),(1,3,8,10),(1,4,7,9),(1,5,6,12),(1,5,7,9),(1,5,7,12),
(1,6,11,12),(1,7,8,12),(1,8,10,11),(1,8,11,12),(2,3,4,12),(2,3,10,12),
(2,4,8,9),(2,4,8,12),(2,5,6,8),(2,5,8,9),(2,6,7,8),(2,6,7,11),(2,7,8,12),
(2,7,10,11),(2,7,10,12),(3,4,5,6),(3,4,5,11),(3,4,6,7),(3,4,11,12),(3,5,6,8),
(3,5,8,9),(3,5,9,11),(3,6,7,8),(3,8,9,10),(3,9,10,12),(3,9,11,12),(4,5,6,10),
(4,5,10,11),(4,6,7,9),(4,6,9,10),(4,8,9,10),(4,8,10,11),(4,8,11,12),(5,6,10,12),
(5,7,9,11),(5,7,10,11),(5,7,10,12),(6,7,9,11),(6,9,10,12),(6,9,11,12)
]
G1 = {1:2,2:1,3:6,6:3,4:5,5:4,7:8,8:7,9:9,10:11,11:10,12:12}
G2 = {1:3,3:5,5:1,2:4,4:6,6:2,7:8,8:9,9:7,10:11,11:12,12:10}
MINOR_COLS = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,32,34,36,37,39,40,41,42,43,46,47,48,50,52,53,54,55,61,62,63,65,67,70,71,74,84]

def compose(p,q):
    return {i:p[q[i]] for i in range(1,13)}

def pkey(p): return tuple(p[i] for i in range(1,13))

def group_generated(gens):
    ident={i:i for i in range(1,13)}
    seen={pkey(ident):ident}; stack=[ident]
    while stack:
        a=stack.pop()
        for b in gens:
            c=compose(a,b)
            k=pkey(c)
            if k not in seen:
                seen[k]=c; stack.append(c)
    return list(seen.values())

def perm_set(p,s): return tuple(sorted(p[x] for x in s))

def rank_mod(A,p):
    A=[[x%p for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[(x-z*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def null_left_mod(A,p):
    # nonzero w with w^T A=0, where A is m x n and nullity is one.
    M=[[A[i][j]%p for i in range(len(A))] for j in range(len(A[0]))] # A^T
    rows=len(M); cols=len(M[0]); r=0; piv=[]
    for c in range(cols):
        q=next((i for i in range(r,rows) if M[i][c]),None)
        if q is None: continue
        M[r],M[q]=M[q],M[r]
        inv=pow(M[r][c],-1,p); M[r]=[(x*inv)%p for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]:
                z=M[i][c]; M[i]=[(x-z*y)%p for x,y in zip(M[i],M[r])]
        piv.append(c); r+=1
        if r==rows: break
    free=[c for c in range(cols) if c not in piv]
    assert len(free)==1
    x=[0]*cols; x[free[0]]=1
    for rr in range(r-1,-1,-1):
        c=piv[rr]
        x[c]=(-sum(M[rr][j]*x[j] for j in free))%p
    assert any(x)
    assert all(sum(x[i]*A[i][j] for i in range(cols))%p==0 for j in range(len(A[0])))
    return x

def bareiss_det(M):
    A=[row[:] for row in M]; n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            q=next((i for i in range(k+1,n) if A[i][k]!=0),None)
            if q is None: return 0
            A[k],A[q]=A[q],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        for i in range(k+1,n): A[i][k]=0
        prev=piv
    return sign*A[n-1][n-1]

def tri_chain(t):
    a,b,c=t
    return [((b,c),1),((a,c),-1),((a,b),1)]

def mapped_cycle_coords(t,p,idx):
    v=[0]*len(idx)
    for (u,w),coef in tri_chain(t):
        x,y=p[u],p[w]
        if x>y: x,y=y,x; coef=-coef
        if x!=1:
            v[idx[(x,y)]]+=coef
    return v

F=set(tuple(sorted(f)) for f in FACETS)
assert len(F)==54
V=sorted({x for f in F for x in f}); assert V==list(range(1,13))
E=sorted({e for f in F for e in combinations(f,2)})
T=sorted({t for f in F for t in combinations(f,3)})
assert (len(V),len(E),len(T),len(F))==(12,66,108,54)
assert len(E)==66 # complete one-skeleton

# Fundamental cycle coordinates from star tree at vertex 1.
N=list(combinations(range(2,13),2)); idx={e:i for i,e in enumerate(N)}
A=[[0]*len(T) for _ in range(len(N))]
for j,t in enumerate(T):
    for e,coef in tri_chain(t):
        if 1 not in e: A[idx[e]][j]=coef
minor=[[A[i][j] for j in MINOR_COLS] for i in range(55)]
det=bareiss_det(minor)
assert abs(det)==3,det
r3=rank_mod(A,3); assert r3==54
# Since the full-rank minor has determinant 3, H1 is finite of order dividing 3.
# Since reduction mod 3 has one-dimensional quotient, 3 divides its order.
# Therefore H1 is exactly Z/3.

w=null_left_mod(A,3)
all3=list(combinations(V,3)); Tset=set(T)
missing=[t for t in all3 if t not in Tset]
assert len(missing)==112
vals=[]
for t in missing:
    v=mapped_cycle_coords(t,{i:i for i in V},idx)
    val=sum(a*b for a,b in zip(w,v))%3
    assert val in (1,2)
    vals.append(val)
assert Counter(vals)==Counter({1:56,2:56})

G=group_generated([G1,G2]); assert len(G)==6
for p in G:
    assert {perm_set(p,f) for f in F}==F
# Orbits on missing triangles.
unseen=set(missing); orbits=[]
while unseen:
    t=min(unseen)
    orb={perm_set(p,t) for p in G}
    assert orb <= set(missing)
    orbits.append(sorted(orb)); unseen-=orb
sizes=Counter(map(len,orbits))
assert sizes==Counter({6:15,3:6,2:1,1:2}),sizes
fixed=[t for t in all3 if all(perm_set(p,t)==t for p in G)]
assert fixed==[(7,8,9),(10,11,12)]
assert all(t in set(missing) for t in fixed)

# Homology action: evaluate a fixed essential triangle cycle before/after each generator.
t0=(7,8,9)
v0=mapped_cycle_coords(t0,{i:i for i in V},idx)
e0=sum(a*b for a,b in zip(w,v0))%3; assert e0 in (1,2)
scalars=[]
for p in (G1,G2):
    vp=mapped_cycle_coords(t0,p,idx)
    ep=sum(a*b for a,b in zip(w,vp))%3
    scalars.append((ep*pow(e0,-1,3))%3)
assert scalars==[2,1],scalars
print('VERIFY_OK f=12,66,108,54 H1=Z/3 determinant_minor=-3 rank_mod3=54 missing3=112 essential3=112 values=56,56 aut_group=S3 order=6 missing_orbits=6x15,3x6,2x1,1x2 fixed_triples=7-8-9|10-11-12 action_generators=-1,+1')
