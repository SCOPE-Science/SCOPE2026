"""Enumerate crown dominating-set TAR reconfiguration components for n=3..8.
Standalone Python 3; no third-party modules.
"""
from math import comb


def dominating(mask, n):
    full = (1 << n) - 1
    a = mask & full
    b = (mask >> n) & full
    for i in range(n):
        bit = 1 << i
        if not (a & bit) and not (b & (full ^ bit)):
            return False
        if not (b & bit) and not (a & (full ^ bit)):
            return False
    return True


def expected(n, k):
    if k == 2:
        return n
    if k == 3:
        return n + (2 if n == 3 else 0)
    if k == 4:
        if n == 3:
            return 1
        return 1 + comb(n,2)*comb(n-2,2) + (2 if n == 4 else 0)
    if k == n:
        return 3
    return 1


def run():
    total_sets = 0
    total_edges = 0
    checks = 0
    by_n = {}
    for n in range(3,9):
        all_masks = [mask for mask in range(1 << (2*n)) if dominating(mask,n)]
        by_n[n] = {}
        for k in range(2,n+2):
            feasible = {s for s in all_masks if s.bit_count() <= k}
            unseen = set(feasible)
            component_sizes = []
            edges = 0
            while unseen:
                seed = unseen.pop()
                queue = [seed]
                for s in queue:
                    for v in range(2*n):
                        t = s ^ (1 << v)
                        if t in feasible:
                            edges += 1
                            if t in unseen:
                                unseen.remove(t)
                                queue.append(t)
                component_sizes.append(len(queue))
            component_sizes.sort(reverse=True)
            assert len(component_sizes) == expected(n,k), (n,k,len(component_sizes),expected(n,k))
            if n >= 4 and k == 4:
                isolated = comb(n,2)*comb(n-2,2)+(2 if n==4 else 0)
                assert len(component_sizes)==isolated+1
                assert component_sizes.count(1)==isolated, (n,component_sizes)
            if 5 <= k == n:
                assert component_sizes.count(1)==2, (n,k,component_sizes)
            if k == 3:
                assert component_sizes.count(2*n-1)==n, (n,k,component_sizes)
                if n==3: assert component_sizes.count(1)==2
            checks += 1
            total_sets += len(feasible)
            total_edges += edges//2
            by_n[n][k] = len(component_sizes)
    print('VERIFY_OK orders=3..8 cases=%d set_visits=%d edge_visits=%d component_counts=%r' %
          (checks, total_sets, total_edges, by_n))

if __name__ == '__main__':
    run()
