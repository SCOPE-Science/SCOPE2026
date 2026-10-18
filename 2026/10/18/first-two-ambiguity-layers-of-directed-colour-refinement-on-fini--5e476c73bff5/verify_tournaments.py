#!/usr/bin/env python3
"""Exhaustive tournament and directed colour-refinement certificate through n=7.

All operations use integer arithmetic and the Python standard library.
"""
from itertools import combinations, permutations, product
from collections import defaultdict

COUNTS = (0, 1, 1, 2, 4, 12, 56, 456)

def decode(n, bits):
    """Return a tournament; each upper-triangle bit represents an arc i -> j."""
    a = [[False] * n for _ in range(n)]
    for i, j in reversed(list(combinations(range(n), 2))):
        v = bits & 1
        bits >>= 1
        a[i][j] = bool(v)
        a[j][i] = not bool(v)
    assert bits == 0
    return a

def encode(a, ordering):
    code = 0
    for i, j in combinations(ordering, 2):
        code = (code << 1) | int(a[i][j])
    return code

def canonical(a):
    """Canonical bit code, sorting by outdegree and trying equal-degree orders."""
    n = len(a)
    by_degree = defaultdict(list)
    for i in range(n):
        by_degree[sum(a[i])].append(i)
    groups = [tuple(by_degree[d]) for d in sorted(by_degree)]
    smallest = None
    for blocks in product(*(permutations(group) for group in groups)):
        order = tuple(v for block in blocks for v in block)
        key = encode(a, order)
        if smallest is None or key < smallest:
            smallest = key
    return smallest

def extend(a, mask):
    n = len(a)
    b = [row[:] + [not bool((mask >> i) & 1)] for i, row in enumerate(a)]
    b.append([bool((mask >> i) & 1) for i in range(n)] + [False])
    return b

def types_at(n, types_before):
    if n == 1:
        return {0}
    answer = set()
    for code in types_before:
        prior = decode(n-1, code)
        for mask in range(1 << (n-1)):
            answer.add(canonical(extend(prior, mask)))
    return answer

def induced_degree_profile(a, subset):
    return tuple(sorted(sum(a[i][j] for j in subset) for i in subset))

def count_transitive_four(a):
    return sum(induced_degree_profile(a, s) == (0,1,2,3)
               for s in combinations(range(len(a)), 4))

def witnesses(same):
    a = [[False]*6 for _ in range(6)]
    def add(i,j):
        assert not (a[i][j] or a[j][i])
        a[i][j] = True
    for i in range(3):
        j=(i+1)%3
        add(i,j)
        if same: add(3+i,3+j)
        else: add(3+j,3+i)
    for i in range(3):
        for j in range(3):
            if i==j: add(i,3+j)
            else: add(3+j,i)
    assert all(a[i][j] != a[j][i] for i in range(6) for j in range(i+1,6))
    return a

def main():
    prior = None
    for n in range(1,8):
        reps = types_at(n, prior)
        assert len(reps) == COUNTS[n], (n,len(reps))
        # No duplicate canonical codes; verify chosen representations have fixed canonical code.
        assert all(canonical(decode(n,code))==code for code in reps)
        codes = sorted(reps)
        # Globally synchronous refinement; no graph-dependent palettes.
        old = [0] * (n*len(codes))
        matrix = [decode(n,c) for c in codes]
        rounds=[]
        for _ in range(n*len(codes)+1):
            colors=max(old)+1
            keys=[]
            for ix,a in enumerate(matrix):
                for v in range(n):
                    bins=[0]*colors
                    incoming=[0]*colors
                    for w in range(n):
                        if a[v][w]: bins[old[n*ix+w]]+=1
                        if a[w][v]: incoming[old[n*ix+w]]+=1
                    keys.append((old[n*ix+v],tuple(bins),tuple(incoming)))
            mapping={k:i for i,k in enumerate(sorted(set(keys)))}
            nxt=[mapping[k] for k in keys]
            rounds.append(len(mapping))
            if len(mapping)==colors:
                old=nxt;break
            old=nxt
        else: raise AssertionError('unexpectedly long refinement')
        buckets=defaultdict(list)
        for ix,code in enumerate(codes):
            buckets[tuple(sorted(old[n*ix:n*(ix+1)]))].append(code)
        collisions=[sorted(v) for v in buckets.values() if len(v)>1]
        print(f'n={n}: {len(codes)} isomorphism types, {len(buckets)} 1-WL types, collisions={collisions}, refinement_colors={rounds}')
        if n<=5:
            assert not collisions
        elif n==6:
            assert sorted(collisions)==[[9378,9381]], collisions
        else:
            assert sorted(collisions)==[[9378,9381],[232512,232706,238754],[559362,559365],[594448,594468]]
            assert all(len({count_transitive_four(decode(n,c)) for c in group}) == len(group) for group in collisions)
            assert all(sum(row)==3 for c in [232512,232706,238754] for row in decode(n,c))
        prior=reps
    a,b=witnesses(False),witnesses(True)
    assert set((canonical(a),canonical(b)))=={9378,9381}
    assert sorted(sum(row) for row in a)==[2,2,2,3,3,3]
    assert sorted(sum(row) for row in b)==[2,2,2,3,3,3]
    assert {count_transitive_four(a),count_transitive_four(b)}=={0,3}
    print('Witnesses: opposite/same cyclic order, transitive 4-subtournaments:', count_transitive_four(a),count_transitive_four(b))
    print('VERIFIED: complete directed 1-WL quotient through order 7')

if __name__=='__main__': main()
