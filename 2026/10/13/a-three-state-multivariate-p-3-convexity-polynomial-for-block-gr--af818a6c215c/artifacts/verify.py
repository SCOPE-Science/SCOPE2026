#!/usr/bin/env python3
"""Exact P3-convex-set polynomial for block graphs; independent brute verification.

Uses only Python's standard library. All graphs have vertices 0,...,n-1.
The algorithm takes finite undirected simple edge lists.
"""
from itertools import combinations
from random import Random


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        if v:
            for j, w in enumerate(b):
                if w: out[i+j] += v * w
    return out


def normalize(a, length=None):
    if length is not None:
        return (a + [0]*length)[:length]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def blocks_and_components(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        if a == b or not (0 <= a < n and 0 <= b < n):
            raise ValueError('not a finite simple graph')
        adj[a].add(b); adj[b].add(a)
    if sum(map(len,adj)) != 2*len(set(tuple(sorted(e)) for e in edges)):
        raise ValueError('duplicate edge')

    time=0
    disc=[-1]*n; low=[0]*n
    estack=[];blocks=[];components=[]
    def dfs(u,parent,comp):
        nonlocal time
        disc[u]=low[u]=time; time+=1
        comp.append(u)
        for v in sorted(adj[u]):
            if disc[v]<0:
                estack.append((u,v))
                dfs(v,u,comp)
                low[u]=min(low[u],low[v])
                if low[v]>=disc[u]:
                    bs=set()
                    while True:
                        e=estack.pop()
                        bs.update(e)
                        if e==(u,v):break
                    blocks.append(tuple(sorted(bs)))
            elif v!=parent and disc[v]<disc[u]:
                low[u]=min(low[u],disc[v])
                estack.append((u,v))
    for u in range(n):
        if disc[u]<0:
            cc=[]
            dfs(u,-1,cc)
            assert not estack
            components.append(tuple(cc))

    for b in blocks:
        if any(v not in adj[u] for u,v in combinations(b,2)):
            raise ValueError('input is not a block graph')
    return adj, blocks, components


def convex_poly_block_graph(n, edges):
    adj,blocks,components=blocks_and_components(n,edges)
    inc=[[] for _ in range(n)]
    for i,B in enumerate(blocks):
        for v in B:inc[v].append(i)

    def vertex(v, parent_block):
        # For v=0: 0 or 1 selected neighbors from descendant blocks.
        # For v=1: arbitrary descendant-neighbor state.
        z0=[1];z1=[0];s=[0,1]
        for b in inc[v]:
            if b==parent_block:continue
            n0,n1,ns=block(b,v)
            z1=add(mul(z1,n0),mul(z0,n1))
            z0=mul(z0,n0)
            s=mul(s,ns)
        return z0,z1,s

    def block(b,parent_v):
        # Counts of selections inside this clique block allowed when parent_v
        # is omitted (with either 0 or 1 selected neighbors) or selected.
        zero=[1];one=[0];all_zero=[1];all_sel=[1]
        for w in blocks[b]:
            if w==parent_v:continue
            m0,m1,ms=vertex(w,b)
            zero=mul(zero, add(m0,m1))
            one=add(mul(one,m0),mul(all_zero,ms))
            all_zero=mul(all_zero,m0)
            all_sel=mul(all_sel,ms)
        return zero,one,add(all_zero,all_sel)

    ans=[1]
    for C in components:
        r=C[0]
        z0,z1,s=vertex(r,None)
        ans=mul(ans,add(add(z0,z1),s))
    return normalize(ans,n+1)


def brute_poly(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    out=[0]*(n+1)
    for bits in range(1<<n):
        if all((bits>>v)&1 or sum((bits>>u)&1 for u in adj[v]) <= 1 for v in range(n)):
            out[bits.bit_count()]+=1
    return out


def edges_of_mask(n,m):
    pairs=list(combinations(range(n),2))
    return [e for i,e in enumerate(pairs) if (m>>i)&1]


def glued_block_graph(rng,max_n):
    # Start with a vertex, glue random cliques at existing articulation vertices.
    n=1;edges=[]
    while n<max_n:
        k=rng.randint(2,min(max_n-n+1,5))
        old=rng.randrange(n)
        fresh=list(range(n,n+k-1))
        B=[old]+fresh
        edges.extend(combinations(B,2))
        n += k-1
    return n,edges


def weighted_partition(n, edges, weights):
    # A scalar evaluation of the multivariate arithmetic circuit.
    _,blocks,components=blocks_and_components(n,edges)
    incidences=[[] for _ in range(n)]
    for k,B in enumerate(blocks):
        for v in B: incidences[v].append(k)

    def vertex(v,parent):
        z0,z1,selected=1,0,weights[v]
        for i in incidences[v]:
            if i==parent: continue
            u0,u1,u_selected=block(i,v)
            z0,z1,selected=(z0*u0,
                            z1*u0+z0*u1,
                            selected*u_selected)
        return z0,z1,selected

    def block(i,parent):
        zero,one,all0,all1=1,0,1,1
        for w in blocks[i]:
            if w==parent: continue
            p,q,r=vertex(w,i)
            zero,one,all0,all1=(zero*(p+q),
                                one*p+all0*r,
                                all0*p,
                                all1*r)
        return zero,one,all0+all1

    ans=1
    for cc in components:
        v=cc[0]
        a,b,c=vertex(v,None)
        ans*=a+b+c
    return ans


def weighted_brute(n,edges,weights):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    total=0
    for mask in range(1<<n):
        if all(((mask>>v)&1) or sum((mask>>u)&1 for u in adj[v])<=1
               for v in range(n)):
            term=1
            for v in range(n):
                if (mask>>v)&1: term*=weights[v]
            total+=term
    return total


def run():
    graph_cases=0;subset_cases=0;block_graphs=0;weighted_cases=0
    for n in range(0,7):
        for m in range(1 << (n*(n-1)//2)):
            edges=edges_of_mask(n,m)
            try:
                f=convex_poly_block_graph(n,edges)
            except ValueError:
                continue
            g=brute_poly(n,edges)
            if f!=g:
                raise AssertionError(('all small graphs',n,edges,f,g))
            graph_cases+=1
            block_graphs+=1
            subset_cases+=(1<<n)
            if graph_cases%17==0:
                wts=[1+((3*v+graph_cases)%7) for v in range(n)]
                if weighted_partition(n,edges,wts)!=weighted_brute(n,edges,wts):
                    raise AssertionError(('weighted labeled',n,edges,wts))
                weighted_cases+=1
    rng=Random(20261008)
    random_cases=0
    for trial in range(700):
        max_n=rng.randint(7,14)
        n,edges=glued_block_graph(rng,max_n)
        f=convex_poly_block_graph(n,edges)
        g=brute_poly(n,edges)
        if f!=g:
            raise AssertionError(('random glue',trial,n,edges,f,g))
        random_cases+=1
        subset_cases+=(1<<n)
        if trial%10==0:
            wts=[1+rng.randrange(7) for _ in range(n)]
            if weighted_partition(n,edges,wts)!=weighted_brute(n,edges,wts):
                raise AssertionError(('weighted glued',n,edges,wts))
            weighted_cases+=1
    # Closed-form check for generalized windmills, independent of DP:
    from math import comb
    for nblades in range(1,11):
        for m in range(2,7):
            total=1+nblades*m
            B=[(0,)+tuple(range(1+j*m,1+(j+1)*m)) for j in range(nblades)]
            edges=set()
            for bs in B:
                edges.update(tuple(sorted(e)) for e in combinations(bs,2))
            f=convex_poly_block_graph(total,sorted(edges))
            expected=[0]*(total+1)
            expected[0]=1; expected[1]=total
            for t in range(1,nblades+1):
                expected[1+m*t]+=comb(nblades,t)
            if f!=expected:
                raise AssertionError(('windmill',nblades,m,f,expected))
    print('ALL CHECKS PASSED; small_labeled_block_graphs='+str(block_graphs)+
          '; random_glued_block_graphs='+str(random_cases)+
          '; vertex_subsets_checked='+str(subset_cases)+
          '; weighted_specializations_checked='+str(weighted_cases)+
          '; generalized_windmill_profiles=60; all_labeled_graphs_n<=6')

if __name__ == '__main__':
    run()
