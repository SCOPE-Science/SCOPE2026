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

The standalone `verify.py` was executed with Python 3 and SymPy and completed all assertions. It checks the two boundary-sensitive signed transition identities, stationary moments, the Poisson equation, the all-lag covariance coefficients, the rational long-run variance, exact finite-time covariance summations for four parameters and five time horizons, and the limiting divergence coefficient. It uses no cached numerical result and imports no nonstandard code beyond SymPy.

The proof of the chain coding requires the uniform-on-dyadic-cell property under conditioning on the observed depth history; this follows from the affine maps on binary cylinders and is stated explicitly in `RESULT.md`. The central limit theorem uses the stationary countable-state martingale approximation, not a finite-state truncation. The simultaneous \(q\to0\), \(N\to\infty\) limit is an exact geometric Riemann-sum argument, not an extrapolation from numerical experiments.

The original 2021 paper's full text was inaccessible; the author's 2023 thesis supplies the precise defining maps and invariant density. Independent scholarly validation has not been performed.
