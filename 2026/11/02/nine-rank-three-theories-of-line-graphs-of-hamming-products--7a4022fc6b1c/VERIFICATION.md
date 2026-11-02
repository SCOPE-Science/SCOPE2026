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
# Reproduction and limits

Run `python3 check_line_hamming_orbits.py` and `python3 check_line_hamming_literal.py` in an environment with Python 3 and only its standard library. The first creates the literal Hamming-edge incidence sets and evaluates rank-three edge-adjacency extension spectra on 234 parameter tuples in dimensions one through five, comparing all tuples to nine predictions and testing that the predicted spectra differ. It uses factorwise symbol-permutation symmetry to select one original edge per coordinate axis. The second separately constructs full line-graph adjacency matrices and all atomic three-vertex diagrams, recursively derives two-point and one-point logical types, and verifies nine representative theories and ten further examples, without invoking coordinate orbits.

The two `.out` files are captured reference outputs. Successful runs print `VERIFY_OK`; this was observed for both. Programs provide finite corroboration only. The infinite classification uses the mathematical proof in `RESULT.md`. No proof assistant, independent auditor, external mathematical certification, or exhaustive literature-priority validation is asserted.
