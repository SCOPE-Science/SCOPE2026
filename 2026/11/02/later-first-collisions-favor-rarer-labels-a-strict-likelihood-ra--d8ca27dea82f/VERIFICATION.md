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

# Verification

The finite verifier `verify.py` is standalone Python 3 with no third-party dependencies. It checks the theorem against a second implementation that enumerates the ordered, mutually distinct prefixes prior to the first repetition, rather than relying on elementary-symmetric coefficients. It also verifies all consecutive pairwise likelihood-ratio cross-products, ties, normalization, conditional mean monotonicity, and exact covariance inequalities.

Packaged execution: `PASS: 2,235 exact rational assertions across 25 probability vectors, with independent prefix enumeration.`

These are finite tests, not proof of the universal statements. The all-size proof reduces to elementary first-repeat event counting, strict Newton inequalities for positive elementary symmetric polynomials, and the finite-support likelihood-ratio ordering implication. Historical priority remains qualified because not all older possible sources were fully accessible.
