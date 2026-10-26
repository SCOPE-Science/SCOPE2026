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

Run `python verify.py` using NumPy and SciPy. The code builds the three-site exponential product, independently computes a real matrix logarithm, checks the exact-mean identity, and checks the long-range coupling's sign relative to the variance midpoint for 132 combinations. Six additional special cases compare the closed hyperbolic-sine expression.

The analytic proof uses only the Gaussian moment-generating formula, the logarithmic resolvent identity, nonnegative exponential-series comparison, and a reciprocal integral substitution. It does not depend on floating-point computation. Higher weak moments, non-diagonal diffusion, and other integrator families have not been verified.
