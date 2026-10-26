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

The independently written standard-library checker is `artifacts/verify.py`. Execute `python artifacts/verify.py` from the artifact root. It passed **6,700 deterministic assertions**, comparing distinct convolution and autocorrelation formulas, exact integer arithmetic, random complex coefficients and explicit finite-grid Fourier averages. The symbolic difference certificate in RESULT.md is algebraically verified by substitution; the strongest equality classification comes from nonnegative terms and their zero conditions, not numerical sampling.

The exact identity behind the calculation is the probability-normalized moment equal to squared autocorrelation energy. The checker examines finite samples; no sample establishes the claimed theorem for infinitely many coefficients or grids. The mathematical proof and boundary cases are fully stated in RESULT.md. No independent scientific audit or third-party validation has been performed. Bibliographic-priority uncertainty is disclosed in REVIEW.md and AUDIT.json.
