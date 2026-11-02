#!/usr/bin/env python3
"""Independent finite lower-bound check via shortest-path assignment.

A closed walk covering every required arc can be decomposed into
source-to-sink augmentation paths. Since every supply/demand is 1,
the exact minimum augmentation is a minimum-cost bipartite matching.
Hungarian implementation below requires no dependencies.
"""

def runs_ok(value, n):
    bits = [(value >> (n - 1 - i)) & 1 for i in range(n)]
    return all(not (bits[j] == bits[j+1] == bits[j+2])
               for j in range(n-2))


def distance(u, v, width):
    for step in range(width + 1):
        overlap = width - step
        if overlap == 0 or u % (1 << overlap) == v >> step:
            return step
    raise AssertionError('all states reachable')


def assignment_min_cost(a):
    # Hungarian primal-dual algorithm for a square integer cost matrix.
    n = len(a)
    if not n:
        return 0
    u, v, p, way = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
    for i in range(1, n+1):
        p[0] = i
        j0 = 0
        minv = [10**9] * (n+1)
        used = [False] * (n+1)
        while True:
            used[j0] = True
            i0, delta, j1 = p[j0], 10**9, 0
            for j in range(1, n+1):
                if not used[j]:
                    cur = a[i0-1][j-1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j], way[j] = cur, j0
                    if minv[j] < delta:
                        delta, j1 = minv[j], j
            for j in range(n+1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    result = sum(a[p[j]-1][j-1] for j in range(1,n+1))
    assert len(set(p[1:])) == n
    return result


def fibonacci(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a


def verify():
    for n in range(3, 14):
        width = n - 1
        mask = (1 << width) - 1
        deg = [0] * (1 << width)
        count = 0
        for w in range(1 << n):
            if runs_ok(w, n):
                deg[w >> 1] += 1
                deg[w & mask] -= 1
                count += 1
        assert set(deg) <= {-1, 0, 1}
        src = [v for v, d in enumerate(deg) if d < 0]
        dst = [v for v, d in enumerate(deg) if d > 0]
        assert len(src) == len(dst)
        costs = [[distance(u,v,width) for v in dst] for u in src]
        opt_extra = assignment_min_cost(costs)
        expected_extra = 2 * fibonacci(n-1) - 2
        assert opt_extra == expected_extra, (n, opt_extra, expected_extra)
        print(f'n={n:2d} imbalance_pairs={len(src):3d} exact_shortest_extra={opt_extra:4d} total={count+opt_extra:5d}')
    print('CROSSCHECK_OK')


if __name__ == '__main__': verify()
