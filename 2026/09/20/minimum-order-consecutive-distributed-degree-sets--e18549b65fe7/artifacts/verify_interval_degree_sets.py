#!/usr/bin/env python3
"""Verification for the consecutive distributed-degree-set theorem.

No third-party packages are required.
"""
from math import ceil


def parts_from_counts(counts):
    seq = []
    for d, c in enumerate(counts, start=1):
        seq.extend([d] * c)
    return sorted(seq, reverse=True)


def positive_compositions(total, k):
    if k == 1:
        yield (total,)
        return
    for first in range(1, total - k + 2):
        for tail in positive_compositions(total - first, k - 1):
            yield (first,) + tail


def gale_ryser(rows, cols):
    rows = sorted(rows, reverse=True)
    cols = sorted(cols, reverse=True)
    if sum(rows) != sum(cols):
        return False
    if rows and rows[0] > len(cols):
        return False
    if cols and cols[0] > len(rows):
        return False
    for k in range(1, len(rows) + 1):
        if sum(rows[:k]) > sum(min(k, c) for c in cols):
            return False
    return True


def ordinary_order(a, b):
    """Minimum order without a connectivity requirement; assumes 1 <= a <= b."""
    assert 1 <= a <= b
    H = (b * (b + 1) - a * (a + 1)) // 2
    return a + b + ceil(H / a)


def connected_order(a, b):
    """Minimum connected order, or None when no connected realization exists."""
    assert 1 <= a <= b
    if a == 1 and b > 1:
        return None
    return ordinary_order(a, b)


def theorem_sequences(a, b):
    """Degree sequences used by the sharp construction, with 1 <= a <= b."""
    assert 1 <= a <= b
    H = (b * (b + 1) - a * (a + 1)) // 2
    rows = list(range(a, 0, -1))
    if H:
        m = ceil(H / a)
        r = H - a * (m - 1)
        rows += [a] * (m - 1) + [r]
        rows.sort(reverse=True)
    cols = list(range(b, 0, -1))
    return rows, cols


def has_connected_realization(rows, cols):
    """Test the connected-realization criterion used in the proof.

    For positive bigraphic sequences, E >= |V|-1 is necessary and sufficient for
    the existence of a connected simple bipartite realization; sufficiency follows
    from the component-merging 2-switch lemma proved in RESULT.md.
    """
    return (
        bool(rows and cols)
        and min(rows) > 0
        and min(cols) > 0
        and gale_ryser(rows, cols)
        and sum(rows) >= len(rows) + len(cols) - 1
    )


def exhaustive_min_order(a, b, require_connected):
    """Brute-force degree multiplicities for small interval sets [a] and [b]."""
    assert 1 <= a <= b
    predicted = connected_order(a, b) if require_connected else ordinary_order(a, b)
    if predicted is None:
        # The theorem proves structural nonexistence. Search a finite window as a
        # consistency check rather than treating this finite search as a proof.
        upper = ordinary_order(a, b) + 8
    else:
        upper = predicted
    for n in range(a + b, upper + 1):
        for x in range(a, n - b + 1):
            y = n - x
            for rc in positive_compositions(x, a):
                rows = parts_from_counts(rc)
                rs = sum(rows)
                for cc in positive_compositions(y, b):
                    cols = parts_from_counts(cc)
                    if sum(cols) != rs or not gale_ryser(rows, cols):
                        continue
                    if not require_connected or has_connected_realization(rows, cols):
                        return n
    return None


def main():
    checked = 0
    for a in range(1, 21):
        for b in range(a, 41):
            rows, cols = theorem_sequences(a, b)
            assert set(rows) == set(range(1, a + 1))
            assert set(cols) == set(range(1, b + 1))
            assert sum(rows) == sum(cols)
            assert gale_ryser(rows, cols)
            assert len(rows) + len(cols) == ordinary_order(a, b)
            if a == 1 and b > 1:
                assert connected_order(a, b) is None
                assert not has_connected_realization(rows, cols)
            else:
                assert connected_order(a, b) == ordinary_order(a, b)
                assert has_connected_realization(rows, cols)
            checked += 1

    print(f"constructive Gale-Ryser checks: {checked} parameter pairs passed")
    print("small exhaustive ordinary / connected minima:")
    for a in range(1, 4):
        vals = []
        for b in range(a, 7):
            ordinary = exhaustive_min_order(a, b, require_connected=False)
            connected = exhaustive_min_order(a, b, require_connected=True)
            assert ordinary == ordinary_order(a, b)
            assert connected == connected_order(a, b)
            vals.append(f"({a},{b}):{ordinary}/{connected}")
        print("  " + "  ".join(vals))
    print("all checks passed")


if __name__ == "__main__":
    main()
