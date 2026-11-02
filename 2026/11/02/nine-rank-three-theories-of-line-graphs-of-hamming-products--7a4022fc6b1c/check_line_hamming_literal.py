#!/usr/bin/env python3
"""Direct full rank-three first-order type recursion for small line Hamming graphs.
This implementation does not use edge-orbit representatives or geometric lemmas.
"""
from itertools import product


def line_graph(q):
    words = list(product(*[range(a) for a in q]))
    edges = [(u, v) for i, u in enumerate(words) for v in words[i+1:]
             if sum(a != b for a, b in zip(u, v)) == 1]
    return [[int(bool(set(e) & set(f)) and i != j) for j, f in enumerate(edges)]
            for i, e in enumerate(edges)]


def exact_type3(q):
    A = line_graph(q)
    n = len(A)
    def atomic(xs):
        return tuple((int(xs[i] == xs[j]), A[xs[i]][xs[j]])
                     for i in range(len(xs)) for j in range(i, len(xs)))
    pairs = {(a,b): (atomic((a,b)),frozenset(atomic((a,b,c)) for c in range(n)))
             for a in range(n) for b in range(n)}
    ones = frozenset((atomic((a,)),frozenset(pairs[a,b] for b in range(n)))
                     for a in range(n))
    return ones


def main():
    reps = {
        'one_2':(2,), 'one_3':(3,), 'one_4':(4,), 'one_5':(5,),
        'one_6plus':(6,), 'square':(2,2), 'thin3':(2,3),
        'thin4plus':(2,4), 'stable':(2,2,2),
    }
    types = {k:exact_type3(q) for k,q in reps.items()}
    assert len(set(types.values())) == 9
    comparisons = {
        'one_6plus':[(7,), (8,)],
        'thin4plus':[(2,5),(2,6),(5,2)],
        'stable':[(3,3),(2,2,3),(2,3,3),(2,2,2,2),(3,4)],
    }
    done=0
    for k, cases in comparisons.items():
        for q in cases:
            assert exact_type3(q)==types[k],(k,q)
            done+=1
    print('VERIFY_OK complete literal rank-three types: 9 distinct exemplars and',done,'additional graphs')
    for k,q in reps.items():
        print(k, q, 'line vertices',len(line_graph(q)))

if __name__=='__main__':
    main()
