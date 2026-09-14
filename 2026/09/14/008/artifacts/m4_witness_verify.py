"""Verify the candidate least witness: a=[1,1,1,1,1,0,1,1,1,1,2] (deg 11),
claimed in I^(7) with matching number 5, hence in I^(7)\\I^6 and forcing
rho >= 7/6. Also check any failing pair with ratio > 7/6 exists in wider search
(higher caps), and check stable-Harbourne-shaped sub-question: smallest m in
I^(m)\\I^r for each r.

Verification must be human-checkable:
 (a) cover sums: list all 16 cover-sums, min = 7.
 (b) non-membership in I^6: certify matching number <= 5. ILP says 5; produce a
     human-checkable upper bound: fractional packing dual certificate. The LP
     max sum y_e s.t. vertex capacities a has integer optimum (bipartite? NO --
     general graph matching with vertex capacities = b-matching, whose LP with
     blossom constraints...). Instead certify nu<=5 by exhibiting a vertex cover
     of the capacitated multiset? A clean combinatorial certificate: find a set
     of vertices T such that sum_{v in T} a_v + (#edges avoiding T ... ) hmm.
     Simplest rigorous certificate: Tutte--Berge-type bound is complex; instead
     prove by a case split / small exact branch-and-bound implemented in pure
     Python (no solver), recorded here, so the check is reproducible without CBC.
"""
import sys
sys.path.insert(0, ".")
from m4_data import COVERS, EDGES, n

a = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2]
print("candidate a =", a, "deg =", sum(a))
print("--- (a) cover sums ---")
sums = sorted((sum(a[v] for v in C), C) for C in COVERS)
for s, C in sums:
    print(f"  sum={s} cover={C}")
print("min cover sum =", sums[0][0])
assert sums[0][0] == 7

# --- (b) exact b-matching number via pure-python branch and bound ---
# edges indexed; capacities a. Branch on first usable edge: take k copies?
# Simpler: expand multiset into unit-stubs? 11 units is small: enumerate matchings
# over unit copies: create copies (v,i), list all copy-edges, max set of
# vertex-disjoint copy-edges by branch and bound. Copy-edges: for each graph edge
# (u,v): copies deg... total pairs = sum over edges a_u*a_v <= manageable.
copies = {v: [(v, i) for i in range(a[v])] for v in range(n)}
pair_list = []
for (u, v) in EDGES:
    for cu in copies[u]:
        for cv in copies[v]:
            pair_list.append((cu, cv))
print("num unit copy-edges:", len(pair_list))

best = [0]
bestm = [None]
# order pairs; branch and bound with simple upper bound (remaining pairs greedy allowed)
pair_list.sort()
import sys as _s
sys.setrecursionlimit(10000)

# Use bitmask over 11 unit vertices
units = []
for v in range(n):
    for i in range(a[v]):
        units.append((v, i))
idx = {u: k for k, u in enumerate(units)}
N = len(units)
emask = []
for (cu, cv) in pair_list:
    emask.append((1 << idx[cu]) | (1 << idx[cv]))
# dedupe identical masks (multiple identical copy pairs give same mask? no: distinct copies differ)
emask = sorted(set(emask), key=lambda m: m)
print("distinct unit edges:", len(emask), "units:", N)

from functools import lru_cache

# order edges to improve pruning: static order fine at this size? 2^11 states only!
# DP over used-mask: dp(mask) = max matching within unused. memoize.
calls = [0]


@lru_cache(maxsize=None)
def dp(used):
    calls[0] += 1
    # first free unit
    for k in range(N):
        if not (used >> k) & 1:
            break
    else:
        return 0
    # option: leave k unmatched
    val = dp(used | (1 << k))
    for m in emask:
        if (m >> k) & 1 and (m & used) == 0:
            val = max(val, 1 + dp(used | m))
    return val


nu = dp(0)
print("exact b-matching number (DP over unit copies):", nu, "states:", calls[0])
assert nu == 5, nu

# Also produce an explicit matching of size 5 (witness that nu>=5, so exactly 5).
def find_match(used):
    for k in range(N):
        if not (used >> k) & 1:
            break
    else:
        return []
    # try to achieve dp(used)
    target = dp(used)
    if dp(used | (1 << k)) == target:
        return find_match(used | (1 << k))
    for m in emask:
        if (m >> k) & 1 and (m & used) == 0:
            if 1 + dp(used | m) == target:
                return [m] + find_match(used | m)
    raise AssertionError


inv = {k: u for u, k in idx.items()}
M = find_match(0)
print("explicit max matching (unit copies):", [(inv[m & -m .bit_length() if False else 0] if False else bin(m)) for m in M])
def bits(m):
    return [inv[k] for k in range(N) if (m >> k) & 1]
print("matching edges:", [bits(m) for m in M])
assert len(M) == 5

# Monomial name
names = [f"v{i}" for i in range(5)] + [f"u{i}" for i in range(5)] + ["w"]
mon = "*".join(f"{names[v]}^{a[v]}" for v in range(n) if a[v])
print("monomial:", mon)
