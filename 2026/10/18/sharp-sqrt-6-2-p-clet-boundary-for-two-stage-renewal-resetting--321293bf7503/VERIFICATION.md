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

# Verification of the Erlang-two drift-search classification

The standalone source `verify.py` checks the exact derivative identity, exponential-series coefficient formulae, the polynomial all-index identity, the ordered positive-root intervals and the critical expansion using SymPy. Independent quadrature of the inverse-Gaussian first-passage density and survival probability verifies the renewal mean formula across a grid of positive drift and clock rates and includes the zero-drift numerical limit. The program also compares analytically bracketed optimal rates and the positive-drift monotonic regime with direct formula values, using high precision for the derivative root. All 71 assertions passed when executed with Python, SymPy, SciPy, numpy and mpmath.

Run `python verify.py` from the directory containing the embedded script. The mathematical proof of root uniqueness for all positive parameters is the complete coefficient-sign argument in `RESULT.md`; finite sampled comparisons do not certify untested parameters and are not used in place of that proof.

Source-comparison limitations: the primary papers' mathematical content was read and compared, but a publication-priority determination by an independent scholar has not been performed. No claim of independently audited verification is made.
