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

Run `python verify.py` with Python 3.9 or later; no third-party packages are needed. The program directly computes the integer recurrence, exhaustively tests the **original shortest-path definition** for every subset of the binary three-cube and of the mixed 2-by-2-by-3 Hamming graph, and compares it with the derived coefficients. Independently, it builds the Hamming-distance-two conflict graph and computes its complete independent-set polynomial by recursive branch counting for dimension triples (2,2,2), (2,2,3), (2,3,3), (3,3,3), (3,3,4). It also checks the first two extreme-regime formulas at multiple larger parameters and the tied four-label boundary formula.

Actual execution completed successfully with final marker `VERIFY_OK`. It printed `ORIGINAL_GEODESICS_OK`, `DISTANCE_TWO_INDEPENDENT_SETS_OK`, `GEODESIC_EQUIVALENCE_OK`, and `EXTREMAL_COUNTS_OK` for the indicated cases. Exhaustion is **only** for those finite cases. The all-integer identities, disjoint-support bijection, and maximum-set classifications for arbitrary dimensions are supported by the written proof in `RESULT.md`, not inferred from finite computation. This package does not contain independent human validation.
