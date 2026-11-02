"""Exact finite checks for the S5 bisimulation edge-cover theorem.
Run: python checker.py
No external libraries are required.
"""
from functools import lru_cache
from itertools import product
from math import comb


def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n - 1):
        for j in range(max(p, default=-1) + 2):
            yield p + (j,)


@lru_cache(None)
def bipartite_covers(a, b):
    return sum((-1) ** (i + j) * comb(a, i) * comb(b, j)
               * 2 ** ((a - i) * (b - j))
               for i in range(a + 1) for j in range(b + 1))


@lru_cache(None)
def minimal_bipartite_covers(a, b):
    """Star-forest recurrence, not the direct relation enumeration."""
    if a == b == 0:
        return 1
    if not a or not b:
        return 0
    # Component containing the first left-hand vertex.
    v = sum(comb(b, r) * minimal_bipartite_covers(a - 1, b - r)
            for r in range(1, b + 1))
    v += sum(b * comb(a - 1, s - 1) * minimal_bipartite_covers(a - s, b - 1)
             for s in range(2, a + 1))
    return v


def vertex_classes(part):
    d = {}
    for v, j in enumerate(part):
        d.setdefault(j, []).append(v)
    return list(d.values())


def weights(part1, colors1, part2, colors2):
    ca, cb = vertex_classes(part1), vertex_classes(part2)
    edges = []
    for i, A in enumerate(ca):
        a = {c: sum(colors1[x] == c for x in A) for c in set(colors1[x] for x in A)}
        for j, B in enumerate(cb):
            b = {c: sum(colors2[y] == c for y in B) for c in set(colors2[y] for y in B)}
            if set(a) == set(b):
                beta, mu = 1, 1
                for c in a:
                    beta *= bipartite_covers(a[c], b[c])
                    mu *= minimal_bipartite_covers(a[c], b[c])
                edges.append((i, j, beta, mu))
    return len(ca), len(cb), edges


def predicted(part1, colors1, part2, colors2):
    r, s, edges = weights(part1, colors1, part2, colors2)
    total = 1
    for _, _, beta, _ in edges:
        total *= 1 + beta
    total -= 1
    minimal = sum(mu for _, _, _, mu in edges)
    global_total = global_min = 0
    for subset in range(1 << len(edges)):
        active = [e for z, e in enumerate(edges) if subset & (1 << z)]
        if ({i for i, j, _, _ in active} != set(range(r)) or
                {j for i, j, _, _ in active} != set(range(s))):
            continue
        value, minvalue = 1, 1
        for _, _, beta, mu in active:
            value *= beta
            minvalue *= mu
        global_total += value
        deg_l = [0] * r
        deg_r = [0] * s
        for i, j, _, _ in active:
            deg_l[i] += 1
            deg_r[j] += 1
        if all(deg_l[i] == 1 or deg_r[j] == 1 for i, j, _, _ in active):
            global_min += minvalue
    return (total, minimal, global_total, global_min)


def direct(part1, colors1, part2, colors2):
    a, b = len(part1), len(part2)
    whole = 1 << (a * b)
    valid = [False] * whole
    global_valid = [False] * whole
    # Directly check the atomic, forth and back clauses for every relation.
    for mask in range(1, whole):
        pairs = [(i, j) for i in range(a) for j in range(b)
                 if mask & (1 << (i * b + j))]
        if any(colors1[i] != colors2[j] for i, j in pairs):
            continue
        okay = True
        for i, j in pairs:
            for x in range(a):
                if part1[x] == part1[i] and not any(x == v and part2[w] == part2[j]
                                                       for v, w in pairs):
                    okay = False
                    break
            if not okay:
                break
            for y in range(b):
                if part2[y] == part2[j] and not any(y == w and part1[v] == part1[i]
                                                       for v, w in pairs):
                    okay = False
                    break
            if not okay:
                break
        if okay:
            valid[mask] = True
            global_valid[mask] = (len({i for i, _ in pairs}) == a
                                  and len({j for _, j in pairs}) == b)
    # A subset zeta transform to test minimality by actual inclusion.
    def count_minimal(flags):
        has_sub = flags[:]
        count = 0
        for mask in range(1, whole):
            any_proper = False
            for p in range(a * b):
                if mask & (1 << p):
                    sub = mask ^ (1 << p)
                    if has_sub[sub]:
                        any_proper = True
            if flags[mask] and not any_proper:
                count += 1
            has_sub[mask] = flags[mask] or any_proper
        return count
    return (sum(valid), count_minimal(valid),
            sum(global_valid), count_minimal(global_valid))


def run():
    assert [(bipartite_covers(a, b), minimal_bipartite_covers(a, b))
            for a, b in [(1, 1), (2, 2), (2, 3), (3, 3), (4, 4)]] == [
                (1, 1), (7, 2), (25, 6), (265, 15), (41503, 184)]
    tested = 0
    for n in range(1, 4):
        for m in range(1, 4):
            for p in partitions(n):
                for q in partitions(m):
                    for c in product(range(2), repeat=n):
                        for d in product(range(2), repeat=m):
                            x = predicted(p, c, q, d)
                            y = direct(p, c, q, d)
                            assert x == y, (p, c, q, d, x, y)
                            tested += 1
    # All four variables of the weighted component graph matter.
    assert predicted((0, 1), (0, 0), (0, 1), (0, 0)) == (15, 4, 7, 2)
    assert predicted((0, 0), (0, 0), (0, 0), (0, 0)) == (7, 2, 7, 2)
    assert predicted((0, 0), (0, 1), (0, 1), (0, 1)) == (0, 0, 0, 0)
    # Larger independent check with 4 vs. 3 states and a fixed disconnected pair.
    cases = [((0, 0, 1, 1), (0, 1, 0, 1), (0, 0, 1), (1, 0, 0)),
             ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0), (0, 0, 0)),
             ((0, 1, 2, 3), (0, 0, 0, 0), (0, 1, 2), (0, 0, 0)),
             ((0, 0, 1, 1), (0, 0, 1, 1), (0, 1, 2), (0, 1, 1))]
    for case in cases:
        assert predicted(*case) == direct(*case), case
        tested += 1
    print(f"ALL_CHECKS_OK model_pairs={tested} profile_cases=5")

if __name__ == '__main__':
    run()
