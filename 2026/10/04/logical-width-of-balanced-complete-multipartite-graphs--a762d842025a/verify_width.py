#!/usr/bin/env python3
"""Finite sanity checks for the k-pebble lower-bound witnesses.

For 1 <= r,s <= 4, this script forms the two balanced complete multipartite
structures used in the proof and checks that equality of atomic k-tuple types
is a back-and-forth relation for k=max(r,s).  An unplaced pebble is denoted -1.
This is a finite verification aid; the theorem itself is proved symbolically.
"""
from itertools import product


def vertices(r, s):
    return [(a, b) for a in range(r) for b in range(s)]


def atomic_type(tup, verts):
    # Canonicalize a partial tuple by equality and same-part information.
    # Complete multipartite adjacency is exactly: distinct and different part.
    ans = []
    for i, x in enumerate(tup):
        if x == -1:
            ans.append(('U',))
            continue
        vx = verts[x]
        row = []
        for j in range(i):
            y = tup[j]
            if y == -1:
                row.append('U')
            elif x == y:
                row.append('=')
            elif vx[0] == verts[y][0]:
                row.append('N')  # distinct nonadjacent vertices, same part
            else:
                row.append('E')  # adjacent vertices, different parts
        ans.append(tuple(row))
    return tuple(ans)


def type_graph(r, s, k):
    vs = vertices(r, s)
    reps = {}
    domain = range(-1, len(vs))
    for tup in product(domain, repeat=k):
        typ = atomic_type(tup, vs)
        reps.setdefault(typ, tup)
    moves = {}
    for typ, tup in reps.items():
        per_coordinate = []
        for i in range(k):
            opts = set()
            for v in range(len(vs)):
                nxt = list(tup)
                nxt[i] = v
                opts.add(atomic_type(tuple(nxt), vs))
            per_coordinate.append(frozenset(opts))
        moves[typ] = tuple(per_coordinate)
    return set(reps), moves


def check_pair(r1, s1, r2, s2, k):
    t1, m1 = type_graph(r1, s1, k)
    t2, m2 = type_graph(r2, s2, k)
    assert t1 == t2, (r1, s1, r2, s2, k, 'type sets differ')
    for typ in t1:
        assert m1[typ] == m2[typ], (r1, s1, r2, s2, k, 'move sets differ', typ)


def main():
    cases = 0
    for r in range(1, 5):
        for s in range(1, 5):
            k = max(r, s)
            if s >= r:
                check_pair(r, s, r, s + 1, k)
            else:
                check_pair(r, s, r + 1, s, k)
            cases += 1
    print(f'VERIFY_OK cases={cases} r_s_range=1..4 lower_witness_pebble_bisimulation')


if __name__ == '__main__':
    main()
