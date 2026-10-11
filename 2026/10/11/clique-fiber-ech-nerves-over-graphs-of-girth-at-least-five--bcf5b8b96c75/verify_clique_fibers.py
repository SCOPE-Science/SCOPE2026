#!/usr/bin/env python3
"""Finite exact collapse and mod-two homology tests for high-girth clique-fiber Čech nerves."""
from itertools import combinations

def path(n):
    return [set(j for j in (i-1,i+1) if 0<=j<n) for i in range(n)]
def cycle(n):
    return [set(((i-1)%n,(i+1)%n)) for i in range(n)]
def star(n):
    return [set(range(1,n))]+[{0} for _ in range(n-1)]
def petersen():
    edges=[(i,(i+1)%5) for i in range(5)] + [(i,i+5) for i in range(5)] + [(i+5,((i+2)%5)+5) for i in range(5)]
    a=[set() for _ in range(10)]
    for x,y in edges:a[x].add(y);a[y].add(x)
    return a

def facet_faces(facets):
    out={0}
    for f in facets:
        s=f
        while s:
            out.add(s);s=(s-1)&f
    return out

def neighborhood_facets(H,m):
    return [sum(1<<(v*m+b) for b in range(m))|sum(1<<(u*m+a) for u in H[v]) for v in range(len(H)) for a in range(m)]

def edge_facets(H,m):
    return [sum(1<<(u*m+b) for b in range(m))|(1<<(v*m+a)) for u in range(len(H)) for v in H[u] for a in range(m)]

def f2_betti(K,N):
    dim={}
    for f in K:
        if f:dim.setdefault(f.bit_count()-1,[]).append(f)
    ranks={}
    for d in range(1,max(dim)+1):
        low={z:i for i,z in enumerate(dim.get(d-1,[]))};piv={}
        for face in dim.get(d,[]):
            s=face;z=0
            while s:
                b=s&-s;s-=b;z^=1<<low[face^b]
            while z:
                t=z.bit_length()-1
                if t in piv:z^=piv[t]
                else:piv[t]=z;break
        ranks[d]=len(piv)
    return {d:len(f)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
            for d,f in dim.items() if len(f)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)}

def test(H,m):
    n=len(H);E=sum(map(len,H))//2; N=n*m
    K=facet_faces(neighborhood_facets(H,m));initial=len(K)
    target=facet_faces(edge_facets(H,m))
    pairs=[]
    for v in range(n):
        for a in range(m):
            neighbors=[u*m+a for u in H[v]]
            free_fiber=[v*m+b for b in range(m) if b!=a]
            pivot=1<<(v*m+a)
            for r in range(2,len(neighbors)+1):
                for L in combinations(neighbors,r):
                    off=sum(1<<t for t in L)
                    for k in range(m):
                        for B in combinations(free_fiber,k):
                            low=off|sum(1<<t for t in B)
                            pairs.append((low,low|pivot))
    assert len(pairs)==m*(2**(m-1))*sum(2**len(a)-len(a)-1 for a in H)
    assert len(set(q for p in pairs for q in p))==2*len(pairs)
    for s,t in sorted(pairs,key=lambda x:-x[0].bit_count()):
        assert s in K and t in K
        cofaces=[s|(1<<v) for v in range(N) if not(s>>v)&1 and (s|(1<<v)) in K]
        assert cofaces==[t],(n,m,s,t,cofaces)
        K.remove(s);K.remove(t)
    assert K==target,(n,m,len(K^target))
    beta=f2_betti(K,N)
    expected={1:E-n+1,2:E*(m-1)**2}
    expected={k:v for k,v in expected.items() if v}
    assert beta==expected,(n,m,beta,expected)
    return initial,len(pairs),len(K)

examples=[('path5',path(5)),('star5',star(6)),('cycle5',cycle(5)),('cycle7',cycle(7)),('Petersen',petersen())]
for name,H in examples:
    for m in (2,3,4):
        before,pairs,after=test(H,m)
        print(f'{name}, clique width {m}: {before} to {after} faces, {pairs} collapse pairs')
print('VERIFY_OK')
