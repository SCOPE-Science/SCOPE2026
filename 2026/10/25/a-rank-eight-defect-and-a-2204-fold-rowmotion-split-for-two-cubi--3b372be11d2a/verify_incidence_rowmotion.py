#!/usr/bin/env python3
"""Exact rowmotion census for two eight-vertex cubic graph incidence posets."""
from collections import Counter
from itertools import permutations
from math import lcm, comb


def cube_edges():
    return sorted({tuple(sorted((x, x ^ (1 << bit))))
                   for x in range(8) for bit in range(3)})


def wagner_edges():
    return sorted({tuple(sorted((x, (x + 1) % 8))) for x in range(8)}
                  | {(x, x + 4) for x in range(4)})


def compute(name, edges):
    n = 8
    m = len(edges)
    assert m == 12 and len(set(edges)) == 12
    assert all(0 <= a < b < n for a, b in edges)
    assert all(sum(v in edge for edge in edges) == 3 for v in range(n))
    # Vertex-transitivity, checked independently using the full finite permutation set.
    edge_set = set(edges)
    images = set()
    automorphisms = 0
    for p in permutations(range(n)):
        if {tuple(sorted((p[a], p[b]))) for a, b in edges} == edge_set:
            automorphisms += 1
            images.add(p[0])
    assert len(images) == n
    # Enumerate each ideal uniquely as (vertex bitset, chosen induced-edge bitset).
    induced = []
    for v in range(1 << n):
        induced.append(sum((1 << j) for j, (a, b) in enumerate(edges)
                           if (v >> a) & 1 and (v >> b) & 1))
    states = []
    for v in range(1 << n):
        e = induced[v]
        t = e
        while True:
            states.append((v, t))
            if t == 0:
                break
            t = (t - 1) & e
    signature = Counter((v.bit_count(), induced[v].bit_count()) for v in range(1 << n))
    rank_from_subsets = Counter()
    for (k, ecount), mult in signature.items():
        for j in range(ecount + 1):
            rank_from_subsets[k + j] += mult * comb(ecount, j)
    rank_from_enumeration = Counter(v.bit_count() + e.bit_count() for v, e in states)
    assert rank_from_subsets == rank_from_enumeration
    # An independent ideal-count identity: sum_{U subset V} 2^{|E[U]|}.
    assert len(states) == sum(1 << e.bit_count() for e in induced)
    index = {s: k for k, s in enumerate(states)}
    assert len(index) == len(states)

    def direct(v, chosen):
        new_edges = induced[v] & ~chosen
        new_vertices = ((1 << n) - 1) & ~v
        for j, (a, b) in enumerate(edges):
            if (new_edges >> j) & 1:
                new_vertices |= (1 << a) | (1 << b)
        return new_vertices, new_edges

    # Completely separate definition: top-to-bottom elementary toggles on
    # the 20-element incidence poset, with bits 0..7 vertices and 8..19 edges.
    successors = [0] * (n + m)
    predecessors = [0] * (n + m)
    for j, (a, b) in enumerate(edges):
        successors[a] |= 1 << (n + j)
        successors[b] |= 1 << (n + j)
        predecessors[n + j] |= (1 << a) | (1 << b)

    def toggles(v, chosen):
        state = v | (chosen << n)
        for pos in range(n + m - 1, -1, -1):
            mask = 1 << pos
            if state & mask:
                if not state & successors[pos]:
                    state ^= mask
            else:
                if (state & predecessors[pos]) == predecessors[pos]:
                    state ^= mask
        return state & ((1 << n) - 1), state >> n

    nxt = []
    for v, e in states:
        direct_state = direct(v, e)
        assert direct_state == toggles(v, e)
        assert direct_state in index
        nxt.append(index[direct_state])
    assert len(set(nxt)) == len(states), 'Rowmotion must be a permutation.'

    seen = bytearray(len(states))
    lengths = Counter()
    orbit_count = 0
    for initial in range(len(states)):
        if seen[initial]:
            continue
        p = initial
        count = 0
        while not seen[p]:
            seen[p] = 1
            p = nxt[p]
            count += 1
        assert p == initial
        orbit_count += 1
        lengths[count] += 1
    assert all(seen)
    assert sum(k * v for k, v in lengths.items()) == len(states)
    assert sum(lengths.values()) == orbit_count
    order = lcm(*lengths.keys())
    print(name, 'aut=', automorphisms, 'ideals=',len(states),
          'orbits=', orbit_count, 'order=', order,
          'max_length=', max(lengths))
    print(name, 'orbit_length_multiplicities=', sorted(lengths.items()))
    return len(states),orbit_count,order,max(lengths),lengths,signature,rank_from_subsets


def main():
    c=compute('Cube Q3',cube_edges())
    w=compute('Wagner M8',wagner_edges())
    assert (c[0], c[1], c[2], c[3]) == (12643, 1093, 110880, 90)
    assert (w[0], w[1], w[2], w[3]) == (12641, 901, 244379520, 232)
    assert w[2] == 2204*c[2]
    assert c[4][90] == 16 and w[4][232] == 2
    defect = Counter({(4,0): 2, (4,1): -8, (4,2): 12, (4,3): -8, (4,4): 2})
    assert all(c[5][key] - w[5][key] == defect[key] for key in set(c[5])|set(w[5])|set(defect))
    assert all(c[6][i]-w[6][i] == (2 if i==8 else 0) for i in range(21))
    print('Induced subgraph polynomial difference = 2*u^4*(1-v)^4')
    print('Rank polynomial difference = 2*t^8')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
