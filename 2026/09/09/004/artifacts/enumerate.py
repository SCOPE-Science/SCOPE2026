#!/usr/bin/env python3
"""Dual-implementation mesh-occurrence enumerator for Fang et al. 2026 Class 69.
Pattern convention: mesh pattern (pi,R) with pi=12 (dots (1,1),(2,2));
R = set of shaded cells indexed by bottom-left corner (x,y) in {0,1,2}^2.
Dots at positions i1<i2 with values a<b form an occurrence iff no other
element of sigma lies in any shaded (pos-interval x vault, value-band y) rectangle:
  x=0: positions left of i1; x=1: strictly between i1,i2; x=2: right of i2;
  y=0: values <a; y=1: a<value<b; y=2: values >b.
Class 69 (Remark 1.3 / Conj 1 of arXiv:2606.14367), pi=12:
  A={(1,2),(1,1),(2,1),(0,0)}  B={(2,2),(0,1),(1,1),(1,0)}
  C={(0,2),(1,1),(2,1),(1,0)}  D={(1,2),(0,1),(1,1),(2,0)}
Two independent counters (count_ref: pair-of-positions loops with per-cell scans;
count_alt: value-pair loops with numpy segment tests) must agree everywhere.
Usage: python3 enumerate.py  (runs full S_7..S_9 + involution census, writes tables/*.json)
"""
import itertools, json, os, sys, time
from collections import Counter
try:
    import numpy as np
    HAVE_NP = True
except ImportError:
    HAVE_NP = False

PATS = {
 'A': frozenset({(1,2),(1,1),(2,1),(0,0)}),
 'B': frozenset({(2,2),(0,1),(1,1),(1,0)}),
 'C': frozenset({(0,2),(1,1),(2,1),(1,0)}),
 'D': frozenset({(1,2),(0,1),(1,1),(2,0)}),
}
NAMES = ['A','B','C','D']

def count_ref(sigma, R):
    n = len(sigma); cnt = 0; occs=[]
    for i1 in range(n):
        a = sigma[i1]
        for i2 in range(i1+1, n):
            b = sigma[i2]
            if a > b: continue
            ok = True
            for (x, y) in R:
                plo, phi = (-1, i1) if x == 0 else ((i1, i2) if x == 1 else (i2, n))
                vlo, vhi = (0, a) if y == 0 else ((a, b) if y == 1 else (b, n + 1))
                for j in range(plo + 1, phi):
                    if j == i1 or j == i2: continue
                    if vlo < sigma[j] < vhi: ok = False; break
                if not ok: break
            if ok: cnt += 1; occs.append((a, b))
    return cnt, occs

def count_fast4(sigma):
    # joint 4-pattern counter: single pass per pair, classify others into 3x3 grid
    n = len(sigma); c = [0,0,0,0]
    # A: not (12 or 11 or 21 or 00); B: not (22 or 01 or 11 or 10)
    # C: not (02 or 11 or 21 or 10); D: not (12 or 01 or 11 or 20)
    for i1 in range(n):
        a = sigma[i1]
        for i2 in range(i1+1, n):
            b = sigma[i2]
            if a > b: continue
            p = [[False]*3 for _ in range(3)]
            for j in range(n):
                if j == i1 or j == i2: continue
                x = 0 if j < i1 else (1 if j < i2 else 2)
                v = sigma[j]
                y = 0 if v < a else (1 if v < b else 2)
                p[x][y] = True
            if not (p[1][2] or p[1][1] or p[2][1] or p[0][0]): c[0] += 1
            if not (p[2][2] or p[0][1] or p[1][1] or p[1][0]): c[1] += 1
            if not (p[0][2] or p[1][1] or p[2][1] or p[1][0]): c[2] += 1
            if not (p[1][2] or p[0][1] or p[1][1] or p[2][0]): c[3] += 1
    return c

def count_alt(sigma, R):
    assert HAVE_NP, "numpy required for independent checker"
    s = np.asarray(sigma); n = len(s)
    pos = np.empty(n + 1, dtype=int)
    for i, v in enumerate(s): pos[v] = i
    cnt = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            i1, i2 = int(pos[a]), int(pos[b])
            if i1 > i2: continue
            ok = True
            for (x, y) in R:
                seg = s[:i1] if x == 0 else (s[i1+1:i2] if x == 1 else s[i2+1:])
                if len(seg) == 0: continue
                lo, hi = (0, a) if y == 0 else ((a, b) if y == 1 else (b, n + 1))
                if bool(np.any((seg > lo) & (seg < hi))): ok = False; break
            if ok: cnt += 1
    return cnt

def involutions(n):
    res = []
    def rec(rem, cur):
        if not rem:
            res.append(tuple(cur[i] for i in range(1, len(cur) + 1))); return
        a = rem[0]
        cur[a] = a; rec(rem[1:], cur); del cur[a]
        for idx in range(1, len(rem)):
            b = rem[idx]
            cur[a] = b; cur[b] = a
            rec(rem[1:idx] + rem[idx+1:], cur)
            del cur[a]; del cur[b]
    rec(tuple(range(1, n + 1)), {})
    return res

def main():
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tables')
    os.makedirs(out, exist_ok=True)
    log = []
    # cross-validate implementations on random perms + all involutions n<=7
    import random
    random.seed(12345)
    for n in (7, 8, 9):
        for _ in range(1500):
            s = list(range(1, n + 1)); random.shuffle(s)
            for nm in NAMES:
                assert count_ref(s, PATS[nm])[0] == count_alt(s, PATS[nm]), (s, nm)
    for n in range(1, 8):
        for s in involutions(n):
            l = list(s)
            for nm in NAMES:
                assert count_ref(l, PATS[nm])[0] == count_alt(l, PATS[nm]), (s, nm)
    log.append("cross-implementation agreement OK (random S7-S9 x1500 + all involutions n<=7)")
    full = {}
    for n in (7, 8, 9):
        t0 = time.time()
        d = {k: Counter() for k in NAMES}
        for s in itertools.permutations(range(1, n + 1)):
            cc = count_fast4(list(s))
            for k, v in zip(NAMES, cc): d[k][v] += 1
        # independent replay of avoidance column (k=0) with count_ref
        for k in NAMES:
            z = sum(1 for s in itertools.permutations(range(1, n + 1)) if count_ref(list(s), PATS[k])[0] == 0)
            assert z == d[k][0], (n, k)
        full[n] = {k: dict(sorted(v.items())) for k, v in d.items()}
        json.dump(full[n], open(os.path.join(out, f'dist_S{n}.json'), 'w'), indent=1)
        log.append(f"S_{n}: " + "; ".join(f"{k}0={d[k][0]}" for k in NAMES) + f" eq4={d['A']==d['B']==d['C']==d['D']} ({time.time()-t0:.1f}s)")
    invtab = {}
    for n in (7, 8, 9):
        inv = involutions(n)
        d = {k: Counter() for k in NAMES}
        for s in inv:
            for k in NAMES: d[k][count_ref(list(s), PATS[k])[0]] += 1
        invtab[n] = {k: dict(sorted(v.items())) for k, v in d.items()}
        json.dump(invtab[n], open(os.path.join(out, f'dist_inv{n}.json'), 'w'), indent=1)
        log.append(f"inv{n} (#={len(inv)}): A0={d['A'][0]} C0={d['C'][0]} A==B:{d['A']==d['B']} C==D:{d['C']==d['D']} Across:{d['A']==d['C']}")
    print("\n".join(log))
    open(os.path.join(out, 'LOG.txt'), 'w').write("\n".join(log) + "\n")

if __name__ == '__main__':
    main()
