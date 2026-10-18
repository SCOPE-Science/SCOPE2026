#!/usr/bin/env python3
"""Exact finite checks for facets of matched-edge-deleted biclique metrics.
Only Python standard library. Mathematical proof of all-dimensional result is separate.
"""
from collections import deque, Counter
from math import comb


def graph(p,q,k):
    assert p>=3 and q>=3 and 0<=k<=min(p,q)
    edges=[(i,p+j) for i in range(p) for j in range(q) if not(i==j and i<k)]
    adj=[set() for _ in range(p+q)]
    for i,j in edges: adj[i].add(j);adj[j].add(i)
    order=[0];par={0:None}
    for u in order:
        for v in sorted(adj[u]):
            if v not in par:
                par[v]=u;order.append(v)
    assert len(order)==p+q
    return edges,adj,order,par


def enumerate_facets(p,q,k):
    edges,adj,order,par=graph(p,q,k)
    f=[0]*(p+q);seen=set()
    def rec(idx):
        if idx==len(order):
            candidate=tuple(f)
            assert all(abs(f[a]-f[b])==1 for a,b in edges)
            seen.add(candidate)
            return
        u=order[idx]
        for new in (f[par[u]]-1,f[par[u]]+1):
            if all(abs(new-f[v])==1 for v in adj[u] if v in order[:idx]):
                f[u]=new
                rec(idx+1)
    rec(1)
    return seen


def enumerate_polar_vertices_unrestricted(p,q,k):
    """Independent polar check allowing slack edges before tight-graph rank testing."""
    edges,adj,order,par=graph(p,q,k)
    f=[0]*(p+q);vertices=set()
    def rec(idx):
        if idx==len(order):
            tight=[(a,b) for a,b in edges if abs(f[a]-f[b])==1]
            seen={0};todo=[0]
            for v in todo:
                for a,b in tight:
                    if a==v and b not in seen:seen.add(b);todo.append(b)
                    if b==v and a not in seen:seen.add(a);todo.append(a)
            if len(seen)==p+q:vertices.add(tuple(f))
            return
        u=order[idx]
        for new in (f[par[u]]-1,f[par[u]],f[par[u]]+1):
            if all(abs(new-f[v])<=1 for v in adj[u] if v in order[:idx]):
                f[u]=new;rec(idx+1)
    rec(1)
    return vertices

def orbit_generators(p,q,k):
    n=p+q
    gens=[]
    for start,end in ((0,k),(k,p),(p,p+k),(p+k,n)):
        for i in range(start,end-1):
            # Matched-side permutations must simultaneously permute both endpoints
            if i<k or p<=i<p+k:
                # only construct them once, when traversing X side
                if i>=p:continue
                perm=list(range(n))
                perm[i],perm[i+1]=perm[i+1],perm[i]
                perm[p+i],perm[p+i+1]=perm[p+i+1],perm[p+i]
            else:
                perm=list(range(n));perm[i],perm[i+1]=perm[i+1],perm[i]
            gens.append(tuple(perm))
    if p==q:
        perm=list(range(n))
        for i in range(p):perm[i]=p+i;perm[p+i]=i
        gens.append(tuple(perm))
    return gens


def transformed(v,perm,sign=1):
    # perm old vertex -> new vertex
    w=[0]*len(v)
    for i,j in enumerate(perm): w[j]=sign*v[i]
    b=w[0]
    return tuple(x-b for x in w)


def orbits(p,q,k,fs):
    gens=orbit_generators(p,q,k)
    gens.append(tuple(range(p+q)))
    open_set=set(fs);out=[]
    while open_set:
        v=next(iter(open_set));O={v};todo=[v]
        for w in todo:
            for i,g in enumerate(gens):
                nxt=transformed(w,g,sign=(-1 if i==len(gens)-1 else 1))
                assert nxt in fs,(p,q,k,nxt)
                if nxt not in O:O.add(nxt);todo.append(nxt)
        open_set.difference_update(O)
        out.append(O)
    return out


def closed_form_orbits(p,q,k):
    def a(s,k):return ((k+1)*(s-k+1)+int(k%2==0 and (s-k)%2==0))//2
    if p==q:return a(p,k)+int(k>0)
    return a(p,k)+a(q,k)-1+int(k>0)


def family_class(v,p,q,k):
    xs=v[:p]; ys=v[p:]
    if len(set(xs))==1:return 'X-constant'
    if len(set(ys))==1:return 'Y-constant'
    return 'defect'


def predicted_orbit_sizes(p,q,k):
    def groups(s):
        outcomes=[];seen=set()
        for j in range(k+1):
            for z in range(s-k+1):
                if (j,z) in seen:continue
                partner=(k-j,s-k-z)
                seen.update(((j,z),partner))
                size=comb(k,j)*comb(s-k,z)*(1 if partner==(j,z) else 2)
                outcomes.append((size,(j,z) in ((0,0),(k,s-k))))
        return outcomes
    a,b=groups(p),groups(q)
    if p==q:
        sizes=[2 if is_const else 2*size for size,is_const in a]
    else:
        sizes=[2]+[size for size,is_const in a if not is_const]+[size for size,is_const in b if not is_const]
    if k>0:sizes.append(2*k)
    return sorted(sizes)

def main():
    cases=0;orbit_cases=0
    for p in range(3,7):
        for q in range(p,8):
            for k in range(min(p,q)+1):
                fs=enumerate_facets(p,q,k)
                formula=2**p+2**q-2+2*k
                assert len(fs)==formula,(p,q,k,len(fs),formula)
                # Every non-constant-family facet has a unique removed pair at gap 3.
                special=[f for f in fs if family_class(f,p,q,k)=='defect']
                assert len(special)==2*k,(p,q,k,len(special))
                for f in special:
                    assert sum(abs(f[i]-f[p+i])==3 for i in range(k))==1
                cases+=1
                if p+q<=8:
                    assert enumerate_polar_vertices_unrestricted(p,q,k)==fs, (p,q,k,'polar mismatch')
                if p+q<=11:
                    Oo=orbits(p,q,k,fs)
                    pred=closed_form_orbits(p,q,k)
                    assert len(Oo)==pred,(p,q,k,len(Oo),pred)
                    assert sorted(map(len,Oo))==predicted_orbit_sizes(p,q,k),(p,q,k,sorted(map(len,Oo)),predicted_orbit_sizes(p,q,k))
                    assert sum(map(len,Oo))==formula
                    orbit_cases+=1
    for n in range(3,9):
        assert len(enumerate_facets(n,n,n))==2**(n+1)+2*n-2
    print(f'PASS: {cases} spanning-tree enumerations, unrestricted polar/rank checks at p+q<=8, {orbit_cases} exact symmetry-orbit cross-checks; crown counts n=3..8')

if __name__=='__main__':main()
