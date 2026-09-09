"""Exhaustive C8/C6 census from ALL 126 starts (no symmetry reduction).

Replays and hardens counterexample_check.py: DFS closed-walk census of
length 8 (C8) and length 6 (C6) through every vertex. Expected:
  directed C8 total = 0 (C8-free),
  directed C6 total = 410640 * 12 = 4927680
    (410640 = 2 * C(60,3)*3!*2!/2 undirected C6, each counted from
     6 starts x 2 directions).
USAGE: python3 output/artifacts/exhaustive_verify.py  (stdlib only, ~1 min)
"""
import json
import sys

sys.path.insert(0, "output/artifacts")
from counterexample_check import build, adj_list


def census_from_all_starts(adj, L):
    nbr = {v: sorted(adj[v]) for v in adj}
    sys.setrecursionlimit(10000)
    total = 0
    for s in adj:
        stack = [(s, [s], {s})]
        while stack:
            v, path, seen = stack.pop()
            k = len(path) - 1
            if k == L - 1:
                if s in nbr[v]:
                    total += 1
                continue
            for w in nbr[v]:
                if w == s or w in seen:
                    continue
                stack.append((w, path + [w], seen | {w}))
    return total


def main():
    X, Y, X1, Y1, X2, Y2, edges = build()
    adj = adj_list(X, Y, edges)
    assert len(X) == 63 and len(Y) == 63 and len(edges) == 360
    tot8 = census_from_all_starts(adj, 8)
    tot6 = census_from_all_starts(adj, 6)
    result = {
        "directed_C8_all_starts": tot8,
        "directed_C6_all_starts": tot6,
        "expected_C8": 0,
        "expected_C6": 410640 * 12,
        "pass": (tot8 == 0 and tot6 == 410640 * 12),
    }
    print(json.dumps(result, indent=2))
    with open("output/artifacts/exhaustive_result.json", "w") as f:
        json.dump(result, f, indent=2)
    assert result["pass"]
    print("EXHAUSTIVE_OK")


if __name__ == "__main__":
    main()
