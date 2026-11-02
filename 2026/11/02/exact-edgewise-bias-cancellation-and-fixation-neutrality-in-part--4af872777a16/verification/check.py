"""Exact checks of the two-opinion, fixed-preference copying chain.

Run with Python 3.10+ and SymPy.  All matrix computations are exact rationals.
"""
from fractions import Fraction as Q
from sympy import Matrix, Rational

CASES = [
    ('edge', 2, [(0, 1, 1)]),
    ('path3', 3, [(0, 1, 1), (1, 2, 1)]),
    ('path4', 4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)]),
    ('star5', 5, [(0, j, 1) for j in range(1, 5)]),
    ('cycle4', 4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]),
    ('complete23', 5, [(u, v, 1) for u in range(2) for v in range(2, 5)]),
    ('cycle6', 6, [(j, (j + 1) % 6, 1) for j in range(6)]),
    ('weighted_path3', 3, [(0, 1, Q(2, 3)), (1, 2, Q(5, 4))]),
    ('weighted_cycle4', 4, [(0, 1, Q(2, 3)), (1, 2, 3), (2, 3, Q(3, 5)), (3, 0, 2)]),
    ('weighted_complete23', 5, [(u, v, Q((u+2)*(v+1), 7)) for u in range(2) for v in range(2, 5)]),
]

def partition_and_neighbors(n, edges):
    adj = [dict() for _ in range(n)]
    for u, v, w in edges:
        assert 0 <= u < n and 0 <= v < n and u != v and w > 0
        assert v not in adj[u]
        adj[u][v] = Q(w)
        adj[v][u] = Q(w)
    sides = [None] * n
    sides[0] = +1
    todo = [0]
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if sides[v] is None:
                sides[v] = -sides[u]
                todo.append(v)
            else:
                assert sides[v] == -sides[u]
    assert all(s is not None for s in sides)
    return sides, adj

def chain_step(n, adj, biases, state):
    p = {state: Q(1)}
    for u in range(n):
        d_u = sum(adj[u].values())
        for v, w in adj[u].items():
            if ((state >> u) & 1) == ((state >> v) & 1):
                continue
            spin_v = 1 if (state >> v) & 1 else -1
            prob = Q(1, n) * w / d_u * (1 + spin_v * biases[u]) / 2
            target = state ^ (1 << u)
            p[target] = p.get(target, Q(0)) + prob
            p[state] -= prob
    assert sum(p.values()) == 1 and all(v >= 0 for v in p.values())
    return p

def verify_case(name, n, edges, h):
    sides, adj = partition_and_neighbors(n, edges)
    biases = [Q(s) * h for s in sides]
    degrees = [sum(adj[u].values()) for u in range(n)]
    D = sum(degrees)
    M = lambda state: sum(degrees[u] * ((state >> u) & 1) for u in range(n)) / D
    for state in range(1 << n):
        p = chain_step(n, adj, biases, state)
        assert sum(prob * M(other) for other, prob in p.items()) == M(state), (name, state)
        cross = sum(Q(w) * (biases[u] + biases[v]) for u, v, w in edges
                    if ((state >> u) & 1) != ((state >> v) & 1))
        drift = sum(prob * M(other) for other, prob in p.items()) - M(state)
        assert drift == cross / (2 * n * D)
    states = list(range(1, (1 << n) - 1))
    if n <= 5:
        pos = {s: k for k, s in enumerate(states)}
        A = Matrix.eye(len(states))
        b = Matrix.zeros(len(states), 1)
        for state in states:
            for target, prob in chain_step(n, adj, biases, state).items():
                rr = Rational(prob.numerator, prob.denominator)
                if target == (1 << n) - 1:
                    b[pos[state]] += rr
                elif target:
                    A[pos[state], pos[target]] -= rr
        solution = A.inv() * b
        for state in states:
            expected = M(state)
            assert solution[pos[state]] == Rational(expected.numerator, expected.denominator)
    polarized = sum(1 << u for u, s in enumerate(sides) if s == 1)
    assert M(polarized) == Q(1, 2)
    assert chain_step(n, adj, biases, polarized)[polarized] == (1 + h) / 2
    return (1 << n), len(states) if n <= 5 else 0

if __name__ == '__main__':
    tested = solved = 0
    for name, n, edges in CASES:
        for h in (Q(1, 3), Q(3, 4)):
            checked, solved_here = verify_case(name, n, edges, h)
            tested += checked
            solved += solved_here
            print(f'{name}: preference={h}, configurations={checked}, exact transient solves={solved_here}')
    # A nonbipartite triangle with an unequal edge-sum preference has nonzero drift.
    adj = [{1: Q(1), 2: Q(1)}, {0: Q(1), 2: Q(1)}, {0: Q(1), 1: Q(1)}]
    bias = [Q(1, 3), Q(0), Q(0)]
    initial = 1
    M = lambda z: Q(sum((z >> u) & 1 for u in range(3)), 3)
    drift = sum(p * M(s) for s, p in chain_step(3, adj, bias, initial).items()) - M(initial)
    assert drift == Q(1, 54)
    print(f'nonbipartite contrast drift={drift}')
    print(f'PASS: {tested} rational drift checks; {solved} independently solved absorbing-chain states; exact waiting law.')
