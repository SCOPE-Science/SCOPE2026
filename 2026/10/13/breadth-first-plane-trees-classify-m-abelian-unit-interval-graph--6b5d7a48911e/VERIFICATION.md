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

Run `python3 verify.py` next to this file with standard Python 3.8 or later; it requires no external data, package installations, or internet connection. The saved deterministic transcript is `verification_output.txt`.

The source iterates every nondecreasing legal parent sequence at orders \(1\) through \(9\), constructs the adjacency sets, enumerates independent vertex subsets, independently determines the fewest consecutive clique blocks, checks breadth-first reconstruction, and compares height distributions with an independently computed Dyck-walk dynamic program. It verifies the exact rational generating-function coefficient recursions and the special-case formulas. All tested equalities hold.

All 6,917 tested ordered-area-sequence objects are finite evidence. The all-orders theorem requires and is supported by the proof in RESULT.md. No test here establishes publication priority, equivalence to every possible historical formulation, or an external audit.
