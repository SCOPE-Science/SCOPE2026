"""Finite-field checks for low-degree cubic Mayer homology of bidirected graphs.

The computation uses the non-regular q-boundary on *all* vertex words,
then enforces allowed-path constraints; it is not a proof of the general theorem.
"""
from collections import defaultdict, deque
from itertools import combinations


def rank(columns, p):
    pivots = {}
    for col in columns:
        vector = {k: a % p for k, a in col.items() if a % p}
        while vector:
            lead = min(vector)
            if lead not in pivots:
                unit = pow(vector[lead], -1, p)
                pivots[lead] = {k: (a * unit) % p for k, a in vector.items()}
                break
            factor = vector[lead]
            for k, a in pivots[lead].items():
                new = (vector.get(k, 0) - factor * a) % p
                if new:
                    vector[k] = new
                else:
                    vector.pop(k, None)
    return len(pivots)


def cycle(n):
    return [tuple(sorted((i, (i + 1) % n))) for i in range(n)]


def path(n):
    return [(i, i + 1) for i in range(n - 1)]


def star(n):
    return [(0, i) for i in range(1, n)]


def petersen():
    vertices = list(combinations(range(5), 2))
    return [(i, j) for i, a in enumerate(vertices)
            for j, b in enumerate(vertices) if i < j and not set(a) & set(b)]


def even_walk_components(adj):
    colors = {}
    bipartite = True
    for root in range(len(adj)):
        if root in colors:
            continue
        colors[root] = 0
        q = deque([root])
        while q:
            v = q.popleft()
            for u in adj[v]:
                if u not in colors:
                    colors[u] = 1 - colors[v]
                    q.append(u)
                elif colors[u] == colors[v]:
                    bipartite = False
    return 2 if bipartite else 1


def check_graph(label, n, edges, p, xi):
    assert xi % p != 1 and pow(xi, 3, p) == 1
    assert n >= 2 and all(0 <= u < v < n for u, v in edges)
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    assert all(adj)
    for u in range(n):
        for v in adj[u]:
            for w in adj[v]:
                if w != u:
                    assert w not in adj[u], 'triangle detected'
        for v in range(u + 1, n):
            assert len(adj[u] & adj[v]) <= 1, 'four-cycle detected'
    c = even_walk_components(adj)
    allowed = {0: [(i,) for i in range(n)]}
    for dim in range(1, 4):
        allowed[dim] = [a + (v,) for a in allowed[dim - 1]
                        for v in sorted(adj[a[-1]])]
    allowed_sets = {dim: set(rows) for dim, rows in allowed.items()}

    def boundary(word):
        if len(word) == 1:
            return {}
        z = defaultdict(int)
        for j in range(len(word)):
            term = word[:j] + word[j + 1:]
            z[term] = (z[term] + pow(xi, j, p)) % p
        return {key: val for key, val in z.items() if val}

    def boundary_of_combo(combo):
        z = defaultdict(int)
        for word, coeff in combo.items():
            for target, term_coeff in boundary(word).items():
                z[target] = (z[target] + coeff * term_coeff) % p
        return {key: val for key, val in z.items() if val}

    def squared(word):
        return boundary_of_combo(boundary(word))

    def constraints(word, dim):
        z = {}
        for target, coeff in boundary(word).items():
            if target not in allowed_sets[dim - 1]:
                z[(1, target)] = coeff
        if dim >= 2:
            for target, coeff in squared(word).items():
                if target not in allowed_sets[dim - 2]:
                    z[(2, target)] = coeff
        return z

    omega2_dim = len(allowed[2]) - rank(
        [constraints(word, 2) for word in allowed[2]], p)
    omega3_dim = len(allowed[3]) - rank(
        [constraints(word, 3) for word in allowed[3]], p)

    # Independently proposed explicit basis in degree two.
    b2 = []
    for center in range(n):
        near = sorted(adj[center])
        for neighbor in near[1:]:
            b2.append({(center, neighbor, center): 1,
                       (center, near[0], center): -1})
    assert all(not any(target not in allowed_sets[1]
                       for target in boundary_of_combo(comb)) for comb in b2)

    d1_rank = rank([boundary(word) for word in allowed[1]], p)
    d2_rank = rank([boundary_of_combo(combo) for combo in b2], p)
    d2square_rank = rank([
        boundary_of_combo(boundary_of_combo(combo)) for combo in b2], p)

    m = len(edges)
    assert omega2_dim == 2 * m - n, (label, omega2_dim, 2 * m - n)
    assert omega3_dim == 0, (label, omega3_dim)
    assert d1_rank == n, (label, d1_rank)
    assert d2_rank == 2 * m - n, (label, d2_rank)
    assert d2square_rank == n - c, (label, d2square_rank, n - c)

    # The second q=2 homology rank is ker(d^2|Omega_2), not dim(Omega_2).
    betti_q1 = (n - d2square_rank, 2 * m - d1_rank, 0, 0)
    betti_q2 = (n - d1_rank, 2 * m - d2_rank,
                omega2_dim - d2square_rank, 0)
    assert betti_q1 == (c, 2 * m - n, 0, 0)
    assert betti_q2 == (0, n, 2 * m - 2 * n + c, 0)
    print(f'{label:12s} F_{p}: n={n:2d}, m={m:2d}, c={c}; '
          f'omega2={omega2_dim:2d}, omega3=0; '
          f'q1={betti_q1} q2={betti_q2}')


if __name__ == '__main__':
    graphs = [(f'P{n}', n, path(n)) for n in range(2, 7)]
    graphs += [(f'S{n}', n, star(n)) for n in range(4, 7)]
    graphs += [(f'C{n}', n, cycle(n)) for n in range(5, 9)]
    graphs += [('Petersen', 10, petersen())]
    for p, xi in [(7, 2), (13, 3)]:
        for label, n, edges in graphs:
            check_graph(label, n, edges, p, xi)
    print('PASS: all 26 complete low-degree finite-field checks')
