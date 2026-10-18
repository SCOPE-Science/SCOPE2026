"""Standalone exact checks for independent-domination vertex alteration in cyclic clique blow-ups.
All computations use only the Python standard library.
"""
from itertools import combinations
from math import comb, ceil


def independent_domination(adj, retained):
    """Brute-force minimum independent dominating set in an induced graph.
    adj is an array of neighbor bit masks; retained is a vertex bit mask.
    """
    vertices = [i for i in range(len(adj)) if retained & (1 << i)]
    if not vertices:
        return 0
    for k in range(1, len(vertices) + 1):
        for choice in combinations(vertices, k):
            chosen = sum(1 << v for v in choice)
            if any(adj[v] & chosen for v in choice):
                continue
            covered = chosen
            for v in choice:
                covered |= adj[v]
            if covered & retained == retained:
                return k
    raise AssertionError('Every finite graph has a maximal independent set')


def cycle_adjacency(n):
    a = [0] * n
    for v in range(n):
        a[v] |= (1 << ((v - 1) % n)) | (1 << ((v + 1) % n))
    return a


def blowup_adjacency(base, q):
    n = len(base)
    a = [0] * (n * q)
    for u in range(n):
        for i in range(q):
            at = u * q + i
            for v in range(n):
                for j in range(q):
                    if (u == v and i != j) or ((base[u] >> v) & 1):
                        a[at] |= 1 << (v * q + j)
    return a


def induced_cycle_paths_indom(n, deleted):
    """Independent domination via path lengths, independently of graph subset search."""
    D = set(deleted)
    if not D:
        return (n + 2) // 3
    order = sorted(D)
    result = 0
    for j, v in enumerate(order):
        next_v = order[(j + 1) % len(order)]
        gap = (next_v - v - 1) % n
        result += (gap + 2) // 3
    return result


def expected(n):
    k, r = divmod(n, 3)
    if r == 0:
        return (3, k * k * (k + 1) // 2, k * k * (k - 1) // 2)
    if r == 1:
        return (1, n, 0)
    return (2, n * (k + 1) // 2, 0)


def verify_cycle_classes():
    for n in range(3, 31):
        t, down_expected, up_expected = expected(n)
        old = (n + 2) // 3
        for r in range(t):
            for D in combinations(range(n), r):
                assert induced_cycle_paths_indom(n, D) == old, (n, D)
        down = up = 0
        for D in combinations(range(n), t):
            delta = induced_cycle_paths_indom(n, D) - old
            down += delta < 0
            up += delta > 0
            if delta:
                cyclic_gaps = [(D[(j + 1) % t] - D[j] - 1) % n for j in range(t)]
                if n % 3 == 0:
                    assert (delta == -1 and all(x % 3 == 0 for x in cyclic_gaps)) or (delta == 1 and all(x % 3 == 1 for x in cyclic_gaps)), (n, D, delta)
                elif n % 3 == 2:
                    assert delta == -1 and all(x % 3 == 0 for x in cyclic_gaps), (n, D, delta)
                else:
                    assert delta == -1
        assert (down, up) == (down_expected, up_expected), (n, down, up)
    print('Cycle gap classification agrees through n=30')


def verify_direct_cycle():
    for n in range(3, 12):
        a = cycle_adjacency(n)
        t = expected(n)[0]
        for r in range(t + 1):
            for D in combinations(range(n), r):
                kept = sum(1 << v for v in range(n) if v not in D)
                assert independent_domination(a, kept) == induced_cycle_paths_indom(n, D), (n, D)
    print('Direct vertex-set independent-domination search agrees through n=11')


def verify_blowup_transfer():
    count = 0
    for n in range(1, 5):
        edges = list(combinations(range(n), 2))
        for edge_set in range(1 << len(edges)):
            base = [0] * n
            for i, (u, v) in enumerate(edges):
                if edge_set & (1 << i):
                    base[u] |= 1 << v
                    base[v] |= 1 << u
            a = blowup_adjacency(base, 2)
            for deleted in range(1 << (2 * n)):
                surviving = ((1 << (2 * n)) - 1) ^ deleted
                base_kept = 0
                for v in range(n):
                    if surviving & (3 << (2 * v)):
                        base_kept |= 1 << v
                got = independent_domination(a, surviving)
                want = independent_domination(base, base_kept)
                assert got == want, (n, edge_set, deleted, got, want)
                count += 1
    print('Direct clique-substitution transfer:', count, 'exhaustive labeled-graph/deletion pairs (q=2,n<=4)')


def verify_specific_cycles_blowup():
    for n, q in [(3, 2), (4, 2), (5, 2), (6, 2), (3, 3), (4, 3)]:
        a = blowup_adjacency(cycle_adjacency(n), q)
        N = n*q
        original = independent_domination(a, (1 << N) - 1)
        t, down_expected, up_expected = expected(n)
        count_down = count_up = 0
        for r in range(q*t+1):
            for D in combinations(range(N), r):
                deleted = sum(1 << v for v in D)
                v = independent_domination(a, ((1 << N)-1) ^ deleted)
                if r < q*t:
                    assert v == original, (n,q,r,D)
                else:
                    count_down += v < original
                    count_up += v > original
                    if v != original:
                        for fiber in range(n):
                            masks = deleted & (((1 << q)-1) << (q*fiber))
                            assert masks in (0, ((1 << q)-1) << (q*fiber))
        assert (count_down,count_up)==(down_expected,up_expected), (n,q,count_down,count_up)
    print('Direct clique-cycle checks n=3..6 q=2 and n=3..4 q=3: OK')


if __name__ == '__main__':
    verify_cycle_classes()
    verify_direct_cycle()
    verify_blowup_transfer()
    verify_specific_cycles_blowup()
    print('VERIFY_OK')
