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

# Verification of the square-gap theta-cubic law

Run `python verify.py` with Python 3, SymPy and Mpmath. The checker uses exact symbolic series algebra to verify that the cubic implicit root and the claimed entropy expansion agree through order \(t\), evaluates the Gaussian Poisson-summation identity at two positive parameters, and numerically solves the original return-length mean equation at five marker densities. It then compares the computed entropy with the algebraic cubic approximation and the truncated asymptotic expansion.

For the Gaussian input series, a finite cutoff is chosen so the omitted positive terms have individually exponentially small Gaussian tails; numerical checks are supplementary. The unrestricted stationary variational bound follows from inducing, conditional entropy, and relative entropy. The uniform exponentially small analytic error follows from Poisson summation on a fixed optimizer window, not from numerical sample sizes. No independent validation has been performed.
