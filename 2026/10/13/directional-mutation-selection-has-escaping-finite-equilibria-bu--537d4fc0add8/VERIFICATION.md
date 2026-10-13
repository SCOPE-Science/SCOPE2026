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
# Verification notes

The complete theorem and its proof are in `RESULT.md`; this section records reproducibility checks rather than an independent certification.

The bundled `verifier.py` was executed from the package source directory with Python, NumPy, and SciPy and produced `VERIFY_OK`. It computes the exact \(p_k\) recurrence with rational arithmetic and checks five finite symmetric Perron problems for the logistic mortality profile, their positive equilibrium residuals, and the stated one-sided mass bound. Negative numerical rounding at the smallest components is clipped in the illustrative test only; exact Perron positivity follows from strictly positive finite matrices. The mathematical infinity claims follow from summation, discrete-Laplace Green identity, half-line concavity, and Rayleigh test-block estimates, not from finite tests.

Mathematical limits: every claim is restricted to the stated discrete-Laplace mutation kernel, bounded strictly-above-limit mortality, and unrenormalized absorbing-boundary trait truncations. No stochastic simulation, dynamic convergence, infinite-time drift rate, or general mutation-kernel extension was established. Originality comparison with the complete 1996 Bürger–Bomze manuscript was unavailable; only its bibliographic abstract and related context were examined.
