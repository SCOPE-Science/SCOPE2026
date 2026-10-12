#!/usr/bin/env python3
"""Standalone exhaustive checks of connected-domination cactus factorization.
Requires networkx 3.x; no external data or service is needed.
"""
import random
from collections import defaultdict
from math import comb
import networkx as nx


def cactus_blocks(G):
    if G.number_of_nodes() == 0 or not nx.is_connected(G):
        return None
    blocks = []
    for vertices in nx.biconnected_components(G):
        H = G.subgraph(vertices)
        edges = H.number_of_edges()
        if len(vertices) == 2:
            if edges != 1:
                return None
            blocks.append(('edge', set(vertices)))
        elif edges == len(vertices) and all(H.degree(v) == 2 for v in vertices):
            blocks.append(('cycle', set(vertices)))
        else:
            return None
    return blocks


def formula_coefficients(G):
    n = G.number_of_nodes()
    if n == 1:
        return {1: 1}
    if n == 2:
        return {1: 2, 2: 1}
    blocks = cactus_blocks(G)
    if blocks is None:
        return None
    cuts = set(nx.articulation_points(G))
    leaves = sum(1 for _, d in G.degree() if d == 1)
    p = {len(cuts): 1}
    for _ in range(leaves):
        new = defaultdict(int)
        for degree, coeff in p.items():
            new[degree] += coeff
            new[degree+1] += coeff
        p = dict(new)
    for kind, verts in blocks:
        if kind != 'cycle':
            continue
        free = verts - cuts
        q = len(free)
        t = sum(u in free and v in free for u,v in G.subgraph(verts).edges())
        factor = {q: 1}
        if q:
            factor[q-1] = factor.get(q-1,0) + q
        if t:
            assert q >= 2
            factor[q-2] = factor.get(q-2,0) + t
        new = defaultdict(int)
        for i,a in p.items():
            for j,b in factor.items():
                new[i+j] += a*b
        p = dict(new)
    return {degree: count for degree,count in p.items() if count}


def direct_coefficients(G):
    nodes = list(G)
    n = len(nodes)
    adj = [sum(1<<j for j,v in enumerate(nodes) if G.has_edge(u,v)) for u in nodes]
    all_bits=(1<<n)-1
    out=defaultdict(int)
    tested=0
    for subset in range(1,1<<n):
        tested += 1
        dom=subset
        seen=0
        pending=subset & -subset
        while pending:
            bit=pending&-pending
            pending-=bit
            if bit&seen:
                continue
            seen |= bit
            i=bit.bit_length()-1
            dom |= adj[i]
            pending |= adj[i]&subset&~seen
        if seen != subset:
            continue
        # Dom check must include neighbors of every selected vertex.
        if dom != all_bits:
            for i in range(n):
                if subset>>i&1:
                    dom |= adj[i]
            if dom != all_bits:
                continue
        out[subset.bit_count()] +=1
    return dict(out),tested


def random_cactus(rng,max_n):
    G=nx.Graph();G.add_node(0)
    while G.number_of_nodes() < max_n:
        old=rng.choice(list(G.nodes()))
        remaining=max_n-G.number_of_nodes()
        if remaining>=2 and rng.random()<0.46:
            k=rng.randint(2,min(5,remaining))
            nv=list(range(G.number_of_nodes(),G.number_of_nodes()+k))
            cyc=[old]+nv
            G.add_edges_from(zip(cyc,cyc[1:]+cyc[:1]))
        else:
            new=G.number_of_nodes()
            G.add_edge(old,new)
    return G


def run():
    atlas_count=0
    checks=0
    examples=[]
    for G in nx.graph_atlas_g():
        if G.number_of_nodes()<1 or cactus_blocks(G) is None:
            continue
        atlas_count+=1
        predicted=formula_coefficients(G)
        observed,used=direct_coefficients(G)
        checks+=used
        if predicted!=observed:
            raise AssertionError(('atlas',G.number_of_nodes(),sorted(G.edges()),predicted,observed))
        if G.number_of_nodes()==7 and len(examples)<5:
            examples.append((G.number_of_nodes(),len(list(nx.articulation_points(G))),observed))
    rng=random.Random(20261009)
    random_count=0
    for i in range(720):
        n=rng.randint(8,15)
        G=random_cactus(rng,n)
        predicted=formula_coefficients(G)
        observed,used=direct_coefficients(G)
        checks+=used
        random_count+=1
        if predicted!=observed:
            raise AssertionError(('random', sorted(G.edges()),predicted,observed))
    # Symbolic discriminant checks independent of polynomial roots:
    # for every cycle, q and t are exact vertex / edge counts, and q^2>=4t
    # unless its sole block is a triangle.
    tested_block_count=0
    for i in range(1600):
        G=random_cactus(rng,rng.randint(4,38))
        cuts=set(nx.articulation_points(G))
        for kind, verts in cactus_blocks(G):
            if kind=='cycle':
                free=verts-cuts
                q=len(free)
                t=sum(u in free and v in free for u,v in G.subgraph(verts).edges())
                assert q*q>=4*t,(q,t,sorted(G.edges()))
                tested_block_count+=1
    assert formula_coefficients(nx.cycle_graph(3)) == {1:3,2:3,3:1}
    assert formula_coefficients(nx.cycle_graph(4)) == {2:4,3:4,4:1}
    print('VERIFY_OK')
    print('atlas_cactus_graphs',atlas_count)
    print('random_cactus_graphs',random_count)
    print('total_bruteforce_candidate_subsets',checks)
    print('random_extra_blocks_discriminant',tested_block_count)
    print('special_triangular_cycle_nonreal_quadratic', 'x^2+3*x+3')
    print('special_square_cycle',formula_coefficients(nx.cycle_graph(4)))

if __name__=='__main__': run()
