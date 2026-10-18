#!/usr/bin/env python3
"""Exact finite-state proof check and independent edge-level tests for triangular books."""
from collections import Counter
from itertools import product
from math import factorial

TYPES = tuple(product(range(3), repeat=2))
INDEX = {t: i for i, t in enumerate(TYPES)}


def valid_type_counts(counts, spine=0):
    """Equivalent local neighbourhood checks for the nine page types."""
    row = [sum(counts[j] for j, (a, b) in enumerate(TYPES) if a == k)
           for k in range(3)]
    col = [sum(counts[j] for j, (a, b) in enumerate(TYPES) if b == k)
           for k in range(3)]
    if not any(row[k] + col[k] == 1 for k in range(3)):
        return False
    for j, (a, b) in enumerate(TYPES):
        if not counts[j]:
            continue
        if not any(row[k] - (a == k) + (b == k) + (spine == k) == 1
                   for k in range(3)):
            return False
        if not any(col[k] - (b == k) + (a == k) + (spine == k) == 1
                   for k in range(3)):
            return False
    return True


def predicted_capped_states():
    singles = {
        (0, 0): [(1, 2), (2, 1)],
        (1, 1): [(1, 2), (2, 1)],
        (2, 2): [(1, 2), (2, 1)],
    }
    doubles = {
        (0, 0): [((1, 1), (2, 0)), ((1, 0), (2, 2)),
                 ((0, 2), (1, 1)), ((0, 1), (2, 2))],
        (1, 1): [((2, 0), (2, 2)), ((1, 0), (2, 2)),
                 ((0, 2), (2, 2)), ((0, 1), (2, 2))],
        (2, 2): [((1, 1), (2, 0)), ((1, 1), (1, 0)),
                 ((1, 1), (0, 2)), ((1, 1), (0, 1))],
    }
    expected = set()
    for base, defects in singles.items():
        for defect in defects:
            state = [0] * 9
            state[INDEX[base]] = 3
            state[INDEX[defect]] = 1
            expected.add(tuple(state))
    for base, defect_pairs in doubles.items():
        for a, b in defect_pairs:
            state = [0] * 9
            state[INDEX[base]] = 3
            state[INDEX[a]] = 1
            state[INDEX[b]] = 1
            expected.add(tuple(state))
    assert len(expected) == 18
    return expected


def proof_finite_state_check():
    expected = predicted_capped_states()
    seen = set()
    total = 0
    for v in product(range(4), repeat=9):
        total += 1
        ok = valid_type_counts(v)
        if 3 in v:
            if ok:
                seen.add(v)
            assert ok == (v in expected), ("capped state", v)
        elif sum(v) >= 5:
            assert not ok, ("uncapped-large state", v)
    assert seen == expected
    assert total == 4 ** 9
    return total, len(seen)


def graph_edges(n):
    return ((0, 1),) + tuple((endpoint, i + 2) for i in range(n)
                            for endpoint in (0, 1))


def direct_graph_count(n, palette):
    """Tests graph open edge neighbourhoods without using page-type totals."""
    edges = graph_edges(n)
    adj = []
    for k, (u, v) in enumerate(edges):
        adj.append(tuple(j for j, (a, b) in enumerate(edges)
                         if j != k and (u == a or u == b or v == a or v == b)))
    ans = 0
    for colors in product(range(palette), repeat=len(edges)):
        good = True
        for neighbours in adj:
            tally = [0] * palette
            for j in neighbours:
                tally[colors[j]] += 1
            if 1 not in tally:
                good = False
                break
        ans += good
    return ans


def weak_compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for c in range(n + 1):
            for tail in weak_compositions(n - c, k - 1):
                yield (c,) + tail


def orbit_count(n):
    # The factor three chooses the color of the distinguished common edge.
    fact = factorial(n)
    fac = [factorial(i) for i in range(n + 1)]
    answer = 0
    for v in weak_compositions(n, 9):
        if valid_type_counts(v):
            denominator = 1
            for x in v:
                denominator *= fac[x]
            answer += fact // denominator
    return 3 * answer


def main():
    nstates, families = proof_finite_state_check()
    print(f"capped vectors checked={nstates}; valid large-n families={families}")
    expected_small = {3: 198, 4: 1080, 5: 810}
    for n, expected in expected_small.items():
        actual = direct_graph_count(n, 3)
        assert actual == expected, (n, actual, expected)
        assert orbit_count(n) == actual
        print(f"direct graph 3-colour count n={n}: {actual}")
    for n in (3, 4, 5):
        assert direct_graph_count(n, 2) == 0
    print("two named colours: no valid assignments for n=3,4,5")
    for n in range(5, 13):
        actual = orbit_count(n)
        expected = 18 * n * (2 * n - 1)
        assert actual == expected, (n, actual, expected)
        print(f"orbit n={n}: {actual}")
    print("PASS: universal classification and independent finite tests")


if __name__ == "__main__":
    main()
