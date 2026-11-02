"""Exact checks for one-edge cascade inhibition under uniform fractional thresholds.
Run with Python 3, no third-party packages.
"""
from fractions import Fraction
from itertools import combinations


def terminal(n, edges, seed, phi):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    active = {seed}
    while True:
        following = active | {
            v for v in range(n) if v not in active
            and adj[v]
            and Fraction(len(adj[v] & active), len(adj[v])) >= phi
        }
        if following == active:
            return frozenset(active)
        active = following


def connected(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    while True:
        next_seen = seen | set().union(*(adj[u] for u in seen))
        if next_seen == seen:
            return len(seen) == n
        seen = next_seen


def expected_bound(n, phi):
    q = phi.denominator // phi.numerator
    if n <= q + 1:
        return 0
    if phi > Fraction(1, 2):
        return 2
    return n - 1


def witness(n, phi):
    q = phi.denominator // phi.numerator
    if phi > Fraction(1, 2):
        # Center vertex zero with every other vertex a leaf.
        E = [(0, j) for j in range(1, n)]
        extra = (1, 2)
    else:
        assert n >= q + 2
        # One seed, gateway vertex 1, q-2 additional leaves,
        # and a path starting at q and ending at n-1.
        E = [(0, 1)] + [(1, j) for j in range(2, q)]
        E += [(1, q)] + [(j, j + 1) for j in range(q, n - 1)]
        extra = (1, n - 1)
    return E, extra


def main():
    phis = [Fraction(1, 5), Fraction(1, 4), Fraction(1, 3),
            Fraction(2, 5), Fraction(1, 2), Fraction(3, 5),
            Fraction(3, 4), Fraction(9, 10)]
    tests = 0
    connected_cases = 0
    for n in range(3, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            E = [pair for i, pair in enumerate(pairs) if mask >> i & 1]
            if not connected(n, E) or len(E) == len(pairs):
                continue
            connected_cases += 1
            available = [edge for edge in pairs if edge not in E]
            for phi in phis:
                expected = expected_bound(n, phi)
                for seed in range(n):
                    old = terminal(n, E, seed, phi)
                    for e in available:
                        new = terminal(n, E + [e], seed, phi)
                        loss = len(old) - len(new)
                        assert loss <= expected, (n, phi, E, seed, e, loss)
                        tests += 1
    witness_tests = 0
    for phi in phis:
        q = phi.denominator // phi.numerator
        for n in range(max(3, q + 2), max(3, q + 2) + 8):
            E, e = witness(n, phi)
            assert e not in E
            assert connected(n, E)
            initial = terminal(n, E, 0, phi)
            final = terminal(n, E + [e], 0, phi)
            assert len(initial) == n
            assert len(final) == (n - 2 if phi > Fraction(1, 2) else 1)
            assert len(initial) - len(final) == expected_bound(n, phi)
            witness_tests += 1
    print(f"PASS {tests} exact small-graph comparisons on {connected_cases} connected noncomplete graphs")
    print(f"PASS {witness_tests} exact constructive examples")


if __name__ == '__main__':
    main()
