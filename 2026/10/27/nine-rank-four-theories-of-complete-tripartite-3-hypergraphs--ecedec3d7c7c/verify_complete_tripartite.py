"""Finite exhaustive quantifier-rank verification for complete tripartite 3-hypergraphs.

The signature has equality and one symmetric ternary relation E. Every relation
triple is an edge exactly if its vertices belong to three distinct parts.
The two independent routines compute full first-order quantifier-rank types.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement


def atom_parts(t):
    n=len(t)
    return (tuple(t[i]==t[j] for i in range(n) for j in range(i+1,n)),
            tuple(len({t[i][0],t[j][0],t[k][0]})==3
                  for i in range(n) for j in range(i+1,n) for k in range(j+1,n)))


def symbolic_type(sizes, depth):
    """Orbit-reduced exact Hintikka recursion."""
    @lru_cache(None)
    def rec(t, remaining):
        atom=atom_parts(t)
        if not remaining:
            return (atom,)
        used=[set() for _ in sizes]
        for color,index in t:
            used[color].add(index)
        options=[]
        for color,size in enumerate(sizes):
            options.extend((color,j) for j in sorted(used[color]))
            if len(used[color]) < size:
                options.append((color,len(used[color])))
        return (atom, frozenset(rec(t+(v,),remaining-1) for v in options))
    return rec((),depth)


def atom_vertices(t, vertex_colors):
    n=len(t)
    return (tuple(t[i]==t[j] for i in range(n) for j in range(i+1,n)),
            tuple(len({vertex_colors[t[i]],vertex_colors[t[j]],vertex_colors[t[k]]})==3
                  for i in range(n) for j in range(i+1,n) for k in range(j+1,n)))


def brute_type(sizes,depth):
    """Independent full-vertex recursion, with no quotient by symmetry."""
    colors=tuple(c for c,n in enumerate(sizes) for _ in range(n))
    @lru_cache(None)
    def rec(t,remaining):
        atom=atom_vertices(t,colors)
        if remaining==0:
            return (atom,)
        extensions=set()
        for v in range(len(colors)):
            extensions.add(rec(t+(v,),remaining-1))
        return (atom,frozenset(extensions))
    return rec((),depth)


def partition(signatures):
    d=defaultdict(list)
    for k,v in signatures.items():d[v].append(k)
    return tuple(sorted((tuple(sorted(v)) for v in d.values()),key=lambda x:x[0]))


def expected_class(t):
    """Predicted nine classes, for ordered positive side sizes."""
    a,b,c=sorted(min(z,3) for z in t)
    if (a,b,c) in {(2,2,3),(2,3,3)}:return (2,2,3)
    return (a,b,c)


def run():
    triples=list(combinations_with_replacement(range(1,5),3))
    sym3={ns:symbolic_type(ns,3) for ns in triples}
    sym4={ns:symbolic_type(ns,4) for ns in triples}
    br4={ns:brute_type(ns,4) for ns in triples}
    assert partition(sym4)==partition(br4)
    assert len(partition(sym3))==4
    groups=partition(sym4)
    assert len(groups)==9
    assert all(expected_class(x)==expected_class(y) for g in groups for x in g for y in g)
    assert len(set(expected_class(ns) for ns in triples))==9
    assert all((expected_class(x)==expected_class(y))==(sym4[x]==sym4[y])
               for x in triples for y in triples)
    reps=tuple(g[0] for g in groups)
    assert reps==((1,1,1),(1,1,2),(1,1,3),(1,2,2),(1,2,3),
                  (1,3,3),(2,2,2),(2,2,3),(3,3,3))
    assert max(sum(g[0]) for g in groups)==9
    print('FULL_VERTEX_AND_ORBIT_RECURSIONS_AGREE_OK capped_structures=20 rank=4')
    print('RANK_THREE_TYPES_OK count=4')
    print('RANK_FOUR_TYPES_OK count=9')
    for i,g in enumerate(groups,1):
        print(f'CLASS_{i:02d} rep={g[0]} capped_members={g}')
    print('SHARP_INTERNAL_REPRESENTATIVE_OK vertices=9')
    for n in range(5,11):
        for ns in combinations_with_replacement(range(1,n+1),3):
            if any(z<=4 for z in ns) or ns==(n,n,n):
                assert symbolic_type(ns,4)==sym4[tuple(min(z,4) for z in ns)]
    print('LARGER_SIZE_TESTS_OK max_part_size=10')
    print('VERIFY_OK')

if __name__=='__main__':run()
