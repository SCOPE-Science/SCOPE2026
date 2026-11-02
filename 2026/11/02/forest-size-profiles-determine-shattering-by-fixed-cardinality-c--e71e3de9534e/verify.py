"""Finite checks for fixed-cardinality cut-query shattering.

All enumeration is finite and supplements, rather than replaces, the general proof.
"""
from itertools import combinations
from functools import lru_cache


def component_orders(n, edges):
    parent = list(range(n))
    def root(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    for u, v in edges:
        ru, rv = root(u), root(v)
        if ru == rv:
            return None
        parent[ru] = rv
    sizes = {}
    for i in range(n):
        r = root(i)
        sizes[r] = sizes.get(r, 0) + 1
    return tuple(sorted(sizes.values()))


def profile_criterion(sizes, a):
    states = {1}
    for t in sizes:
        nxt = set()
        for reachable in states:
            for c in range(t // 2 + 1):
                nxt.add((reachable << c) | (reachable << (t - c)))
        states = nxt
    return all((reachable >> a) & 1 for reachable in states)


def direct_shattered(n, a, edges):
    patterns = set()
    for marked in combinations(range(n), a):
        m = set(marked)
        pat = 0
        for j, (u, v) in enumerate(edges):
            if (u in m) == (v in m):
                pat |= 1 << j
        patterns.add(pat)
    return len(patterns) == (1 << len(edges))


def run():
    checked = 0
    for n in range(2, 7):
        q = list(combinations(range(n), 2))
        for a in range(1, n // 2 + 1):
            direct_max = -1
            profile_max = -1
            for mask in range(1 << len(q)):
                S = tuple(e for j, e in enumerate(q) if (mask >> j) & 1)
                direct = direct_shattered(n, a, S)
                sizes = component_orders(n, S)
                theorem = sizes is not None and profile_criterion(sizes, a)
                assert direct == theorem, (n, a, S, direct, theorem)
                if direct:
                    direct_max = max(direct_max, len(S))
                    profile_max = max(profile_max, len(S))
                checked += 1
            assert direct_max == profile_max
            print(f'n={n} a={a} direct_vc={direct_max} all_edge_sets_checked={1 << len(q)}')
    for a in range(1, 9):
        n = 3 * a + 1
        star = tuple((0, j) for j in range(1, 2 * a + 1))
        sizes = component_orders(n, star)
        assert len(star) == 2 * a
        assert profile_criterion(sizes, a)
    print('SATURATION_STAR_PROFILES_PASS a=1..8')
    print('ALL_FIXED_CARDINALITY_CUT_CHECKS_PASS', checked)


if __name__ == '__main__':
    run()
