#!/usr/bin/env python3
from itertools import product, combinations

def inv_mod(a,p):
    return pow(a,p-2,p)

def rref_basis(vectors,p,n):
    rows=[list(v) for v in vectors if any(x%p for x in v)]
    r=0
    for c in range(n):
        pivot=next((i for i in range(r,len(rows)) if rows[i][c]%p),None)
        if pivot is None: continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        inv=inv_mod(rows[r][c]%p,p)
        rows[r]=[(x*inv)%p for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]%p:
                a=rows[i][c]%p
                rows[i]=[(rows[i][j]-a*rows[r][j])%p for j in range(n)]
        r+=1
        if r==len(rows): break
    rows=[tuple(row) for row in rows if any(row)]
    return tuple(rows[:r])

def span_from_basis(B,p,n):
    if not B: return frozenset({(0,)*n})
    out=set()
    for coeffs in product(range(p), repeat=len(B)):
        out.add(tuple(sum(coeffs[i]*B[i][j] for i in range(len(B)))%p for j in range(n)))
    return frozenset(out)

def all_subspaces(p,n):
    vecs=[v for v in product(range(p), repeat=n) if any(v)]
    bases={()}
    # Generate canonical row spaces from subsets of size up to n.
    for k in range(1,n+1):
        for comb in combinations(vecs,k):
            B=rref_basis(comb,p,n)
            if len(B)==k:
                bases.add(B)
    return sorted({span_from_basis(B,p,n) for B in bases}, key=lambda S:(len(S),sorted(S)))

def intersection_graph(subspaces, full):
    zero=frozenset({next(iter(full))}) if False else None
    # infer zero vector by length of tuple
    n=len(next(iter(full))); z=(0,)*n
    verts=[S for S in subspaces if S!=frozenset({z}) and S!=full]
    adj=[set() for _ in verts]
    for i,A in enumerate(verts):
        for j in range(i+1,len(verts)):
            B=verts[j]
            if len((A & B)-{z})>0:
                adj[i].add(j); adj[j].add(i)
    return verts,adj

def gamma_t(adj):
    N=len(adj)
    if any(len(a)==0 for a in adj): return None
    for k in range(1,N+1):
        for D in combinations(range(N),k):
            Ds=set(D)
            if all(adj[v] & Ds for v in range(N)):
                return k
    return None

def vector_space_case(p,n,expect):
    subs=all_subspaces(p,n)
    full=frozenset(product(range(p),repeat=n))
    verts,adj=intersection_graph(subs,full)
    got=gamma_t(adj)
    assert got==expect,(p,n,len(subs),len(verts),got,expect)
    return len(subs),len(verts),got

# Homogeneous semisimple stress tests.
results=[]
for p,n,e in [(2,2,None),(2,3,3),(2,4,3),(3,3,4)]:
    results.append((p,n,*vector_space_case(p,n,e)))

# Nonsemisimple uniserial Z/4 and Z/8: vertices are proper nonzero subgroups.
# Z/4: one vertex -> isolated; Z/8: subgroups of orders 2 and 4 intersect nontrivially.
assert gamma_t([set()]) is None
assert gamma_t([{1},{0}])==2

# Mixed semisimple Z-module C2^2 (+) C3. Submodules split as A (+) B,
# with A a subspace of F2^2 and B in {0,C3}.
subs2=all_subspaces(2,2)
zero2=frozenset({(0,0)}); full2=frozenset(product(range(2),repeat=2))
Bparts=[0,1]
verts=[]
for A in subs2:
    for B in Bparts:
        if A==zero2 and B==0: continue
        if A==full2 and B==1: continue
        verts.append((A,B))
adj=[set() for _ in verts]
for i,(A,b) in enumerate(verts):
    for j in range(i+1,len(verts)):
        C,d=verts[j]
        nonzero_A=len((A&C)-{(0,0)})>0
        nonzero_B=(b==1 and d==1)
        if nonzero_A or nonzero_B:
            adj[i].add(j); adj[j].add(i)
assert gamma_t(adj)==2

# Three distinct simple types: C2 (+) C3 (+) C5 is cyclic of order 30.
# Proper nonzero subgroups are uniquely determined by orders 2,3,5,6,10,15;
# intersection order is gcd of subgroup orders.
orders=[2,3,5,6,10,15]
adj=[set() for _ in orders]
import math
for i,a in enumerate(orders):
    for j in range(i+1,len(orders)):
        if math.gcd(a,orders[j])>1:
            adj[i].add(j); adj[j].add(i)
assert gamma_t(adj)==2

print('VERIFY_OK')
for p,n,ns,nv,gt in results:
    print(f'F_{p}^{n}: subspaces={ns}, vertices={nv}, gamma_t={gt}')
print('Z/4Z: total_domination=undefined (isolated vertex)')
print('Z/8Z: gamma_t=2')
print('C2^2 (+) C3: gamma_t=2')
print('C2 (+) C3 (+) C5: gamma_t=2')
