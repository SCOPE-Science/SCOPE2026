#!/usr/bin/env python3
from itertools import product


def board_edges(a, b, t):
    return [(i, j) for i in range(a) for j in range(b) if not (i == j and i < t)]


def dominates(edges, chosen_mask):
    chosen = [edges[i] for i in range(len(edges)) if (chosen_mask >> i) & 1]
    for r, c in edges:
        if not any(r == x or c == y for x, y in chosen):
            return False
    return True


def minimal_eds_sizes(a, b, t):
    edges = board_edges(a, b, t)
    ans = set()
    tested = 0
    for mask in range(1 << len(edges)):
        tested += 1
        if not dominates(edges, mask):
            continue
        minimal = True
        bits = mask
        while bits:
            bit = bits & -bits
            if dominates(edges, mask ^ bit):
                minimal = False
                break
            bits ^= bit
        if minimal:
            ans.add(mask.bit_count())
    return ans, tested


def theorem_predicts_wed(a, b, t):
    if a > b:
        a, b = b, a
    return (
        a == 1
        or (t == 0 and a == b)
        or (a == 2 and t == 2)
        or (a, b, t) == (2, 3, 1)
        or (a, b, t) == (3, 4, 3)
    )


def is_dominating_set(a, b, t, F):
    E = board_edges(a, b, t)
    F = set(F)
    return all(any(r == x or c == y for x, y in F) for r, c in E)


def is_minimal(a, b, t, F):
    F = list(F)
    if not is_dominating_set(a, b, t, F):
        return False
    return all(not is_dominating_set(a, b, t, F[:i] + F[i + 1:]) for i in range(len(F)))


def negative_witnesses(a, b, t):
    # Assumes 2 <= a <= b and the theorem predicts non-WED.
    witnesses = []
    if t == 0 and a < b:
        A = [(i, 0) for i in range(a)]
        B = [(0, j) for j in range(b)]
        return [A, B]
    if a == b and t >= 1:
        full = [(i, (i + 1) % a) for i in range(a)]
        h = 0
        rows = [i for i in range(a) if i != h]
        cols = [j for j in range(b) if j != h]
        # Greedy cyclic matching on the reduced square; only (2,2,2) fails and is positive.
        if len(rows) == 1:
            reduced = [(rows[0], cols[0])]
        else:
            reduced = []
            for p, r in enumerate(rows):
                for off in range(1, len(cols) + 1):
                    c = cols[(p + off) % len(cols)]
                    if (r, c) in board_edges(a, b, t):
                        reduced.append((r, c))
                        break
        return [full, reduced]
    # Unbalanced t>=1.
    A = [(i, a) for i in range(a)]  # unmatched column a exists because b>a
    witnesses.append(A)
    if a >= 4:
        B = [(1, 0), (0, 1)] + [(0, j) for j in range(2, b)]
        witnesses.append(B)
    elif a == 3 and t <= 2:
        B = [(2, j) for j in range(b)]
        witnesses.append(B)
    elif a == 3 and t == 3 and b >= 5:
        C = [(2, 1), (1, 2)] + [(1, j) for j in range(3, b)]
        witnesses.append(C)
    elif a == 2 and t == 1 and b >= 4:
        C = [(1, j) for j in range(1, b)]
        witnesses.append(C)
    return witnesses


def main():
    exhaustive_cases = 0
    subset_candidates = 0
    for a in range(1, 5):
        for b in range(a, 5):
            for t in range(a + 1):
                sizes, tested = minimal_eds_sizes(a, b, t)
                exhaustive_cases += 1
                subset_candidates += tested
                observed = len(sizes) <= 1
                expected = theorem_predicts_wed(a, b, t)
                assert observed == expected, (a, b, t, sizes, expected)

    witness_cases = 0
    witness_sets = 0
    for a in range(2, 13):
        for b in range(a, 16):
            for t in range(a + 1):
                if theorem_predicts_wed(a, b, t):
                    continue
                W = negative_witnesses(a, b, t)
                assert len(W) >= 2, (a, b, t, W)
                sizes = []
                for F in W:
                    assert all(e in board_edges(a, b, t) for e in F), (a, b, t, F)
                    assert is_minimal(a, b, t, F), (a, b, t, F)
                    sizes.append(len(F))
                assert len(set(sizes)) >= 2, (a, b, t, sizes)
                witness_cases += 1
                witness_sets += len(W)

    print(
        "ALL CHECKS PASSED; "
        f"exhaustive_cases={exhaustive_cases}; "
        f"subset_candidates={subset_candidates}; "
        f"negative_witness_cases={witness_cases}; "
        f"negative_witness_sets={witness_sets}; "
        "exhaustive_range=1<=a<=b<=4; "
        "witness_range=2<=a<=12,a<=b<=15"
    )


if __name__ == "__main__":
    main()
