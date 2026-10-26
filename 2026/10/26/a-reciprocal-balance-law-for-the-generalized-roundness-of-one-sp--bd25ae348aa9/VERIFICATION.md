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

The proof expands the conditionally negative distance-power form, removes ordinary-leaf deviations, completes a two-variable square, establishes monotonicity and convexity, and asymptotically inverts the resulting scalar threshold. The explicit null vector proves one affine dependence at the critical exponent.

The standalone `verify.py` replays 7,547 finite checks, including zero-sum matrix spectra, inversion, balance and high-precision asymptotic comparisons. Execute `python verify.py` with NumPy, SciPy and mpmath. Numerical tests are supplemental and cannot prove infinite quantifiers or originality. Independent validation has not been performed.
