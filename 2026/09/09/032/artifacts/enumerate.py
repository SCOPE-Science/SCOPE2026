"""Regenerate S_n(123)/S_n(132) by backtracking with O(k) incremental pruning.
Compute (fp,exc,des) trivariate + Krattenthaler-Dyck replay (des = valleys+triple-falls).
Stdlib only. Processes perms on the fly (no big lists)."""
import json, sys, time

def census(n, pat):
    from collections import Counter
    tri = Counter()
    cur = [0]*n
    used = [False]*(n+1)
    count = 0
    replay_ok = True
    dyck_ok = True
    # witnesses: store one perm per (fp,exc,des) cell? store few
    wit = {}
    def has_pat(k):
        # k = index of last placed element (0-based), ck=cur[k]
        ck = cur[k]
        if pat == 123:
            # need i<j<k with cur[i]<cur[j]<ck : O(k) scan keeping min
            m = cur[0]
            for j in range(1, k+1):
                cj = cur[j]
                if m < cj < ck and j < k:
                    # careful: need j<k as middle; last elem is max
                    return True
                # also middle could be... only last is max, so j ranges 0..k-1 as middle
                if cj < m: m = cj
            # redo cleanly: middle j in 1..k-1
            m = cur[0]
            for j in range(1, k):
                if m < cur[j] < ck: return True
                if cur[j] < m: m = cur[j]
            return False
        else:  # 132: need i<j<k with cur[i]<ck<cur[j]
            m = cur[0]
            for j in range(1, k):
                if m < ck < cur[j]: return True
                if cur[j] < m: m = cur[j]
            return False
    # stats incremental: fp/exc from values, des from adjacencies
    def rec(pos):
        nonlocal count, replay_ok, dyck_ok
        if pos == n:
            p = tuple(cur)
            fp = exc = des = 0
            for i, x in enumerate(cur):
                if x == i+1: fp += 1
                elif x > i+1: exc += 1
            for i in range(n-1):
                if cur[i] > cur[i+1]: des += 1
            tri[(fp,exc,des)] += 1
            count += 1
            if (fp,exc,des) not in wit:
                wit[(fp,exc,des)] = p
            if pat == 123:
                st = krattenthaler_123(cur, n)
                # check dyck
                h = 0; okd = True
                for s in st:
                    h += 1 if s == 0 else -1
                    if h < 0: okd = False; break
                if h != 0: okd = False
                if not okd: dyck_ok = False
                v = tf = 0
                for i in range(len(st)-1):
                    if st[i]==1 and st[i+1]==0: v += 1
                for i in range(len(st)-2):
                    if st[i]==1 and st[i+1]==1 and st[i+2]==1: tf += 1
                if v+tf != des: replay_ok = False
            return
        for v in range(1, n+1):
            if not used[v]:
                cur[pos] = v; used[v] = True
                if pos < 2 or not has_pat(pos):
                    rec(pos+1)
                cur[pos] = 0; used[v] = False
    if n == 0:
        return 1, {}, True, True, {}
    rec(0)
    return count, dict(tri), dyck_ok, replay_ok, wit

def krattenthaler_123(cur, n):
    # blocks: each LTR min starts a block; word = following non-minima
    # returns list of 0=U,1=D
    steps = []
    xprev = n+1
    i = 0
    minsofar = n+1
    while i < n:
        x = cur[i]
        # x must be a new LTR min here? not necessarily: words contain non-minima
        # parse: collect block starting at LTR min
        assert x < minsofar, (cur, i)
        j = i+1
        while j < n and cur[j] > min(x, minsofar) and cur[j] > x:
            # cur[j] is not a new LTR min iff cur[j] > x (since x is current min)
            j += 1
        wlen = j-(i+1)
        steps += [0]*(xprev-x)
        steps += [1]*(wlen+1)
        xprev = x; minsofar = x
        i = j
    return steps

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    pat = int(sys.argv[2]) if len(sys.argv) > 2 else 123
    t0 = time.time()
    out = {}
    for n in range(0, N+1):
        if n == 0:
            out["0"] = {"count": 1, "cells": 1, "tri": {"0,0,0": 1}, "dyck_ok": True, "replay_ok": True}
            continue
        c, t, dok, rok, wit = census(n, pat)
        out[str(n)] = {"count": c, "cells": len(t),
            "tri": {"%d,%d,%d" % k: v for k, v in sorted(t.items())},
            "dyck_ok": dok, "replay_ok": rok}
        print(f"n={n} pat={pat} count={c} cells={len(t)} dyck_ok={dok} replay_ok={rok} t={time.time()-t0:.1f}s", flush=True)
    fn = f"output/artifacts/tri_{pat}_n{N}.json"
    json.dump(out, open(fn, "w"), indent=1)
    print("wrote", fn, flush=True)
