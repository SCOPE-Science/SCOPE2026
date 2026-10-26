#!/usr/bin/env python3
"""Exhaustive, self-contained rowmotion orbit verifier for Petersen incidence poset.
Run with Python 3.10+: python verify_petersen_rowmotion.py
"""
from itertools import combinations
from collections import Counter
from math import lcm

EXPECTED = {
 2:891, 3:11, 5:5, 6:685, 7:10, 8:456, 10:715, 11:10,
 12:510, 14:690, 16:120, 18:70, 20:390, 21:10,
 22:90, 24:15, 28:300, 32:120, 33:40, 34:60,
 36:180, 40:30, 42:80, 44:90, 52:75, 60:20,
 64:30, 66:30, 68:30, 72:60, 74:60, 88:60,
 92:30, 100:60, 116:30, 118:60, 120:24, 136:30, 192:30
}

def generalized_petersen_edges():
    """Outer pentagon, inner pentagram, and five spokes."""
    E = {tuple(sorted((i, (i+1)%5))) for i in range(5)}
    E |= {tuple(sorted((5+i, 5+(i+2)%5))) for i in range(5)}
    E |= {(i, i+5) for i in range(5)}
    return sorted(E)

def kneser_petersen_edges():
    """Disjointness among the ten 2-subsets of a 5-set."""
    V = list(combinations(range(5), 2))
    return [(i,j) for i in range(10) for j in range(i+1,10)
            if not (set(V[i]) & set(V[j]))]

def enumerate_ideals(edges):
    """All ideals correspond bijectively to U subset vertices and F subset E[U]."""
    n = 10
    edge_mask = [0] * (1 << n)
    for u in range(1 << n):
        edge_mask[u] = sum(1 << j for j,(a,b) in enumerate(edges)
                           if u & (1<<a) and u & (1<<b))
    for u in range(1 << n):
        mask = edge_mask[u]
        f = mask
        while True:
            yield u, f
            if f == 0:
                break
            f = (f - 1) & mask

def independent_transitions(edges, u, f):
    """Directly compute minimal complement, then its downward closure."""
    n = 10
    new_vertex = ((1 << n) - 1) & ~u
    new_edges = 0
    for j,(a,b) in enumerate(edges):
        if not f & (1 << j) and u & (1<<a) and u & (1<<b):
            new_edges |= 1 << j
            new_vertex |= (1<<a) | (1<<b)
    return new_vertex, new_edges

def toggle_transitions(edges, u, f):
    """Apply upper-rank toggles, then lower-rank toggles."""
    for j,(a,b) in enumerate(edges):
        bit=1<<j
        if f & bit:
            f ^= bit
        elif (u & (1<<a)) and (u & (1<<b)):
            f |= bit
    for v in range(10):
        bit = 1<<v
        if not u & bit:
            u |= bit
        elif all(not (f & (1 << j)) for j,(a,b) in enumerate(edges)
                 if a == v or b == v):
            u ^= bit
    return u,f

def count_orbits(edges, dynamics):
    assert len(edges)==15 and len(set(edges))==15
    assert len({a for e in edges for a in e})==10
    assert all(sum(v in e for e in edges)==3 for v in range(10))
    states = set(enumerate_ideals(edges))
    assert len(states)==133958, len(states)
    # Exhaustively ensure the defining map and two independent formulas agree
    # on every ideal, and that every target remains an ideal.
    if dynamics is independent_transitions:
        for s in states:
            t=independent_transitions(edges,*s)
            assert t in states
            assert t==toggle_transitions(edges,*s)
    unvisited = set(states)
    hist = Counter()
    while unvisited:
        start = next(iter(unvisited))
        here = start
        length = 0
        while here in unvisited:
            unvisited.remove(here)
            length += 1
            here = dynamics(edges, *here)
        assert here == start, ('not a permutation',start,here,length)
        hist[length]+=1
    assert sum(k*v for k,v in hist.items())==len(states)
    return hist

def main():
    for name, edges, dyn in [
        ('GP(5,2), minimal-complement', generalized_petersen_edges(), independent_transitions),
        ('KG(5,2), toggles', kneser_petersen_edges(), toggle_transitions),
    ]:
        histogram=count_orbits(edges,dyn)
        assert histogram==EXPECTED,(name,histogram)
        period=lcm(*histogram)
        assert period==356800176532800,period
        assert sum(histogram.values())==6207
        print(name, 'ideals=133958 cycles=6207 orbit_lengths=39 max=192 period='+str(period))
    print('VERIFY_OK')
if __name__ == '__main__':
    main()
