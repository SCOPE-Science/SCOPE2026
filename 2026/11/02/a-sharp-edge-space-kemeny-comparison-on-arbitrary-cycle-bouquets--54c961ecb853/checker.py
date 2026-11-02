"""Exact finite-dimensional checks for the directed-edge Kemeny identities.

Run: python3 checker.py
Requires only the Python 3 standard library. Finite checks are not an
alternative to the all-parameter arguments in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def directed_edges(lengths):
    adj = {0: set()}
    next_vertex = 1
    for length in lengths:
        assert length >= 3
        ring = [0] + list(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        for a, b in zip(ring, ring[1:] + ring[:1]):
            adj.setdefault(a, set()).add(b)
            adj.setdefault(b, set()).add(a)
    arcs = [(a, b) for a in sorted(adj) for b in sorted(adj[a])]
    return adj, arcs


def transition(lengths, nonbacktracking):
    adj, arcs = directed_edges(lengths)
    index = {arc: i for i, arc in enumerate(arcs)}
    n = len(arcs)
    p = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, (u, v) in enumerate(arcs):
        options = adj[v] - {u} if nonbacktracking else adj[v]
        assert options
        for w in options:
            p[i][index[(v, w)]] = F(1, len(options))
        assert sum(p[i]) == 1
    assert all(sum(p[i][j] for i in range(n)) == 1 for j in range(n))
    return p


def trace_inverse(a):
    """Compute trace(A^-1) by exact rational row reduction."""
    n = len(a)
    aug = [list(row) + [F(int(i == j)) for j in range(n)]
           for i, row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k] != 0)
        aug[k], aug[pivot] = aug[pivot], aug[k]
        factor = aug[k][k]
        aug[k] = [v / factor for v in aug[k]]
        for i in range(n):
            if i == k or aug[i][k] == 0:
                continue
            factor = aug[i][k]
            aug[i] = [a - factor*b for a, b in zip(aug[i], aug[k])]
    return sum(aug[i][n+i] for i in range(n))


def kemeny_from_transitions(p):
    n = len(p)
    z = [[F(int(i == j)) - p[i][j] + F(1, n)
          for j in range(n)] for i in range(n)]
    return trace_inverse(z) - 1


def closed_forms(lengths):
    m = len(lengths)
    M = sum(lengths)
    S2 = sum(x*x for x in lengths)
    S3 = sum(x*x*x for x in lengths)
    k_nb = (F((2*m-1)**2*M, 2*m*(m-1)) - F(1, 2)
            - F((m-1)*S2, 2*m*M))
    k_e = F(M + m - 1) + F(S2-m, 3) - F(S3-M, 6*M)
    return k_nb, k_e


def predicted_sign(lengths):
    if len(lengths) == 2 and tuple(sorted(lengths)) in ((3, 3), (3, 4)):
        return -1
    if len(lengths) == 2 and tuple(sorted(lengths)) == (4, 4):
        return 0
    return 1


def main():
    cases = [(3,3), (3,4), (3,5), (4,4),
             (3,3,3), (3,3,4), (3,4,5), (3,3,6)]
    checks = 0
    for lengths in cases:
        kn, ke = closed_forms(lengths)
        assert kemeny_from_transitions(transition(lengths, True)) == kn
        assert kemeny_from_transitions(transition(lengths, False)) == ke
        checks += 2
        gap = ke - kn
        assert (gap > 0) - (gap < 0) == predicted_sign(lengths)
        checks += 1
        print(f'{lengths}: NB={kn}, edge={ke}, edge-minus-NB={gap}')
    # Exact checks of the all-size sign classification on a larger integer grid.
    for m in range(2, 5):
        for lengths in product(range(3, 8), repeat=m):
            kn, ke = closed_forms(lengths)
            gap = ke-kn
            assert (gap > 0) - (gap < 0) == predicted_sign(lengths)
            checks += 1
    print(f'CHECKS_OK {checks} exact comparisons')


if __name__ == '__main__':
    main()
