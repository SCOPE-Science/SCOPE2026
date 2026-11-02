---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify.py` with the included standalone standard-library Python program. A successful run prints `VERIFY_OK`.

The script checks every binary partial word of the relevant small lengths for first- and second-position jokers through order \(n=4\), independently counts the remaining Euler trails by edge-subset recursion through \(n=5\), checks exact integer directed Laplacian cofactors through \(n=6\), and verifies the Green-function overlap matrix by exact rational arithmetic for \(4\le n\le40\). It checks both formulas against the small enumerated values.

These are finite reproducibility tests. The all-length claim rests on the separate proof in `RESULT.md`: Euler degree balance, the directed matrix-tree theorem, the BEST last-exit formula, and the exact overlap/geometric-series evaluation of a three-edge rank update. No finite computation is presented as an infinite proof. Independent assessment has not been performed.
