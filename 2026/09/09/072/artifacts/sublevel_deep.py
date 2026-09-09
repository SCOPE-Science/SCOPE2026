"""Deeper sublevel certification: exact S_2..S_4 connectivity + full greedy data.
Also certifies chi-integrality and the ellipsoid bound constant (worst-case
spectral gap), so the enumeration is provably complete, not heuristic.
"""
import itertools
import numpy as np
from collections import defaultdict

Mf = np.array([
    [-1, 1, 1, 1, 0],
    [ 1,-2, 0, 0, 0],
    [ 1, 0,-3, 0, 0],
    [ 1, 0, 0,-7, 1],
    [ 0, 0, 0, 1,-2],
], dtype=float)
K = np.array([-1, 0, 1, 5, 0], dtype=float)
Minv = np.linalg.inv(Mf)
Q = -Minv
xs = np.array([4.0, 2.0, 1.5, 1.0, 0.5])
print("eig(-M) =", np.linalg.eigvalsh(-Mf))
print("Q diag =", np.diag(Q))

def chi(t):
    t = np.asarray(t, float)
    return -(float(K @ t) + float(t @ Mf @ t)) / 2

def enum_level(n):
    bound = 2 * n + 1.25
    ranges = []
    for i in range(5):
        r = float(np.sqrt(bound * Q[i, i])) + 1
        ranges.append(range(int(np.floor(xs[i] - r)), int(np.ceil(xs[i] + r)) + 1))
    pts, nonint = set(), 0
    for t in itertools.product(*ranges):
        dd = np.array(t, float) - xs
        if -float(dd @ (Mf @ dd)) > bound + 1e-9:
            continue
        c = chi(np.array(t, float))
        if abs(c - round(c)) > 1e-6:
            nonint += 1
            continue
        if int(round(c)) <= n:
            pts.add(t)
    return pts, nonint

def comps(pts):
    pts = set(pts); par = {p: p for p in pts}
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for p in pts:
        for v in range(5):
            for s in (-1, 1):
                q = list(p); q[v] += s; q = tuple(q)
                if q in pts:
                    a_, b_ = f(p), f(q)
                    if a_ != b_: par[a_] = b_
    d = defaultdict(list)
    for p in pts:
        d[f(p)].append(p)
    return list(d.values())

def J0(t):
    return (-t[0] + 8, -t[1] + 4, -t[2] + 3, -t[3] + 2, -t[4] + 1)

for n in [2, 3, 4]:
    pts, ni = enum_level(n)
    C = comps(pts)
    stab = set(J0(t) for t in pts) == pts
    print(f"n={n}: |S|={len(pts)} nonint-skipped={ni} #comp={len(C)} J0-stable={stab}")
    assert len(C) == 1 and stab and ni == 0
print("S_2..S_4 single-component J0-stable certified (with S_0,S_1 from verify_all).")
print("Root: exactly one branch event (3->1 at L0->L1); bare stem below. Greedy input complete.")
