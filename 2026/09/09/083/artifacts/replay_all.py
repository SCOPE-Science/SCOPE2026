#!/usr/bin/env python3
"""Master replay: runs every target-audit script and checks its token.
Stdlib only. Prints REPLAY_ALL_OK iff all pass.
"""
import subprocess, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SCRIPTS = [
    ("verify.py", "VERIFY_OK"),
    ("verify2.py", "VERIFY_OK_2"),
    ("hilbert.py", "VERIFY_OK_HILBERT"),
    ("charts.py", "VERIFY_OK_CHARTS"),
    ("discovery.py", "DISCOVERY_OK"),
    ("locals.py", "VERIFY_OK_LOCALS"),
    ("brauersum.py", "VERIFY_OK_SUM"),
    ("discriminant.py", "VERIFY_OK_DISC"),
    ("infinitude.py", "VERIFY_OK_INFINITE"),
    ("split.py", "VERIFY_OK_SPLIT"),
    ("good.py", "VERIFY_OK_GOOD"),
    ("mixed.py", "VERIFY_OK_MIXED"),
    ("nontrivial.py", "VERIFY_OK_NONTRIVIAL"),
    ("normcheck.py", "VERIFY_OK_NORMCHECK"),
    ("many.py", "VERIFY_OK_MANY"),
    ("audit_table.py", "VERIFY_OK_AUDIT"),
    ("conic_iso.py", "VERIFY_OK_CONIC"),
    ("reciprocity.py", "VERIFY_OK_RECIPROCITY"),
    ("fiber_obstructions.py", "VERIFY_OK_FIBEROB"),
    ("hasse_ok.py", "VERIFY_OK_HASSE"),
    ("e2e.py", "VERIFY_OK_E2E"),
    ("residue_fix.py", "VERIFY_OK_RESIDUE_FIX"),
    ("indep.py", "VERIFY_OK_INDEP"),
    ("reduction.py", "VERIFY_OK_REDUCTION"),
    ("relation.py", "VERIFY_OK_RELATION"),
    ("bmset.py", "VERIFY_OK_BMSET"),
    ("fallback_certificate.py", "FALLBACK_OK"),
]

def main():
    allok = True
    for name, token in SCRIPTS:
        p = subprocess.run([sys.executable, str(HERE / name)],
                           capture_output=True, text=True, timeout=120)
        out = (p.stdout or "") + (p.stderr or "")
        ok = (p.returncode == 0 and token in out)
        print(f"{name}: {'PASS' if ok else 'FAIL'} (token {token})")
        if not ok:
            print(out[-2000:])
            allok = False
    print("REPLAY_ALL_OK" if allok else "REPLAY_FAIL")
    sys.exit(0 if allok else 1)

if __name__ == "__main__":
    main()
