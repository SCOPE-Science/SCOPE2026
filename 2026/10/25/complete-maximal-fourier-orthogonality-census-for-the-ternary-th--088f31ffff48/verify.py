#!/usr/bin/env python3
"""Exhaustive integer-only verification of maximal Fourier-orthogonal sets.

Only Python's standard library is required.  The explicit graph encodes the
Fourier zero set of the Cartesian digit cube.  The pivoting recursion is the
Bron--Kerbosch maximal-clique enumeration (every terminal clique is maximal).
"""
from collections import Counter
from itertools import product


def graph(q, dimension):
    n = 2*q
    vertices = list(product(range(n), repeat=dimension))
    adjacency = [0] * len(vertices)
    for i, u in enumerate(vertices):
        for j in range(i+1, len(vertices)):
            v = vertices[j]
            if any((u[k]-v[k]) % n in range(2, n, 2) for k in range(dimension)):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    return vertices, adjacency


def count_maximal_cliques(adjacency):
    N = len(adjacency)
    counts = Counter()
    witness = {}
    all_nodes = (1 << N) - 1
    nodes = [i for i in range(N)]
    visited = 0

    def iter_bits(bits):
        while bits:
            b = bits & -bits
            yield b.bit_length()-1
            bits ^= b

    def search(chosen, P, X):
        nonlocal visited
        visited += 1
        if not P and not X:
            counts[len(chosen)] += 1
            witness.setdefault(len(chosen),tuple(chosen))
            return
        pool = P | X
        pivot = max(iter_bits(pool), key=lambda u: (adjacency[u] & P).bit_count())
        branch = P & ~adjacency[pivot]
        while branch:
            bit = branch & -branch
            v = bit.bit_length()-1
            search(chosen+(v,), P & adjacency[v], X & adjacency[v])
            P ^= bit
            X |= bit
            branch ^= bit
    search((), all_nodes, 0)
    return counts, witness, visited


def assert_witness(vertices,adj,wit):
    sz=len(wit)
    for i in range(sz):
        for j in range(i+1,sz):
            assert (adj[wit[i]]>>wit[j])&1
    for u in range(len(vertices)):
        if u not in wit:
            assert any(not ((adj[u]>>v)&1) for v in wit)


def main():
    expectations = {
        (2,1): {2:2},
        (2,2): {4:12},
        (2,3): {4:128,8:744},
        (3,1): {3:2},
        (3,2): {9:28},
        (3,3): {12:34992,13:11664,14:11664,15:34992,27:154952},
    }
    for q, dim in expectations:
        V,A=graph(q,dim)
        actual,W,visited=count_maximal_cliques(A)
        assert dict(actual)==expectations[(q,dim)], (q,dim,actual)
        for size,example in W.items():
            assert_witness(V,A,example)
        print('q=%s dimension=%s vertices=%s recursion_nodes=%s counts=%s' %
              (q,dim,len(V),visited,dict(sorted(actual.items()))))
        if q==3 and dim==3:
            for size in sorted(W):
                print('EXAMPLE',size, [V[i] for i in W[size]])
    print('All exact graph census checks passed.')

if __name__=='__main__':
    main()
