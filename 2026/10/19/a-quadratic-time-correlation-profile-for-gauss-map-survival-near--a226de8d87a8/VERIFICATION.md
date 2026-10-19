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

Run `python verify.py` with Python 3 and `mpmath`. The executable checks 507 exact rational cylinder formulas, nine high-precision transfer/digamma comparisons, 81 residual comparisons against an analytic bound, nine zeta-tail asymptotic checks, nine positivity checks, and four quadratic-time scaling diagnostics, totaling **619 passed**. These are finite arithmetic consistency tests and do not certify the universal quantifiers or the originality assessment.

The mathematical proof requires exact inverse branches, positivity under iteration, uniform Taylor-remainder bounds and the first two Hurwitz-zeta asymptotic terms. At irrational boundary points, finite cylinders partition up to a countable set of zero measure. The statement does not require an externally certified spectral eigenpair, an infinite computation, or numerical convergence from a finite sample.

The numerical checks operate on the actual standalone executable in this package; no external state or saved output is a proof dependency.
