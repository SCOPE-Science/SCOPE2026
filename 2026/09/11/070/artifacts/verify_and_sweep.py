"""Independent verification (different code path) + error-diagnosis sweep.

(a) Multiset path: sum over unordered multisets with 1/|Stab| computed from
    Counter/factorial orbit sizes; must reproduce star_sum.py exactly.
(b) Exact difference S-TARGET and 2-adic valuation of denominator.
(c) Sweep of plausible erroneous readings to diagnose the target's origin.
"""
from fractions import Fraction
from itertools import product as iprod, combinations_with_replacement
from collections import Counter
from math import factorial

LAM = [Fraction(0), Fraction(1), Fraction(3), Fraction(7), Fraction(11)]
TARGET = Fraction(589731482057, 6)


def eT(k):
    p = Fraction(1)
    for j in range(5):
        if j == k:
            continue
        p *= LAM[k] - LAM[j]
    return p


def Qe(k, q):
    p = Fraction(1)
    for m in range(6):
        p *= (5 - m) * LAM[k] + m * LAM[q]
    return p


def J_of(ws):
    prodw = Fraction(1)
    s = Fraction(0)
    for w in ws:
        prodw *= w
        s += Fraction(1, 1) / w
    return s / prodw


def ordered_star(k, qs):
    ws = [LAM[k] - LAM[q] for q in qs]
    if any(w == 0 for w in ws):
        return None
    J = J_of(ws)
    outer = Fraction(1)
    for w in ws:
        outer *= Fraction(1, 1) / (-w)
    peq = Fraction(1)
    for q in qs:
        peq *= eT(q)
    invN = Fraction(1, 1) / (eT(k) * peq) * outer * J
    num = Fraction(1)
    for q in qs:
        num *= Qe(k, q)
    den = (5 * LAM[k]) ** 3
    if den == 0:
        return Fraction(0)
    return num / den * invN


# (a) multiset path
S_multi = Fraction(0)
for k in range(5):
    others = [j for j in range(5) if j != k]
    for ms in combinations_with_replacement(others, 4):
        c = Counter(ms)
        stab = Fraction(1)
        for v in c.values():
            stab *= factorial(v)
        # ordered value is the same for all orderings (symmetric); take one
        v = ordered_star(k, ms)
        S_multi += v / stab
print("multiset-path S =", S_multi)
print("  float:", float(S_multi))

# ordered path
S_ord = Fraction(0)
for k in range(5):
    others = [j for j in range(5) if j != k]
    for qs in iprod(others, repeat=4):
        S_ord += ordered_star(k, qs)
S_ord /= 24
print("ordered-path  S =", S_ord)
print("agree:", S_multi == S_ord)

# (b) difference + valuations
D = S_ord - TARGET
print("S - TARGET =", D)
print("nonzero:", D != 0)
den = S_ord.denominator
v2 = (den & -den).bit_length() - 1 if den % 2 == 0 else 0
# exact v2:
t = den
v = 0
while t % 2 == 0:
    t //= 2
    v += 1
print("v2(denominator of S) =", v)
print("odd part of denominator =", t)
print("denominator == 2^v ?", den == 2 ** v)
print("TARGET denominator:", TARGET.denominator, "v2 =", 1)

# (c) diagnosis sweep: plausible wrong readings
print("--- diagnosis sweep ---")
def sweep(name, twist_pow=None, node_pow=4, central=True, use_Jalt=False,
          div=24, fiber_mult=5, edge_range=None):
    S = Fraction(0)
    for k in range(5):
        others = [j for j in range(5) if j != k]
        for qs in iprod(others, repeat=4):
            ws = [LAM[k] - LAM[q] for q in qs]
            if any(w == 0 for w in ws):
                continue
            sw = sum(ws)
            if use_Jalt and sw == 0:
                continue
            J = (Fraction(1, 1) / sw) if use_Jalt else J_of(ws)
            outer = Fraction(1)
            for w in ws:
                outer *= Fraction(1, 1) / (-w)
            peq = Fraction(1)
            for q in qs:
                peq *= eT(q)
            invN = Fraction(1, 1) / (eT(k) * peq) * outer * J
            num = Fraction(1)
            for q in qs:
                p = Fraction(1)
                rng = edge_range if edge_range else range(6)
                for m in rng:
                    p *= (fiber_mult - m) * LAM[k] + m * LAM[q] \
                        if fiber_mult == 5 else ((5 - m) * LAM[k] + m * LAM[q])
                num *= p
            denp = (fiber_mult * LAM[k]) ** node_pow
            cen = (fiber_mult * LAM[k]) if central else Fraction(1)
            if denp == 0:
                # limit: count net power of LAM[k]
                continue
            S += cen * num / denp * invN
    S /= div
    print(f"{name}: float {float(S)} match={S == TARGET}")
    return S

sweep("standard", div=24)
sweep("Jalt=1/sumw", use_Jalt=True)
sweep("div-by-6", div=6)
sweep("no-division", div=1)
sweep("no-node-sub node_pow=0", node_pow=0)
sweep("node_pow=3", node_pow=3)
sweep("no-central-H0", central=False)
sweep("edge m=1..5 only", edge_range=range(1, 6))
sweep("edge m=0..4 only", edge_range=range(0, 5))
print("DIAGNOSIS DONE")
