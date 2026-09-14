"""Independent end-to-end verification of the certified error bound.

Reads output/artifacts/candidate_exact.json (exact P, Q as fraction strings).
Replays Lemma A (denominator lower bound on 40001-node grid + Q' majorant)
and Lemma B (K=2000 cells, shifted majorants, exact endpoint values).
Uses ONLY exact Fraction arithmetic. Asserts total <= 0.01.
Runtime ~1-2 min.
"""
from fractions import Fraction as F
from math import comb
import json

d = json.load(open("output/artifacts/candidate_exact.json"))
P = [F(s) for s in d["P"]]
Q = [F(s) for s in d["Q"]]
assert len(P) == 6 and len(Q) == 6 and Q[0] == 1
TL, TR = F(-3, 2), F(1, 2)

def peval(c, t):
    v = F(0)
    for x in reversed(c):
        v = v * t + x
    return v

def pder(c):
    return [F(k + 1) * c[k + 1] for k in range(len(c) - 1)] if len(c) > 1 else [F(0)]

def pmul(a, b):
    o = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return o

def psub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else F(0)) - (b[i] if i < len(b) else F(0)) for i in range(n)]

def pshift(c, a):
    n = len(c) - 1
    return [sum(c[k] * comb(k, j) * a ** (k - j) for k in range(j, n + 1)) for j in range(n + 1)]

# ---- Lemma A ----
Qp = pder(Q)
R = F(3, 2)
Q1 = sum(F(k) * abs(Q[k]) * R ** (k - 1) for k in range(1, 6))
nA = 40000
minQ = min(peval(Q, TL + (TR - TL) * F(i, nA)) for i in range(nA + 1))
m = minQ - Q1 * F(1, 20000) / 2
print("Lemma A: minGridQ =", float(minQ), " m =", float(m))
assert m > F(9, 10), "denominator bound failed"

# ---- Lemma B ----
Pp = pder(P)
W = psub(pmul(Pp, Q), pmul(P, Qp))
Q2 = pmul(Q, Q)
U = psub(pmul(pder(W), Q2), pmul(pmul(pmul([F(2)], W), Q), Qp))
K = 2000
width = (TR - TL) / K
rho = width / 2
maxend = F(0)
for i in range(K + 1):
    t = TL + width * i
    e = abs(peval(P, t) / peval(Q, t) - abs(t))
    maxend = max(maxend, e)
maxcorr = F(0)
for i in range(K):
    c = TL + width * i + rho
    Qs = pshift(Q, c)
    Us = pshift(U, c)
    Q1loc = sum(F(j) * abs(Qs[j]) * rho ** (j - 1) for j in range(1, len(Qs)))
    mc = abs(Qs[0]) - Q1loc * rho
    assert mc > 0
    M2 = sum(abs(Us[j]) * rho ** j for j in range(len(Us))) / mc ** 4
    maxcorr = max(maxcorr, M2 * rho ** 2 / 2)
total = maxend + maxcorr
print("Lemma B: maxend =", float(maxend), " maxcorr =", float(maxcorr))
print("TOTAL =", float(total))
assert total <= F(1, 100), "threshold FAILED"
print("CERTIFIED: sup error <=", float(total), "<= 0.01  QED")
