#!/usr/bin/env python3
from functools import lru_cache
from math import factorial


def book_graph(n):
    # Vertices: 0=u, 1=v, then a_i,b_i for i=0,...,n-1.
    N = 2 + 2*n
    adj = [set() for _ in range(N)]
    def add(x,y):
        adj[x].add(y); adj[y].add(x)
    add(0,1)
    for i in range(n):
        a = 2 + 2*i
        b = a + 1
        add(0,a); add(a,b); add(b,1)
    return adj


def direct_check(n):
    adj = book_graph(n)
    N = len(adj)
    neigh = [sum(1 << w for w in adj[z]) for z in range(N)]
    full = (1 << N) - 1

    @lru_cache(None)
    def best(dom):
        ans = 0
        for m in neigh:
            if m & ~dom:
                ans = max(ans, 1 + best(dom | m))
        return ans

    @lru_cache(None)
    def count(dom):
        rem = best(dom)
        if rem == 0:
            return 1
        ans = 0
        for m in neigh:
            if m & ~dom:
                nd = dom | m
                if 1 + best(nd) == rem:
                    ans += count(nd)
        return ans

    @lru_cache(None)
    def maxsets(dom):
        rem = best(dom)
        if rem == 0:
            return frozenset([0])
        out = set()
        for z,m in enumerate(neigh):
            if m & ~dom:
                nd = dom | m
                if 1 + best(nd) == rem:
                    for s in maxsets(nd):
                        out.add(s | (1 << z))
        return frozenset(out)

    L = {0} | {3 + 2*i for i in range(n)}
    R = {1} | {2 + 2*i for i in range(n)}
    expected_sets = set()
    for ell in L:
        for r in R:
            expected_sets.add(full ^ (1 << ell) ^ (1 << r))

    got_sets = maxsets(0)
    assert best(0) == 2*n
    assert count(0) == 4*factorial(2*n)
    assert got_sets == frozenset(expected_sets)
    return len(got_sets), count(0), best.cache_info().currsize


def main():
    total_sets = total_states = 0
    last_count = None
    for n in range(1,8):
        set_count, seq_count, states = direct_check(n)
        assert set_count == (n+1)**2
        total_sets += set_count
        total_states += states
        last_count = seq_count
    print(f"VERIFY_OK n_range=1..7 maximum_sets={total_sets} dp_states={total_states} n7_sequences={last_count}")

if __name__ == '__main__':
    main()
