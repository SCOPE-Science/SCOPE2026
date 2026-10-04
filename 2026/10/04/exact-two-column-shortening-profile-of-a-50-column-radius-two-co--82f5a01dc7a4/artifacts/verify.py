#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROFILE = json.loads((HERE / "double_deletion_profile.json").read_text(encoding="utf-8"))
COLS = PROFILE["columns"]
SPACE = 1 << 10


def covered_direct(remaining):
    out = {0}
    out.update(remaining)
    for a, b in combinations(remaining, 2):
        out.add(a ^ b)
    return out


def build_supports(cols):
    reps = [[] for _ in range(SPACE)]
    reps[0].append(frozenset())
    for a in cols:
        reps[a].append(frozenset((a,)))
    for a, b in combinations(cols, 2):
        reps[a ^ b].append(frozenset((a, b)))
    return reps


def holes_direct(deleted):
    remaining = [x for x in COLS if x not in deleted]
    return SPACE - len(covered_direct(remaining))


def holes_incidence(deleted, reps):
    d = frozenset(deleted)
    return sum(1 for rs in reps if all(r & d for r in rs))


def main():
    assert len(COLS) == 50
    assert len(set(COLS)) == 50
    assert all(0 < x < SPACE for x in COLS)
    assert len(covered_direct(COLS)) == SPACE

    reps = build_supports(COLS)
    assert all(reps)
    assert sum(map(len, reps)) == 1276

    singles = [(holes_direct({a}), a) for a in COLS]
    one_min = min(h for h, _ in singles)
    one_argmin = sorted(a for h, a in singles if h == one_min)
    assert one_min == PROFILE["single_deletion_anchor"]["minimum"]
    assert one_argmin == PROFILE["single_deletion_anchor"]["minimizers"]

    hist = Counter()
    argmin = []
    best = None
    checked = 0
    for a, b in combinations(COLS, 2):
        d = {a, b}
        h1 = holes_direct(d)
        h2 = holes_incidence(d, reps)
        assert h1 == h2
        hist[h1] += 1
        checked += 1
        if best is None or h1 < best:
            best = h1
            argmin = [[a, b]]
        elif h1 == best:
            argmin.append([a, b])

    expected_hist = {int(k): v for k, v in PROFILE["two_deletion_histogram"].items()}
    assert checked == 1225
    assert dict(sorted(hist.items())) == dict(sorted(expected_hist.items()))
    assert sum(hist.values()) == 1225
    assert best == PROFILE["minimum"] == 27
    assert argmin == PROFILE["minimizers"]

    print("VERIFY_OK")
    print("two_deletions_checked=1225")
    print("minimum=27")
    print("minimizers=" + json.dumps(argmin, separators=(",", ":")))
    print("histogram=" + json.dumps(dict(sorted(hist.items())), separators=(",", ":")))


if __name__ == "__main__":
    main()
