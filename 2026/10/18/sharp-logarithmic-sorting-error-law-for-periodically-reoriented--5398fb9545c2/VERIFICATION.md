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

# Reproducibility and verification

The analytic proof in `RESULT.md` supplies the full conditional-independence argument, positive-definiteness and Stratonovich normalization, exact characteristic and moment formulas, the exponential-tilting lower bound, and the wrapped-normal Laplace asymptotics. The estimates are valid for fixed positive \(z\); no result is claimed for joint limits with \(z\) or particle number varying in an unspecified manner.

Run the standalone `verify.py` with Python 3, NumPy, and SciPy. Its twelve independent Fourier–Bessel versus angular quadrature comparisons passed; three small-positive-variance rate/optimizer tests passed; and a direct Euler–Itô simulation of the original correlated three-coordinate stochastic differential equation passed the longitudinal and transverse mean/variance checks. The simulation does not use the derived one-cycle endpoint identity as its update rule.

These are corroborating finite numerical tests, not substitutes for the infinite-cycle large-deviation argument or the exact weak-diffusion asymptotics. The Gaussian angle-distribution assumption, perfect resets, positive-definite mobility, and isotropic Schur complement are explicit modeling premises. The primary source establishes the underlying drift, not the present full counting law.
