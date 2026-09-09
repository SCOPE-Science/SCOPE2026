"""TARGET: Mubayi-Rodl-type lower bound pi(C5^(3)) >= 2*sqrt(3)-3.

Construction family F(n; b, levels): split V = A u B, |B| ~ b*n.
  Top edges: all triples with exactly 2 vertices in A ("AAB").
  Plus recursively the same construction inside B (base level: AAB only).
Claims verified here (stdlib + sympy only):
  (C1) No circular (A/B)-labeling of Z5, except all-B, has all 5 length-2
       windows in {AAB, BBB}. Hence any tight C5 either lies entirely in B
       (descend) or has a non-edge window (contradiction). By induction on
       recursion depth, every member is C5-free. Base level (AAB only): needs
       all windows exactly AAB, also impossible by the same census.
  (C2) Asymptotic density: with |B|/n -> b, per-level AAB density
       3*b*(1-b)^2... (exact: C(|A|,2)*|B|/C(n,3) -> 3*(1-b)^2*b),
       recursion gives fixed point d = 3*b*(1-b)/(1+b+b^2), maximized at
       b* = (sqrt(3)-1)/2 with value 2*sqrt(3)-3 (exact sympy calculus).
  (C3) Finite instances (n=9,12 two-level; n=6,7,8 one-level) are C5-free by
       brute force and have densities approaching from above (small-n effect).
Usage: python3 mr_lower_bound.py -> prints VERIFY_OK / VERIFY_FAIL.
"""
import itertools
import math
from math import comb

# ---- (C1) labeling census: brute force over 2^5 labelings ----
def window_classes(bits):
    out = []
    for k in range(5):
        w = (bits[k], bits[(k + 1) % 5], bits[(k + 2) % 5])
        nA = w.count('A')
        out.append(nA)
    return out

bad_nonBBB = []   # non-all-B labelings whose windows are all AAB(2A) or BBB(0A)
allAAB = []       # labelings whose windows are ALL exactly AAB (base-level check)
for bits in itertools.product('AB', repeat=5):
    nB = bits.count('B')
    ws = window_classes(bits)
    if all(w in (0, 2) for w in ws) and nB < 5:
        bad_nonBBB.append(bits)
    if all(w == 2 for w in ws):
        allAAB.append(bits)

print("(C1) non-all-B labelings with all windows AAB-or-BBB:", bad_nonBBB)
print("(C1) labelings with all windows exactly AAB:", allAAB)

# ---- (C2) exact density optimization (sympy) ----
import sympy as sp
b = sp.symbols('b', real=True)
f = 3 * b * (1 - b) / (1 + b + b**2)
df = sp.diff(f, b)
sols = sp.solve(df, b)
bopt = None
for s in sols:
    if s.is_real and 0 < s < 1:
        bopt = s
dPanel_opt = sp.simplify(f.subs(b, bopt))
target = sp.simplify(2 * sp.sqrt(3) - 3)
print("(C2) stationary points:", sols)
print("(C2) interior optimum b* =", bopt, "=", float(bopt))
print("(C2) d(b*) =", dPanel_opt, " target 2*sqrt3-3 =", target,
      " equal:", sp.simplify(dPanel_opt - target) == 0)
print("(C2) numeric:", float(dPanel_opt))

# ---- (C3) finite instances ----
def build(n, a, levels=2):
    E = set()
    A0 = set(range(a))
    B0 = set(range(a, n))
    for t in itertools.combinations(range(n), 3):
        if sum(1 for v in t if v in A0) == 2:
            E.add(t)
    if levels >= 2 and len(B0) >= 3:
        a1 = int(round(len(B0) * float(bopt)))
        a1 = max(1, min(len(B0) - 1, a1))
        B0l = sorted(B0)
        A1 = set(B0l[:a1])
        for t in itertools.combinations(B0l, 3):
            if sum(1 for v in t if v in A1) == 2:
                E.add(t)
    return E

def has_c5(E, n):
    E = set(E)
    for verts in itertools.combinations(range(n), 5):
        seen = set()
        for p in itertools.permutations(verts):
            if p[0] != min(p) or p[1] > p[4]:
                continue
            e = frozenset(tuple(sorted((p[k], p[(k + 1) % 5], p[(k + 2) % 5])))
                           for k in range(5))
            if e in seen:
                continue
            seen.add(e)
            if e <= E:
                return True
    return False

alpha = 1 - float(bopt)
ok3 = True
for n in (9, 12):
    a = int(round(alpha * n))
    E = build(n, a, levels=2)
    c5 = has_c5(E, n)
    print("(C3) 2-level n=%d a=%d edges=%d density=%.4f C5=%s"
          % (n, a, len(E), len(E) / comb(n, 3), c5))
    ok3 = ok3 and (not c5)
for n in (6, 7, 8):
    a = int(round(alpha * n))
    E = build(n, a, levels=1)
    c5 = has_c5(E, n)
    print("(C3) 1-level n=%d a=%d density=%.4f C5=%s"
          % (n, a, len(E) / comb(n, 3), c5))
    ok3 = ok3 and (not c5)

ok1 = (bad_nonBBB == []) and (allAAB == [])
ok2 = (sp.simplify(dPanel_opt - target) == 0)
if ok1 and ok2 and ok3:
    print("VERIFY_OK")
else:
    print("VERIFY_FAIL", ok1, ok2, ok3)
