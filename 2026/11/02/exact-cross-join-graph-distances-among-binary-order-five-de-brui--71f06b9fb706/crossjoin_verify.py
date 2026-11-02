#!/usr/bin/env python3
"""Exact cross-join metric certificate for binary order-five de Bruijn cycles.
Requires Python >=3.8; no dependencies or external files.
"""
from collections import Counter, deque
from itertools import combinations

ORDER = 5
STATES = 1 << ORDER
PAIRS = 1 << (ORDER-1)
UNIVERSE = 1 << PAIRS
FULL = (1 << STATES) - 1

def successor(mask, s):
    tail = s & (PAIRS-1)
    bit = (mask >> tail) & 1
    if s & PAIRS:
        bit ^= 1
    return (tail << 1) | bit

def cycle(mask):
    """Return 0-rooted Hamiltonian orbit, or None."""
    seen = 0
    x = 0
    walk = []
    for _ in range(STATES):
        if (seen >> x) & 1:
            return None
        seen |= 1 << x
        walk.append(x)
        x = successor(mask, x)
    return walk if x == 0 and seen == FULL else None

def certified_graph():
    cycles = {}
    for mask in range(UNIVERSE):
        walk = cycle(mask)
        if walk is not None:
            cycles[mask] = walk
    assert len(cycles) == 2048
    masks = tuple(sorted(cycles))
    index = {mask:i for i,mask in enumerate(masks)}
    adjacency = [[] for _ in masks]
    toggles = [(1 << i) | (1 << j) for i,j in combinations(range(PAIRS),2)]
    for pos,mask in enumerate(masks):
        orbit = cycles[mask]
        location = {v:i for i,v in enumerate(orbit)}
        assert len(location) == STATES
        for i,j in combinations(range(PAIRS),2):
            ai,bi = location[i],location[i+PAIRS]
            aj,bj = location[j],location[j+PAIRS]
            span = (bi-ai) % STATES
            alternating = (((aj-ai) % STATES < span) !=
                           ((bj-ai) % STATES < span))
            other = mask ^ ((1 << i) | (1 << j))
            # Independently verify the two-switch criterion by alternation.
            assert alternating == (other in index), (mask,i,j)
            if alternating:
                adjacency[pos].append(index[other])
    assert all(i in adjacency[j] for i,row in enumerate(adjacency) for j in row)
    assert len({(min(i,j),max(i,j)) for i,row in enumerate(adjacency) for j in row}) == 38704
    return masks,adjacency

def distance_spectrum(adjacency):
    n = len(adjacency)
    pairs = Counter()
    eccentricities = Counter()
    witness = None
    for src in range(n):
        distance = [-1]*n
        distance[src] = 0
        queue = deque((src,))
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if distance[v] == -1:
                    distance[v] = distance[u]+1
                    queue.append(v)
        assert all(x >= 0 for x in distance)
        e = max(distance)
        eccentricities[e]+=1
        for dst in range(src+1,n):
            pairs[distance[dst]]+=1
            if distance[dst]==7 and witness is None:
                witness = (src,dst)
    return pairs,eccentricities,witness

def main():
    masks,adj = certified_graph()
    degree = Counter(len(row) for row in adj)
    # The degree distribution alone is already in Alhakim (2018), Table 1.
    earlier_degrees = {31:88,32:152,33:240,34:272,35:216,
                       36:136,37:208,38:16,39:176,40:64,41:48,
                       42:16,43:40,45:112,47:136,48:48,
                       49:32,51:16,60:8,62:16,64:8}
    assert degree == earlier_degrees
    pairs,ecc,witness=distance_spectrum(adj)
    expected_pairs = {1:38704,2:305376,3:758800,4:710976,
                      5:254800,6:27104,7:368}
    expected_ecc = {5:48,6:1264,7:736}
    assert pairs == expected_pairs, pairs
    assert ecc == expected_ecc, ecc
    assert sum(pairs.values()) == len(masks)*(len(masks)-1)//2
    assert sum(ecc.values()) == len(masks)
    assert witness is not None
    print('NODES',len(masks))
    print('EDGES',pairs[1])
    print('DIAMETER',max(ecc))
    print('RADIUS',min(ecc))
    print('UNORDERED_DISTANCE_COUNTS',dict(sorted(pairs.items())))
    print('ECCENTRICITY_COUNTS',dict(sorted(ecc.items())))
    print('DISTANCE_SEVEN_PAIR',masks[witness[0]],masks[witness[1]])
    print('VERIFY_OK')

if __name__=='__main__':
    main()
