"""Independent finite-graph percolation check for the two-hub SIR seeding theorem.
No external data or packages are needed besides sympy for polynomial comparison.
Run: python bistar_verify.py
"""
from itertools import combinations
from math import comb
import sympy as sp

p = sp.symbols('p')

def graph_edges(leaves):
    # Hubs are 0,1; each owns 'leaves' terminal vertices.
    return [(0, 1)] + [(0, 2+j) for j in range(leaves)] + [(1, 2+leaves+j) for j in range(leaves)]

def reach_components(N, edges, mask):
    adj = [[] for _ in range(N)]
    for j, (u, v) in enumerate(edges):
        if mask >> j & 1:
            adj[u].append(v); adj[v].append(u)
    labels = [-1] * N
    sizes = []
    for u in range(N):
        if labels[u] != -1:
            continue
        stack = [u]
        labels[u] = len(sizes)
        size = 0
        while stack:
            v = stack.pop(); size += 1
            for w in adj[v]:
                if labels[w] == -1:
                    labels[w] = labels[u]
                    stack.append(w)
        sizes.append(size)
    return labels, sizes

def verify(n):
    N = 2 * n + 2
    edges = graph_edges(n)
    E = len(edges)
    total_pairs = comb(N, 2)
    accumulator = [0] * (E+1)
    for mask in range(1 << E):
        labels, sizes = reach_components(N, edges, mask)
        hub_infected = sum(size for i,size in enumerate(sizes) if i in {labels[0],labels[1]})
        uniform_sum = 0
        for u, v in combinations(range(N), 2):
            uniform_sum += sizes[labels[u]]
            if labels[u] != labels[v]:
                uniform_sum += sizes[labels[v]]
        accumulator[mask.bit_count()] += hub_infected * total_pairs - uniform_sum
    exact = sum(sp.Rational(acc, total_pairs)*p**k*(1-p)**(E-k) for k, acc in enumerate(accumulator))
    formula = n*p*(p-1)*(3*n*(n-1)*p**2+(3*n-1)*p-4*n*n+2*n+2) / ((n+1)*(2*n+1))
    assert sp.expand(exact-formula) == 0, (n, sp.factor(exact-formula))
    return 1 << E, (1 << E)*total_pairs, sp.factor(exact)

if __name__ == '__main__':
    total_configs=0
    total_pairs=0
    for n in range(1,7):
        c,b,polynomial=verify(n)
        total_configs+=c;total_pairs+=b
        print(f'n={n}: {c} retained-edge graphs, {b} graph/seed-pair cases; identity verified')
        print(f'  difference E_hubs-E_uniform = {polynomial}')
    assert float((-5+sp.sqrt(265))/12) > 0.93
    assert float((-5+sp.sqrt(265))/12) < 0.95
    print(f'PASS: {total_configs} percolation configurations, {total_pairs} seeded configuration cases')
