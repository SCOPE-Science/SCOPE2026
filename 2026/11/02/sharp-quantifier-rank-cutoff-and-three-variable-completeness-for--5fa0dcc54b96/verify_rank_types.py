#!/usr/bin/env python3
"""Independent finite three-variable rank-type calculation for ternary cyclic orders.

No hypothesis about the expected threshold is used to build the logical types.
For each n, all assignments of three pebbles are considered up to rotation.
The rank-(r+1) type consists of the atomic type and, for each pebble,
the set of rank-r types available by replacing that pebble.
"""
from collections import defaultdict
from itertools import product


def canonical(assignment, n):
    origin = next((v for v in assignment if v >= 0), 0)
    return tuple(-1 if v < 0 else (v-origin) % n for v in assignment)


def atom(assignment, n):
    a = assignment
    assigned = tuple(v >= 0 for v in a)
    equalities = tuple(a[i] == a[j] and a[i] >= 0
                       for i in range(3) for j in range(i+1, 3))
    if not all(assigned) or len(set(a)) < 3:
        orientation = 0
    else:
        orientation = 1 if 0 < (a[1]-a[0]) % n < (a[2]-a[0]) % n else -1
    return assigned, equalities, orientation


def check(maximum_n=40, maximum_rank=6):
    lengths = range(3, maximum_n + 1)
    states = {n: sorted({canonical(a, n) for a in product(range(-1,n),repeat=3)})
              for n in lengths}
    cases = [(n, a) for n in lengths for a in states[n]]
    atoms = {(n,a): atom(a,n) for n,a in cases}
    neighbors = {}
    for n,a in cases:
        neighbors[n,a] = tuple(
            tuple({canonical(a[:i]+(v,)+a[i+1:],n) for v in range(n)})
            for i in range(3))
    def number(signatures):
        # repr sorting avoids dependence on randomized set iteration.
        labels = {s:i for i,s in enumerate(sorted(set(signatures.values()),key=repr))}
        return {key:labels[val] for key,val in signatures.items()}
    colors = number(atoms)
    checked = 0
    for rank in range(maximum_rank + 1):
        groups = defaultdict(list)
        for n in lengths:
            groups[colors[n,(-1,-1,-1)]].append(n)
        partition = sorted(groups.values(),key=lambda g:g[0])
        if rank <= 2:
            expected = [list(lengths)]
        else:
            threshold = 1 << (rank-1)
            expected = [[n] for n in lengths if n < threshold]
            if threshold <= maximum_n:
                expected.append(list(range(max(3,threshold),maximum_n+1)))
        if partition != expected:
            raise AssertionError(f'rank={rank}: got {partition}; expected {expected}')
        checked += 1
        print(f'rank={rank} classes={len(partition)} cutoff={1<<(rank-1) if rank>=3 else "none"} PASS')
        if rank == maximum_rank:
            break
        sig = {(n,a):(atoms[n,a],tuple(tuple(sorted({colors[n,t] for t in neighbors[n,a][i]}))
                                     for i in range(3))) for n,a in cases}
        colors = number(sig)
    print(f'VERIFY_RANK_TYPES_OK n=3..{maximum_n} ranks=0..{maximum_rank} states={len(cases)}')

if __name__=='__main__':
    check()
