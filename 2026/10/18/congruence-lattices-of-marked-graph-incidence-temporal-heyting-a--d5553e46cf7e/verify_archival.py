#!/usr/bin/env python3
"""Independent exhaustive tests of the archival-upset formula for finite incidence transits."""
from itertools import combinations


def components(n, nonreflexive):
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in nonreflexive:
        parent[root(u)] = root(v)
    groups = {}
    for v in range(n):
        groups.setdefault(root(v), []).append(v)
    return list(groups.values())


def predicted(n, edges, mask):
    nonreflexive = [edges[i] for i in range(len(edges)) if not (mask >> i) & 1]
    reflexive = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
    comps = components(n, nonreflexive)
    answer = 0
    for subset in range(1 << len(comps)):
        unselected = set()
        for i, comp in enumerate(comps):
            if (subset >> i) & 1:
                unselected.update(comp)
        inside = sum(u in unselected and v in unselected for u, v in reflexive)
        answer += 1 << inside
    return answer


def direct(n, edges, mask):
    """Evaluate upset and archival definitions with quantifiers over every point."""
    m = len(edges)
    size = n + m
    successors = [set() for _ in range(size)]
    for k, (u, v) in enumerate(edges):
        successors[u].add(n + k)
        successors[v].add(n + k)
        if (mask >> k) & 1:
            successors[n + k].add(n + k)
    nvalid = 0
    for bits in range(1 << size):
        # A subset is an upset iff no chosen vertex has an unchosen edge above it.
        if any((bits >> u) & 1 and not (bits >> (n + i)) & 1
               for i, (u, v) in enumerate(edges)):
            continue
        if any((bits >> v) & 1 and not (bits >> (n + i)) & 1
               for i, (u, v) in enumerate(edges)):
            continue
        # Archival: x outside, z inside, x R z -> some y inside
        # that has x <= y and y R z.
        valid = True
        for x in range(size):
            if (bits >> x) & 1:
                continue
            for z in successors[x]:
                if not (bits >> z) & 1:
                    continue
                witnessed = False
                for y in range(size):
                    if not (bits >> y) & 1:
                        continue
                    x_le_y = y == x or y in successors[x]
                    y_R_z = z in successors[y]
                    if x_le_y and y_R_z:
                        witnessed = True
                        break
                if not witnessed:
                    valid = False
                    break
            if not valid:
                break
        nvalid += valid
    return nvalid


def test(max_n=4):
    total = 0
    for n in range(max_n + 1):
        complete = list(combinations(range(n), 2))
        cnt = 0
        for g in range(1 << len(complete)):
            edges = [e for j, e in enumerate(complete) if g >> j & 1]
            for loops in range(1 << len(edges)):
                got = direct(n, edges, loops)
                want = predicted(n, edges, loops)
                if got != want:
                    raise AssertionError((n, edges, loops, got, want))
                cnt += 1
        print('n',n,'cases',cnt,'OK',flush=True)
        total += cnt
    print('PASS:',total,'edge-labelled graphs with all edge reflexivity patterns, n<=',max_n)

if __name__ == '__main__':
    test()
