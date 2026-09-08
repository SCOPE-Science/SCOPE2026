#!/usr/bin/env python3
"""Lane-247 independent verifier (different code path from census.py).

1. Re-tallies headline cyclic codes with a string-based b-symbol weight,
   recomputes Hamming distance, spectrum, Luo Griesmer value, Singleton value,
   family-A/B membership from scratch.
2. Constructs Family-A reference (31,5,24)^2_2 directly from primitive
   polynomial h=x^5+x^2+1 via g=(x^31+1)/h (no divisor enumeration),
   confirming the bound implementation is tight on known ground truth.
Stdlib only.
"""
import json

def gf2_mod(a, b):
    db = a.bit_length() - 1 - (b.bit_length() - 1)
    # generic long division
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a
def gf2_mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r
def gf2_divmod(a, b):
    q = 0
    while a.bit_length() >= b.bit_length():
        s = a.bit_length() - b.bit_length()
        q ^= 1 << s; a ^= b << s
    return q, a

def codewords(n, g):
    k = n - (g.bit_length() - 1)
    out = []
    for m in range(1 << k):
        out.append(gf2_mul(m, g))
    return out

def wt2_str(c, n):
    bits = [(c >> i) & 1 for i in range(n)]  # bits[i] = c_i
    w = 0
    for i in range(n):
        if bits[i] or bits[(i + 1) % n]: w += 1
    return w

def spec_of(n, g):
    spec = [0] * (n + 1); dh = n + 1
    for c in codewords(n, g):
        assert c < (1 << n), (n, hex(g), hex(c))
        w = wt2_str(c, n); spec[w] += 1
        if c:
            h = bin(c).count("1")
            if h < dh: dh = h
    assert spec[0] == 1
    d2 = next(i for i in range(1, n + 1) if spec[i] > 0)
    return spec, dh, d2

def gval(n, k):
    best = 0
    for d in range(n + 1):
        if sum((2 * d + (1 << i) - 1) // (1 << i) for i in range(k)) <= 3 * n:
            best = d
    return best

def fam(n, k, d):
    tA = k; A = tA >= 2 and n == 2**tA - 1 and d == 3 * 2**(tA - 2)
    tB = k - 1; B = tB >= 2 and n == 2**tB - 1 and d == 3 * 2**(tB - 2) - 1
    return A, B

heads = [(8, 0x33), (12, 0xbd), (14, 0xb97), (4, 0x5), (6, 0x15)]
res = []
for n, g in heads:
    spec, dh, d2 = spec_of(n, g)
    k = n - (g.bit_length() - 1)
    dG = gval(n, k); dS = n - k + 2
    A, B = fam(n, k, d2)
    nz = sorted(set(w for w in range(1, n + 1) if spec[w]))
    res.append({"n": n, "k": k, "gen": hex(g), "dH": dh, "d2": d2,
                "dG": dG, "gapG": dG - d2, "dS": dS, "gapS": dS - d2,
                "meetsG": d2 == dG, "inFamA": A, "inFamB": B,
                "nonzero_weights": nz,
                "spectrum": spec})
    print(f"n={n} k={k} g={hex(g)} dH={dh} d2={d2} dG={dG} gapG={dG-d2} "
          f"dS={dS} gapS={dS-d2} meets={d2==dG} A={A} B={B} weights={nz}")

# Family-A ground truth: (31,5,24) from h=x^5+x^2+1
h = 0b100101
x31 = (1 << 31) | 1
g31, r = gf2_divmod(x31, h)
assert r == 0, hex(r)
spec31, dh31, d231 = spec_of(31, g31)
dG31 = gval(31, 5)
print(f"FamA n=31 k=5 g=hex({hex(g31)[:10]}...) dH={dh31} d2={d231} dG={dG31} "
      f"gap={dG31-d231} A={fam(31,5,d231)}")
assert dh31 == 16 and d231 == 24 and dG31 == 24

with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-247/output/artifacts/verify.json", "w") as f:
    json.dump({"headlines": res,
               "familyA_ref": {"n": 31, "k": 5, "dH": dh31, "d2": d231, "dG": dG31,
                               "gen_hex": hex(g31), "spectrum": spec31}}, f, indent=1)
print("VERIFY_OK")
