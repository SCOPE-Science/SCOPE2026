#!/usr/bin/env python3
"""Independent finite checks for isolated gaps in Fibonacci-shifted numerical semigroups."""
import heapq
import math


def fibonacci(n):
    f = [0, 1]
    for _ in range(2, n + 1):
        f.append(f[-1] + f[-2])
    return f


def zeckendorf_indices(x, f):
    chosen = []
    for i in range(len(f) - 1, 1, -1):
        if f[i] <= x:
            chosen.append(i)
            x -= f[i]
    assert x == 0
    return tuple(reversed(chosen))


def formula_gaps(a, f):
    m = f[a]
    indices = range(6, a)
    states = [()]
    for i in indices:
        states += [q + (i,) for q in tuple(states) if not q or i - q[-1] >= 2]
    return { (1 + len(q))*m + f[2] + f[4] + sum(f[i] for i in q)
             for q in states }


def apéry(m, gs):
    d = [None]*m
    d[0] = 0
    queue = [(0, 0)]
    while queue:
        v,r = heapq.heappop(queue)
        if d[r] != v:
            continue
        for g in gs:
            rr = (r + g)%m
            nv = v + g
            if d[rr] is None or nv < d[rr]:
                d[rr] = nv
                heapq.heappush(queue, (nv,rr))
    return d


def main():
    f = fibonacci(24)
    checked = 0
    all_gap_checks = 0
    for a in range(3, 23):
        m = f[a]
        gs = [m] + [m + f[i] for i in range(2, a)]
        W = apéry(m, gs)
        assert all(v is not None for v in W)
        beta = [len(zeckendorf_indices(r, f)) for r in range(m)]
        assert W == [beta[r]*m+r for r in range(m)]
        bound = max(W) - m
        # Independent, elementary dynamic-programming membership test.
        inside = [False]*(bound + 2)
        inside[0] = True
        for n in range(1, bound+2):
            inside[n] = any(n >= g and inside[n-g] for g in gs)
        assert all(inside[n] == (n >= W[n % m]) for n in range(bound+2))
        actual = {n for n in range(1, bound+1)
                  if not inside[n] and inside[n-1] and inside[n+1]}
        expected = formula_gaps(a, f) if a >= 5 else ({1} if a == 3 else set())
        assert actual == expected, (a, actual ^ expected)
        assert len(actual) == (f[a-4] if a >= 5 else (1 if a == 3 else 0))
        if a >= 5:
            for q in range(1, (a-5)//2 + 2):
                count = sum(g//m == q for g in actual)
                expected_count = math.comb(a-5-(q-1), q-1) if a-5-(q-1) >= q-1 else 0
                assert count == expected_count, (a,q,count,expected_count)
        checked += 1
        all_gap_checks += bound+2
        print(f'a={a}, multiplicity={m}, conductor={bound+1}, isolated={len(actual)}')
    print(f'VERIFIED: {checked} complete parameter cases, {all_gap_checks} independent membership decisions')


if __name__ == '__main__':
    main()
