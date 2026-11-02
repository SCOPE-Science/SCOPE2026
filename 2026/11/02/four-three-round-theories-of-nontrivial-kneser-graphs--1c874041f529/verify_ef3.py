#!/usr/bin/env python3
"""Independent exact depth-three Hintikka-type computation with repetitions.
Builds the atomic two/three-tuple types explicitly, and nests the
sets of attainable extensions. Applicable to any loopless graph.
"""
from itertools import combinations
from math import comb


def rank_three_type(n,k):
    v=[frozenset(c) for c in combinations(range(n),k)]
    N=len(v)
    edge=[[int(a.isdisjoint(b)) if i!=j else 0 for j,b in enumerate(v)] for i,a in enumerate(v)]
    def atom(a,b,c):
        return (int(a==b),int(a==c),int(b==c),edge[a][b],edge[a][c],edge[b][c])
    one_types=set()
    for a in range(N):
        two_types=set()
        for b in range(N):
            three_types=frozenset(atom(a,b,c) for c in range(N))
            two_types.add(((int(a==b),edge[a][b]),three_types))
        one_types.add(frozenset(two_types))
    return frozenset(one_types)


def predicted_class(n,k):
    if n==2*k: return 'M'
    if n<=3*k-2: return 'L'
    if n==3*k-1: return 'T'
    return 'S'


def main():
    # Includes at least two members of each class, with different k.
    cases=[(4,2),(6,3), # matchings
           (7,3),(9,4), # low range
           (5,2),(8,3), # narrow triangle-free threshold
           (6,2),(9,3),(10,3)] # stable tail
    sig={}
    for n,k in cases:
        if comb(n,k)>140: raise RuntimeError('unsafe resource bound')
        t=rank_three_type(n,k)
        sig[n,k]=t
        print('case',n,k,'vertices',comb(n,k),'class',predicted_class(n,k), 'first_types',len(t), 'pair_types',len(next(iter(t))))
    classes={c:{sig[n,k] for n,k in cases if predicted_class(n,k)==c} for c in 'MLTS'}
    assert all(len(ts)==1 for ts in classes.values())
    assert len({next(iter(ts)) for ts in classes.values()})==4
    print('exact_distinct_quantifier_rank_three_types',4)
    print('PASS')

if __name__=='__main__': main()
