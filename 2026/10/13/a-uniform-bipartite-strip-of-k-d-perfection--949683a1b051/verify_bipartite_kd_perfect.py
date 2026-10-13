#!/usr/bin/env python3
"""Finite stress test for the bipartite k,d-perfection strip.

This is not the proof of the theorem.  It directly reconstructs the k-uniform
geodesic hypergraph for small labeled bipartite graphs and checks the defining
chromatic/clique equality on every nonempty induced subgraph.
"""
from itertools import combinations, permutations
from math import ceil


def induced_adj(adj, verts):
    verts = tuple(verts)
    idx = {v:i for i,v in enumerate(verts)}
    out = [set() for _ in verts]
    for i,v in enumerate(verts):
        for w in adj[v]:
            if w in idx:
                out[i].add(idx[w])
    return out


def distances(adj):
    n=len(adj)
    inf=n+1
    D=[[inf]*n for _ in range(n)]
    for s in range(n):
        D[s][s]=0
        q=[s]
        for v in q:
            for w in adj[v]:
                if D[s][w]==inf:
                    D[s][w]=D[s][v]+1
                    q.append(w)
    return D


def geodesic_hyperedges(adj,k,d):
    n=len(adj)
    if k>n:
        return set()
    D=distances(adj)
    edges=set()
    maxL=min(d,n-1)
    # Enumerate oriented simple paths; retain exactly those whose length equals
    # the graph distance between their endpoints, hence are shortest paths.
    for L in range(max(k-1,1), maxL+1):
        for seq in permutations(range(n), L+1):
            if any(seq[i+1] not in adj[seq[i]] for i in range(L)):
                continue
            if D[seq[0]][seq[-1]] != L:
                continue
            for e in combinations(seq,k):
                edges.add(frozenset(e))
    return edges


def omega_kd(n, hedges, k):
    # Every set of size < k is vacuously a k,d-clique.
    best=min(n,k-1)
    for r in range(k,n+1):
        for S in combinations(range(n),r):
            S=set(S)
            ok=True
            for e in combinations(S,k):
                if frozenset(e) not in hedges:
                    ok=False
                    break
            if ok:
                best=r
    return best


def check_induced(adj, original_sides, verts, k, d):
    sub=induced_adj(adj,verts)
    n=len(sub)
    if n==0:
        return
    # Translate inherited bipartition to induced labels.
    side0=set()
    side1=set()
    for new,v in enumerate(verts):
        (side0 if original_sides[v]==0 else side1).add(new)
    hedges=geodesic_hyperedges(sub,k,d)
    # Compute the exact chromatic number here from the hyperedge dichotomy:
    # one color works iff there are no hyperedges; otherwise verify explicitly
    # that the inherited two-coloring has no monochromatic hyperedge.
    if not hedges:
        chi=1
    else:
        for e in hedges:
            if e <= side0 or e <= side1:
                raise AssertionError(("monochromatic geodesic hyperedge", k,d,verts,e))
        chi=2
    omega=omega_kd(n,hedges,k)
    rhs=ceil(omega/(k-1)) if omega else 0
    if chi!=rhs:
        raise AssertionError(("perfection failure",k,d,verts,chi,omega,rhs,hedges))


def main():
    graph_count=0
    induced_count=0
    parameter_checks=0
    nonempty_hypergraph_checks=0
    # Fixed labeled sides of orders a,b.  This includes disconnected graphs,
    # isolated vertices, complete bicliques, cycles, trees, and dense examples.
    for a in range(1,4):
        for b in range(1,4):
            n=a+b
            cross=[(i,a+j) for i in range(a) for j in range(b)]
            sides=[0]*a+[1]*b
            for mask in range(1<<len(cross)):
                graph_count += 1
                adj=[set() for _ in range(n)]
                for t,(u,v) in enumerate(cross):
                    if (mask>>t)&1:
                        adj[u].add(v); adj[v].add(u)
                for smask in range(1,1<<n):
                    verts=[i for i in range(n) if (smask>>i)&1]
                    induced_count += 1
                    for k in range(2,6):
                        for d in range(k-1,2*k-2):  # k-1 <= d <= 2k-3
                            check_induced(adj,sides,verts,k,d)
                            parameter_checks += 1
                            # Cheaply count nontrivial geodesic-hypergraph cases
                            # without relying on this count for correctness.
                            if len(verts)>=k:
                                sub=induced_adj(adj,verts)
                                if geodesic_hyperedges(sub,k,d):
                                    nonempty_hypergraph_checks += 1
    # Arithmetic boundary used in the analytic proof.
    arithmetic_cases=0
    for k in range(2,101):
        for d in range(k-1,2*k-2):
            assert ceil((d+1)/2) <= k-1
            assert ceil((2*k-2)/(k-1)) == 2
            arithmetic_cases += 1
    print("ALL CHECKS PASSED; "
          f"labeled_bipartite_graphs={graph_count}; "
          f"nonempty_induced_subgraphs={induced_count}; "
          f"parameter_checks={parameter_checks}; "
          f"nonempty_geodesic_hypergraph_checks={nonempty_hypergraph_checks}; "
          f"arithmetic_cases={arithmetic_cases}; "
          "side_sizes=1..3; k_range=2..5; strip=k-1..2k-3")

if __name__=='__main__':
    main()
