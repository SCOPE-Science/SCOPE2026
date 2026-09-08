"""Self-contained audit script for lane-09 Betti census.
Re-derives from scratch (no inputs): enumeration, h4-distribution, the 1752
cubic-generated ideals, their graded Betti tables via Koszul-homology Tor
computation mod two primes + exact rationals on orbit reps, S4 orbits,
Borel-fixed scan, and the full 15504-ideal stratum census.
Run: python3 audit_betti.py   (~30-60 s, stdlib only)
"""
import time
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction
from math import comb

t_start = time.time()
NVAR = 4

def mons(deg, n=4):
    out = []
    def rec(i, rem, cur):
        if i == n - 1:
            out.append(tuple(cur + [rem])); return
        for e in range(rem + 1):
            rec(i + 1, rem - e, cur + [e])
    rec(0, deg, [])
    return out

Q0 = [(0, 0, 0, 0)]; Q1 = mons(1); Q2 = mons(2); Q3 = mons(3); Q4 = mons(4)
PURE = [(3, 0, 0, 0), (0, 3, 0, 0), (0, 0, 3, 0), (0, 0, 0, 3)]
NONPURE = [m for m in Q3 if m not in PURE]
SUB = {i: list(combinations(range(4), i)) for i in range(5)}

def divides(a, b): return all(x <= y for x, y in zip(a, b))
def add_var(m, v):
    L = list(m); L[v] += 1; return tuple(L)

def rank_entries(rows, cols, entries, mod=None):
    if rows == 0 or cols == 0: return 0
    if mod is None:
        M = [[Fraction(0)] * cols for _ in range(rows)]
        for r, c, v in entries: M[r][c] += v
        r = 0
        for c in range(cols):
            piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
            if piv is None: continue
            M[r], M[piv] = M[piv], M[r]
            for i in range(rows):
                if i != r and M[i][c] != 0:
                    f = M[i][c] / M[r][c]
                    for j in range(c, cols): M[i][j] -= f * M[r][j]
            r += 1
        return r
    M = [[0] * cols for _ in range(rows)]
    for r, c, v in entries: M[r][c] = (M[r][c] + v) % mod
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] % mod != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], -1, mod)
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c] * inv % mod
                for j in range(c, cols): M[i][j] = (M[i][j] - f * M[r][j]) % mod
        r += 1
    return r

def betti_of_survivors(Tset, mod=32003):
    B = {0: Q0, 1: Q1, 2: Q2, 3: sorted(Tset)}
    H = {0: 1, 1: 4, 2: 10, 3: 5}
    for d in (4, 5, 6, 7): B[d] = []; H[d] = 0
    bidx = {(d, m): j for d in range(8) for j, m in enumerate(B[d])}
    beta = {}
    for j in range(8):
        dims = {i: comb(4, i) * (H[j - i] if 0 <= j - i <= 7 else 0) for i in range(5)}
        ranks = {}
        for i in range(1, 5):
            ds, dt = j - i, j - i + 1
            if dims[i] == 0 or dims[i - 1] == 0: ranks[i] = 0; continue
            ent = []
            for si, S in enumerate(SUB[i]):
                for mi, m in enumerate(B[ds]):
                    col = si * len(B[ds]) + mi
                    for pos, k in enumerate(S):
                        Tt = tuple(v for v in S if v != k)
                        if dt < 0 or dt > 3: continue
                        n = add_var(m, k)
                        if (dt, n) not in bidx: continue
                        row = SUB[i - 1].index(Tt) * len(B[dt]) + bidx[(dt, n)]
                        ent.append((row, col, -1 if pos % 2 else 1))
            ranks[i] = rank_entries(dims[i - 1], dims[i], ent, mod)
        ranks[0] = ranks[5] = 0
        for i in range(5):
            beta[(i, j)] = dims[i] - ranks[i] - (ranks[i + 1] if i + 1 <= 5 else 0)
    return beta

def key(b): return tuple(b[(i, j)] for i in range(5) for j in range(8))

# ---- Step 1: candidate space + h4 filter ----
S_list = list(combinations(range(16), 5))
assert len(S_list) == 4368 == comb(16, 5)
h4dist, H40 = Counter(), []
for S in S_list:
    comp = [NONPURE[i] for i in range(16) if i not in set(S)] + PURE
    h4 = sum(1 for Q in Q4 if not any(divides(c, Q) for c in comp))
    h4dist[h4] += 1
    if h4 == 0: H40.append(S)
print("h4-distribution:", dict(sorted(h4dist.items())))
assert dict(h4dist) == {0: 1752, 1: 2124, 2: 468, 3: 24} and len(H40) == 1752

# ---- Step 2: Betti census mod 32003 ----
census, wit, mem = Counter(), {}, {}
for S in H40:
    T = set(NONPURE[i] for i in S)
    b = betti_of_survivors(T, mod=32003)
    assert b[(0, 0)] == 1 and b[(1, 3)] == 15 and sum(b[(1, j)] for j in range(8)) == 15
    k = key(b)
    census[k] += 1
    if k not in wit: wit[k] = S; mem[k] = b
print("distinct tables (mod 32003):", len(census))
assert len(census) == 10 and sum(census.values()) == 1752

# ---- Step 3: independent second prime ----
c2 = Counter()
for S in H40:
    c2[key(betti_of_survivors(set(NONPURE[i] for i in S), mod=1000003))] += 1
assert sorted(c2.values()) == sorted(census.values()) and len(c2) == 10
print("second-prime (1000003) agreement: OK")

# ---- Step 4: Euler check on all + rationals on S4-orbit reps ----
for S in H40:
    b = mem[key(betti_of_survivors(set(NONPURE[i] for i in S), mod=32003))]
    for j in range(8):
        lhs = sum(((-1) ** i) * b[(i, j)] for i in range(5))
        rhs = sum(H_ * (((-1) ** (j - k)) * comb(4, j - k) if 0 <= j - k <= 4 else 0)
                  for k, H_ in ((0, 1), (1, 4), (2, 10), (3, 5)))
        assert lhs == rhs
print("Euler checks (all 1752): OK")

perms = list(permutations(range(4)))
def pmon(m, pr): return tuple(m[pr[i]] for i in range(4))
def orbit_of(S):
    T = [NONPURE[i] for i in S]
    orb = set()
    for pr in perms:
        Tp = sorted(pmon(m, pr) for m in T)
        assert all(m not in PURE for m in Tp)
        orb.add(tuple(sorted(NONPURE.index(m) for m in Tp)))
    return orb & set(H40)
seen, reps = set(), []
for S in H40:
    if S in seen: continue
    orb = orbit_of(S)
    seen |= orb
    reps.append(S)
from collections import Counter as _C
print("S4 orbits:", len(reps), dict(sorted(_C(len(orbit_of(S)) for S in reps).items())))
assert len(reps) == 80
for S in reps:
    T = set(NONPURE[i] for i in S)
    assert key(betti_of_survivors(T, mod=None)) == key(betti_of_survivors(T, mod=32003))
print(f"exact-rational agreement on all {len(reps)} orbit reps: OK")

# ---- Step 5: Borel-fixed scan (any variable order) ----
def stable(Tset, order):
    I3 = set(m for m in Q3 if m not in Tset)
    pos = {v: r for r, v in enumerate(order)}
    for m in I3:
        for j in range(4):
            if m[j]:
                for i in range(4):
                    if pos[i] < pos[j]:
                        L = list(m); L[j] -= 1; L[i] += 1
                        if tuple(L) not in I3: return False
    return True
n_stable = sum(1 for S in H40
               if any(stable(set(NONPURE[i] for i in S), o) for o in perms))
print("Borel-fixed among 1752 (any order):", n_stable)
assert n_stable == 0

# ---- Step 6: full gen-degree-<=4 stratum ----
Tall = list(combinations(Q3, 5))
assert len(Tall) == 15504 == comb(20, 5)
full = Counter()
for T in Tall:
    full[key(betti_of_survivors(set(T), mod=32003))] += 1
print("full stratum: ideals=15504 distinct tables=", len(full))
print("ALL AUDIT CHECKS PASSED in %.1fs" % (time.time() - t_start))
