"""Finite exact tests for order-aware recovery under sequential anchoring.

The general theorems use combinatorial arguments; these finite tests are
not proofs for unbounded numbers of alternatives.
Requires only Python 3 standard library.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def observed(p, t, sigma):
    """Return retained alternatives in presentation order."""
    rank = {a: k for k, a in enumerate(p)}
    best = len(p)
    retained = []
    for a in sigma:
        is_record = rank[a] < best
        if is_record:
            best = rank[a]
            if rank[a] < t:
                retained.append(a)
    return tuple(retained)


def edges_of_record_positions(m, rec):
    """Immediate strict comparisons: better alternative, worse alternative."""
    edges = []
    first = rec[0]
    for j in range(first):
        edges.append((first, j))
    for h, r in enumerate(rec):
        if h:
            edges.append((r, rec[h - 1]))
        end = rec[h + 1] if h + 1 < len(rec) else m
        for j in range(r + 1, end):
            edges.append((r, j))
    assert len(edges) == m - 1
    return edges


def tree_pairs(m, edges):
    reach = {i: set() for i in range(m)}
    for a, b in edges:
        reach[a].add(b)
    for _ in range(m):
        for i in range(m):
            reach[i] |= set().union(*(reach[j] for j in tuple(reach[i]))) if reach[i] else set()
    return {(a, b) for a in range(m) for b in reach[a]}


def forced_pairs(rankings, m):
    """Pairwise comparisons on which all compatible strict orders agree."""
    possibilities = [set() for _ in combinations(range(m), 2)]
    pairs = list(combinations(range(m), 2))
    for p in rankings:
        rank = {x: k for k, x in enumerate(p)}
        for q, (i, j) in enumerate(pairs):
            possibilities[q].add(rank[i] < rank[j])
    return {(i, j) if True in possibilities[q] else (j, i)
            for q, (i, j) in enumerate(pairs) if len(possibilities[q]) == 1}


def check_known_order():
    count_ballots = 0
    for m in range(3, 8):
        orders = list(permutations(range(m)))
        observed_fibers = defaultdict(set)
        for p in orders:
            for t in range(1, m + 1):
                record = observed(p, t, tuple(range(m)))
                assert record
                observed_fibers[record].add(p)

        assert len(observed_fibers) == 2**m - 1
        for rec, fiber in observed_fibers.items():
            edges = edges_of_record_positions(m, rec)
            mathematically_allowed = {
                p for p in orders if all(p.index(a) < p.index(b) for a, b in edges)
            }
            assert fiber == mathematically_allowed, (m, rec, "wrong identified set")
            pos1 = tuple(i + 1 for i in rec)
            product = 1
            for r in pos1[1:]:
                product *= r - 1
            predicted_count = factorial(m - 1) // product
            assert len(fiber) == predicted_count, (m, rec, "wrong hook formula")

            k = len(rec)
            predicted_pairs = m - k + sum(r - 1 for r in pos1[1:])
            reached = tree_pairs(m, edges)
            actual = forced_pairs(fiber, m)
            assert reached == actual, (m, rec, "wrong pairwise identification")
            assert len(actual) == predicted_pairs

            no_order_pairs = m - 1 + (k - 1) * (k - 2) // 2
            gain = sum(r - h for h, r in enumerate(pos1[1:], start=2))
            assert predicted_pairs == no_order_pairs + gain
            count_ballots += 1

        # All-tolerant random-ranking model: exact mean of comparable pairs.
        empirical_sum = Fraction(0)
        empirical_second = Fraction(0)
        for p in orders:
            rec = observed(p, m, tuple(range(m)))
            positions = [i + 1 for i in rec]
            k = len(rec)
            c = m - k + sum(j - 1 for j in positions[1:])
            empirical_sum += c
            empirical_second += c*c
        empirical_mean = empirical_sum / factorial(m)
        empirical_var = empirical_second / factorial(m) - empirical_mean**2
        H = sum(Fraction(1, j) for j in range(1, m + 1))
        H2 = sum(Fraction(1, j*j) for j in range(1, m + 1))
        assert empirical_mean == 2*m - 2*H
        assert empirical_var == Fraction(m*m - 9*m, 2) + 8*H - 4*H2
        print(f"known order m={m}: {len(observed_fibers)} ballots; exact fibers, tree pairs, moments OK")

    print("total checked known-order ballots:", count_ballots)


def check_unobserved_order():
    for m in range(3, 6):
        orders = list(permutations(range(m)))
        possible = defaultdict(set)
        for p in orders:
            for t in range(1, m + 1):
                for sigma in orders:
                    ballot = tuple(reversed(observed(p, t, sigma)))
                    possible[ballot].add(p)
        for ballot, allowed in possible.items():
            R = set(ballot)
            predicted = {
                p for p in orders
                if p[0] == ballot[0] and tuple(x for x in p if x in R) == ballot
            }
            assert predicted == allowed, (m, ballot)
            assert len(allowed) == factorial(m - 1)//factorial(len(ballot) - 1)
        print(f"unobserved order m={m}: {len(possible)} ballots; exact fibers OK")


if __name__ == '__main__':
    check_known_order()
    check_unobserved_order()
    print("ALL EXACT FINITE CHECKS PASSED")
