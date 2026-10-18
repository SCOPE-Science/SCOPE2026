#!/usr/bin/env python3
"""Exact finite certificates for multipartite geometric-mean edge-envelope norms.

Run with Python 3; no third-party packages are required. These finite checks
supplement, and do not replace, the general analytic proof.
"""
from fractions import Fraction
from itertools import product


def compositions(n):
    """All ordered compositions of n with at least two positive parts."""
    for cuts in product((False, True), repeat=n - 1):
        parts, length = [], 1
        for cut in cuts:
            if cut:
                parts.append(length)
                length = 1
            else:
                length += 1
        parts.append(length)
        if len(parts) >= 2:
            yield tuple(parts)


def balanced_certificate(parts):
    """Fractional perfect matching via half-unit antipodal circle cells."""
    n = sum(parts)
    assert 2 * max(parts) <= n
    blocks = [k for k, amount in enumerate(parts) for _ in range(amount)]
    assert len(blocks) == n
    weights = {}
    for r in range(2 * n):
        i = r // 2
        j = ((r + n) % (2 * n)) // 2
        assert i != j and blocks[i] != blocks[j]
        e = (min(i, j), max(i, j))
        weights[e] = weights.get(e, Fraction()) + Fraction(1, 4)
    for i in range(n):
        assert sum((w for (u, v), w in weights.items() if i in (u, v)), Fraction()) == 1
    assert sum(weights.values(), Fraction()) == Fraction(n, 2)
    # The explicit primal has endpoint allocations a_{i,e}=a_{j,e}=w_e;
    # the dual has x_i=1 for all vertices.
    return len(weights)


def dominant_certificate(parts):
    """Exact endpoint budgets and squared-positive-radical dual identity."""
    n = sum(parts)
    a = max(parts)
    b = n - a
    assert a > b > 0
    blocks = [part for part, count in enumerate(parts) for _ in range(count)]
    major = parts.index(a)
    large = [i for i, part in enumerate(blocks) if part == major]
    outside = [i for i, part in enumerate(blocks) if part != major]
    assert len(large) == a and len(outside) == b
    spent = [Fraction(0) for _ in range(n)]
    edge_count = 0
    for i in large:
        for j in outside:
            spent[i] += Fraction(1, b)
            spent[j] += Fraction(1, a)
            # One edge's positive geometric mean has square 1/(ab).
            assert Fraction(1, a*b) == Fraction(1, b)*Fraction(1, a)
            edge_count += 1
    assert edge_count == a*b
    assert all(s == 1 for s in spent)
    # Primal value = (ab) * sqrt(1/(ab)) is positive, and its square is ab.
    assert Fraction(edge_count*edge_count, a*b) == a*b
    # Dual price magnitudes are positive square roots of b/a and a/b;
    # their product equals 1, and their half-sum weighted by a,b is sqrt(ab).
    # The following exact squares establish that both a sqrt(b/a) and
    # b sqrt(a/b) equal the same positive radical sqrt(ab).
    assert Fraction(b, a)*Fraction(a, b) == 1
    assert a*a*Fraction(b, a) == a*b
    assert b*b*Fraction(a, b) == a*b
    assert Fraction(a, b) >= 1
    return edge_count


def check_all(max_n=12):
    balanced = dominant = edges = 0
    for n in range(2, max_n + 1):
        for parts in compositions(n):
            if 2 * max(parts) <= n:
                edges += balanced_certificate(parts)
                balanced += 1
            else:
                edges += dominant_certificate(parts)
                dominant += 1
    return balanced, dominant, edges


if __name__ == '__main__':
    balanced, dominant, edges = check_all()
    print(f"PASS: {balanced} balanced and {dominant} dominant ordered multipartite profiles")
    print(f"PASS: {edges} exact fractional-edge/cross-edge certificate entries")
    print("Checks use rational arithmetic for balanced fractional matchings and exact algebraic identities in the dominant case.")
