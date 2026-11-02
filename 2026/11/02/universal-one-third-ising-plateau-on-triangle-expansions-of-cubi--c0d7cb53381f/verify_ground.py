#!/usr/bin/env python3
"""Exact finite checks for antiferromagnetic Ising models on triangle-expanded cubic graphs.
No external modules are needed. Execute: python3 verify_ground.py
"""
from collections import Counter


def expanded_graph(n, edges):
    incidence = {(v, e): 3*v + k for v in range(n)
                 for k, e in enumerate(i for i, (a,b) in enumerate(edges) if a == v or b == v)}
    bonds = []
    for v in range(n):
        positions = [incidence[v,e] for e, (a,b) in enumerate(edges) if v in (a,b)]
        assert len(positions) == 3
        bonds.extend([(positions[0],positions[1]),(positions[0],positions[2]),(positions[1],positions[2])])
    bonds.extend((incidence[u,e],incidence[v,e]) for e,(u,v) in enumerate(edges))
    return bonds


def gray_minima(n, edges):
    bonds = expanded_graph(n, edges)
    sites = 3*n
    neighbors = [[] for _ in range(sites)]
    for u,v in bonds:
        neighbors[u].append(v); neighbors[v].append(u)
    spins = [-1]*sites
    energy = len(bonds)
    m = -sites
    minima = [10**9]*(sites+1)
    minima[sites] = energy
    for k in range(1,1<<sites):
        site = (k & -k).bit_length()-1
        energy -= 2*spins[site]*sum(spins[v] for v in neighbors[site])
        m -= 2*spins[site]
        spins[site] *= -1
        q = (sites-m)//2
        if energy < minima[q]:
            minima[q] = energy
    for q, measured in enumerate(minima):
        magnetization = sites-2*q
        predicted = max(abs(magnetization)-5*n//2,3*abs(magnetization)-9*n//2)
        assert measured == predicted, (n,q,measured,predicted)
    return sites, 1<<sites


def cube_ground_counts():
    # A minus at an incidence means its original edge and vertex are selected.
    # All fixed-magnetization minimizers have at most one minus per original edge.
    edges = [(v,v^(1<<axis)) for v in range(8) for axis in range(3)
             if not (v & (1<<axis))]
    c = [0]*8
    counts = Counter()
    def dfs(k,q):
        if k == len(edges):
            if (q <= 8 and all(t <= 1 for t in c)) or (8 <= q <= 12 and all(1 <= t <= 2 for t in c)):
                counts[q] += 1
            return
        u,v = edges[k]
        dfs(k+1,q)
        if c[u] < 2:
            c[u] += 1; dfs(k+1,q+1); c[u] -= 1
        if c[v] < 2:
            c[v] += 1; dfs(k+1,q+1); c[v] -= 1
    dfs(0,0)
    answer = [counts[q] for q in range(13)]
    assert answer == [1,24,240,1296,4092,7632,8056,4272,828,3312,4572,2520,450]
    assert sum(answer[8:13]) == 11682
    assert sum(answer[:9]) == 26441
    return answer


if __name__ == '__main__':
    k4 = [(u,v) for u in range(4) for v in range(u+1,4)]
    prism = [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]
    for label,n,edges in [('K4',4,k4),('triangular prism',6,prism)]:
        sites,states = gray_minima(n,edges)
        print(f'{label}: {sites} spins, {states} states, all fixed-magnetization minima verified')
    print('cube Q=0..12 fixed-magnetization degeneracies:', cube_ground_counts())
    print('cube coexistence degeneracies: h/J=1 -> 11682; h/J=3 -> 26441')
    print('PASS')
