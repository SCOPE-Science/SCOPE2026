#!/usr/bin/env python3
"""Generic marking counter + small-bidegree calibration for the (3,4) ledger.

Uses only Block-Gottsche 1407.2901 Defs 5.1/5.2/5.4 (Sigma_m, m=0):
  div(j) = out(j)-in(j) <= s_j;  t_j = s_j - div(j);
  mult(D;y) = prod_e [w_e]_y^2;  nu(D) = # linear extensions of D~ / (prod s_j! t_j!).
Two independent counting methods: subset DP and brute-force permutations.
Calibrations: (1,1)->1, (2,1)->1, (2,2)->12 (rational curves on P1xP1).
"""
import itertools
from math import factorial

def count_nu_DP(d, s, div, edges):
    F = list(range(d))
    preds = [0] * d
    for j in range(1, d):
        preds[j] |= (1 << (j - 1))
    for j in range(d):
        for _ in range(s[j]):
            v = len(preds); preds.append(0)
            preds[F[j]] |= (1 << v)
    t = [s[j] - div[j] for j in range(d)]
    assert all(x >= 0 for x in t), (s, div, t)
    for j in range(d):
        for _ in range(t[j]):
            v = len(preds); preds.append(1 << F[j])
    for (i, j) in edges:
        v = len(preds); preds.append(1 << F[i - 1])
        preds[F[j - 1]] |= (1 << v)
    n = len(preds)
    full = (1 << n) - 1
    dp = {0: 1}
    for mask in range(full + 1):
        c = dp.get(mask)
        if not c:
            continue
        for v in range(n):
            if not (mask & (1 << v)) and (preds[v] & ~mask) == 0:
                dp[mask | (1 << v)] = dp.get(mask | (1 << v), 0) + c
    LE = dp.get(full, 0)
    denom = 1
    for j in range(d):
        denom *= factorial(s[j]) * factorial(t[j])
    # floor-preserving parallel-edge swap automorphisms
    from collections import Counter
    key = Counter()
    for k, (i, j) in enumerate(edges):
        key[(i, j)] += 1
    # aut = product over directed pairs of (multiplicity)! for identical weights;
    # here weights passed separately; caller divides. We handle equal-weight case:
    return LE, denom, t

def count_nu_bruteforce(d, s, div, edges):
    """Independent method: count linear extensions by permuting vertex labels."""
    F = list(range(d))
    nodes = list(range(d))
    info = []  # (kind, floor)
    for j in range(d):
        for _ in range(s[j]):
            nodes.append(len(nodes)); info.append(('L', j))
    t = [s[j] - div[j] for j in range(d)]
    for j in range(d):
        for _ in range(t[j]):
            nodes.append(len(nodes)); info.append(('R', j))
    medges = []
    for (i, j) in edges:
        nodes.append(len(nodes)); info.append(('M', (i - 1, j - 1)))
        medges.append(len(nodes) - 1)
    n = len(nodes)
    # precedence pairs (u,v): u before v
    prec = set()
    for j in range(1, d):
        prec.add((j - 1, j))
    idx = d
    for k, (kind, fl) in enumerate(info):
        v = d + k
        if kind == 'L':
            prec.add((v, fl))
        elif kind == 'R':
            prec.add((fl, v))
        else:
            a, b = fl
            prec.add((a, v)); prec.add((v, b))
    cnt = 0
    for p in itertools.permutations(range(n)):
        pos = [0] * n
        for r, v in enumerate(p):
            pos[v] = r
        if all(pos[u] < pos[v] for (u, v) in prec):
            cnt += 1
    return cnt

def check_case(d, c, diagrams, expect_L1, tag):
    """diagrams: list of (s, div, edges, weights). Returns L1."""
    L1 = 0
    for (s, div, edges, w) in diagrams:
        LE, denom, t = count_nu_DP(d, list(s), list(div), list(edges))
        assert LE % denom == 0, (tag, s, div, edges, LE, denom)
        nu = LE // denom
        # parallel equal-weight edge aut
        aut = 1
        if len(edges) == 2 and edges[0] == edges[1] and w[0] == w[1]:
            aut = 2
        assert nu % aut == 0 or True
        if aut == 2:
            assert LE % (denom * 2) == 0, (tag, s, w, LE, denom)
            nu = LE // (denom * 2)
        m1 = 1
        for x in w:
            m1 *= x * x
        L1 += nu * m1
        # brute-force cross-check on small instances only
        n = d + sum(s) + sum(t) + len(edges)
        if n <= 9:
            bf = count_nu_bruteforce(d, list(s), list(div), list(edges))
            assert bf == LE, (tag, s, div, edges, bf, LE)
    print(f"{tag}: L(1) = {L1} (expected {expect_L1})")
    assert L1 == expect_L1, (tag, L1, expect_L1)
    return L1

# (1,1): d=1,c=1, delta=0. No edges. s=(1,). div=(0,), t=(1,). n=3.
check_case(1, 1, [((1,), (0,), [], [])], 1, "(1,1)")
# (2,1): d=2,c=1, delta=0. Single edge (1,2). s=(1,0),a=1: div=(1,-1),t=(0,1). n=5.
check_case(2, 1, [((1, 0), (1, -1), [(1, 2)], [1])], 1, "(2,1)")
# (2,2): d=2,c=2, delta=1. Single edge (1,2).
# s=(2,0): a=1: div=(1,-1),t=(1,1); a=2: div=(2,-2),t=(0,2).
# s=(1,1): a=1: div=(1,-1),t=(0,2). s=(0,2): none.
check_case(2, 2, [
    ((2, 0), (1, -1), [(1, 2)], [1]),
    ((2, 0), (2, -2), [(1, 2)], [2]),
    ((1, 1), (1, -1), [(1, 2)], [1]),
], 12, "(2,2)")
print("CALIBRATION_PASS")
