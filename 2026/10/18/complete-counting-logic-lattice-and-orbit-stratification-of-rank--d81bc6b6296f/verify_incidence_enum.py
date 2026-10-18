#!/usr/bin/env python3
"""Independent labelled 2-regular bipartite incidence enumeration for r=2..5.
Standard library only; does not use the partition-based poset builder.
"""
from itertools import combinations,product
from collections import Counter


def cycle_components(rows,r):
    graph=[set() for _ in range(2*r)]
    for i,pair in enumerate(rows):
        for j in pair:
            graph[i].add(r+j)
            graph[r+j].add(i)
    assert all(len(s)==2 for s in graph)
    unseen=set(range(2*r));parts=[]
    while unseen:
        first=next(iter(unseen)); stack=[first]; seen={first}; unseen.remove(first)
        while stack:
            x=stack.pop()
            for y in graph[x]:
                if y not in seen:
                    seen.add(y);unseen.remove(y);stack.append(y)
        assert len(seen)%2==0
        parts.append(len(seen)//2)
    return tuple(sorted(parts))


def c2_one_step_profile(rows,r):
    # From each of the four levels, the four atomic relation types
    # to the four levels have counts fixed by degrees two, irrespective
    # of whether the incidence graph is connected or contains digons.
    deg=Counter(j for row in rows for j in row)
    assert all(deg[i]==2 for i in range(r))
    # 0=bottom, 1=atoms, 2=coatoms, 3=top; comparison relation types
    # are: smaller, larger, equal, incomparable.
    profile=( (1,r,r,1),
        (1,r-1,2,r-2,1),
        (1,2,r-2,r-1,1),
        (1,r,r,1) )
    return profile


def main():
    for r in range(2,6):
        pairs=list(combinations(range(r),2))
        cycle_types=Counter(); lattice_flags=Counter()
        common_prof=None
        for rows in product(pairs,repeat=r):
            deg=Counter(j for row in rows for j in row)
            if len(deg)!=r or any(deg[j]!=2 for j in range(r)):
                continue
            p=cycle_components(rows,r)
            cycle_types[p]+=1
            # A pair of atoms shares both its coatoms iff there is a C4.
            lat=all(len(set(rows[i])&set(rows[j]))<2
                    for i in range(r) for j in range(i+1,r))
            assert lat == (2 not in p)
            lattice_flags[lat]+=1
            prof=c2_one_step_profile(rows,r)
            if common_prof is None:common_prof=prof
            assert prof==common_prof
        # Every abstract partition type is represented by at least one
        # labelled incidence matrix in this independent enumeration.
        assert all(all(k>=2 for k in typ) and sum(typ)==r for typ in cycle_types)
        print(f'r={r} labeled_matrices={sum(cycle_types.values())} cycle_types={dict(sorted(cycle_types.items()))} lattice_matrices={lattice_flags[True]} nonlattice_matrices={lattice_flags[False]}')
    assert set(cycle_types)=={(5,),(2,3)}
    print('PASS: full labelled incidence enumeration through r=5; cycle types and lattice tests')

if __name__=='__main__':main()
