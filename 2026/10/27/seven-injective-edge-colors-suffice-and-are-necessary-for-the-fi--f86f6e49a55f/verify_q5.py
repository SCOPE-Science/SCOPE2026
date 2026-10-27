"""Exact, dependency-free certificate for injective seven-edge coloring of Q_5.

Run: python3 verify_q5.py
All tests use exact integer arithmetic; there is no numerical optimization.
"""
from collections import Counter

N = 5
EDGES = [(u, u ^ (1 << i)) for u in range(1 << N)
         for i in range(N) if u < (u ^ (1 << i))]
COLORS = (
    0, 6, 5, 3, 2, 0, 0, 0, 0, 1, 1, 6, 6, 4, 2, 3,
    5, 5, 5, 5, 6, 3, 2, 4, 2, 3, 6, 6, 1, 3, 1, 3,
    2, 4, 6, 5, 0, 4, 5, 2, 4, 2, 6, 3, 3, 0, 2, 1,
    1, 2, 1, 2, 3, 4, 6, 5, 0, 4, 5, 3, 4, 3, 6, 2,
    2, 0, 3, 1, 5, 4, 0, 6, 5, 4, 4, 1, 0, 6, 1, 1,
)


def adjacent(x, y):
    return (x ^ y).bit_count() == 1


def conflicting(e, f):
    """There is a *third* cube edge between endpoints of e and f."""
    if len(set(e + f)) != 4:
        # Shared-endpoint cube edges cannot belong to a triangle.
        return False
    return any(adjacent(x, y) for x in e for y in f)


def colors_by_greedy_independent_classes(P, compatibility):
    order, bounds = [], []
    color = 0
    while P:
        color += 1
        available = P
        while available:
            bit = available & -available
            v = bit.bit_length() - 1
            order.append(v)
            bounds.append(color)
            P &= ~bit
            available &= ~bit
            available &= ~compatibility[v]
    return order, bounds


def verify_upper_bound():
    anchor = (0, 1)
    candidates = [e for e in EDGES if e != anchor and not conflicting(e, anchor)]
    assert len(candidates) == 51
    m = len(candidates)
    compatibility = []
    for i, e in enumerate(candidates):
        compatibility.append(sum((1 << j) for j, f in enumerate(candidates)
                                 if i != j and not conflicting(e, f)))
    calls = 0
    branches = 0

    def contains_clique_of_twelve(P, depth):
        nonlocal calls, branches
        calls += 1
        if depth == 12:
            return True
        if not P:
            return False
        order, bounds = colors_by_greedy_independent_classes(P, compatibility)
        for j in range(len(order) - 1, -1, -1):
            if depth + bounds[j] < 12:
                return False
            v = order[j]
            bit = 1 << v
            assert P & bit
            branches += 1
            if contains_clique_of_twelve(P & compatibility[v], depth + 1):
                return True
            P &= ~bit
        return False

    assert not contains_clique_of_twelve((1 << m) - 1, 0)
    print(f"anchor=(0,1) admissible_other_edges={m} search_calls={calls} branches={branches}")
    print("no_twelve_clique_after_anchor=PASS; every edge packing has at most twelve edges")


def verify_coloring():
    assert len(EDGES) == len(COLORS) == 80
    assert all(adjacent(*e) for e in EDGES)
    assert set(COLORS) == set(range(7))
    conflicts = sum(1 for i in range(80) for j in range(i + 1, 80)
                    if conflicting(EDGES[i], EDGES[j]))
    assert conflicts == 1120
    for i in range(80):
        for j in range(i + 1, 80):
            if conflicting(EDGES[i], EDGES[j]):
                assert COLORS[i] != COLORS[j], (i, j)
    sizes = sorted(Counter(COLORS).values())
    assert sizes == [11, 11, 11, 11, 12, 12, 12]
    print(f"cube_edges={len(EDGES)} conflict_pairs={conflicts} colors=7 sizes={sizes}")
    print("seven_color_certificate=PASS")


if __name__ == "__main__":
    verify_upper_bound()
    verify_coloring()
    print("chi_injective_prime_Q5=7")
