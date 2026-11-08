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

## Verification procedure
Execute `python3 verify.py` with Python 3 standard library. The program enumerates every nonnegative count triple adding to 16 (153 triples), computes each multinomial likelihood exactly, and derives all moments of observed richness and each exact-frequency count. It compares the resulting covariance fractions against a separately implemented indicator identity. No floating-point arithmetic or heuristic tolerance occurs. It checks all sign phases, selected exact boundary values, and analogous exact calculations for two-species laws. The 16-index census is exhaustive; it is not a proof that 16 is minimal for all three-category vectors.

## Scientific limits
The analytic two-species minimal-support lemma handles all sample sizes. The three-species claim is limited to the fully verified vector and sample size. Historical priority and independent mathematical audit remain unperformed.
