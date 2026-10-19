"""Finite-field checks for conjugacy classes of unicyclic height-one incidence-algebra unit groups.

Requires only the Python 3 standard library.  Run: python verify.py
"""
from collections import Counter
from itertools import product

C4 = ((0, 1), (2, 1), (2, 3), (0, 3))
G6A = C4 + ((0, 4), (0, 5))
G6B = C4 + ((0, 4), (2, 5))
C6 = ((0, 1), (2, 1), (2, 3), (4, 3), (4, 5), (0, 5))

class Field:
    def __init__(self, q):
        self.q = q
        if q == 4:
            self.mul = lambda a, b: self._m4(a, b)
            self.inv = {1: 1, 2: 3, 3: 2}.__getitem__
            self.add = lambda a, b: a ^ b
        else:
            self.mul = lambda a, b: (a * b) % q
            self.inv = lambda a: pow(a, -1, q)
            self.add = lambda a, b: (a + b) % q
    @staticmethod
    def _m4(a, b):
        v = 0
        if b & 1:
            v ^= a
        if b & 2:
            v ^= a << 1
        if v & 8:
            v ^= 0b1110
        if v & 4:
            v ^= 0b111
        return v
    def quotient(self, a, b):
        return self.mul(a, self.inv(b))


def weights(E, diagonal, F):
    return tuple(F.quotient(diagonal[lower], diagonal[upper]) for lower, upper in E)


def masks(q, E):
    n = 1 + max(max(edge) for edge in E)
    F = Field(q)
    masks = Counter()
    for diagonal in product(range(1, q), repeat=n):
        w = weights(E, diagonal, F)
        mask = sum(1 << i for i, scalar in enumerate(w) if scalar == 1)
        masks[mask] += 1
    return masks


def class_number_by_commutations(q, E):
    n = 1 + max(max(edge) for edge in E)
    counts = masks(q, E)
    # For each pair of diagonal unit-tuples, solve the independent linear
    # commutation conditions on two off-diagonal vectors. Their solution
    # count is q^(|E| + number of simultaneously trivial edge weights).
    total = sum(a * b * q ** ((s & t).bit_count())
                for s, a in counts.items() for t, b in counts.items())
    assert total % (q - 1) ** n == 0
    return total // ((q - 1) ** n)


def cycle_formula(q, m, c):
    return q ** (m - c) * (q ** c + q ** 2 - 2 * q)


def isomorphism_on_diagonals(source, target, diagonal, F):
    # Source/target have identical named cycle edges, and edge positions
    # correspond in the two graphs. Keep root 0 and all edge ratios.
    wanted = weights(source, diagonal, F)
    n = 1 + max(max(edge) for edge in target)
    ans = [None] * n
    ans[0] = diagonal[0]
    # Omit edge 3, which closes the unique cycle.
    while None in ans:
        progressed = False
        for i, (lower, upper) in enumerate(target):
            if i == 3:
                continue
            w = wanted[i]
            if ans[lower] is not None and ans[upper] is None:
                ans[upper] = F.quotient(ans[lower], w)
                progressed = True
            if ans[lower] is None and ans[upper] is not None:
                ans[lower] = F.mul(w, ans[upper])
                progressed = True
        assert progressed
    assert weights(target, ans, F) == wanted
    return tuple(ans)


def check_explicit_isomorphism(q):
    F = Field(q)
    torus = list(product(range(1, q), repeat=6))
    mapping = {d: isomorphism_on_diagonals(G6A, G6B, d, F) for d in torus}
    assert len(set(mapping.values())) == len(torus)
    # Test multiplicativity of the explicit vertex-torus map, not just
    # equality of commuting probabilities.
    pairs = product(torus, torus) if q <= 3 else ((torus[i], torus[(37*i+1) % len(torus)]) for i in range(400))
    for a, b in pairs:
        c = tuple(F.mul(x, y) for x, y in zip(a, b))
        assert mapping[c] == tuple(F.mul(x, y) for x, y in zip(mapping[a], mapping[b]))
    # Since each edge weight is preserved, the same radical coordinates
    # produce a homomorphism of the full semidirect-product groups.
    for a in torus:
        assert weights(G6A, a, F) == weights(G6B, mapping[a], F)


def main():
    for q in (2, 3, 4, 5):
        for graph, c in ((C4, 4), (G6A, 4), (G6B, 4), (C6, 6)):
            observed = class_number_by_commutations(q, graph)
            expected = cycle_formula(q, len(graph), c)
            assert observed == expected, (q, graph, observed, expected)
            print('q={} vertices={} edges={} cycle={} classes={}'.format(
                q, 1 + max(max(e) for e in graph), len(graph), c, observed))
    for q in (2, 3, 4, 5):
        check_explicit_isomorphism(q)
    # The explicit six-vertex graphs have distinct degree multisets.
    def degree_sequence(edges):
        n = 1 + max(max(edge) for edge in edges)
        return sorted((sum(v in edge for edge in edges) for v in range(n)), reverse=True)
    assert degree_sequence(G6A) == [4, 2, 2, 2, 1, 1]
    assert degree_sequence(G6B) == [3, 3, 2, 2, 1, 1]
    assert cycle_formula(3, 6, 4) == 756
    assert cycle_formula(3, 6, 6) == 732
    assert cycle_formula(2, 6, 4) == cycle_formula(2, 6, 6) == 64
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
