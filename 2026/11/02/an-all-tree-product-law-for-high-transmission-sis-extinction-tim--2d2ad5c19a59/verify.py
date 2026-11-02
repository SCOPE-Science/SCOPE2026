"""Exact finite checks for a high-transmission SIS extinction-time theorem.

Only Python's standard library is required. These finite checks accompany,
but do not replace, the general analytic proof.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import prod


def cut(n, arcs, mask):
    return sum((w for (u, v), w in arcs.items()
                if mask & (1 << u) and not (mask & (1 << v))), F(0))


def coefficient(n, arcs):
    """C(G) via the inverse-cut recurrence (without recovery-rate factors)."""
    H = [F(0)] * (1 << n)
    H[0] = F(1)
    for mask in range(1, (1 << n) - 1):
        boundary = cut(n, arcs, mask)
        assert boundary > 0
        H[mask] = sum((H[mask ^ (1 << v)] for v in range(n)
                       if mask & (1 << v)), F(0)) / boundary
    full = (1 << n) - 1
    return sum((H[full ^ (1 << v)] for v in range(n)), F(0))


def permutation_coefficient(n, arcs):
    total = F(0)
    for order in permutations(range(n)):
        mask = 0
        term = F(1)
        for v in order[:-1]:
            mask |= 1 << v
            term /= cut(n, arcs, mask)
        total += term
    return total


def bidirected(n, edges):
    arcs = {}
    for u, v, w1, w2 in edges:
        assert u != v and w1 > 0 and w2 > 0
        arcs[u, v] = F(w1)
        arcs[v, u] = F(w2)
    return arcs


def tree_coefficient(edges):
    return prod((F(1, 1) / F(w1) + F(1, 1) / F(w2)
                 for _, _, w1, w2 in edges), start=F(1))


def is_connected(n, edges):
    seen = {0}
    for _ in range(n):
        for u, v in edges:
            if u in seen or v in seen:
                seen.update((u, v))
    return len(seen) == n


def prufer_tree(seq):
    n = len(seq) + 2
    deg = [1] * n
    for x in seq:
        deg[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i, d in enumerate(deg) if d == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    u, v = [i for i, d in enumerate(deg) if d == 1]
    edges.append((u, v))
    return edges


def mean_extinction_exact(n, arcs, recovery, intensity):
    """Solve the finite CTMC hitting-time equations by rational elimination."""
    size = (1 << n) - 1
    a = [[F(0) for _ in range(size + 1)] for _ in range(size)]
    for S in range(1, 1 << n):
        i = S - 1
        exit_rate = F(0)
        for v in range(n):
            if S & (1 << v):
                q = recovery[v]
                exit_rate += q
                T = S ^ (1 << v)
                if T:
                    a[i][T - 1] -= q
            else:
                q = intensity * sum((arcs.get((u, v), F(0))
                                     for u in range(n) if S & (1 << u)), F(0))
                exit_rate += q
                if q:
                    a[i][(S | (1 << v)) - 1] -= q
        a[i][i] += exit_rate
        a[i][-1] = F(1)
    for j in range(size):
        pivot = next(k for k in range(j, size) if a[k][j])
        a[j], a[pivot] = a[pivot], a[j]
        piv = a[j][j]
        for k in range(j + 1, size):
            if a[k][j]:
                mult = a[k][j] / piv
                for t in range(j, size + 1):
                    a[k][t] -= mult * a[j][t]
    x = [F(0)] * size
    for j in range(size - 1, -1, -1):
        x[j] = (a[j][-1] - sum((a[j][k] * x[k]
                             for k in range(j + 1, size)), F(0))) / a[j][j]
    return x[-1]


def run():
    checks = 0
    # Exhaustive all labelled simple connected graphs through four nodes:
    # coefficient recurrence equals the independent permutation formula.
    for n in range(2, 5):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        for choices in product((0, 1), repeat=len(pairs)):
            ed = [pairs[j] for j, flag in enumerate(choices) if flag]
            if not is_connected(n, ed):
                continue
            weighted = [(u, v, 1 + (u + 2 * v) % 4, 1 + (2 * u + v) % 5)
                        for u, v in ed]
            arcs = bidirected(n, weighted)
            assert coefficient(n, arcs) == permutation_coefficient(n, arcs)
            checks += 1
            # Adding any missing bidirected positive contact lowers C strictly.
            if n == 4:
                c = coefficient(n, arcs)
                for u, v in pairs:
                    if (u, v) not in ed:
                        arcs2 = dict(arcs)
                        arcs2[u, v] = F(2)
                        arcs2[v, u] = F(3)
                        assert coefficient(n, arcs2) < c
                        checks += 1
    # Every labelled tree on 2..6 nodes, with asymmetric arc weights.
    tree_checks = 0
    for n in range(2, 7):
        for seq in product(range(n), repeat=n - 2):
            edge_pairs = prufer_tree(seq)
            edges = [(u, v, 1 + (u + 3 * v) % 7,
                      1 + (3 * u + v) % 7) for u, v in edge_pairs]
            assert coefficient(n, bidirected(n, edges)) == tree_coefficient(edges)
            tree_checks += 1
    checks += tree_checks
    # Independent exact CTMC solutions for the first nonisomorphic trees.
    n = 4
    path = bidirected(n, [(0, 1, 1, 1), (1, 2, 1, 1), (2, 3, 1, 1)])
    star = bidirected(n, [(0, 1, 1, 1), (0, 2, 1, 1), (0, 3, 1, 1)])
    triangle = bidirected(3, [(0, 1, 1, 1), (1, 2, 1, 1), (0, 2, 1, 1)])
    for arc, size, pref in [(path, 4, F(1, 8)),
                            (star, 4, F(1, 8)),
                            (triangle, 3, F(2, 3))]:
        for intensity in (F(100), F(1000)):
            m = mean_extinction_exact(size, arc, [F(1)] * size, intensity)
            relative = abs(m / intensity ** (size - 1) / pref - 1)
            assert relative < F(1, 8)
            checks += 1
    # Heterogeneous recovery rates and directional transfer on a tree.
    edges = [(0, 1, 2, 3), (1, 2, 4, 5)]
    mu = [F(2), F(3), F(5)]
    c = coefficient(3, bidirected(3, edges))
    assert c == (F(1, 2) + F(1, 3)) * (F(1, 4) + F(1, 5))
    factor = 1 / (prod(mu) * c)
    for intensity in (F(500), F(2000)):
        m = mean_extinction_exact(3, bidirected(3, edges), mu, intensity)
        assert abs(m / (intensity ** 2) / factor - 1) < F(1, 12)
        checks += 1
    print('ALL_CHECKS_PASSED')
    print('tree_product_checks:', tree_checks)
    print('total_exact_checks:', checks)
    print('path_P3_C:', coefficient(3, bidirected(3, [(0, 1, 1, 1), (1, 2, 1, 1)])))
    print('triangle_K3_C:', coefficient(3, triangle))
    print('tree_directed_heterogeneous_factor:', factor)
    print('Interpretation: finite rational tests corroborate; the proof is analytic.')


if __name__ == '__main__':
    run()
