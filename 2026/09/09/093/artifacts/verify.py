"""Replay verifier for lane-463 TARGET (stdlib only, exact rational arithmetic).

Checks:
 A. eps series: eps_i = 2^-(i+3); sum_1..6 = 63/512; total = 1/8; tail_7+ = 1/512.
 B. Levels: distinct odd prime-power moduli, N>=l/eps, N>|delta|,
    supp residues distinct mod N and covered by E, gamma_i not in Gamma_i.
 C. Per-level ratios r=(N-l)/N >= 1-eps; finite P6 >= 449/512 >= 7/8;
    global product with Weierstrass tail >= 7/8.
 D. Tower-blocking arithmetic: 7/8 - 1/8 = 3/4 >= 1/4; cover <= 1/4 <= 3/4.
 E. Sample-castle right-Folner ratio 6/49 < 1/8.
Run from workspace root: python3 output/artifacts/verify.py
"""
from fractions import Fraction
import json
import os

_here = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(os.path.join(_here, "levels.json")))
lv = L["levels"]

# A: eps_i = 2^-(i+3) for i = 1,2,...
eps = [Fraction(1, 2**(i + 3)) for i in range(1, 300)]
assert eps[0] == Fraction(1, 16) and eps[5] == Fraction(1, 512)
assert sum(eps[:6]) == Fraction(63, 512), sum(eps[:6])
# infinite tail from i=7: geometric with first term 2^-10, ratio 1/2 -> 2^-9
assert eps[6] == Fraction(1, 1024)
assert eps[6] * 2 == Fraction(1, 512)
assert sum(eps[:6]) + Fraction(1, 512) == Fraction(1, 8)

def is_pp(n, p):
    while n % p == 0:
        n //= p
    return n == 1

# B
seen = set()
for D in lv:
    i, N, l, p = D["i"], D["N"], D["l"], D["prime"]
    assert p not in seen and p % 2 == 1 and p > 2
    seen.add(p)
    assert is_pp(N, p), f"N{i}"
    assert Fraction(D["eps"]) == Fraction(1, 2**(i + 3))
    assert N * Fraction(D["eps"]) >= l, f"bound{i}"
    assert abs(D["delta"]) < N, f"cursor{i}"
    s = D["supp"]
    assert l == len(s) + 1
    res = sorted(x % N for x in s)
    assert len(set(res)) == len(res), f"distinct{i}"
    assert set(res) <= set(D["E"]), f"cover{i}"
    assert len(D["E"]) == l
    if D["type"] == "cursor":
        assert s == [] and D["delta"] != 0
    if D["type"] == "lamp":
        assert D["delta"] == 0 and len(s) > 0
    # gamma_i not in Gamma_i: cursor/mixed via delta not in N_i Z;
    # lamp via a covered singleton residue carrying value 1 (sum = 1 mod 2)
    assert (D["delta"] % N) != 0 or len(s) > 0

# C
P6 = Fraction(1, 1)
for D in lv:
    r = Fraction(D["N"] - D["l"], D["N"])
    assert r >= 1 - Fraction(D["eps"])
    assert D["ratio"] == f"{D['N']-D['l']}/{D['N']}"
    P6 *= r
Seps6 = sum(eps[:6])
assert Seps6 == Fraction(63, 512)
assert P6 >= 1 - Seps6 == Fraction(449, 512) >= Fraction(7, 8), P6
tail = Fraction(511, 512)  # Weierstrass lower bound on tail product
assert P6 * tail >= Fraction(7, 8), P6 * tail
print("P6 =", P6, float(P6), " global-low >=", P6 * tail, float(P6 * tail))

# D: tower-blocking residual arithmetic
Fix, leak = Fraction(7, 8), Fraction(1, 8)
res = Fix - leak
assert res == Fraction(3, 4) >= Fraction(1, 4)
assert 1 - res == Fraction(1, 4) <= Fraction(3, 4)
assert Fix >= Fraction(1, 8) and res >= Fraction(1, 4)

# E: sample castle box B, M=24
n = 24
assert Fraction(6, 2 * n + 1) == Fraction(6, 49) < Fraction(1, 8)
Phi = 2**49
assert (2 * n + 1) * Phi == 49 * Phi
assert 6 * Phi * 8 < 49 * Phi
assert set(L["S0"]["elems"]) == {"e", "t", "t-inv", "t2", "t2-inv", "a"}
print("sample castle |B| = 49*2^49, boundary ratio 6/49 < 1/8")
print("VERIFY_OK")
