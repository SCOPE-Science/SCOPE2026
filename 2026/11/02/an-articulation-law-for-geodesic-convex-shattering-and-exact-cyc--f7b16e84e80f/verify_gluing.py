#!/usr/bin/env python3
"""Standalone finite consistency checks for an articulation-shattering identity.
No nonstandard dependencies are required. All graph distances are reconstructed.
"""
from itertools import combinations, permutations
from math import comb
from collections import deque


def dist(n, edges):
    adj = [set() for _ in range(n)]
    for a,b in edges:
        assert a != b
        adj[a].add(b); adj[b].add(a)
    out=[]
    for a in range(n):
        row=[-1]*n; row[a]=0; queue=deque([a])
        while queue:
            x=queue.popleft()
            for y in adj[x]:
                if row[y]<0:
                    row[y]=row[x]+1; queue.append(y)
        assert all(x>=0 for x in row), 'graph must be connected'
        out.append(row)
    return out


def convex_masks(n, edges):
    d=dist(n,edges)
    path_intervals=[]
    for a in range(n):
        for b in range(a+1,n):
            between=sum(1<<v for v in range(n) if d[a][v]+d[v][b]==d[a][b])
            path_intervals.append(((1<<a)|(1<<b),between))
    return [c for c in range(1<<n)
            if all((c & ends)!=ends or (c&inside)==inside
                   for ends,inside in path_intervals)]


def trace_polynomials(n, concepts, root=0):
    """Directly enumerate all support traces; no gluing or cycle formula used."""
    phi=[0]*(n+1)
    psi=[0]*(n+1)
    containing=[c for c in concepts if c & (1<<root)]
    for s in range(1<<n):
        size=s.bit_count()
        want=1<<size
        if len({c&s for c in concepts})==want:
            phi[size]+=1
        if not (s & (1<<root)) and len({c&s for c in containing})==want:
            psi[size]+=1
    return trim(phi),trim(psi)


def trim(x):
    while len(x)>1 and x[-1]==0:
        x.pop()
    return x


def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,c in enumerate(a):out[i]+=c
    for i,c in enumerate(b):out[i]+=c
    return trim(out)


def subtract(a,b):
    out=[0]*max(len(a),len(b))
    for i,c in enumerate(a):out[i]+=c
    for i,c in enumerate(b):out[i]-=c
    return trim(out)


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]+=u*v
    return trim(out)


def wedge(graphs):
    """Each rooted factor is labelled 0,...,n-1 with root 0."""
    edges=[];offset=1
    for n,E in graphs:
        mapping={0:0}
        for x in range(1,n):mapping[x]=offset+x-1
        edges.extend((mapping[a],mapping[b]) for a,b in E)
        offset+=n-1
    return offset,edges


def gluing_prediction(local):
    pred=[1]
    for phi,psi in local:pred=mul(pred,psi)
    for phi,psi in local:pred=add(pred,subtract(phi,psi))
    pred=add(pred,[0,1-len(local)])
    return pred


def cycle(m):
    return m,[(i,(i+1)%m) for i in range(m)]


def cycle_pred(m):
    h=(m-1)//2
    triples=sum(1 for a in range(1,h+1)
                for b in range(1,h+1)
                if 1<=m-a-b<=h)
    assert (m*triples)%3==0
    return trim([1,m,comb(m,2),m*triples//3]),[1,m-1,h*h]


def connected(n,E):
    if n==1:return True
    adj=[set() for _ in range(n)]
    for u,v in E:adj[u].add(v);adj[v].add(u)
    seen={0};stack=[0]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen:seen.add(y);stack.append(y)
    return len(seen)==n


def representative_rooted_graphs():
    reps=[]
    for n in range(1,5):
        pairs=list(combinations(range(n),2))
        seen=set()
        for mask in range(1<<len(pairs)):
            E=[e for k,e in enumerate(pairs) if mask>>k&1]
            if not connected(n,E):continue
            forms=[]
            for p in permutations(range(n)):
                forms.append(tuple(sorted(tuple(sorted((p[u],p[v]))) for u,v in E)))
            key=min(forms)
            if key in seen:continue
            seen.add(key)
            for root in range(n):
                other=[v for v in range(n) if v!=root]
                remap={root:0}
                remap.update({v:i+1 for i,v in enumerate(other)})
                reps.append((n,[(remap[u],remap[v]) for u,v in E]))
    return reps


def check_all():
    for m in range(3,13):
        got=trace_polynomials(m,convex_masks(*cycle(m)))
        expect=cycle_pred(m)
        assert got==expect, ('cycle',m,got,expect)
    print('CYCLE_ROOTED_AND_FULL_PROFILE_PASS m=3..12')
    graphs=representative_rooted_graphs()
    locals_=[trace_polynomials(n,convex_masks(n,E)) for n,E in graphs]
    tests=0
    for i,(n,E) in enumerate(graphs):
        for j,(m,F) in enumerate(graphs):
            N,all_edges=wedge([(n,E),(m,F)])
            observed=trace_polynomials(N,convex_masks(N,all_edges))[0]
            predicted=gluing_prediction([locals_[i],locals_[j]])
            assert observed==predicted, (i,j,observed,predicted)
            tests+=1
    print('ROOTED_GRAPH_PAIR_GLUE_PASS rooted_inputs=%d pairs=%d' % (len(graphs),tests))
    for ms in ((3,4,5),(4,5,6),(5,5),(5,5,5),(3,3,6),(3,6,4)):
        fs=[cycle(m) for m in ms]
        N,E=wedge(fs)
        observed=trace_polynomials(N,convex_masks(N,E))[0]
        predicted=gluing_prediction([cycle_pred(m) for m in ms])
        assert observed==predicted, (ms,observed,predicted)
        if ms==(5,5,5):
            assert observed==[1,13,78,175,240,192,64]
    print('MIXED_CYCLE_BOUQUETS_PASS cases=6')
    print('ALL_ARTICULATION_SHATTERING_CHECKS_PASS')

if __name__=='__main__':
    check_all()
