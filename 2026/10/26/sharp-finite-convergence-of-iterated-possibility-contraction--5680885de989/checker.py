"""Reproduce finite tests of a modal-contraction convergence theorem.

No third-party packages are required. Run: python3 checker.py
Rows are successor-set bitmasks, and p_truth is a bitmask of p-worlds.
"""
from itertools import product


def step(rows, p_truth):
    """Hedged contraction on the modal formula possibility(p)."""
    n = len(rows)
    universe = (1 << n) - 1
    possible = sum((1 << w) for w, row in enumerate(rows)
                   if row & p_truth)
    false_worlds = universe ^ possible
    return tuple(row | false_worlds if row & ~possible == 0 else row
                 for row in rows)


def first_fixed_stage(rows, p_truth, limit):
    for stage in range(limit + 1):
        nxt = step(rows, p_truth)
        if nxt == rows:
            assert step(nxt, p_truth) == nxt
            return stage
        rows = nxt
    raise AssertionError("failed to stabilize by claimed upper bound")


def sharp_path(n):
    # Arrows i -> i+1; the final world has no outgoing arrow.
    rows = tuple((1 << (i + 1)) if i < n - 1 else 0 for i in range(n))
    p_truth = 1  # p holds only at world zero
    current = rows
    for stage in range(n):
        # Exactly the last 'stage' rows have received additions.
        active = {w for w, row in enumerate(current) if row & p_truth}
        assert active == set(range(n - stage, n)), (n, stage, active)
        following = step(current, p_truth)
        assert following != current, (n, stage)
        current = following
    assert step(current, p_truth) == current
    assert first_fixed_stage(rows, p_truth, n) == n


def main():
    cases = 0
    for n in range(1, 5):
        counts = {}
        for p_truth in range(1 << n):
            for rows in product(range(1 << n), repeat=n):
                stage = first_fixed_stage(rows, p_truth, n)
                counts[stage] = counts.get(stage, 0) + 1
                cases += 1
        assert max(counts) == n, (n, counts)
        print("exhaustive_n", n, "counts", sorted(counts.items()))
    for n in range(1, 25):
        sharp_path(n)
    print("sharp_paths_checked_through", 24)
    print("total_exhaustive_cases", cases)
    print("ALL_CHECKS_OK")


if __name__ == '__main__':
    main()
