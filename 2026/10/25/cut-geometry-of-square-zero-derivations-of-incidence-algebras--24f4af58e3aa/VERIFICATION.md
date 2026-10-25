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

The source `check_incidence_d2.py` is self-contained and requires Python 3.8 or later. Run `python check_incidence_d2.py`. The program generates finite poset incidence bases, computes square-zero-derivation identities from matrix-unit commutators, independently tests the order-ideal cut condition, and tests exact closed formulas for finite chains.

The test cases include chains of lengths 2–5 and the diamond and fork posets over fields of 2, 3 and 4 elements; the checker constructs extension-field arithmetic explicitly for order 4. All 15 enumerations are complete within each stated parameter case, but no finite test certifies the universal result. The characteristic-two example is a genuine exception to the odd-characteristic cut characterization, not a counterexample to the theorem as scoped.

The general theorem is justified by the structural argument in RESULT.md: derivations are inner, the square-zero equation forces scalar diagonal, and the matrix-unit coefficient equations impose the cut condition. The scheme-theoretic structure beyond the reduced locus and independent review remain unverified.
