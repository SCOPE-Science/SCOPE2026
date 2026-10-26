#!/usr/bin/env python3
"""Independent finite checks for arithmetic-progression semigroup quotients.

A finite check is not an infinite proof; see RESULT.md for the proof.
"""
import heapq
from math import gcd


def apery_by_dijkstra(m, generators):
    dist = [None] * m
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        value, residue = heapq.heappop(heap)
        if value != dist[residue]:
            continue
        for g in generators:
            t = (residue + g) % m
            nv = value + g
            if dist[t] is None or nv < dist[t]:
                dist[t] = nv
                heapq.heappush(heap, (nv, t))
    assert all(v is not None for v in dist)
    return dist


def theorem(a, d):
    assert a >= 5 and a % 2 == d % 2 == 1 and gcd(a, d) == 1
    x, y = (a + d) // 2, (a + 3 * d) // 2
    q, r = divmod(a, 3)
    if r == 0:
        return ((q - 1) * y + 2 * x - a,)
    if r == 1:
        return tuple(sorted(((q - 1) * y + 2 * x - a, q * y - a)))
    return tuple(sorted(((q - 1) * y + 2 * x - a, q * y + x - a)))


def run():
    count = 0
    membership_tests = 0
    for a in range(5, 100, 2):
        for d in range(1, 80, 2):
            if gcd(a, d) != 1:
                continue
            x, y = (a + d) // 2, (a + 3 * d) // 2
            ds = apery_by_dijkstra(a, (a, a+d, a+2*d, a+3*d))
            dt = apery_by_dijkstra(a, (a, x, y))
            model = [(u // 3)*y + (u % 3)*x for u in range(a)]
            assert sorted(model) == sorted(dt), (a, d, 'Apéry')
            observed_pf = tuple(sorted(w - a for w in dt if all(w + z > dt[(w+z)%a] for z in (x, y))))
            assert observed_pf == theorem(a, d), (a, d, 'pseudo-Frobenius')
            # Membership checked using two independent Cayley graphs:
            # the original four generators and the predicted quotient triple.
            boundary = max(dt) + a + max(x, y)
            for n in range(boundary + 1):
                in_quotient = 2*n >= ds[(2*n)%a]
                in_triple = n >= dt[n % a]
                assert in_quotient == in_triple, (a, d, n, 'quotient')
            membership_tests += boundary + 1
            f = max(dt) - a
            assert f == max(observed_pf)
            count += 1
    print('PASS: parameter pairs', count)
    print('PASS: independent quotient membership comparisons', membership_tests)
    print('PASS: complete Apéry, Frobenius and pseudo-Frobenius comparisons', count)
    print('Scope: odd 5 <= a < 100; odd 1 <= d < 80; gcd(a,d)=1.')
    print('Infinite theorem established by the separate proof, not these tests.')

if __name__ == '__main__':
    run()
