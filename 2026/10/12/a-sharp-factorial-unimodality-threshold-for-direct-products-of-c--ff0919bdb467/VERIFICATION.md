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

# Mathematical verification

The standalone `verify.py` computes all-pairs graph distances directly from the adjacency characterization for small instances; it does **not** assume the coefficient counting classification when testing individual vertex subsets. The script exhaustively checks 139,776 candidate subsets across six graph instances, comparing their exact general-position cardinalities to the published corrected formula. It then calculates complete coefficient sequences for 747 parameter pairs inside the theorem's domain and compares the direct unimodality test to the proposed factorial threshold, including tests near the transitions. For larger factorial boundaries, it tests the decisive coefficients locally and checks boundary signs for \(a=5,6,\ldots,11\).

Run with `python verify.py` (Python standard library only). The accompanying `verification_output.txt` is the captured output from a local execution of this exact script. The theorem is established by the general algebraic inequalities in `RESULT.md`, not by finite sampling. Neither the experiments nor the source comparisons constitute independent mathematical certification or exhaustive validation of all input sizes.
