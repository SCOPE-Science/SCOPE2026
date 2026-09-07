#!/usr/bin/env python3
"""Independent verifier for the rt=34 one-cluster 5-cycle witness.
No search heuristics: direct simulation + exact power-automaton BFS (256 masks)
forward from FULL and reverse from singletons. Runs in <2 s with stdlib only.
Usage: python3 replay_verify.py
"""
import json, os, sys
from collections import deque

N = 8
FULL = (1 << N) - 1

def load_witness():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "witness_main.json")) as f:
        return json.load(f)

def simulate(a, b, w):
    mp = {'a': a, 'b': b}
    S = set(range(N))
    for ch in w:
        t = mp[ch]
        S = {t[s] for s in S}
    return S

def images(a, b):
    ia, ib = [0]*256, [0]*256
    for mask in range(256):
        ra = rb = 0
        for bit in range(N):
            if mask >> bit & 1:
                ra |= 1 << a[bit]
                rb |= 1 << b[bit]
        ia[mask], ib[mask] = ra, rb
    return ia, ib

def forward_bfs(a, b):
    ia, ib = images(a, b)
    dist = {FULL: 0}
    parent = {}
    q = deque([FULL])
    expanded = 0
    singletons = {1 << i for i in range(N)}
    target = None
    while q:
        m = q.popleft()
        expanded += 1
        if m in singletons:
            target = m
            break
        for letter, img in (('a', ia), ('b', ib)):
            nm = img[m]
            if nm not in dist:
                dist[nm] = dist[m] + 1
                parent[nm] = (m, letter)
                q.append(nm)
    word = None
    if target is not None:
        w = []
        cur = target
        while cur != FULL:
            prev, letter = parent[cur]
            w.append(letter)
            cur = prev
        word = ''.join(w[::-1])
    return dist, parent, target, word, expanded

def reverse_bfs(a, b):
    ia, ib = images(a, b)
    from collections import defaultdict
    rev = defaultdict(list)
    # combined reverse edges labelled; simpler: two tables
    rev_a = defaultdict(list); rev_b = defaultdict(list)
    for m in range(256):
        rev_a[ia[m]].append(m)
        rev_b[ib[m]].append(m)
    dist = {1 << i: 0 for i in range(N)}
    q = deque([1 << i for i in range(N)])
    while q:
        m = q.popleft()
        for rtab in (rev_a, rev_b):
            for p in rtab[m]:
                if p not in dist:
                    dist[p] = dist[m] + 1
                    q.append(p)
    return dist

def is_one_cluster_5cycle(a):
    seen_global = set()
    cycles = []
    for s in range(N):
        seen = {}
        cur = s
        while cur not in seen and cur not in seen_global:
            seen[cur] = True
            cur = a[cur]
        if cur in seen:
            c = cur
            cyc = []
            while True:
                cyc.append(c)
                c = a[c]
                if c == cur:
                    break
            cycles.append(tuple(sorted(cyc)))
        seen_global.update(seen.keys())
    uniq = set(cycles)
    return len(uniq) == 1 and len(next(iter(uniq))) == 5

def main():
    wit = load_witness()
    a = tuple(wit["a"]); b = tuple(wit["b"]); w = wit["w"]; L = wit["L"]
    assert len(w) == L, (len(w), L)
    ok = True
    print(f"witness: a={a} b={b} L={L}")
    c1 = is_one_cluster_5cycle(a) and tuple(a[:5]) == (1, 2, 3, 4, 0)
    print("check1 one-cluster 5-cycle canonical-a:", c1)
    ok &= c1
    c2 = sorted(b) == list(range(N))
    print("check2 b is permutation:", c2)
    ok &= c2
    fin = simulate(a, b, w)
    c3 = len(fin) == 1
    print(f"check3 replay resets to {fin}:", c3)
    ok &= c3
    # no proper prefix resets
    S = set(range(N))
    mp = {'a': a, 'b': b}
    prefix_reset = None
    for i, ch in enumerate(w):
        S = {mp[ch][s] for s in S}
        if len(S) == 1:
            prefix_reset = i + 1
            break
    c4 = prefix_reset == len(w)
    print(f"check4 first-reset prefix = {prefix_reset} (== L):", c4)
    ok &= c4
    dist, parent, target, bw, expanded = forward_bfs(a, b)
    c5 = dist.get(target) == L and len(bw) == L and simulate(a, b, bw) == fin
    print(f"check5 forward BFS: dist={dist.get(target)} expanded={expanded} reachable={len(dist)}:", c5)
    ok &= c5
    # stored table cross-check
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "dist_main.json")) as f:
        stored = json.load(f)
    c6 = all(dist.get(int(k)) == v for k, v in stored["forward_dist"].items()) and len(dist) == len(stored["forward_dist"])
    print(f"check6 stored distance table matches recomputed ({len(dist)} entries):", c6)
    ok &= c6
    distR = reverse_bfs(a, b)
    c7 = distR.get(FULL) == L
    print(f"check7 reverse BFS dist[FULL]={distR.get(FULL)} == L:", c7)
    ok &= c7
    print("ALL CHECKS PASSED" if ok else "FAILURE")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
