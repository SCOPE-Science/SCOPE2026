#!/usr/bin/env python3
"""Lane-247: exhaustive binary cyclic b-symbol (b=2) census, 3<=n<=15.

For each n: enumerate all monic g | x^n+1 over GF(2) (each = one cyclic code),
tally b-symbol weight over all 2^k codewords with DUAL tally
(tuple-window vs bitwise c|rotl(c)), compute full spectrum, d_2,
Luo b-symbol Griesmer value d_G(n,k) and Singleton value d_S=n-k+2 + gaps.
Record-max per length (tie-break: larger k, then smaller generator int).
Also spot-check Family A at n=31 (Hamming (31,5) code -> (31,5,24)^2_2).
Stdlib only. Writes output/artifacts/*.csv/.json + prints summary.
"""
import json, csv, os

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-247/output/artifacts"
os.makedirs(OUT, exist_ok=True)

def deg(p): return p.bit_length() - 1
def polymod(a, b):
    db = deg(b)
    while a.bit_length() - 1 >= db:
        a ^= b << (a.bit_length() - 1 - db)
    return a
def polymul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r
def popcount(x): return bin(x).count("1")
def rotl(c, n):
    return ((c << 1) | (c >> (n - 1))) & ((1 << n) - 1) if n > 1 else c & 1

def wt2_tuple(c, n):
    # windows (c_i, c_{i+1}), i=0..n-1 cyclic, c_0 = LSB
    w = 0
    for i in range(n):
        a = (c >> i) & 1; b = (c >> ((i + 1) % n)) & 1
        if a or b: w += 1
    return w
def wt2_bits(c, n):
    return popcount(c | rotl(c, n))

def monic_divisors(n):
    xn1 = (1 << n) | 1
    out = []
    for g in range(1, 1 << (n + 1)):
        if not (g & 1): continue            # constant term must be 1
        if not (g >> deg(g)) & 1: continue  # monic by construction
        if polymod(xn1, g) == 0:
            out.append(g)
    return sorted(out)

def griesmer_val(n, k):
    # max d in [0,n] with sum_{i<k} ceil(2d/2^i) <= 3n
    best = 0
    for d in range(n + 1):
        s = 0
        for i in range(k):
            num = 2 * d; den = 1 << i
            s += (num + den - 1) // den
            if s > 3 * n: break
        if s <= 3 * n: best = d
    return best

def famA(n, k, d):
    t = k
    return t >= 2 and n == (1 << t) - 1 and d == 3 * (1 << (t - 2))
def famB(n, k, d):
    t = k - 1
    return t >= 2 and n == (1 << t) - 1 and d == 3 * (1 << (t - 2)) - 1

rows = []       # every cyclic code
per_n_best = {} # n -> row dict of record
dual_checks = 0
for n in range(3, 16):
    best = None
    for g in monic_divisors(n):
        k = n - deg(g)
        if k < 1:
            continue  # skip g=x^n+1 (zero code)
        spec = [0] * (n + 1)
        dh = n + 1
        for m in range(1 << k):
            c = polymul(m, g)  # deg <= n-1, no reduction needed
            assert c < (1 << n), (n, hex(g), hex(c))
            w1 = wt2_tuple(c, n); w2 = wt2_bits(c, n)
            assert w1 == w2, (n, hex(g), hex(c), w1, w2)
            dual_checks += 1
            spec[w1] += 1
            if c:
                h = popcount(c)
                if h < dh: dh = h
        d2 = next(i for i in range(n + 1) if spec[i] > 0 and (i > 0 or spec[0] == 1 and i == 0 and False) ) if False else None
        # min over nonzero codewords: smallest i>0 with count>0 (spec[0] counts only zero word)
        assert spec[0] == 1
        d2 = next(i for i in range(1, n + 1) if spec[i] > 0)
        dG = griesmer_val(n, k); dS = n - k + 2
        row = {"n": n, "k": k, "gen": hex(g), "gen_int": g, "dH": dh,
               "d2": d2, "spectrum": spec, "dG": dG, "gapG": dG - d2,
               "dS": dS, "gapS": dS - d2,
               "meetsG": d2 == dG, "inFamA": famA(n, k, d2), "inFamB": famB(n, k, d2)}
        rows.append(row)
        key = (d2, k, -g)
        if best is None or (d2, k, -g) > (best["d2"], best["k"], -best["gen_int"]):
            best = row
    per_n_best[n] = best

# spot check Family A at n=31: primitive Hamming (31,5) code
n31 = 31
divs31 = monic_divisors(n31)
# find degree-26 divisor (k=5) that yields dH=7: test each k=5 code's Hamming distance
famA31 = None
for g in divs31:
    if n31 - deg(g) != 5: continue
    dh = n31 + 1; spec = [0]*(n31+1); ok = True
    for m in range(1 << 5):
        c = polymul(m, g)
        w1 = wt2_tuple(c, n31); w2 = wt2_bits(c, n31)
        if w1 != w2: ok = False; break
        spec[w1] += 1
        if c and popcount(c) < dh: dh = popcount(c)
    if not ok: continue
    d2 = next(i for i in range(1, n31+1) if spec[i] > 0)
    if dh == 7:
        famA31 = {"gen": hex(g), "dH": dh, "d2": d2, "dG": griesmer_val(n31,5),
                  "spectrum": spec}
        break

print(f"total codes surveyed n=3..15: {len(rows)}; dual-tally checks: {dual_checks}")
print("n : (#codes) best(d2,k,gen,dH,dG,gapG,dS,gapS,meetsG,inA,inB)")
for n in range(3, 16):
    b = per_n_best[n]
    nc = sum(1 for r in rows if r["n"] == n)
    print(f"{n:3d} : ({nc:3d}) d2={b['d2']:2d} k={b['k']:2d} g={b['gen']:>6s} "
          f"dH={b['dH']:2d} dG={b['dG']:2d} gapG={b['gapG']} dS={b['dS']:2d} gapS={b['gapS']} "
          f"meets={int(b['meetsG'])} A={int(b['inFamA'])} B={int(b['inFamB'])}")
print("nontrivial (k>=2) Griesmer-meeting codes n=3..15:")
found_any = False
for r in rows:
    if r["k"] >= 2 and r["meetsG"]:
        print(f"  n={r['n']} k={r['k']} g={r['gen']} d2={r['d2']} A={int(r['inFamA'])} B={int(r['inFamB'])}")
        found_any = True
if not found_any: print("  NONE")
print("Family A spot check n=31:", famA31["gen"] if famA31 else None,
      ("dH=%d d2=%d dG=%d" % (famA31["dH"], famA31["d2"], famA31["dG"])) if famA31 else "")

# write artifacts
with open(f"{OUT}/census_all.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["n","k","gen_hex","dH","d2","dG","gapG","dS","gapS","meetsG","inFamA","inFamB","spectrum"])
    for r in rows:
        w.writerow([r["n"],r["k"],r["gen"],r["dH"],r["d2"],r["dG"],r["gapG"],r["dS"],r["gapS"],
                    int(r["meetsG"]),int(r["inFamA"]),int(r["inFamB"]),"|".join(map(str,r["spectrum"]))])
best_out = {str(n): {kk: per_n_best[n][kk] for kk in
          ("n","k","gen","dH","d2","spectrum","dG","gapG","dS","gapS","meetsG","inFamA","inFamB")}
          for n in per_n_best}
with open(f"{OUT}/best_per_length.json", "w") as f:
    json.dump({"b": 2, "q": 2, "scope": "all binary cyclic codes, 3<=n<=15, exhaustive",
               "dual_tally_checks": dual_checks, "records": best_out,
               "familyA_spotcheck_n31": ({kk: famA31[kk] for kk in ("gen","dH","d2","dG")} if famA31 else None)},
              f, indent=1)
print("artifacts written.")
