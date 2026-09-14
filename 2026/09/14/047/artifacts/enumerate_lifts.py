"""Enumerate 2-lift signings of small d-regular bipartite bases.
Measure P(Ramanujan), P(girth increase), P(both).
"""
import itertools
import numpy as np
import networkx as nx

def signed_lift_spectrum(G, edges, signs):
    # G: nx Graph, edges: list of (u,v), signs: list of +-1
    # Build lift adjacency (2n x 2n) and compute spectrum
    n = G.number_of_nodes()
    nodes = list(G.nodes())
    idx = {v:i for i,v in enumerate(nodes)}
    N = 2*n
    A = np.zeros((N,N))
    for (u,v),s in zip(edges, signs):
        iu, iv = idx[u], idx[v]
        if s == 1:
            A[iu, iv] += 1; A[iv, iu] += 1
            A[iu+n, iv+n] += 1; A[iv+n, iu+n] += 1
        else:
            A[iu, iv+n] += 1; A[iv+n, iu] += 1
            A[iu+n, iv] += 1; A[iv, iu+n] += 1
    w = np.linalg.eigvalsh(A)
    return w

def signed_adj_spectrum(G, edges, signs):
    n = G.number_of_nodes()
    nodes = list(G.nodes())
    idx = {v:i for i,v in enumerate(nodes)}
    As = np.zeros((n,n))
    for (u,v),s in zip(edges, signs):
        iu, iv = idx[u], idx[v]
        As[iu,iv] += s; As[iv,iu] += s
    w = np.linalg.eigvalsh(As)
    return w

def lift_graph(G, edges, signs):
    # return networkx lift graph with nodes (v,k)
    H = nx.Graph()
    nodes = list(G.nodes())
    for v in nodes:
        H.add_node((v,0)); H.add_node((v,1))
    for (u,v),s in zip(edges, signs):
        if s==1:
            H.add_edge((u,0),(v,0)); H.add_edge((u,1),(v,1))
        else:
            H.add_edge((u,0),(v,1)); H.add_edge((u,1),(v,0))
    return H

def girth(G):
    # shortest cycle length; inf if forest
    # BFS from each node, find shortest cycle
    best = float('inf')
    nodes = list(G.nodes())
    for s in nodes:
        # BFS tree with parent tracking for cycle detection (unweighted)
        # standard: BFS, when encountering visited neighbor not parent, cycle len = dist[u]+dist[v]+1
        dist = {s:0}
        parent = {s:None}
        from collections import deque
        q = deque([s])
        order = [s]
        while q:
            u = q.popleft()
            for w in G.neighbors(u):
                if w not in dist:
                    dist[w]=dist[u]+1; parent[w]=u; q.append(w)
                elif parent[u]!=w and dist[w]<=dist[u]:
                    # found cycle; avoid trivial back edge; dist condition avoids double count but keep min
                    c = dist[u]+dist[w]+1
                    if c<best: best=c
        if best==3: return 3
    return best

def enumerate_base(G, name, ramanujan_bound, limit=None):
    edges = list(G.edges())
    m = len(edges)
    g0 = girth(G)
    print(f"=== {name}: n={G.number_of_nodes()}, m={m}, girth={g0}, bound={ramanujan_bound:.4f}")
    total=0; ram=0; gir=0; both=0
    both_examples=[]
    # for m up to ~15 enumerate all; else sample
    if m<=20:
        it = itertools.product([1,-1], repeat=m)
        N = 2**m
    else:
        import random
        N = 2000
        it = ([1 if random.random()<0.5 else -1 for _ in range(m)] for _ in range(N))
    for signs in it:
        signs=list(signs)
        total+=1
        ws = signed_adj_spectrum(G, edges, signs)
        r = max(abs(ws))
        is_ram = (r <= ramanujan_bound + 1e-8)
        H = lift_graph(G, edges, signs)
        gh = girth(H)
        is_gir = (gh is not None and gh>g0)
        ram+=is_ram; gir+=is_gir; both+=(is_ram and is_gir)
        if is_ram and is_gir and len(both_examples)<3:
            both_examples.append((tuple(signs), float(r), gh))
        # connectivity check for both examples later
    print(f"total={total} P(ram)={ram/total:.4f} P(gir+)={gir/total:.4f} P(both)={both/total:.4f}")
    for e in both_examples:
        print("  both ex:", e)
    return total,ram,gir,both

import math
# K3,3
K33 = nx.complete_bipartite_graph(3,3)
enumerate_base(K33, "K3,3 d=3", 2*math.sqrt(2))
# cube
Q3 = nx.cubical_graph()
enumerate_base(Q3, "Q3 cube d=3", 2*math.sqrt(2))
# K4,4 (m=16, 2^16=65536, feasible but eig per signing heavy; sample)
K44 = nx.complete_bipartite_graph(4,4)
enumerate_base(K44, "K4,4 d=4", 2*math.sqrt(3))
