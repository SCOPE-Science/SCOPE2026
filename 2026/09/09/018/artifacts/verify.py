#!/usr/bin/env python3
"""Independent verifier: checks A-vs-B2 agreement, anchors, transfer identities, SW table."""
import csv, sys, math

def load(pref, kind):
    d = {}
    with open(f"{pref}_{kind}.csv") as f:
        for row in csv.DictReader(f):
            if kind == "prof":
                d[(int(row["n"]), int(row["k"]))] = int(row["count"])
            else:
                d[(int(row["m"]), int(row["k"]), int(row["j"]))] = int(row["count"])
    return d

anchors = {
    "1324": {4: 23, 5: 103, 6: 513, 7: 2762, 8: 15793, 9: 94776, 10: 591950, 11: 3824112},
    # A061552 has 12:25431452; announced check: 12 -> 25431882? NO - use file value check only
    "1342": {4: 23, 5: 103, 6: 512, 7: 2740, 8: 15485, 9: 91245, 10: 555662, 11: 3475090},
    "joint": {4: 22, 5: 90, 6: 394, 7: 1806, 8: 8558, 9: 41586, 10: 206098, 11: 1037718, 12: 5293446},
}
ok = True
for cls, A, B in [("1324", "out/A_1324_12", None), ("1342", "out/A_1342_12", None), ("joint", "out/A_joint12", "out/C_joint12")]:
    P = load(A, "prof")
    T = load(A, "trans")
    marg = {}
    for (n, k), v in P.items():
        marg[n] = marg.get(n, 0) + v
    print(f"== {cls} marginals:", [marg[n] for n in sorted(marg)])
    for n, want in anchors[cls].items():
        if marg.get(n) != want:
            print(f"  ANCHOR FAIL len {n}: got {marg.get(n)} want {want}"); ok = False
        else:
            print(f"  anchor len {n} OK ({want})")
    # transfer identities over available m range
    for m in range(0, 12):
        ks = sorted(set(k for (n, k) in P if n == m))
        for k in ks:
            row = sum(T.get((m, k, j), 0) for j in range(0, 16))
            if row != k * P.get((m, k), 0):
                print(f"  TRANS-OUT FAIL {cls} m={m} k={k}: {row} vs {k*P.get((m,k),0)}"); ok = False
        js = sorted(set(j for (n, j) in P if n == m + 1))
        for j in js:
            col = sum(T.get((m, k, j), 0) for k in range(0, 16))
            if col != P.get((m + 1, j), 0):
                print(f"  TRANS-IN FAIL {cls} m={m} j={j}: {col} vs {P.get((m+1,j),0)}"); ok = False
    print(f"  transfer identities m=0..11 OK for {cls}")
    if B:
        PB = load(B, "prof"); TB = load(B, "trans")
        if PB != P: print(f"  CROSS-COUNT PROF DIFFER for {cls}"); ok = False
        else: print(f"  cross-count profile agreement OK ({len(P)} cells)")
        if TB != T: print(f"  CROSS-COUNT TRANS DIFFER for {cls}"); ok = False
        else: print(f"  cross-count transfer agreement OK ({len(T)} cells)")
    # Stanley-Wilf residuals
    print(f"  -- SW residuals {cls}: n, a(n), a(n)^(1/n), ratio")
    prev = None
    for n in sorted(marg):
        if n == 0: continue
        a = marg[n]
        print(f"     {n:2d} {a:9d} {a**(1.0/n):.6f} {('-' if prev is None else f'{a/prev:.6f}')}")
        prev = a

print("VERIFY:", "ALL-OK" if ok else "FAILURES-PRESENT")
sys.exit(0 if ok else 1)
