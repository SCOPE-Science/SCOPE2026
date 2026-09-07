"""Standalone verifier for the C=24 gap catalog (stdlib only, no numpy).

Checks for every catalog entry in catalog.json:
 1. Pattern-list completeness: re-enumerates all feasible knapsack patterns
    by DP recursion and requires exact set equality with the stored list.
 2. Dual feasibility (exact Fractions): A^T y <= 1 entrywise, y >= 0,
    and dual objective b^T y equals the claimed LP value.
 3. Primal feasibility (exact Fractions): coverage A*lam >= b and
    sum(lam) equals the claimed LP value (hence both are optimal).
 4. Ceil + Delta arithmetic with integers only.
 5. Packing validity: item multiset equality, every bin load <= C,
    number of bins == OPT.
 6. Lower bound: independent stdlib DFS proves K = OPT-1 bins infeasible.

Usage: python3 recheck.py   (expects catalog.json in the same directory)
"""
import json
import os
import sys
from fractions import Fraction
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
C = 24


def enumerate_patterns(a, cap):
    out = []

    def rec(i, remaining, cur):
        if i == len(a):
            if any(v > 0 for v in cur):
                out.append(tuple(cur))
            return
        for v in range(remaining // a[i] + 1):
            cur.append(v)
            rec(i + 1, remaining - v * a[i], cur)
            cur.pop()

    rec(0, cap, [])
    return out


def infeasible_in_k(items_desc, cap, k, node_limit=5000000):
    """Item-branching DFS decision procedure. Returns (infeasible, nodes)."""
    if sum(items_desc) > k * cap:
        return True, 1
    loads = [0] * k
    seen_states = set()
    nodes = [0]
    over = [False]

    def dfs(i):
        nodes[0] += 1
        if nodes[0] > node_limit:
            over[0] = True
            return None
        if i == len(items_desc):
            return True
        key = (i, tuple(sorted(loads)))
        if key in seen_states:
            return False
        s = items_desc[i]
        order = sorted(range(k), key=lambda j: -loads[j])
        tried_loads = set()
        for j in order:
            if loads[j] + s > cap or loads[j] in tried_loads:
                continue
            tried_loads.add(loads[j])
            empty = (loads[j] == 0)
            loads[j] += s
            r = dfs(i + 1)
            loads[j] -= s
            if r is True:
                return True
            if r is None:
                return None
            if empty:
                break
        seen_states.add(key)
        return False

    r = dfs(0)
    if r is None:
        raise RuntimeError("node limit exceeded")
    return (not r), nodes[0]


def check_entry(e):
    a, b = e["a"], e["b"]
    k = len(a)
    LP = Fraction(e["LP"])
    y = [Fraction(v) for v in e["y"]]
    # 1. pattern completeness
    pats = enumerate_patterns(a, C)
    assert Counter(pats) == Counter(tuple(p) for p in e["patterns"]), \
        "pattern list mismatch"
    P = len(pats)
    # 2. dual certificate
    assert all(v >= 0 for v in y), "dual y negative"
    for p in pats:
        assert sum(Fraction(p[i]) * y[i] for i in range(k)) <= 1, \
            "dual pattern constraint violated"
    assert sum(Fraction(b[i]) * y[i] for i in range(k)) == LP, \
        "dual objective mismatch"
    # 3. primal certificate
    lam = {int(pi): Fraction(v) for pi, v in e["primal"].items()}
    assert sum(lam.values()) == LP, "primal objective mismatch"
    for i in range(k):
        cov = sum(Fraction(pats[pi][i]) * v for pi, v in lam.items())
        assert cov >= b[i], "primal coverage violated"
    # 4. ceil / Delta
    q = LP.numerator // LP.denominator + (1 if LP.numerator % LP.denominator else 0)
    assert q == e["ceil"], "ceil mismatch"
    assert e["Delta"] == e["OPT"] - q == 1, "Delta mismatch"
    # 5. packing
    items = []
    for i in range(k):
        items += [a[i]] * b[i]
    assert Counter(sum(e["packing"], [])) == Counter(items), "packing items mismatch"
    assert len(e["packing"]) == e["OPT"], "packing bin count mismatch"
    for bin_ in e["packing"]:
        assert sum(bin_) <= C, "bin over capacity"
    # 6. lower bound: OPT-1 bins infeasible (independent re-search)
    infeas, nodes = infeasible_in_k(sorted(items, reverse=True), C, e["OPT"] - 1)
    assert infeas, "K=OPT-1 unexpectedly feasible"
    return P, nodes


def main():
    with open(os.path.join(BASE, "catalog.json")) as f:
        cat = json.load(f)
    assert len(cat) == 5, "catalog must hold exactly five entries"
    for idx, e in enumerate(cat):
        P, nodes = check_entry(e)
        print("entry %d: a=%s b=%s LP=%s ceil=%d OPT=%d Delta=1 "
              "patterns=%d lb_nodes=%d  PASS"
              % (idx + 1, e["a"], e["b"], e["LP"], e["ceil"],
                 e["OPT"], P, nodes))
    print("ALL 5 ENTRIES VERIFIED")


if __name__ == "__main__":
    main()
