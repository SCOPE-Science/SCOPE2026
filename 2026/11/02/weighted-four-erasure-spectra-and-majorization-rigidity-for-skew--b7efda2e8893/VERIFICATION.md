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

# Verification and limits

A standalone source file `check_weighted_skew.py` uses only NumPy and SymPy. Execute it with `python3 check_weighted_skew.py`. It constructs the skew conference matrices for three independent prime-field parameters, exhaustively counts all four-subsets, checks exact Pfaffian identities, and independently derives the nonuniform-weight characteristic polynomials with exact symbolic arithmetic. Its success marker is `WEIGHTED_SKEW_CONFERENCE_FOUR_ERASURE_OK`.

The positive-definiteness, class ordering, weight-permutation invariance, Schur-convexity, and complete all-order assertion are analytic theorems proved in `RESULT.md`; the checker is a reproducibility aid, not an external or infinite proof certificate. Historical equivalent statements may exist beyond the sources inspected. Independent audit and validation have not been performed.
