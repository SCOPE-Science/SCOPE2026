#!/usr/bin/env python3
"""Exact rational verifier for a finite binary-tree BMO folding theorem.

Run: python3 VERIFY.py DUAL_CERTIFICATES.json
Requires Python 3 standard library only. No optimization solver is invoked.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

N = 8
NODES = [tuple(range(8)), tuple(range(4)), tuple(range(4, 8))]
NODES.extend(tuple(range(i, i + 2)) for i in range(0, 8, 2))


def representative_colours(depth):
    if depth == 0:
        return [(k,) for k in range(4)]
    low = representative_colours(depth - 1)
    return [a + b for i, a in enumerate(low) for b in low[i:]]


def matrix():
    pos = {}
    j = 8
    for node_id, node in enumerate(NODES):
        for i in node:
            pos[node_id, i] = j
            j += 1
    assert j == 32
    A, b = [], []
    for node_id, node in enumerate(NODES):
        m = len(node)
        for i in node:
            for sign in (-1, +1):
                row = [0] * j
                for k in node:
                    row[k] -= sign
                row[i] += sign * m
                row[pos[node_id, i]] = -m
                A.append(row)
                b.append(0)
        row = [0] * j
        for i in node:
            row[pos[node_id, i]] = 1
        A.append(row)
        b.append(m)
    sign_row_start = len(A)
    for _ in range(8):
        A.append([0] * j)
        b.append(0)
    assert len(A) == 63 and sign_row_start == 55
    return A, b, sign_row_start


def verify(path):
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    assert doc["schema"] == "binary-depth3-bmo-dual-v1"
    assert doc["matrix_scale"] == "integer"
    cases = doc["dual_pairs"]
    assert doc["case_count"] == 1540 == len(cases)
    all_colours = representative_colours(3)
    assert len(all_colours) == len(set(all_colours)) == 1540
    A, b, start = matrix()
    max_upper = Fraction(0)
    for k, item in enumerate(cases):
        codes, sparse_dual = item
        assert tuple(codes) == all_colours[k], ("wrong or missing orbit", k)
        assert all(isinstance(v, int) and 0 <= v < 4 for v in codes)
        eps = [1 if v & 2 else -1 for v in codes]
        ss = [1 if v & 1 else -1 for v in codes]
        for i in range(8):
            A[start + i][i] = -eps[i]
        C = [eps[i] * (8 * ss[i] - sum(ss)) for i in range(8)]
        y = [Fraction(0)] * len(A)
        last = -1
        for record in sparse_dual:
            assert len(record) == 3
            idx, numerator, denominator = record
            assert isinstance(idx, int) and last < idx < len(A)
            assert isinstance(numerator, int) and isinstance(denominator, int)
            assert numerator > 0 and denominator > 0
            y[idx] = Fraction(numerator, denominator)
            last = idx
        # These are exact rational dual feasibility conditions for the primal
        # MAX C.x s.t. A.(x,u) <= b; x free and u >= 0.
        for i in range(32):
            val = sum(y[j] * A[j][i] for j in range(len(A)))
            if i < 8:
                assert val == C[i], ("x dual mismatch", k, i, val, C[i])
            else:
                assert val >= 0, ("u dual mismatch", k, i, val)
        objective = sum(y[j] * b[j] for j in range(len(A)))
        assert objective <= 64, ("dual objective too high", k, objective)
        max_upper = max(max_upper, objective)
    assert max_upper == 64
    print(f"PASS: {len(cases)} orbit-complete cases; all exact dual equalities and bounds; largest scaled upper bound {max_upper}.")
    print("Proof consequence: the root folding bound is 1, and all descendant node bounds follow from four-atom folding.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 VERIFY.py DUAL_CERTIFICATES.json")
    verify(sys.argv[1])
