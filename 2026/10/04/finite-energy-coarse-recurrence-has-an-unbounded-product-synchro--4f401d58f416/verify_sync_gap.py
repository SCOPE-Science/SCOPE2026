#!/usr/bin/env python3
"""Finite sanity checker for the synchronization-gap examples.

This verifies representative finite cases only. The all-parameter theorem is proved
symbolically in RESULT.md.
"""
import heapq, itertools, math

def system(L, D):
    states = ['s'] + [f'q{i}' for i in range(L)] + ['z']
    f = {'s': 'q0', 'z': 'z'}
    for i in range(L - 1):
        f[f'q{i}'] = f'q{i+1}'
    f[f'q{L-1}'] = 'z'
    def d(a, b):
        if a == b:
            return 0.0
        if {a, b} == {'s', f'q{L-1}'}:
            return 1.0
        return float(D)
    return states, f, d

def least_p_energy_single(L, p, D):
    states, f, d = system(L, D)
    start = 's'
    dist = {(start, False): 0.0}
    pq = [(0.0, start, False)]
    while pq:
        cost, u, moved = heapq.heappop(pq)
        if cost != dist[(u, moved)]:
            continue
        if u == start and moved:
            return cost
        for v in states:
            w = d(f[u], v) ** p
            key = (v, True)
            nc = cost + w
            if nc < dist.get(key, float('inf')):
                dist[key] = nc
                heapq.heappush(pq, (nc, v, True))

def least_p_energy_product(L, M, p, D):
    X, f, dx = system(L, D)
    Y, g, dy = system(M, D)
    states = list(itertools.product(X, Y))
    start = ('s', 's')
    dist = {(start, False): 0.0}
    pq = [(0.0, start, False)]
    while pq:
        cost, u, moved = heapq.heappop(pq)
        if cost != dist[(u, moved)]:
            continue
        if u == start and moved:
            return cost
        fu = (f[u[0]], g[u[1]])
        for v in states:
            e = max(dx(fu[0], v[0]), dy(fu[1], v[1]))
            w = e ** p
            key = (v, True)
            nc = cost + w
            if nc < dist.get(key, float('inf')):
                dist[key] = nc
                heapq.heappush(pq, (nc, v, True))

def main():
    D = 100
    for L in range(2, 7):
        for M in range(2, 7):
            g = math.gcd(L, M)
            expected = M // g + L // g - 1
            for p in (1, 2, 3):
                a = least_p_energy_single(L, p, D)
                b = least_p_energy_single(M, p, D)
                prod = least_p_energy_product(L, M, p, D)
                assert a == 1.0 and b == 1.0
                assert prod == float(expected), (L, M, p, prod, expected)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
