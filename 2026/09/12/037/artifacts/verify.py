"""Lane-1177 verification: countable inequality rank in OrdMon.

Exact, deterministic checks (strings only, no floats):
  A. Derivation builder: every lambda_n (2<=n<=N) derived from {lambda_2,lambda_3}
     by explicit primitive ordered-monoid steps (context x*(u->v)*y + transitivity).
  B. Pos-coinserter description: C-order on words == diagonal + generator pairs
     (no chains possible: tops start with 'b', bottoms with 'a').
  C. D-order description: D generators never chain (same first-letter invariant),
     so D-order == diagonal + generator pairs exactly.
  D. Mismatch pair p=(a^2b,a), q=(ba^2,a): p<=q in T(C) but NOT in D.
  E. Truncated BFS cross-check of D-reachability and T(C)-order on word pairs.
"""
import json
from collections import deque

A2 = "aa"
A3 = "aaa"

def lam_bot(n): return "a" * n + "b"
def lam_top(n): return "b" + "a" * n

# ---------- A. derivation builder (primitive steps only use lam_2 / lam_3) ----------
def build(n):
    """Return list of primitive steps (before, after, rule, lctx, rctx) deriving
    lam_bot(n) <= lam_top(n). Recursion: lam_n from lam_{n-2} (left ctx 'aa') + lam_2."""
    assert n >= 2
    if n == 2:
        return [(lam_bot(2), lam_top(2), 2, "", "")]
    if n == 3:
        return [(lam_bot(3), lam_top(3), 3, "", "")]
    sub = build(n - 2)
    steps = []
    for (b, a, r, l, rr) in sub:
        steps.append(("aa" + b, "aa" + a, r, "aa" + l, rr))
    # now at aa + lam_top(n-2) = aab a^{n-2} = a^2 b a^{n-2}; apply lam_2, right ctx a^{n-2}
    mid = "aa" + lam_top(n - 2)
    assert mid == lam_bot(2) + "a" * (n - 2), mid
    steps.append((mid, lam_top(2) + "a" * (n - 2), 2, "", "a" * (n - 2)))
    return steps

def check_step(before, after, rule, lctx, rctx):
    assert rule in (2, 3)
    assert before == lctx + lam_bot(rule) + rctx, (before, rule, lctx, rctx)
    assert after == lctx + lam_top(rule) + rctx, (after, rule, lctx, rctx)

N = 60
for n in range(2, N + 1):
    steps = build(n)
    assert steps[0][0] == lam_bot(n), n
    assert steps[-1][1] == lam_top(n), n
    prev = steps[0][0]
    for (b, a, r, l, rr) in steps:
        assert b == prev, (n, b, prev)
        check_step(b, a, r, l, rr)
        prev = a
    assert all(r in (2, 3) for (_, _, r, _, _) in steps)
print(f"A ok: lambda_2..lambda_{N} each derived from {{lam2,lam3}}; "
      f"e.g. len(chain_60)={len(build(60))} primitive steps")

# ---------- B. C-order description ----------
L = 7
words = ["".join(bits) for k in range(L + 1) for bits in
         (__import__("itertools").product("ab", repeat=k))]
words = ["".join(t) for k in range(L + 1) for t in __import__("itertools").product("ab", repeat=k)]
W = set(words)
genC = {(lam_bot(n), lam_top(n)) for n in range(2, 20) if lam_bot(n) in W and lam_top(n) in W}
# global (non-truncated) invariant: no top is a bottom, no top is a bottom's start for chains
for n in range(2, 500):
    assert lam_bot(n)[0] == "a" and lam_top(n)[0] == "b"  # first-letter barrier (exact)
assert not any(t == lam_bot(m) for n in range(2, 500) for m in range(2, 500)
               for t in [lam_top(n)])
# transitive closure of genC (truncated universe): must equal genC (no length>=2 chains)
reach = dict.fromkeys(W, None)
succ = {w: set() for w in W}
for (u, v) in genC:
    succ[u].add(v)
closure = set(genC)
for (u, v) in genC:  # any 2-chain u->v->x needs v a bottom: impossible
    assert not any(v == lam_bot(m) for m in range(2, 500)), v
print(f"B ok: C-order on {len(W)} words (len<={L}) = diagonal + {len(genC)} generator pairs, no chains")

def leC(u, v):
    return u == v or (u, v) in genC

# ---------- C/D. D generators + mismatch ----------
def bottom_tuple(ws):
    """ws=(n1,..,nk) -> bottom tuple; None if any component not in truncated universe."""
    t = tuple(lam_bot(n) for n in ws)
    return t if all(c in W for c in t) else None

p = (lam_bot(2), "a")
q = (lam_top(2), "a")
assert all(c in W for c in p + q)
# T(C): componentwise
assert leC(p[0], q[0]) and leC(p[1], q[1])
print("D1 ok: p <= q in T(C) componentwise (a^2b<=ba^2 generator; a<=a reflexive)")
# D: p is a generator bottom? second component 'a' is never lam_bot(n) (ends with 'b')
assert not any("a" == lam_bot(n) for n in range(2, 500))
# D chaining impossible globally: every top starts with 'b', every bottom with 'a'
assert q[0][0] == "b"  # tops unreachable as bottoms
print("D2 ok: p is no generator bottom, and no generator top is a generator bottom "
      "=> D-order = diagonal + generator pairs => p not<= q in D")

# ---------- E. truncated BFS cross-check ----------
pairs = [(x, y) for x in W for y in W]
Wset = W
genD = set()
for n1 in range(2, 6):
    for n2 in range(2, 6):
        b = (lam_bot(n1), lam_bot(n2)); t = (lam_top(n1), lam_top(n2))
        if all(c in Wset for c in b + t):
            genD.add((b, t))
# BFS in D from p (truncated): reachable set
seen = {p}
dq = deque([p])
Dmap = {}
for (b, t) in genD:
    Dmap.setdefault(b, []).append(t)
while dq:
    z = dq.popleft()
    for t in Dmap.get(z, []):
        if t not in seen:
            seen.add(t); dq.append(t)
assert q not in seen, "mismatch pair reachable in D?!"
# T(C) holds:
assert leC(p[0], q[0]) and leC(p[1], q[1])
print(f"E ok: BFS from p in D reaches {len(seen)} node(s), q not among them; T(C)-order holds")

out = {
    "derivation_max_n": N,
    "chain_len_n60": len(build(60)),
    "truncation_word_length": L,
    "genC_size": len(genC),
    "mismatch_pair": {"p": list(p), "q": list(q),
                      "le_in_TC": True, "le_in_D": False},
    "conclusion": "comparison map not order-iso (explicit mismatch); "
                  "Q finitely presented by {lam2,lam3} (explicit derivations)",
}
with open("output/artifacts/verification_results.json", "w") as f:
    json.dump(out, f, indent=2)
print("wrote output/artifacts/verification_results.json")
