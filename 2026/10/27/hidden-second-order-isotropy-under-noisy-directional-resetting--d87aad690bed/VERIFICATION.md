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

Run `python3 checker.py` using Python 3 standard library only. The executed stand-alone checker reported `OK; assertions: 2646`. It performs exact rational algebra for the two-angle phase polynomial and selected rational parameters, verifies Fourier coefficients by numerical exponential-last-reset-age quadrature, and checks the finite-time Green–Kubo covariance at nonzero time points along the isotropy curve.

The decisive all-parameter arguments are analytical: the stationary angular generator, exponential first Fourier-mode conditional expectation, exact integrated covariance, polynomial monotonicity, and law of total covariance for mixed reset headings. Numerical checks neither establish uniqueness outside their finite test set nor constitute an independent scholarly audit.

Model boundaries: fixed strictly positive rates, stationarity of angular law, independent equal-probability symmetric two-angle resets for the explicit phase diagram, and isotropy only of centered second moments. No scientific statement about spatial equilibrium or higher-distribution isotropy is made.
