#!/usr/bin/env python3
"""Exhaustive, finite verification for rank-three logic on 2-regular graphs.

Requires only Python 3. Builds the 4**5-1 component-count representatives
obtained after the cycle-length and component-multiplicity reductions.
No external packages, network access, or previously generated data required.
"""
from collections import defaultdict
from itertools import product

LENGTHS = (3, 4, 5, 6, 7)

def graph(parts):
    """Return adjacency bitsets of a disjoint union of simple cycles."""
    n = sum(parts)
    neigh = [0] * n
    base = 0
    for length in parts:
        for j in range(length):
            u = base + j
            v = base + ((j + 1) % length)
            neigh[u] |= 1 << v
            neigh[v] |= 1 << u
        base += length
    return tuple(neigh)

def rank_three_type(neigh):
    """Exact empty-tuple 3-type via the finite back-and-forth recursion.

    rank 0: quantifier-free tuple type (equalities and adjacency).
    rank r+1: that rank-0 tuple type plus the set of rank-r
              extension types after naming one more vertex.

    For a named ordered pair a,b, rank 1 is determined by equality,
    adjacency, and the set of four possible edge-patterns to a third
    DISTINCT vertex c. Third choices c=a,b are already fixed by the
    pair's equality and adjacency. The singleton rank-2 type is then
    the set of such ordered-pair types; the empty rank-3 type is the
    set of singleton rank-2 types. All graphs here have no loops.
    """
    n = len(neigh)
    universe = (1 << n) - 1
    singletons = set()
    for a in range(n):
        pair_types = set()
        Na = neigh[a]
        for b in range(n):
            Nb = neigh[b]
            choice = universe & ~((1 << a) | (1 << b))
            mask = 0
            for p in (0, 1):
                for q in (0, 1):
                    eligible = (choice &
                        (Na if p else ~Na) &
                        (Nb if q else ~Nb))
                    if eligible:
                        mask |= 1 << (2*p + q)
            pair_types.add((int(a == b), int(bool(Na & (1 << b))), mask))
        singletons.add(frozenset(pair_types))
    return frozenset(singletons)

def rank_three_indicators(neigh):
    """Truth values of six explicit rank-at-most-three sentences.

    T: triangle exists; Q: opposite twin pair exists;
    F: nonadjacent pair with common and exclusive neighbors exists;
    I: independent triple; D: dominating set of at most 2 vertices;
    U: universal vertex. See RESULT.md for full sentences.
    """
    n = len(neigh)
    vertices = range(n)
    edge = lambda x,y: bool(neigh[x] & (1 << y))
    T = any(edge(x,y) and edge(y,z) and edge(z,x)
            for x in vertices for y in vertices for z in vertices)
    Q = any(x != y and not edge(x,y) and neigh[x] == neigh[y]
            for x in vertices for y in vertices)
    F = any(x != y and not edge(x,y) and
            (neigh[x] & neigh[y]) and (neigh[x] & ~neigh[y])
            for x in vertices for y in vertices)
    I = any(x != y and x != z and y != z and
            not edge(x,y) and not edge(x,z) and not edge(y,z)
            for x in vertices for y in vertices for z in vertices)
    allmask = (1 << n) - 1
    D = any(((1 << x) | (1 << y) | neigh[x] | neigh[y]) == allmask
            for x in vertices for y in vertices)
    U = any(((1 << x) | neigh[x]) == allmask for x in vertices)
    return tuple(int(v) for v in (T,Q,F,I,D,U))

def run():
    signature_to_type = {}
    type_to_signature = {}
    groups = defaultdict(list)
    for counts in product(range(4), repeat=len(LENGTHS)):
        if not any(counts):
            continue
        parts = tuple(length for length, count in zip(LENGTHS,counts)
                      for _ in range(count))
        G = graph(parts)
        signature = rank_three_indicators(G)
        qtype = rank_three_type(G)
        if signature in signature_to_type:
            assert signature_to_type[signature] == qtype, (parts, signature)
        else:
            signature_to_type[signature] = qtype
        if qtype in type_to_signature:
            assert type_to_signature[qtype] == signature, (parts,signature)
        else:
            type_to_signature[qtype] = signature
        groups[signature].append(parts)
    assert sum(map(len,groups.values())) == 4**5 - 1 == 1023
    assert len(groups) == len(signature_to_type) == len(type_to_signature) == 12
    print('EXHAUSTIVE: 1023 canonical nonempty graphs; exactly 12 rank-3 types.')
    print('Signature order: T (triangle), Q (square), F (cycle length >= 5),'
          ' I (independent triple), D (dominating pair), U (universal).')
    for signature, parts_group in sorted(groups.items(),
            key=lambda item: (sum(min(item[1],key=lambda x:(sum(x),x))),
                              min(item[1],key=lambda x:(sum(x),x)))):
        smallest=min(parts_group,key=lambda x:(sum(x),x))
        print(f'{smallest!s:<16} {signature} count={len(parts_group):3d}')
    print('PASS: all 1023 canonical graphs independently grouped by exact'
          ' back-and-forth rank-three type and six sentence truth values.')

if __name__ == '__main__':
    run()
