#!/usr/bin/env python3
"""Finite corroboration of colour refinement on set-partition lattices.
Usage: python3 check_partition_lattice.py [maximum_n]; stdlib only.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, factorial
import sys


def set_partitions(n):
    if n == 0:
        return [()]
    partitions = [(1, (1,))]
    for e in range(1, n):
        bit = 1 << e
        new=[]
        for k, blocks in partitions:
            for j in range(k):
                z = list(blocks)
                z[j] |= bit
                new.append((k,tuple(z)))
            new.append((k+1,blocks + (bit,)))
        partitions = new
    return [tuple(sorted(bl)) for _,bl in partitions]


def rank_profile(blocks):
    return tuple(sorted((b.bit_count() for b in blocks),reverse=True))


def refines(a, b):
    return all(any(x & y == x for y in b) for x in a)


def refine(colors, predecessors, successors):
    keys=[]
    for i in range(len(colors)):
        keys.append((colors[i],tuple(sorted(Counter(colors[j] for j in predecessors[i]).items())),
                tuple(sorted(Counter(colors[j] for j in successors[i]).items()))))
    lab={v:k for k,v in enumerate(sorted(set(keys)))}
    return [lab[x] for x in keys]


def run(n):
    parts=set_partitions(n)
    size=len(parts)
    p = [[] for _ in range(size)]
    s = [[] for _ in range(size)]
    for i,a in enumerate(parts):
        for j,b in enumerate(parts):
            if i==j or len(a)<=len(b):
                continue
            if refines(a,b):
                s[i].append(j)
                p[j].append(i)
    col=[0]*size
    profiles=[rank_profile(q) for q in parts]
    results=[]
    for step in range(4):
        type_colors=defaultdict(set)
        color_types=defaultdict(set)
        for profile,c in zip(profiles,col):
            type_colors[profile].add(c)
            color_types[c].add(profile)
        results.append(dict(round=step,colors=len(set(col)),
            max_types_per_color=max(map(len,color_types.values())),
            max_colors_per_type=max(map(len,type_colors.values()))))
        if step<3: col=refine(col,p,s)
    assert results[3]['max_types_per_color']==1
    assert results[3]['max_colors_per_type']==1
    assert results[3]['colors']==len(set(profiles))
    print(f'n={n} lattice_vertices={size} integer_partition_profiles={len(set(profiles))} '
          + ' '.join(f'round{d["round"]}={d["colors"]}' for d in results) + ' CHECK_OK')
    return size

if __name__=='__main__':
    mx=int(sys.argv[1]) if len(sys.argv)>1 else 7
    assert 1<=mx<=9
    total=0
    for n in range(1,mx+1): total+=run(n)
    print(f'REFINEMENT_CHECK_OK max_n={mx} total_vertex_instances={total}')
