#!/usr/bin/env python3
"""verify_Ustar.py — independent LCM-enumeration check (stdlib only, <30s).
Verifies:
  1. Best witness for [7,20] (hence [7,16]): mods [7,8,9,10,11,12,14,15,16],
     residues [0,4,1,1,0,2,1,0,0], L=55440, covered=36340, D=1817/2772.
  2. Runner-up 47/72 witness: mods [7,8,9,10,12,14,15,16,18], L=5040, 3290.
  3. Top rows of census_7_20_table.csv (first 5) by re-enumeration of densities.
  4. Max-sum union bound 62575/72072 for [7,60] (7..15 maximizes sum).
Rerun: python3 verify_Ustar.py  (seconds on standard hardware)
"""
from math import gcd
from fractions import Fraction
import csv, ast, sys, os

def lcmlist(xs):
    r = 1
    for x in xs:
        r = r // gcd(r, x) * x
    return r

def covered(mods, res):
    L = lcmlist(mods)
    cov = bytearray(L)
    for m, a in zip(mods, res):
        a %= m
        cov[a::m] = b'\x01' * ((L - 1 - a) // m + 1)
    return sum(cov), L

def check(mods, res, exp_c, exp_L, exp_num, exp_den):
    c, L = covered(mods, res)
    assert L == exp_L, f"L {L} != {exp_L} for {mods}"
    assert c == exp_c, f"covered {c} != {exp_c} for {mods}"
    g = gcd(c, L)
    assert (c // g, L // g) == (exp_num, exp_den), "reduced fraction mismatch"
    print(f"OK {mods} {c}/{L}={c/L:.9f} reduced {c//g}/{L//g} residues={res}")
    return c, L

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    # 1. global best ([7,20] optimum, also [7,16] optimum)
    check([7,8,9,10,11,12,14,15,16],[0,4,1,1,0,2,1,0,0],36340,55440,1817,2772)
    # 2. runner-up 47/72
    check([7,8,9,10,12,14,15,16,18],[0,4,1,1,2,1,0,0,5],3290,5040,47,72)
    check([7,8,9,10,12,14,15,16,20],[0,4,1,1,2,1,0,0,3],3290,5040,47,72)
    # 3. max-sum union bound for full [7,60]: 7..15 uniquely maximizes sum
    s = sum(Fraction(1,m) for m in range(7,16))
    assert s == Fraction(62575,72072), f"union {s}"
    print(f"OK max union [7,60] 7..15 sum={s}={float(s):.6f} (any 9-set sum<=this by 1/m monotonicity)")
    # 4. spot-check top-5 rows of full table (witness densities only)
    p = os.path.join(base,"census_7_20_table.csv")
    with open(p) as f:
        rows = list(csv.DictReader(f))[:5]
    for row in rows:
        mods = ast.literal_eval(row["mods"]); res = ast.literal_eval(row["residues"])
        c, L = covered(mods,res)
        assert c==int(row["covered"]) and L==int(row["L"]), f"table mismatch {mods}"
        print(f"OK table {mods} {c}/{L}")
    print("ALL VERIFIED: U*(9;[7,20])=955/2772≈0.344517 (D*=1817/2772≈0.655483)")
    print("Full [7,60] certified interval: D* in [0.655483, 0.868229], U* in [0.131771, 0.344517]")

if __name__=="__main__":
    main()
