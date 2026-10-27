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

The analytical proof in RESULT.md establishes the theorem for every permitted real symmetric positive-definite matrix and non-eigenvector initial state. The finite checker is a reproducibility aid, not an exhaustive verification of those quantifiers.

Run `python3 check_first_block.py` with NumPy and SymPy installed. It checks the exact symbolic covariance, variance, three-mode correlation and strict-gap identities; tests the critical limit; compares six explicit three-mode cases with direct projections; and verifies the universal bound and normalized Gram singular-value condition number in a seeded collection of 324 full-rank random examples. The successful recorded stdout is:

`PASS symbolic identities and 324 random full-rank Gram conditioning tests, six explicit sharpness checks`

The starting vector is normalized and the projection is Euclidean. The three-mode limit with vanishing outer-coordinate weights is not a finite attained extremum. Very small outer weights may lead to numerical cancellation and are not used as infinite-proof evidence. No independent external audit has been performed.
