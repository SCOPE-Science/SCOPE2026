"""Exact finite-tree certificate for attenuation-dependent optimal nodes.

Requires Python >=3.10, networkx >=3 and sympy >=1.12.
Run: python verify_reentry.py
Graph enumeration uses networkx.nonisomorphic_trees. All polynomial root
comparisons use exact integer/rational arithmetic and Sturm isolation.
"""
import math
from collections import Counter
from fractions import Fraction
import networkx as nx
import sympy as sp

x = sp.Symbol('x')
SHAPE_COUNTS = {2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23,
                9: 47, 10: 106, 11: 235, 12: 551, 13: 1301, 14: 3159}
WITNESS_EDGES = [(0, 11), (1, 0), (1, 2), (1, 9), (1, 10),
                 (2, 3), (2, 7), (3, 4), (3, 5), (3, 6),
                 (7, 8), (11, 12), (12, 13), (13, 14)]


def distance_counts(tree):
    n = len(tree)
    rows = [[0] * n for _ in range(n)]
    for v, distances in nx.all_pairs_shortest_path_length(tree):
        for dist in distances.values():
            rows[v][dist] += 1
    assert all(sum(row) == n for row in rows)
    return rows


def quotient(d1, d2):
    """Coefficients of (C1-C2)/(x(1-x)), increasing power order."""
    diff = [a - b for a, b in zip(d1, d2)]
    assert diff[0] == 0 and sum(diff) == 0
    out = []
    running = 0
    for v in diff[1:-1]:
        running += v
        out.append(running)
    assert running == -diff[-1]
    while out and out[-1] == 0:
        out.pop()
    return out


def transformed(coeff):
    """Bernstein-to-positive-half-line transform of q, degree preserved."""
    d = len(coeff) - 1
    return [sum(coeff[j] * math.comb(d-j, k-j)
                for j in range(k+1)) for k in range(d+1)]


def variation(coeff):
    sg = [1 if a > 0 else -1 for a in coeff if a]
    return sum(sg[k] != sg[k-1] for k in range(1, len(sg)))


def candidate_vertices(rows):
    """Remove only vertices provably dominated at every parameter in (0,1)."""
    n = len(rows)
    dominated = [False] * n
    exceptions = []
    for i in range(n):
        for j in range(i):
            coeff = quotient(rows[i], rows[j])
            if not coeff:
                continue
            transformed_coeff = transformed(coeff)
            changes = variation(transformed_coeff)
            if changes == 0:
                if next(a for a in transformed_coeff if a) > 0:
                    dominated[j] = True
                else:
                    dominated[i] = True
            elif changes >= 2:
                exceptions.append((i, j, coeff))
    return [i for i in range(n) if not dominated[i]], exceptions


def critical_intervals(rows, candidates):
    """All distinct real candidate-crossing roots strictly between zero and one.

    Roots are isolated by an exact Sturm algorithm (sympy intervals), using
    rational endpoints. Shared irreducible factors are processed only once.
    """
    factors = {}
    for a_idx, i in enumerate(candidates):
        for j in candidates[:a_idx]:
            q = quotient(rows[i], rows[j])
            if not q:
                continue
            poly = sp.Poly(sum(z * x**k for k, z in enumerate(q)), x)
            for factor, _ in poly.factor_list()[1]:
                key = tuple(int(z) for z in factor.monic().clear_denoms()[1].all_coeffs())
                factors[key] = factor
    output = []
    for key, poly in factors.items():
        intervals = poly.intervals(eps=sp.Rational(1, 10**12))
        for (left, right), multiplicity in intervals:
            if left >= 1 or right <= 0:
                continue
            assert multiplicity == 1
            assert left >= 0 and right <= 1, (key, left, right)
            assert poly.count_roots(left, right) == 1 or left == right
            output.append((left, right))
    output.sort()
    for a, b in zip(output, output[1:]):
        assert a[1] < b[0], (a, b)
    return output


def exact_winners(rows, candidates, p):
    values = [(i, sum(c * p**j for j, c in enumerate(rows[i]))) for i in candidates]
    biggest = max(v for _, v in values)
    return frozenset(i for i, v in values if v == biggest)


def no_reentry_exact(rows, candidates):
    """Certified winning sets on all intervals between algebraic roots."""
    intervals = critical_intervals(rows, candidates)
    gaps = []
    previous = sp.Rational(0)
    for a, b in intervals:
        assert previous < a or (previous == 0 and a == 0)
        if previous < a:
            gaps.append((previous + a)/2)
        previous = b
    if previous < 1:
        gaps.append((previous+1)/2)
    assert gaps
    win_sets = [exact_winners(rows, candidates, p) for p in gaps]
    # Any globally optimal vertex must be an undominated candidate.
    # Every candidate score difference has no zero in any sampled open gap.
    # A strict/non-strict top interval cannot disappear and reappear.
    for v in candidates:
        bits = [v in w for w in win_sets]
        if True in bits:
            lo = bits.index(True)
            hi = len(bits)-1-bits[::-1].index(True)
            assert all(bits[lo:hi+1]), (v, bits, intervals)
    return len(intervals), len(gaps)


def check_small_trees():
    counts = Counter()
    suspect_shapes = Counter()
    suspect_pairs = Counter()
    root_cells = 0
    for n in range(2, 15):
        for tree in nx.nonisomorphic_trees(n):
            counts[n] += 1
            rows = distance_counts(tree)
            candidates, exceptions = candidate_vertices(rows)
            unresolved = [(i, j) for i, j, _ in exceptions
                          if i in candidates and j in candidates]
            if unresolved:
                suspect_shapes[n] += 1
                suspect_pairs[n] += len(unresolved)
                root_cells += no_reentry_exact(rows, candidates)[0]
            # With no unresolved pair, every surviving vertex's optimum set
            # is an intersection of sets cut by comparisons with <=1 root.
            # Thus all such optimum sets are intervals (possibly empty).
        assert counts[n] == SHAPE_COUNTS[n], (n, counts[n])
    assert dict(counts) == SHAPE_COUNTS
    assert dict(suspect_shapes) == {13:6, 14:17}, dict(suspect_shapes)
    assert dict(suspect_pairs) == {13:6, 14:18}, dict(suspect_pairs)
    return counts, suspect_shapes, suspect_pairs, root_cells


def check_witness():
    tree = nx.Graph()
    tree.add_nodes_from(range(15))
    tree.add_edges_from(WITNESS_EDGES)
    assert nx.is_tree(tree) and len(tree) == 15
    rows = distance_counts(tree)
    q = quotient(rows[1], rows[2])
    assert q == [1, -3, 1, 1, 1], q
    # The quartic has exactly two distinct roots in (0,1).
    poly = sp.Poly(sum(c*x**j for j, c in enumerate(q)), x)
    assert poly.count_roots(0, 1) == 2
    its = [ab for ab, mult in poly.intervals(eps=sp.Rational(1,10**13))
           if 0 < ab[0] < 1]
    assert len(its) == 2 and its[0][1] < its[1][0]
    assert its[0][0] < sp.Rational(44,100) < its[1][0]
    # C_1 strictly exceeds C_v for every other v except v=2.
    for v in range(15):
        if v in (1,2):
            continue
        other_q = quotient(rows[1], rows[v])
        transformed_coeff = transformed(other_q)
        assert any(c > 0 for c in transformed_coeff)
        assert all(c >= 0 for c in transformed_coeff), (v, transformed_coeff)
    # Signs of the exact quartic at three rational points.
    for p, sign in [(sp.Rational(1,4),1),
                    (sp.Rational(1,2),-1),
                    (sp.Rational(9,10),1)]:
        assert sp.sign(poly.eval(p)) == sign
        expected = frozenset({1 if sign > 0 else 2})
        assert exact_winners(rows,list(range(15)),p) == expected
    return q, its


def main():
    counts, exceptional, heavy, cells = check_small_trees()
    q, intervals = check_witness()
    print('VERIFY_OK shape_counts='+str(dict(counts)))
    print('VERIFY_OK exceptional_shapes='+str(dict(exceptional))+
          ' exceptional_pairs='+str(dict(heavy))+
          ' exact_root_cells='+str(cells))
    print('VERIFY_OK witness_15=1 quartic_coefficients='+str(q)+
          ' strict_double_reentry=1 root_intervals='+str(intervals))

if __name__ == '__main__':
    main()
