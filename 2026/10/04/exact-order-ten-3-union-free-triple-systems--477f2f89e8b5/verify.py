#!/usr/bin/env python3
from itertools import combinations

N = 10
VERTICES = tuple(range(N))
EDGE_TUPLES = list(combinations(VERTICES, 3))
EDGE_MASKS = [sum(1 << v for v in e) for e in EDGE_TUPLES]
EDGE_INDEX = {e: i for i, e in enumerate(EDGE_TUPLES)}
FIRST = EDGE_INDEX[(0, 1, 2)]
SECOND_REPS = [
    EDGE_INDEX[(0, 1, 3)],  # intersection size 2 with {0,1,2}
    EDGE_INDEX[(0, 3, 4)],  # intersection size 1
    EDGE_INDEX[(3, 4, 5)],  # intersection size 0
]


def is_three_union_free(edge_indices):
    seen = {}
    edge_indices = tuple(edge_indices)
    for r in (1, 2, 3):
        for sub in combinations(edge_indices, r):
            union = 0
            for i in sub:
                union |= EDGE_MASKS[i]
            if union in seen:
                return False, seen[union], sub
            seen[union] = sub
    return True, None, None


def pair_star_indices(a=0, b=1):
    return [
        i for i, e in enumerate(EDGE_TUPLES)
        if a in e and b in e
    ]


def has_common_pair(edge_indices):
    inter = EDGE_MASKS[edge_indices[0]]
    for i in edge_indices[1:]:
        inter &= EDGE_MASKS[i]
    return inter.bit_count() >= 2


def initial_used_bits(selected):
    unions = []
    for r in (1, 2, 3):
        if r > len(selected):
            break
        for sub in combinations(selected, r):
            u = 0
            for i in sub:
                u |= EDGE_MASKS[i]
            unions.append(u)
    if len(set(unions)) != len(unions):
        raise AssertionError("fixed initial edges already violate 3-union-freeness")
    bits = 0
    for u in unions:
        bits |= 1 << u
    return bits


def new_union_bits(i, selected, used_bits):
    """Return all newly created union masks when edge i is appended, or None on collision."""
    m = EDGE_MASKS[i]
    values = [m]
    values.extend(m | EDGE_MASKS[a] for a in selected)
    values.extend(
        m | EDGE_MASKS[selected[a]] | EDGE_MASKS[selected[b]]
        for a in range(len(selected))
        for b in range(a + 1, len(selected))
    )
    new_bits = 0
    for u in values:
        bit = 1 << u
        if (used_bits & bit) or (new_bits & bit):
            return None
        new_bits |= bit
    return new_bits


def search_containing(second_rep, target_size, require_non_pair_star=False):
    """
    Exhaustively search all target_size-edge families containing FIRST and second_rep.

    Candidates are traversed in a fixed order. If a candidate already creates a repeated
    union with the current selected family, it can be discarded permanently because that
    collision persists after adding further edges. The recursion otherwise enumerates every
    subset of the currently feasible suffix exactly once.
    """
    selected0 = [FIRST, second_rep]
    used0 = initial_used_bits(selected0)
    candidates0 = [i for i in range(len(EDGE_MASKS)) if i not in selected0]
    candidates0.sort(
        key=lambda i: (
            -((EDGE_MASKS[i] & EDGE_MASKS[FIRST]).bit_count()),
            -((EDGE_MASKS[i] & EDGE_MASKS[second_rep]).bit_count()),
            i,
        )
    )
    nodes = 0

    def dfs(selected, used_bits, candidates):
        nonlocal nodes
        nodes += 1
        if len(selected) == target_size:
            if require_non_pair_star and has_common_pair(selected):
                return None
            return selected.copy()
        need = target_size - len(selected)
        if len(candidates) < need:
            return None

        feasible = []
        additions = []
        for i in candidates:
            nb = new_union_bits(i, selected, used_bits)
            if nb is not None:
                feasible.append(i)
                additions.append(nb)
        if len(feasible) < need:
            return None

        for p in range(0, len(feasible) - need + 1):
            i = feasible[p]
            ans = dfs(selected + [i], used_bits | additions[p], feasible[p + 1 :])
            if ans is not None:
                return ans
        return None

    solution = dfs(selected0, used0, candidates0)
    return solution, nodes


def main():
    star = pair_star_indices(0, 1)
    assert len(star) == 8
    ok, a, b = is_three_union_free(star)
    assert ok, (a, b)

    nine_results = []
    for rep in SECOND_REPS:
        sol, nodes = search_containing(rep, 9, require_non_pair_star=False)
        assert sol is None
        nine_results.append((EDGE_TUPLES[rep], nodes))

    eight_nonstar_results = []
    for rep in SECOND_REPS:
        sol, nodes = search_containing(rep, 8, require_non_pair_star=True)
        assert sol is None
        eight_nonstar_results.append((EDGE_TUPLES[rep], nodes))

    print("pair_star_size=8")
    print("pair_star_three_union_free=True")
    print("target9_orbit_searches=")
    for rep, nodes in nine_results:
        print(f"  second={rep} nodes={nodes} solution=None")
    print("target8_non_pair_star_orbit_searches=")
    for rep, nodes in eight_nonstar_results:
        print(f"  second={rep} nodes={nodes} solution=None")
    print("conclusion=U_3(10,3)=8; every extremal family is a pair-star up to relabeling")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
