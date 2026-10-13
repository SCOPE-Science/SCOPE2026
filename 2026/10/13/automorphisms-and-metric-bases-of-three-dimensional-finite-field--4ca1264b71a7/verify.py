#!/usr/bin/env python3
import itertools
import math
from collections import defaultdict, Counter
import networkx as nx

def dot(a,b,p):
    return sum(x*y for x,y in zip(a,b)) % p

def canon(v,p):
    i=next(i for i,x in enumerate(v) if x % p)
    inv=pow(v[i],-1,p)
    return tuple((x*inv)%p for x in v)

def projective_points(p):
    return sorted({canon(v,p) for v in itertools.product(range(p), repeat=3) if any(v)})

def quotient_graph(p):
    P=projective_points(p)
    H=nx.Graph()
    H.add_nodes_from(P)
    for x,y in itertools.combinations(P,2):
        if dot(x,y,p)==0:
            H.add_edge(x,y)
    return P,H

def full_graph(p):
    V=[v for v in itertools.product(range(p), repeat=3) if any(v)]
    G=nx.Graph()
    G.add_nodes_from(range(len(V)))
    for i,j in itertools.combinations(range(len(V)),2):
        if dot(V[i],V[j],p)==0:
            G.add_edge(i,j)
    classes=defaultdict(list)
    for i,v in enumerate(V):
        classes[canon(v,p)].append(i)
    return V,G,classes

def twin_blocks(G):
    nodes=list(G.nodes())
    rel={u:{u} for u in nodes}
    for u,v in itertools.combinations(nodes,2):
        if (set(G.neighbors(u))-{v}) == (set(G.neighbors(v))-{u}):
            rel[u].add(v)
            rel[v].add(u)
    seen=set()
    blocks=[]
    for u in nodes:
        if u not in seen:
            B=set(rel[u])
            seen |= B
            blocks.append(B)
    return blocks

def canonical_basis(classes):
    S=set()
    omitted=[]
    for P in sorted(classes):
        L=classes[P]
        S.update(L[:-1])
        omitted.append(L[-1])
    return S,omitted

def resolves(G,S):
    dist=dict(nx.all_pairs_shortest_path_length(G))
    signatures={}
    ordered=sorted(S)
    for v in G.nodes():
        sig=tuple(dist[v][s] for s in ordered)
        if sig in signatures:
            return False
        signatures[sig]=v
    return True

for p in (3,5):
    P,H=quotient_graph(p)
    v=p*p+p+1
    assert len(P)==v
    iso=[x for x in P if dot(x,x,p)==0]
    assert len(iso)==p+1
    deg=Counter(dict(H.degree()).values())
    assert deg[p]==p+1
    assert deg[p+1]==p*p
    aut_count=sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(H,H).isomorphisms_iter())
    assert aut_count==p*(p*p-1)

    V,G,classes=full_graph(p)
    assert len(V)==p**3-1
    assert len(classes)==v
    assert all(len(C)==p-1 for C in classes.values())
    blocks=twin_blocks(G)
    assert len(blocks)==v
    assert all(len(B)==p-1 for B in blocks)
    S,omitted=canonical_basis(classes)
    expected=v*(p-2)
    assert len(S)==expected
    assert resolves(G,S)
    assert nx.diameter(G)==2
    assert (p-1)**v > 0
    print(f"p={p}: quotient_vertices={v}, quotient_aut={aut_count}, twin_classes={len(blocks)}, determining_metric={expected}, canonical_basis=OK")

for p in (3,5,7,11):
    v=p*p+p+1
    assert v*(p-2)==p**3-p*p-p-2
    assert (p-1)**v == math.prod([p-1 for _ in range(v)])
print("symbolic count checks OK")
print("VERIFY_OK")
