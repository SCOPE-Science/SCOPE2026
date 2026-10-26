#!/usr/bin/env python3
"""Exact finite verifier: extremal independent sets of two symmetric-square graphs.

Requires Python 3.10+ standard library. The pairs are unordered; vertex labels are
4*x+y with x,y in {0,1,2,3}. Execution: python verify_token_independence.py
"""
from collections import Counter
from itertools import combinations, permutations, product

VERTICES = range(16)
ALL_VERTEX_MASK = (1 << 16) - 1
SHIKH_DIFFS = {(1,0), (3,0), (0,1), (0,3), (1,1), (3,3)}


def base_edges(kind):
    edges = set()
    for a,b in combinations(VERTICES,2):
        x,y=divmod(a,4); u,v=divmod(b,4)
        if kind=='rook':
            adjacent = x==u or y==v
        else:
            adjacent = ((u-x)%4,(v-y)%4) in SHIKH_DIFFS
        if adjacent: edges.add((a,b))
    return edges


def maximum_cocliques(edges):
    masks=[]
    for q in combinations(VERTICES,4):
        if all((a,b) not in edges for a,b in combinations(q,2)):
            masks.append(sum(1 << z for z in q))
    return tuple(masks)


def all_extremal_neighborhood_graphs(cocliques):
    """Exhaustively solve reciprocal-neighborhood CSP; no graph-isomorphism library."""
    domains=tuple(tuple(s for s in cocliques if not (s >> v & 1)) for v in VERTICES)
    answers=[]
    nodes=0
    def visit(assigned, neighborhoods, options):
        nonlocal nodes
        nodes+=1
        if assigned==ALL_VERTEX_MASK:
            answers.append(tuple(neighborhoods))
            return
        unassigned=[v for v in VERTICES if not assigned >> v & 1]
        v=min(unassigned,key=lambda i:(len(options[i]),i))
        for proposal in options[v]:
            next_options=list(options)
            for u in unassigned:
                if u==v:continue
                need=(proposal >> u)&1
                next_options[u]=tuple(m for m in options[u] if ((m >> v)&1)==need)
                if not next_options[u]:break
            else:
                next_neighbors=list(neighborhoods)
                next_neighbors[v]=proposal
                visit(assigned | (1<<v), next_neighbors, tuple(next_options))
    visit(0,[0]*16,domains)
    return tuple(answers),nodes


def make_token_edges(edges):
    states=tuple(combinations(VERTICES,2)); state_index={s:i for i,s in enumerate(states)}
    neighbors=[set() for _ in states]
    for k,(a,b) in enumerate(states):
        for u,v in edges:
            if a==u and b!=v: neighbors[k].add(state_index[tuple(sorted((v,b)))])
            if a==v and b!=u: neighbors[k].add(state_index[tuple(sorted((u,b)))])
            if b==u and a!=v: neighbors[k].add(state_index[tuple(sorted((a,v)))])
            if b==v and a!=u: neighbors[k].add(state_index[tuple(sorted((a,u)))])
    assert all(k not in neighbors[k] for k in range(len(states)))
    assert all(k in neighbors[j] for k,n in enumerate(neighbors) for j in n)
    return states,neighbors


def automorphisms(kind,edges):
    if kind=='rook':
        group=[]
        for rows in permutations(range(4)):
            for cols in permutations(range(4)):
                for swap in (False, True):
                    if swap:
                        perm=tuple(4*rows[y]+cols[x] for x in range(4) for y in range(4))
                    else:
                        perm=tuple(4*rows[x]+cols[y] for x in range(4) for y in range(4))
                    group.append(perm)
        assert len(group)==1152
    else:
        origin_symmetries=[]
        for a,b,c,d in product(range(4),repeat=4):
            if (a*d-b*c)%2==0:continue
            image={((a*x+b*y)%4,(c*x+d*y)%4) for x,y in SHIKH_DIFFS}
            if image==SHIKH_DIFFS:origin_symmetries.append((a,b,c,d))
        assert len(origin_symmetries)==12
        group=[]
        for a,b,c,d in origin_symmetries:
            for tx,ty in product(range(4),repeat=2):
                perm=tuple(4*((a*x+b*y+tx)%4)+((c*x+d*y+ty)%4) for x in range(4) for y in range(4))
                group.append(perm)
        assert len(group)==192
    assert len(set(group))==len(group)
    assert all({tuple(sorted((p[u],p[v]))) for u,v in edges}==edges for p in group)
    return tuple(group)


def components(neighbors):
    unseen=set(VERTICES);sizes=[]
    while unseen:
        start=unseen.pop();stack=[start];size=0
        while stack:
            v=stack.pop();size+=1
            for u in VERTICES:
                if neighbors[v]>>u&1 and u in unseen:
                    unseen.remove(u);stack.append(u)
        sizes.append(size)
    return tuple(sorted(sizes))


def shape(neighbors):
    sizes=components(neighbors)
    repeats=tuple(sorted(Counter(neighbors).values()))
    if sizes==(8,8) and repeats==(4,4,4,4):
        return 'two K_{4,4}'
    if sizes==(16,) and repeats==(2,)*8:
        return 'C_8[2K_1]'
    raise AssertionError(('unexpected component shape',sizes,repeats))


def transformed(n,p):
    out=[0]*16
    for v in VERTICES:
        out[p[v]]=sum(1<<p[w] for w in VERTICES if n[v]>>w&1)
    return tuple(out)


def test(kind, expected_cocliques, expected_solutions, expected_types, expected_orbits):
    edges=base_edges(kind)
    assert len(edges)==48
    adj=[set() for _ in VERTICES]
    for x,y in edges:adj[x].add(y);adj[y].add(x)
    assert all(len(adj[v])==6 for v in VERTICES)
    assert all(len(adj[x]&adj[y])==(2 if tuple(sorted((x,y))) in edges else 2)
               for x,y in combinations(VERTICES,2))
    # Exhaustively verify the graph's coclique upper bound, independently
    # of the Hoffman spectral argument. Any five-coclique would be listed.
    assert not any(all(tuple(sorted((a,b))) not in edges for a,b in combinations(q,2))
                   for q in combinations(VERTICES,5))
    cocliques=maximum_cocliques(edges)
    assert len(cocliques)==expected_cocliques
    assert all(sum(v in [w for w in VERTICES if s>>w&1] for s in cocliques)
               ==expected_cocliques//4 for v in VERTICES)
    sols,nodes=all_extremal_neighborhood_graphs(cocliques)
    assert len(sols)==expected_solutions
    assert len(set(sols))==len(sols)
    states, token_neighbors=make_token_edges(edges)
    assert len(states)==120 and sum(map(len,token_neighbors))//2==672
    state_index={a:i for i,a in enumerate(states)}
    shape_counts=Counter()
    for n in sols:
        assert all(n[v].bit_count()==4 and not (n[v]>>v&1) for v in VERTICES)
        assert all((n[v]>>u&1)==(n[u]>>v&1) for v in VERTICES for u in VERTICES)
        code={state_index[(u,v)] for u,v in combinations(VERTICES,2) if n[u]>>v&1}
        assert len(code)==32
        assert all(not (token_neighbors[i]&code) for i in code)
        shape_counts[shape(n)]+=1
    assert dict(shape_counts)==expected_types
    group=automorphisms(kind,edges)
    remaining=set(sols)
    orbit_type_counts=Counter()
    while remaining:
        witness=min(remaining)
        orb={transformed(witness,p) for p in group}
        assert orb <= set(sols)
        remaining.difference_update(orb)
        orbit_type_counts[(shape(witness),len(orb))]+=1
    assert dict(orbit_type_counts)==expected_orbits
    print(kind, 'cocliques',len(cocliques),'F2 states/edges',120,672,
          'alpha',32,'extremal sets',len(sols),'CSP nodes',nodes,
          'shape counts',dict(shape_counts),'orbit types',dict(orbit_type_counts),
          'automorphisms',len(group))


def main():
    test('rook',24,144,{'two K_{4,4}':72,'C_8[2K_1]':72},
         {('two K_{4,4}',18):2, ('two K_{4,4}',36):1, ('C_8[2K_1]',72):1})
    test('shrikhande',16,54,{'two K_{4,4}':30,'C_8[2K_1]':24},
         {('two K_{4,4}',3):2,('two K_{4,4}',6):2,('two K_{4,4}',12):1,('C_8[2K_1]',24):1})
    print('VERIFY_OK')

if __name__=='__main__':main()
