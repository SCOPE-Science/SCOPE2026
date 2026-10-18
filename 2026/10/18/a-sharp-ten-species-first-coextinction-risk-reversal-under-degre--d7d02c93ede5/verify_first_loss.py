#!/usr/bin/env python3
"""Exact finite enumeration for first secondary-extinction risk.

The program uses only Python's standard library. Each nonempty row bitmask
specifies the pollinators visiting one plant. The graph is required connected.
"""
import argparse
import collections
import itertools
import json
from fractions import Fraction
from functools import lru_cache
from math import comb
from pathlib import Path


def connected(rows, b):
    """Independent two-guild breadth-first search."""
    a = len(rows)
    seen = {0}
    queue = [0]
    for u in queue:
        if u < a:
            for j in range(b):
                if (rows[u] >> j) & 1:
                    v = a + j
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
        else:
            bit = 1 << (u-a)
            for i in range(a):
                if rows[i] & bit and i not in seen:
                    seen.add(i)
                    queue.append(i)
    return len(seen) == a + b


@lru_cache(maxsize=None)
def risk_counts(rows, b):
    """Number of k-pollinator failure sets killing at least one plant."""
    out = [0] * (b + 1)
    for failures in range(1 << b):
        if any((row & failures) == row for row in rows):
            out[failures.bit_count()] += 1
    return tuple(out)


def degree_signature(rows, b):
    return (
        tuple(sorted(row.bit_count() for row in rows)),
        tuple(sorted(sum((row >> j) & 1 for row in rows) for j in range(b))),
    )


def comparable(u, v):
    return all(a <= b for a, b in zip(u, v)) or all(a >= b for a, b in zip(u, v))


def risk_probability(rows, b, q):
    return sum(
        Fraction(c) * q**k * (1-q)**(b-k)
        for k, c in enumerate(risk_counts(rows, b))
    )


def direct_probability(rows, b, q):
    """Second implementation: explicit Bernoulli outcomes and neighbor tests."""
    total = Fraction(0)
    for choices in itertools.product((False, True), repeat=b):
        extinct = False
        for row in rows:
            if all(choices[j] for j in range(b) if (row >> j) & 1):
                extinct = True
                break
        if extinct:
            k = sum(choices)
            total += q**k * (1-q)**(b-k)
    return total


def enumerate_small():
    summary = []
    for n in range(2, 10):
        total = 0
        degree_classes = 0
        risk_pairs = 0
        coefficientwise_pairs = 0
        unique_risk_vectors = 0
        for b in range(1, n):
            a = n - b
            if min(a, b) == 1:
                # Only one connected simple bipartite graph is possible.
                continue
            histograms = collections.defaultdict(set)
            for rows in itertools.combinations_with_replacement(range(1, 1 << b), a):
                if not connected(rows, b):
                    continue
                assert set(j for row in rows for j in range(b) if (row >> j) & 1) == set(range(b))
                histograms[degree_signature(rows, b)].add(risk_counts(rows, b))
                total += 1
            degree_classes += len(histograms)
            unique_risk_vectors += sum(len(v) for v in histograms.values())
            for cls in histograms.values():
                for u, v in itertools.combinations(sorted(cls), 2):
                    risk_pairs += 1
                    assert comparable(u, v), (n, a, b, u, v)
                    coefficientwise_pairs += 1
        summary.append({
            "total_species": n,
            "connected_row_multisets_for_nontrivial_splits": total,
            "degree_classes_across_splits": degree_classes,
            "distinct_degree_class_risk_vectors": unique_risk_vectors,
            "distinct_risk_vector_pairs_within_degree_classes": risk_pairs,
            "coefficientwise_comparable_pairs": coefficientwise_pairs,
            "crossing_pairs": 0,
        })
    return summary


def witness():
    G = (1, 1, 3, 6, 10, 12)
    H = (1, 2, 5, 6, 9, 10)
    b = 4
    assert connected(G, b) and connected(H, b)
    assert degree_signature(G, b) == degree_signature(H, b)
    assert degree_signature(G, b) == ((1,1,2,2,2,2),(2,2,3,3))
    assert risk_counts(G, b) == (0,1,6,4,1)
    assert risk_counts(H, b) == (0,2,5,4,1)
    assert (risk_counts(G, b)[1],risk_counts(G, b)[2]) == (1,6)
    assert (risk_counts(H, b)[1],risk_counts(H, b)[2]) == (2,5)
    test_q = (Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10))
    for q in test_q:
        for rows in (G,H):
            assert risk_probability(rows,b,q) == direct_probability(rows,b,q)
        assert risk_probability(G,b,q)-risk_probability(H,b,q) == q*(1-q)**2*(2*q-1)
    for t in range(0,12):
        G_t = G + (1,)*t
        H_t = H + (1,)*t
        assert connected(G_t,b) and connected(H_t,b)
        assert degree_signature(G_t,b) == degree_signature(H_t,b)
        assert risk_counts(G_t,b) == risk_counts(G,b)
        assert risk_counts(H_t,b) == risk_counts(H,b)
    return {
        "guild_sizes": {"plants":6,"pollinators":4},
        "G_plant_neighborhood_bitmasks":list(G),
        "H_plant_neighborhood_bitmasks":list(H),
        "plant_degrees":[1,1,2,2,2,2],
        "pollinator_degrees":[2,2,3,3],
        "G_event_subset_counts_by_failures":[0,1,6,4,1],
        "H_event_subset_counts_by_failures":[0,2,5,4,1],
        "G_minus_H_risk_polynomial":"q*(1-q)**2*(2*q-1)",
        "G_minus_H_at_q_1_over_4":"-9/128",
        "G_minus_H_at_q_3_over_4":"3/128",
        "mean_lost_plants_both":"2*q+4*q**2",
        "unbounded_family":"Append t>=0 distinct degree-one plant vertices, each adjacent only to pollinator 0, in both graphs; first-loss risk polynomials remain unchanged.",
        "direct_probability_tests":[str(q) for q in test_q],
        "extension_tests_t":list(range(12)),
    }


def build_certificate():
    return {
        "schema_version":1,
        "arithmetic":"integers and exact rational fractions",
        "domain":"connected simple bipartite graphs, no isolated vertices, all guild splits, total vertices at most 9",
        "enumeration_representation":"nondecreasing nonzero plant-row bitmask tuples; all pollinator labels retained; every plant permutation is represented",
        "small_census":enumerate_small(),
        "comparison_rule":"for each fixed guild split and both degree multisets, compare all distinct failure-set count vectors coordinatewise",
        "witness_and_extension":witness(),
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',type=Path,help='Write canonical JSON certificate')
    parser.add_argument('--compare',type=Path,help='Compare against embedded canonical JSON certificate')
    args=parser.parse_args()
    cert=build_certificate()
    data=(json.dumps(cert,sort_keys=True,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    if args.compare:
        assert args.compare.read_bytes() == data, 'certificate mismatch'
    if args.write:
        args.write.write_bytes(data)
    print('PASS: exact connected bipartite enumeration, coordinatewise risk order through 9 vertices, sharp 10-vertex witness, independent probability tests and unbounded extension; certificate bytes',len(data))

if __name__=='__main__':main()
