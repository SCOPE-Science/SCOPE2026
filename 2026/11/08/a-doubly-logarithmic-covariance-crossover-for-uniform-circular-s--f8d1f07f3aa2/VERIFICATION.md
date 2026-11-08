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
# Reproducibility

The proof in `RESULT.md` is analytic and applies to all integers \(n\ge2\). The accompanying standalone `verify.py` uses exact `fractions.Fraction` calculations to compare two separately derived covariance expressions for many finite inputs. When mpmath is available, it independently integrates the Dirichlet conditional-maximum function against the beta density, including all piecewise polynomial breakpoints; the comparisons use a strict numerical tolerance of \(10^{-30}\). A further set of checks evaluates the explicit nonnegative error upper bound for the asymptotic window and its predicted signs away from the transition. Execution returned 101 passed assertions, with optional mpmath enabled.

The finite checks establish neither convergence nor uniqueness by themselves. The complete justification is the exact conditional identity, exponential tail estimate, pointwise asymptotic evaluation and convexity argument given in `RESULT.md`. The error estimate involves the event \(M_n\le t\), which is exponentially small in the stated window; no simulation is interpreted as a proof of this bound. No external audit or certification has been performed.
