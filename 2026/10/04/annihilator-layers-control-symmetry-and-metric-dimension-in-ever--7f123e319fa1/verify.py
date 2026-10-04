#!/usr/bin/env python3
from itertools import combinations, product
from collections import deque

def chain_graph(q, ell):
    # abstract vertices by valuation layer i and local index a
    V=[]
    for i in range(1, ell):
        size=(q-1)*(q**(ell-i-1))
        V += [(i,a) for a in range(size)]
    adj={v:set() for v in V}
    for k,u in enumerate(V):
        for v in V[k+1:]:
            if u[0] + v[0] >= ell:
                adj[u].add(v); adj[v].add(u)
    return V,adj

def expected_degree(q,ell,i):
    return q**i - 1 if 2*i < ell else q**i - 2

def distances(V,adj,s):
    d={s:0}; Q=deque([s])
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v]=d[u]+1; Q.append(v)
    return d

def resolves(V,adj,W):
    ds={w:distances(V,adj,w) for w in W}
    seen={}
    for v in V:
        sig=tuple(ds[w].get(v,10**9) for w in W)
        if sig in seen:
            return False
        seen[sig]=v
    return True

def brute_metric_dimension(q,ell):
    V,adj=chain_graph(q,ell)
    n=len(V)
    target=q**(ell-1)-ell
    # prove no set of size < target by exhaustive search only for small n
    for r in range(max(0,target-2), target):
        for W in combinations(V,r):
            assert not resolves(V,adj,W), (q,ell,r,W)
    assert any(resolves(V,adj,W) for W in combinations(V,target))
    return target

def valuation_mod(a,p,ell):
    if a==0: return ell
    i=0
    while a%p==0:
        i+=1; a//=p
    return i

def zmod_graph(p,ell):
    n=p**ell
    V=[a for a in range(1,n) if a%p==0]
    adj={a:set() for a in V}
    for i,a in enumerate(V):
        for b in V[i+1:]:
            if (a*b)%n==0:
                adj[a].add(b); adj[b].add(a)
    vals={a:valuation_mod(a,p,ell) for a in V}
    return V,adj,vals

def trunc_mul(a,b,p,ell):
    out=[0]*ell
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<ell:
                out[i+j]=(out[i+j]+x*y)%p
    return tuple(out)

def trunc_val(a,p,ell):
    for i,x in enumerate(a):
        if x%p:
            return i
    return ell

def trunc_graph(p,ell):
    elems=list(product(range(p), repeat=ell))
    zero=(0,)*ell
    V=[a for a in elems if a!=zero and a[0]==0]
    adj={a:set() for a in V}
    for i,a in enumerate(V):
        for b in V[i+1:]:
            if trunc_mul(a,b,p,ell)==zero:
                adj[a].add(b); adj[b].add(a)
    vals={a:trunc_val(a,p,ell) for a in V}
    return V,adj,vals

def profile(V,adj,vals):
    # layer sizes, degree multiset by layer, and edge-count between layers
    layers={}
    for v in V: layers.setdefault(vals[v],[]).append(v)
    size={i:len(x) for i,x in layers.items()}
    deg={i:sorted(len(adj[v]) for v in x) for i,x in layers.items()}
    edges={}
    ks=sorted(layers)
    for i in ks:
        for j in ks:
            if j<i: continue
            c=0
            A=layers[i]; B=layers[j]
            if i==j:
                for a,b in combinations(A,2):
                    c += b in adj[a]
            else:
                for a in A:
                    for b in B:
                        c += b in adj[a]
            edges[(i,j)]=c
    return size,deg,edges

cases=[(2,2),(2,3),(2,4),(2,5),(3,2),(3,3)]
for q,ell in cases:
    V,adj=chain_graph(q,ell)
    # exact layer sizes/degrees and twin structure
    for i in range(1,ell):
        Li=[v for v in V if v[0]==i]
        assert len(Li)==(q-1)*q**(ell-i-1)
        assert all(len(adj[v])==expected_degree(q,ell,i) for v in Li)
        # same-layer open/closed neighborhoods agree outside the pair
        for a,b in combinations(Li,2):
            assert (adj[a]-{b})==(adj[b]-{a})
    # distinct layers have distinct degrees
    vals=[expected_degree(q,ell,i) for i in range(1,ell)]
    assert len(set(vals))==len(vals)
    # explicit all-but-one-per-layer resolving set
    W=[]
    for i in range(1,ell):
        Li=[v for v in V if v[0]==i]
        W += Li[:-1]
    assert len(W)==q**(ell-1)-ell
    assert resolves(V,adj,W)
    if len(V)<=15:
        assert brute_metric_dimension(q,ell)==q**(ell-1)-ell

# Two nonisomorphic chain rings with same (q,ell) have the same graph profile:
# Z/8Z (characteristic 8) and F_2[x]/(x^3) (characteristic 2).
Vz,Az,vz=zmod_graph(2,3)
Vt,At,vt=trunc_graph(2,3)
assert profile(Vz,Az,vz)==profile(Vt,At,vt)

# Likewise at length 4.
Vz,Az,vz=zmod_graph(2,4)
Vt,At,vt=trunc_graph(2,4)
assert profile(Vz,Az,vz)==profile(Vt,At,vt)

print("VERIFY_OK")
print("abstract_cases=6")
print("metric_dimension_exhaustive_for_all_cases_with_at_most_15_vertices")
print("same_graph_profile=Z8_vs_F2[x]/(x^3)")
print("same_graph_profile=Z16_vs_F2[x]/(x^4)")
