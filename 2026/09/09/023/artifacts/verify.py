"""Self-contained independent verifier: replays the census from committed files.

Usage (from the lane directory containing output/ and work/, OR from anywhere
with --artifacts pointing at the artifacts dir):
    python3 output/artifacts/verify.py
    python3 output/artifacts/verify.py --artifacts output/artifacts

Reads ONLY committed files inside the artifacts dir:
  census_table.csv, katlas_source.json, knotlib.py
(no work/ imports, no network). Checks:
  V1: every census_table.csv row recomputes from the committed PD:
      trace -> signs/writhe/ncomp -> bracket -> Jones, span/deficit,
      positional all-A/all-B circles, single-flip adequacy, g_T formula.
  V2: recomputed Jones equals the committed KnotAtlas reference value
      (801/801 exact coefficient matches).
  V3: ncomp == 1 on every row; traced signs == independent local
      consecutive-edge rule on every row.
  V4: extremal: max deficit unique at K11n19 = 7; runners-up K11n57 (6), 10_132 (5).
  V5: theorem tripwires: span<=c; deficit<=1 iff adequate; deficit-1 => gT 1;
      all 367 K11a alternating diagrams deficit-0/adequate/gT-0.
"""
import argparse
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifacts", default=HERE)
    a = ap.parse_args()
    sys.path.insert(0, a.artifacts)
    import knotlib as K

    src = json.load(open(os.path.join(a.artifacts, "katlas_source.json")))
    rows = list(csv.DictReader(open(os.path.join(a.artifacts, "census_table.csv"))))
    assert len(rows) == 801, len(rows)
    bad = 0
    for row in rows:
        nm = row["knot"]
        S = src[nm]
        pd = K.parse_pd(S["pd"])
        ref = K.parse_jones(S["jones"])
        dt = K.parse_dt(S["dt"])
        D = K.Diagram(pd)
        j = D.jones()
        if j != ref:
            print(f"FAIL {nm}: jones mismatch vs reference"); bad += 1
        if D.ncomp != 1:
            print(f"FAIL {nm}: ncomp={D.ncomp}"); bad += 1
        if K.local_rule_signs(pd) != D.signs:
            print(f"FAIL {nm}: traced signs != local-rule signs"); bad += 1
        st = D.state_data()
        lo, hi = min(j), max(j)
        span, defi = hi - lo, len(dt) - (hi - lo)
        checks = [
            ("c", D.c, int(row["c"])),
            ("span", span, int(row["span"])),
            ("deficit", defi, int(row["deficit"])),
            ("sA", st["sA"], int(row["sA"])),
            ("sB", st["sB"], int(row["sB"])),
            ("A", int(st["A_adequate"]), int(row["A_adequate"])),
            ("B", int(st["B_adequate"]), int(row["B_adequate"])),
            ("adequate", int(st["adequate"]), int(row["adequate"])),
            ("gT", st["gT"], int(row["gT"])),
            ("writhe", D.writhe, int(row["writhe"])),
            ("ncomp", D.ncomp, int(row["ncomp"])),
            ("jones_match", 1, int(row["jones_match"])),
        ]
        for name, x, y in checks:
            if x != y:
                print(f"FAIL {nm}.{name}: recomputed={x} table={y}"); bad += 1
        if span > D.c:
            print(f"FAIL {nm}: span>c"); bad += 1
    by_def = sorted(rows, key=lambda r: -int(r["deficit"]))
    top = by_def[0]
    assert top["knot"] == "K11n19" and int(top["deficit"]) == 7, (top["knot"], top["deficit"])
    assert sum(1 for r in rows if int(r["deficit"]) == 7) == 1, "D* not unique"
    ru = sorted(((r["knot"], int(r["deficit"])) for r in rows), key=lambda t: -t[1])[1:3]
    assert ru == [("K11n57", 6), ("10_132", 5)], ru
    for r in rows:
        adeq, d = int(r["adequate"]), int(r["deficit"])
        if (d <= 1) != (adeq == 1):
            print(f"FAIL structure {r['knot']}: deficit={d} adequate={adeq}"); bad += 1
        if d >= 2 and adeq != 0:
            print(f"FAIL structure {r['knot']}: deficit={d} adequate={adeq}"); bad += 1
        if d == 1 and int(r["gT"]) != 1:
            print(f"FAIL def1 {r['knot']}"); bad += 1
    alt = [r for r in rows if r["knot"].startswith("K11a")]
    assert len(alt) == 367, len(alt)
    assert all(int(r["deficit"]) == 0 and int(r["adequate"]) == 1 and int(r["gT"]) == 0 for r in alt), "K11a tripwire"
    if bad:
        print(f"VERIFY_FAIL ({bad})")
        sys.exit(1)
    print("VERIFY_OK: 801/801 rows replay from committed files; Jones==reference on all; "
          "ncomp==1 and signs==local-rule on all; D*=7 unique at K11n19 "
          "(runners-up K11n57=6, 10_132=5); deficit<=1 iff adequate; "
          "deficit-1 => gT=1; K11a tripwire; span<=c everywhere.")


if __name__ == "__main__":
    main()
