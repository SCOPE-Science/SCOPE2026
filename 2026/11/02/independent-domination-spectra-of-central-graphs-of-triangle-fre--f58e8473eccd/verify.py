"""Reproducible finite checks for maximal-independent-set polynomial of central graphs.
Uses Python's standard library only; no external data or dependencies.
"""
from collections import Counter


def graph_data(n,mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    edges=[p for k,p in enumerate(pairs) if mask>>k&1]
    nb=[0]*n
    for i,j in edges:
        nb[i]|=1<<j;nb[j]|=1<<i
    return edges,nb


def connected(nb):
    n=len(nb); seen=1;todo=1
    while todo:
        b=todo&-todo;todo-=b;v=b.bit_length()-1
        x=nb[v]&~seen;seen|=x;todo|=x
    return seen==(1<<n)-1


def triangle_free(nb):
    return all(not (nb[u]&nb[v]) for u in range(len(nb)) for v in range(u+1,len(nb)) if nb[u]>>v&1)


def central_complement_neighbors(n,edges,nb):
    m=len(edges);N=n+m; h=[0]*N
    for e,(u,v) in enumerate(edges):
        w=n+e; h[w]|=(1<<u)|(1<<v);h[u]|=1<<w;h[v]|=1<<w
    for u in range(n):
        for v in range(u+1,n):
            if not nb[u]>>v&1: h[u]|=1<<v;h[v]|=1<<u
    full=(1<<N)-1
    return [full^(1<<i)^h[i] for i in range(N)]


def maximal_clique_size_polynomial(adj):
    full=(1<<len(adj))-1; out=Counter()
    def bronk(r,p,x):
        if not (p|x):
            out[r.bit_count()]+=1;return
        uv=p|x; pivot=-1;score=-1
        while uv:
            b=uv&-uv;uv-=b;u=b.bit_length()-1
            s=(p&adj[u]).bit_count()
            if s>score:score=s;pivot=u
        cand=p&~adj[pivot]
        while cand:
            b=cand&-cand;cand-=b;v=b.bit_length()-1
            bronk(r|b,p&adj[v],x&adj[v]);p^=b;x|=b
    bronk(0,full,0)
    return +out


def theorem(n,edges,nb):
    m=len(edges);deg=[x.bit_count() for x in nb]
    sup={u for u in range(n) if any(deg[v]==1 for v in range(n) if nb[u]>>v&1)}
    p=Counter({m:1})
    for u in range(n):
        if u not in sup:p[m+1-deg[u]]+=1
    for u,v in edges:p[m+3-deg[u]-deg[v]]+=1
    q=max(deg[u]+deg[v] for u,v in edges)
    if n>=3:
        assert min(p)==m+3-q
        minn=sum(deg[u]+deg[v]==q for u,v in edges)+sum(u not in sup and deg[u]==q-2 for u in range(n))+(q==3)
        assert p[min(p)]==minn
    assert sum(p.values())==m+n+1-len(sup)
    return +p


def run():
    graph_count=0
    for n in range(2,7):
        all_masks=1<<(n*(n-1)//2)
        for mask in range(all_masks):
            edges,nb=graph_data(n,mask)
            if not edges or not connected(nb) or not triangle_free(nb):continue
            p=theorem(n,edges,nb)
            direct=maximal_clique_size_polynomial(central_complement_neighbors(n,edges,nb))
            assert p==direct,(n,mask,p,direct)
            graph_count+=1
    # One larger regular cubic bipartite graph, and a longer cycle.
    samples=[(8,[(i,(i+1)%8) for i in range(8)]),
             (8,[(i,j) for i in range(4) for j in range(4,8)]),
             (10,[(i,(i+1)%10) for i in range(10)])]
    for n,edges in samples:
        nb=[0]*n
        for i,j in edges:nb[i]|=1<<j;nb[j]|=1<<i
        assert theorem(n,edges,nb)==maximal_clique_size_polynomial(central_complement_neighbors(n,edges,nb))
    print('VERIFY_OK all_connected_labelled_triangle_free_orders_2_to_6=',graph_count,
          ' larger_samples=',len(samples), ' all_coefficients_matched=True',sep='')
if __name__=='__main__':run()
