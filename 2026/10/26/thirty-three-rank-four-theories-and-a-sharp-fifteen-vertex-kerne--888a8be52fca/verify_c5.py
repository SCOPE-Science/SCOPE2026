#!/usr/bin/env python3
"""Exact four-round Ehrenfeucht--Fraisse census for C5 independent-clone blow-ups.

Requires Python 3.9+ standard library. Run: python verify_c5.py
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product

Q = 4


def cycle_edge(a, b):
    return a != b and (a - b) % 5 in (1, 4)


# Version A: a complete game tree on the quotient by permutations of
# unselected clones within each of the five independent vertex parts.
def quotient_census():
    intern = {}
    @lru_cache(None)
    def atom(t):
        first = {}
        unique = []
        equality = []
        for v in t:
            if v not in first:
                first[v] = len(first)
                unique.append(v)
            equality.append(first[v])
        edges = tuple((i, j) for i in range(len(unique))
                      for j in range(i + 1, len(unique))
                      if cycle_edge(unique[i][0], unique[j][0]))
        return (tuple(equality), edges)

    def intern_id(key):
        if key not in intern:
            intern[key] = len(intern)
        return intern[key]

    @lru_cache(None)
    def logical_type(s, t, remaining):
        a = atom(t)
        if remaining == 0:
            return intern_id((remaining, a))
        occupied = [0] * 5
        for p, clone in set(t):
            occupied[p] += 1
        extensions = set(t)
        for p in range(5):
            if occupied[p] < s[p]:
                extensions.add((p, occupied[p]))
        return intern_id((remaining, a,
                          frozenset(logical_type(s, t + (v,), remaining - 1)
                                    for v in extensions)))

    classification = defaultdict(list)
    for sizes in product(range(1, Q + 1), repeat=5):
        classification[logical_type(sizes, (), Q)].append(sizes)
    return classification, len(intern)


# Version B: an independent oracle on actual, labelled, finite graphs.
# All individual vertices are considered at every move; no cloning quotient.
def explicit_graph(sizes):
    vertices = [i for i, size in enumerate(sizes) for _ in range(size)]
    n = len(vertices)
    adjacency = [[cycle_edge(vertices[i], vertices[j])
                  for j in range(n)] for i in range(n)]
    return adjacency


def direct_game_types(graphs):
    intern = {}
    result = []
    def intern_id(key):
        if key not in intern:
            intern[key] = len(intern)
        return intern[key]
    for adj in graphs:
        n = len(adj)
        @lru_cache(None)
        def atom(t):
            first = {}
            unique = []
            equality = []
            for v in t:
                if v not in first:
                    first[v] = len(first)
                    unique.append(v)
                equality.append(first[v])
            edges = tuple((i,j) for i in range(len(unique))
                          for j in range(i+1,len(unique))
                          if adj[unique[i]][unique[j]])
            return (tuple(equality),edges)
        @lru_cache(None)
        def typ(t, remaining):
            a = atom(t)
            if remaining == 0:
                return intern_id((0,a))
            return intern_id((remaining, a,
                              frozenset(typ(t+(v,),remaining-1)
                                        for v in range(n))))
        result.append(typ((),Q))
    return result


def representatives(classes):
    ordered = []
    for group in classes.values():
        short = min(group, key=lambda s:(sum(s),s))
        ordered.append((short,group))
    ordered.sort(key=lambda pair:(sum(pair[0]),pair[0]))
    return ordered


def run():
    classes, distinct_types = quotient_census()
    ordered = representatives(classes)
    assert len(classes)==33, len(classes)
    assert sum(map(len,classes.values()))==4**5
    assert max(sum(short) for short,_ in ordered)==15
    assert Counter(sum(short) for short,_ in ordered)=={
        5:1,6:1,7:3,8:4,9:7,10:7,11:6,12:2,13:1,15:1}
    by_sizes = {s:i for i,(_rep,g) in enumerate(ordered) for s in g}
    assert len(by_sizes)==1024
    assert all(by_sizes[s]==by_sizes[tuple(min(x,3) for x in s)]
               for s in by_sizes), 'A four-clone part changed the rank-four theory'
    largest = ordered[-1]
    assert largest[0] == (3,3,3,3,3)
    assert set(largest[1])==set(product((3,4),repeat=5))

    # Independently traverse the full labelled game for all 243 vectors
    # in {1,2,3}^5, with no quotienting of labelled vertices.
    tests = list(product((1,2,3),repeat=5))
    oracle = direct_game_types([explicit_graph(s) for s in tests])
    for i,s in enumerate(tests):
        for j in range(i):
            assert (oracle[i]==oracle[j])==(by_sizes[s]==by_sizes[tests[j]]),(
                    'oracle mismatch',s,tests[j])
    # The exact class table below is a reproducible finite certificate.
    class_id = {s: i+1 for i,(_r,g) in enumerate(ordered) for s in g}
    lines = ['a,b,c,d,e,class_id']
    for s in sorted(class_id):
        lines.append(','.join(map(str,s))+','+str(class_id[s]))
    with open('c5_class_table.csv','w',encoding='utf-8',newline='\n') as f:
        f.write('\n'.join(lines)+'\n')
    print('VERIFY_OK classes=33 cap4_vectors=1024 smallest_max=15')
    print('CAP3_STABILITY_OK vectors=1024')
    print(f'ORACLE_OK labelled_graphs={len(tests)} pair_comparisons={len(tests)*(len(tests)-1)//2}')
    print('min_representative_sizes='+','.join(str(sum(x)) for x,_ in ordered))
    print('class_representatives='+ ';'.join(''.join(map(str,x)) for x,_ in ordered))
    print('classes_with_15_vertex_minimum='+str(sum(sum(rep)==15 for rep,_ in ordered)))
    print('public_census_complete=True')

if __name__=='__main__':
    run()
