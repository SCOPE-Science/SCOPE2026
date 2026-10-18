"""Finite independent checks for maximal-rectangle / maximal-independent-set identity
and the first three terms in the colored-tree component expansion.
Uses standard Python only; not a proof of the infinite asymptotic theorem.
"""
from itertools import combinations
from math import factorial, log


def mis_count(a,b, edges):
    n=a+b
    edge_mask=[(1<<u)|(1<<(a+v)) for u,v in edges]
    adj=[0]*n
    for u,v in edges:
        adj[u]|=1<<(a+v)
        adj[a+v]|=1<<u
    ans=0
    for mask in range(1<<n):
        if any(mask & em == em for em in edge_mask):
            continue
        if all((mask & (1<<u)) or (mask & adj[u]) for u in range(n)):
            ans+=1
    return ans


def concept_count(a,b, forbidden_edges):
    # Start directly from Galois derivation. forbidden edges are non-incidences.
    bad=set(forbidden_edges)
    out=set()
    for extent in range(1<<a):
        intent=sum(1<<j for j in range(b) if all((i,j) not in bad for i in range(a) if (extent>>i)&1))
        final_extent=sum(1<<i for i in range(a) if all((i,j) not in bad for j in range(b) if (intent>>j)&1))
        if final_extent==extent:
            out.add((extent,intent))
    return len(out)


def connected_tree(a,b,edges):
    if len(edges)!=a+b-1: return False
    vertices={0}
    adj={i:set() for i in range(a+b)}
    for u,v in edges:
        adj[u].add(a+v); adj[a+v].add(u)
    frontier=[0]
    for u in frontier:
        for v in adj[u]:
            if v not in vertices:vertices.add(v);frontier.append(v)
    return len(vertices)==a+b


def tree_dp_count(a,b,edges):
    n=a+b
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(a+v);adj[a+v].append(u)
    def walk(v,parent):
        vals=[walk(w,v) for w in adj[v] if w!=parent]
        in_set=1
        out_but_dominated=1
        out_undominated=1
        for A,B,C in vals:
            in_set*=B+C
            out_but_dominated*=A+B
            out_undominated*=B
        return in_set,out_but_dominated-out_undominated,out_undominated
    A,B,C=walk(0,-1)
    return A+B


def test():
    instances=0
    for a in range(1,5):
        for b in range(1,5):
            # exhaustive up to 3x3; sampling deterministic 4-side instances
            if a*b>9:continue
            all_edges=[(i,j) for i in range(a) for j in range(b)]
            for bits in range(1<<(a*b)):
                e=[p for i,p in enumerate(all_edges) if bits>>i&1]
                x=concept_count(a,b,e)
                y=mis_count(a,b,e)
                assert x==y,(a,b,bits,x,y)
                instances+=1
    # independent check of low-tree coefficients via all labelled bipartite trees
    coefficients={}
    n_trees={}
    for v in (2,3,4):
        s=0.0; num=0
        for a in range(1,v):
            b=v-a
            all_edges=[(i,j) for i in range(a) for j in range(b)]
            for edges in combinations(all_edges,v-1):
                if not connected_tree(a,b,edges):continue
                num+=1
                assert tree_dp_count(a,b,edges)==mis_count(a,b,edges)
                s+=log(mis_count(a,b,edges))/(factorial(a)*factorial(b))
        coefficients[v]=s;n_trees[v]=num
    assert abs(coefficients[2]-log(2))<1e-11,coefficients
    assert abs(coefficients[3]-log(2))<1e-11,coefficients
    assert abs(coefficients[4]-(log(3)+log(2)/3))<1e-11,coefficients
    print('VERIFY_OK: exact FCA/MIS identities',instances,'; weighted bipartite spanning trees',n_trees,'; low order',coefficients)

if __name__=='__main__':test()
