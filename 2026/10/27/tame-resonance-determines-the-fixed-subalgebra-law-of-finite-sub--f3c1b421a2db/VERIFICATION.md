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
# Verification and reproducibility

Run `python3 checker.py` from this package. It needs only the Python 3 standard library. For each of ten configurations, it creates an explicit finite field (including extensions of degrees two), directly forms the coefficient matrix of substitution on the truncated polynomial basis, and uses Gaussian elimination over that field to compute the fixed-space dimension of every possible automorphism with the specified linear multiplier. The observed frequencies are compared with the exact predicted integers; the script raises an assertion on disagreement.

The checker also checks monomial-tail fixed bases of canonical normal-form representatives of every possible resonance order. A separate characteristic-two boundary instance with \(m>p\) demonstrates the theorem cannot be extended verbatim. Successful output ends with `ALL_TAME_FIXED_ALGEBRA_TESTS_PASSED 10 38674`.

Finite enumeration is not a proof of a general law; the separate mathematical proof uses triangular normalization and a leading-term argument. No verification of arbitrary characteristic beyond the stated range is claimed.
