"""Independent verifier for Kirkman resolvability dichotomy of two cyclic STS(15)s.
Stdlib only. Rebuilds block lists from generators, checks STS property (105 pairs),
enumerates all parallel classes, decides resolution existence, checks automorphism
orders via point-stabilizer replay (x15 by translation), and validates stored resolution.
Usage: python3 verify.py
"""
from itertools import combinations
from collections import defaultdict, Counter
import math, json, os

N = 15
B_BASES = [(0,1,4),(0,2,8),(0,5,10)]   # System B (resolvable witness)
A_BASES = [(0,1,4),(0,2,9),(0,5,10)]   # System A (non-resolvable witness)

def develop(bases, n=N):
    blocks = set()
    for b in bases:
        for t in range(n):
            blocks.add(tuple(sorted((x+t) % n for x in b)))
    return sorted(blocks)

def check_sts(blocks, n=N):
    assert len(blocks) == n*(n-1)//6 == 35, f"b={len(blocks)} != 35"
    c = Counter()
    for b in blocks:
        assert len(b) == 3 and len(set(b)) == 3
        assert all(0 <= p < n for p in b)
        for p in combinations(sorted(b), 2):
            c[p] += 1
    assert len(c) == n*(n-1)//2 == 105, f"pairs={len(c)}"
    for p in combinations(range(n), 2):
        assert c[p] == 1, f"pair {p} covered {c[p]} times"
    return True

def parallel_classes(blocks, n=N):
    bsets = [set(b) for b in blocks]
    cont = defaultdict(list)
    for i, b in enumerate(bsets):
        for p in b:
            cont[p].append(i)
    pcs = []
    def rec(covered, chosen):
        if len(chosen) == 5:
            if len(covered) == n:
                pcs.append(tuple(sorted(blocks[i] for i in chosen)))
            return
        first = next(p for p in range(n) if p not in covered)
        for i in cont[first]:
            if i in chosen:
                continue
            if bsets[i].isdisjoint(covered):
                chosen.append(i)
                rec(covered | bsets[i], chosen)
                chosen.pop()
    rec(set(), [])
    return pcs

def resolution_search(blocks, pcs, find_all=False):
    bindex = {b: i for i, b in enumerate(blocks)}
    pc_idx = [[bindex[b] for b in pc] for pc in pcs]
    contain = defaultdict(list)
    for j, pc in enumerate(pc_idx):
        for bi in pc:
            contain[bi].append(j)
    used = [False]*len(blocks)
    sols, nodes = [], [0]
    def rec(chosen):
        nodes[0] += 1
        if all(used):
            sols.append(list(chosen))
            return (not find_all)
        f = next(i for i, u in enumerate(used) if not u)
        for j in contain[f]:
            pc = pc_idx[j]
            if all(not used[i] for i in pc):
                for i in pc: used[i] = True
                chosen.append(j)
                done = rec(chosen)
                chosen.pop()
                for i in pc: used[i] = False
                if done and not find_all:
                    return True
        return False
    rec([])
    return sols, nodes[0]

def third_map(blocks):
    third = {}
    for (a, b, c) in blocks:
        for p, q, r in [(a,b,c),(a,c,b),(b,c,a),(b,a,c),(c,a,b),(c,b,a)]:
            third[(p,q)] = r
    assert len(third) == N*(N-1)
    return third

def stab_order(blocks, fix=0, n=N):
    bset, third = set(blocks), third_map(blocks)
    import sys
    sys.setrecursionlimit(10000)
    def fwd_ok(f):
        for b in blocks:
            if all(f[p] != -1 for p in b):
                if tuple(sorted(f[p] for p in b)) not in bset:
                    return False
        return True
    count = 0
    def rec(f, used):
        nonlocal count
        if all(v != -1 for v in f):
            if {tuple(sorted(f[p] for p in b)) for b in blocks} == bset:
                count += 1
            return
        for b in blocks:
            vals = [f[p] for p in b]
            if sum(1 for v in vals if v != -1) == 2:
                u = next(p for p in b if f[p] == -1)
                w = third[tuple(v for v in vals if v != -1)]
                if w in used:
                    return
                f[u] = w; used.add(w)
                if fwd_ok(f):
                    rec(f, used)
                f[u] = -1; used.discard(w)
                return
        u = next(p for p in range(n) if f[p] == -1)
        for w in range(n):
            if w in used:
                continue
            f[u] = w; used.add(w)
            if fwd_ok(f):
                rec(f, used)
            f[u] = -1; used.discard(w)
    f = [-1]*n; f[fix] = fix
    rec(f, {fix})
    return count

def check_resolution(blocks, res):
    assert len(res) == 7, "must have 7 classes"
    seen = set()
    for pc in res:
        assert len(pc) == 5
        pts = set()
        for b in pc:
            assert b in set(blocks), f"block {b} not in system"
            assert b not in seen, f"block {b} reused"
            seen.add(b)
            assert pts.isdisjoint(b), f"class {pc} not disjoint"
            pts.update(b)
        assert pts == set(range(N)), f"class {pc} does not cover Z15"
    assert len(seen) == 35

B = develop(B_BASES); A = develop(A_BASES)
check_sts(B); check_sts(A)
pcsB = parallel_classes(B); pcsA = parallel_classes(A)
solB, nodesB = resolution_search(B, pcsB)
solA, nodesA = resolution_search(A, pcsA)
solsB_all, _ = resolution_search(B, pcsB, find_all=True)
sB = stab_order(B); sA = stab_order(A)
print(f"B: blocks=35 sts=OK npcs={len(pcsB)} resolvable={bool(solB)} nodes={nodesB} nsol={len(solsB_all)} stab={sB} aut={15*sB}")
print(f"A: blocks=35 sts=OK npcs={len(pcsA)} resolvable={bool(solA)} nodes={nodesA} stab={sA} aut={15*sA}")
assert len(pcsB) == 56 and bool(solB) and len(solsB_all) == 240
assert len(pcsA) == 11 and not solA
assert (sB, sA) == (1344, 4), "stabilizer orders must be 1344 (B) and 4 (A)"
assert 15*sB == 20160 and 15*sA == 60
# validate stored resolution artifact
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "resolution_B.json")) as f:
    resB = [tuple(tuple(b) for b in pc) for pc in json.load(f)]
check_resolution(B, resB)
print("stored resolution_B.json: OK (7x5 exact cover of B)")
print("ALL CHECKS PASSED")
