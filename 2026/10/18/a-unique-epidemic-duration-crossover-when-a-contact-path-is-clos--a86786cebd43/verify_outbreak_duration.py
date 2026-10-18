#!/usr/bin/env python3
"""Exact independent edge-subset checks for a rooted one-generation epidemic."""
from collections import deque
import sympy as sp

p = sp.Symbol('p')


def poly_from_subsets(n, cycle):
    edges = [(i, i + 1) for i in range(n - 1)]
    if cycle:
        edges.append((0, n - 1))
    N = len(edges)
    time_counts = [0] * (N + 1)
    reach_counts = [0] * (N + 1)
    for mask in range(1 << N):
        adj = [[] for _ in range(n)]
        for idx, (u, v) in enumerate(edges):
            if mask & (1 << idx):
                adj[u].append(v)
                adj[v].append(u)
        distance = [-1] * n
        distance[0] = 0
        todo = deque([0])
        while todo:
            u = todo.popleft()
            for v in adj[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    todo.append(v)
        k = mask.bit_count()
        time_counts[k] += max(distance)
        reach_counts[k] += sum(z >= 0 for z in distance)
    time_poly = sp.expand(sum(time_counts[k] * p**k * (1-p)**(N-k) for k in range(N+1)))
    reach_poly = sp.expand(sum(reach_counts[k] * p**k * (1-p)**(N-k) for k in range(N+1)))
    return time_poly, reach_poly


def predicted_diff(n):
    return sp.expand(p * (sum(p**(2*j) for j in range((n-2)//2 + 1)) - (n-1)*p**(n-1)))


def proof_by_tails(n):
    half = n//2
    cycle_tail = sum(2*p**t-p**(2*t) for t in range(1, half+1))
    cycle_tail += sum(2*p**t-2*p**n for t in range(half+1, n))
    path_tail = sum(p**t for t in range(1, n))
    return sp.expand(cycle_tail - path_tail)


def main():
    checks = 0
    for n in range(3, 11):
        time_p, reach_p = poly_from_subsets(n, False)
        time_c, reach_c = poly_from_subsets(n, True)
        assert sp.expand(time_p - sum(p**j for j in range(1, n))) == 0
        assert sp.expand(time_c - time_p - predicted_diff(n)) == 0
        assert sp.expand(proof_by_tails(n) - predicted_diff(n)) == 0
        expected_size_diff = sum(p**j for j in range(1, n)) - (n - 1)*p**n
        assert sp.expand(reach_c-reach_p-expected_size_diff) == 0
        checks += 4
    print(f'PASS: {checks} distinct exact symbolic identities, rooted percolation exhaustive to n=10.')
    # Two exact signs at n=5 yield a concrete reversal.
    for rat, sign in [(sp.Rational(1, 2), 1), (sp.Rational(9, 10), -1)]:
        observed = sp.factor(predicted_diff(5).subs(p, rat))
        assert sign * observed > 0
        print(f'n=5, p={rat}: cycle minus path mean duration = {observed}')
    # Distinct feature: size always increases at these same parameters.
    for rat in (sp.Rational(1,2),sp.Rational(9,10)):
        value = (sum(p**j for j in range(1,5))-4*p**5).subs(p,rat)
        assert value > 0
        print(f'n=5, p={rat}: mean outbreak size difference = {value}')
    # A high precision asymptotic landmark (not evidence for the infinite theorem).
    import mpmath as mp
    mp.mp.dps = 40
    gamma = mp.findroot(lambda z: mp.exp(z)-1-2*z, (1,2))
    print('limit gamma =', mp.nstr(gamma,30))
    for n in (11,21,101,1001):
        terms=(n-2)//2+1
        f=lambda x: sum(x**(2*j) for j in range(terms)) - (n-1)*x**(n-1)
        left, right = mp.mpf('0.00001'), mp.mpf('1.0')
        for _ in range(120):
            mid=(left+right)/2
            if f(mid)>0:
                left=mid
            else:
                right=mid
        root=(left+right)/2
        print(f'n={n}, threshold={mp.nstr(root,25)}, n*(1-threshold)={mp.nstr(n*(1-root),18)}')
    print('All checks passed.')

if __name__ == '__main__':
    main()
