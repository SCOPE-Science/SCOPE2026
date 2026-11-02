#!/usr/bin/env python3
"""Independent count-free three-pebble type refinement on small subspace lattices.

Enumerates spans by closure, then refines ordered 3-tuple atomic colors
using sets (not multiplicities) of one-coordinate replacement colors.
"""
from itertools import product
import json


def vec(i, q, d):
    return tuple((i // q ** j) % q for j in range(d))


def latt(d, q):
    vectors = [vec(i, q, d) for i in range(q ** d)]
    index = {v: i for i, v in enumerate(vectors)}
    add = [[index[tuple((a + b) % q for a, b in zip(u, v))]
            for v in vectors] for u in vectors]
    mul = [[index[tuple((t * a) % q for a in v)]
            for v in vectors] for t in range(q)]
    zero = frozenset({0})
    found = {zero}
    queue = [zero]
    for s in queue:
        for v in range(len(vectors)):
            if v in s:
                continue
            nxt = frozenset(add[u][mul[t][v]] for u in s for t in range(q))
            if nxt not in found:
                found.add(nxt)
                queue.append(nxt)
    out = [sum(1 << v for v in s) for s in found]
    return sorted(out)


def init_diagrams(subspaces):
    n = len(subspaces)
    le = [[int(a & b == a) for b in subspaces] for a in subspaces]
    tuples = list(product(range(n), repeat=3))
    diagrams = []
    for tpl in tuples:
        diagrams.append(tuple(le[tpl[i]][tpl[j]] for i in range(3) for j in range(3)))
    return tuples, diagrams


def refine_all(parts):
    # One shared color dictionary ensures comparable color identities across fields.
    data = []
    for subspaces in parts:
        tup, diags = init_diagrams(subspaces)
        n = len(subspaces)
        data.append((n, tup, diags))
    canon = {s: i for i, s in enumerate(sorted(set(diag for _, _, ds in data for diag in ds)))}
    colors = [[canon[s] for s in ds] for _, _, ds in data]
    rounds = 0
    while True:
        keys = []
        for (n, tuples, _), col in zip(data, colors):
            pair_c = {}
            for i in range(n):
                for j in range(n):
                    pair_c[0, i, j] = tuple(sorted({col[t * n * n + i * n + j] for t in range(n)}))
                    pair_c[1, i, j] = tuple(sorted({col[i * n * n + t * n + j] for t in range(n)}))
                    pair_c[2, i, j] = tuple(sorted({col[i * n * n + j * n + t] for t in range(n)}))
            cur = [(col[a * n * n + b * n + c], pair_c[0, b, c],
                    pair_c[1, a, c], pair_c[2, a, b]) for a, b, c in tuples]
            keys.append(cur)
        distinct = sorted(set(s for ks in keys for s in ks))
        mp = {sig: i for i, sig in enumerate(distinct)}
        newcolors = [[mp[s] for s in ks] for ks in keys]
        rounds += 1
        oldcount = len(set(x for arr in colors for x in arr))
        newcount = len(distinct)
        colors = newcolors
        if oldcount == newcount:
            break
        assert rounds < 30
    sets = [set(cs) for cs in colors]
    return rounds, newcount, sets


def main():
    reports = []
    for d in (1, 2, 3):
        fields = (2, 3, 5) if d <= 2 else (2, 3)
        parts = [latt(d, q) for q in fields]
        rounds, c, sets = refine_all(parts)
        assert all(s == sets[0] for s in sets[1:]), (d, fields)
        reports.append({'dimension': d, 'fields': fields,
                        'lattice_sizes': [len(s) for s in parts],
                        'refinement_rounds': rounds, 'global_colors': c,
                        'status': 'PASS'})
    # A control: different dimensions must be distinguishable, as height shows.
    for a, b in ((1, 2), (2, 3)):
        s = [latt(a, 2), latt(b, 2)]
        _, _, color_sets = refine_all(s)
        assert color_sets[0] != color_sets[1], (a, b)
    print(json.dumps({'test': 'direct-three-pebble-refinement',
                      'same_dimension': reports,
                      'different_dimension_controls': 'PASS',
                      'status': 'PASS'}, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
