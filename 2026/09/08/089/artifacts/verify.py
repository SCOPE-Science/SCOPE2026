"""O(n^2) overlay audit for lane-264 (stdlib only).

Usage: python3 verify.py [--cand candidate.json]
Audits pinned baseline triple (A,B,C_pub) from squares.json and,
optionally, a candidate third square C (candidate.json: {"C": [10 rows]}).
"""
import json
import sys
from collections import Counter
from hashlib import sha256
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    with open(HERE / name) as f:
        return json.load(f)


def grid(rows):
    return [[int(c) for c in r] for r in rows]


def is_latin(X):
    n = len(X)
    tgt = list(range(n))
    for i in range(n):
        if sorted(X[i]) != tgt:
            return False
        if sorted(X[r][i] for r in range(n)) != tgt:
            return False
    return True


def overlay(X, Y):
    n = len(X)
    pairs = [(X[i][j], Y[i][j]) for i in range(n) for j in range(n)]
    return len(set(pairs)), Counter(pairs)


def report(name, X, Y):
    d, c = overlay(X, Y)
    n = len(X)
    dup = {k: v for k, v in sorted(c.items()) if v > 1}
    print(f"{name}: distinct={d}/{n*n} deficit={n*n-d} dup_types={len(dup)}")
    for k, v in dup.items():
        print(f"   pair={k} x{v}")
    return d


def main():
    sq = load("squares.json")
    A, B, C = grid(sq["A"]), grid(sq["B"]), grid(sq["C_pub"])
    assert all(is_latin(X) for X in (A, B, C)), "baseline Latin check failed"
    print("baseline Latin checks: A,B,C_pub all Latin OK")
    print("pair sha256:",
          sha256(json.dumps({"A": sq["A"], "B": sq["B"]}).encode()).hexdigest())
    ab = report("AB    ", A, B)
    ac = report("AC_pub", A, C)
    bc = report("BC_pub", B, C)
    print(f"baseline D0 = {(100-ab)+(100-ac)+(100-bc)}")
    if len(sys.argv) > 2 and sys.argv[1] == "--cand":
        cand = load(sys.argv[2])
        Cc = grid(cand["C"])
        ok = is_latin(Cc)
        print("candidate Latin:", ok)
        ab2 = report("AB     ", A, B)
        ac2 = report("AC_cand", A, Cc)
        bc2 = report("BC_cand", B, Cc)
        print(f"candidate D = {(100-ab2)+(100-ac2)+(100-bc2)}")
        if not ok:
            sys.exit("CANDIDATE NOT LATIN")
    print("AUDIT_OK")


if __name__ == "__main__":
    main()
