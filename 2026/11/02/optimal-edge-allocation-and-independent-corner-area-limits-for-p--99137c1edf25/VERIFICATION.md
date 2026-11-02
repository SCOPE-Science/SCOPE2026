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

# Verification record

The mathematical proof is in `RESULT.md`; `verify.py` is an optional finite reproducibility test. It uses only the standard Python library. Execute `python verify.py` in the directory containing the extracted files. A successful execution reports `GEOMETRIC_IDENTITY_PASSED`, `EXACT_MIXED_MOMENTS_PASSED`, `OPTIMIZATION_AND_PARITY_TESTS_PASSED`, `LIMITING_MEAN_VARIANCE_PASSED`, then `ALL_CHECKS_PASSED`.

The main geometric identity is checked against directly computed convex hulls of points sampled on each polygon edge, including an irregular quadrilateral. The finite joint endpoint moment is cross-checked against a separately expanded binomial polynomial. A nonparallelogram admits an explicitly constructed improving edge-weight perturbation, and sample exponential products have empirical mean and variance consistent with the theorem's exact parameters.

These numerical tests verify representative instances and identities; they are not proofs of statements for every polygon or every sample size. The analytic proof establishes the unrestricted fixed-polygon claims. The approximation formula's exceptional-edge error is bounded rather than asserted to vanish for each finite sample. Independent mathematical audit has not been performed.
