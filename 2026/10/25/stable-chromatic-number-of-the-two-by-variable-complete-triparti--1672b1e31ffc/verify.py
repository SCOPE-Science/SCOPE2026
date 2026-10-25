#!/usr/bin/env python3
"""Exact checks for a stable-colouring obstruction on complete tripartite graphs.
Uses only Python's standard library. Execute: python3 verify.py
"""
from itertools import product
from collections import defaultdict, Counter

BASE = ((1, 2, 3, 4), (2, 3, 4, 1),
        (2, 3, 4, 1), (4, 1, 2, 3),
        (2, 3, 4, 1), (4, 1, 2, 3))

def ranks_from_orders(orders):
    return [{color: place for place, color in enumerate(order)} for order in orders]

def valid_colouring(colors, groups):
    return all(colors[u] != colors[v]
               for u in range(len(colors)) for v in range(u)
               if groups[u] != groups[v])

def envy_arcs(colors, groups, ranks):
    arcs = set()
    for u in range(len(colors)):
        for v in range(len(colors)):
            if groups[u] != groups[v] and ranks[u][colors[v]] < ranks[u][colors[u]]:
                arcs.add((u, v))
    return arcs

def cycle_witness(arcs, count):
    # Exact directed cycle detector; return a directed cycle as vertex indices.
    out = [[v for u0, v in arcs if u0 == u] for u in range(count)]
    state = [0] * count
    stack = []
    def dfs(v):
        state[v] = 1
        stack.append(v)
        for w in out[v]:
            if state[w] == 1:
                return tuple(stack[stack.index(w):])
            if state[w] == 0:
                found = dfs(w)
                if found:
                    return found
        stack.pop()
        state[v] = 2
        return ()
    for v in range(count):
        if state[v] == 0:
            found = dfs(v)
            if found:
                return found
    return ()

def base_test():
    groups = [0,0,1,1,2,2]
    ranks = ranks_from_orders(BASE)
    count = Counter()
    exceptional = []
    for coloring in product((1,2,3,4), repeat=6):
        if not valid_colouring(coloring, groups):
            continue
        arcs = envy_arcs(coloring,groups,ranks)
        two = any((v,u) in arcs for (u,v) in arcs)
        witness = cycle_witness(arcs,6)
        assert witness, ('unblocked', coloring)
        if two:
            count[(len(set(coloring)), 2)] += 1
        else:
            triangles = [tr for tr in product(range(6),repeat=3)
                         if len(set(tr)) == 3 and all((tr[q],tr[(q+1)%3]) in arcs for q in range(3))]
            assert triangles, ('no short directed cycle',coloring,witness)
            count[(len(set(coloring)), 3)] += 1
            exceptional.append((coloring,triangles[0]))
    assert count == Counter({(3,2):24, (4,2):68, (4,3):4}), count
    assert len(exceptional) == 4
    print('BASE_OK: 96 complete proper four-colour assignments; 92 blocked by 2-cycles, 4 by 3-cycles')
    print('EXCEPTIONAL:', exceptional)

def constructed_profile(m):
    # Parts A size m, B size m, C size 2; p=m-2 prefix levels,
    # followed by a copy of K_{2,2,2} in the top four hues.
    p = m - 2
    k = m + 2
    orders = []
    for part in range(3):
        if part < 2:
            for i in range(1, p + 1):
                orders.append(tuple([i] + list(range(i + 1, k + 1))
                                    + list(range(i-1, 0, -1))))
        for j in range(2):
            orders.append(tuple(p + x for x in BASE[2*part+j])
                          + tuple(range(p,0,-1)))
    groups = [0]*m + [1]*m + [2]*2
    assert len(orders) == 2*m+2
    assert all(sorted(order) == list(range(1,k+1)) for order in orders)
    return groups, ranks_from_orders(orders)

def proper_colorings_by_parts(sizes, k):
    # Enumerate every proper colouring ONCE by disjoint exact used palettes.
    buckets = []
    for size in sizes:
        d = defaultdict(list)
        for t in product(range(1,k+1), repeat=size):
            mask = sum(1<<(c-1) for c in set(t))
            d[mask].append(t)
        buckets.append(d)
    for ma, aa in buckets[0].items():
        for mb, bb in buckets[1].items():
            if ma & mb: continue
            for mc, cc in buckets[2].items():
                if (ma | mb) & mc: continue
                for a in aa:
                    for b in bb:
                        for c in cc:
                            yield a+b+c

def sample_general(m):
    sizes = (m,m,2)
    k = m + 2
    groups, ranks = constructed_profile(m)
    tested = 0
    bad = 0
    for colors in proper_colorings_by_parts(sizes,k):
        tested += 1
        witness = cycle_witness(envy_arcs(colors,groups,ranks),len(groups))
        if not witness:
            bad += 1
            raise AssertionError(('stable coloring found',m,colors))
    print(f'EXTENSION_OK: m={m}, tested {tested} / all proper {k}-colour assignments, none stable')
    assert tested > 0 and bad == 0

if __name__ == '__main__':
    base_test()
    for m in (2,3,4):
        sample_general(m)
    print('VERIFY_OK')
