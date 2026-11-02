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
# Reproducibility and limits

The included `verify.py` requires `mpmath >= 1.3` (`requirements.txt`) and is run with `python verify.py`. It evaluates the exact scaled log-moment-generating-function series at four tilt values as reset fractions shrink, differentiates the limiting dilogarithm, numerically solves the Legendre stationary equation, checks rate-function symmetry and strict positivity at seven positive displacements, checks the sixth-order coefficient, and checks the linear distant tail. It passed **41 finite assertions** on the prepared package.

All universal assertions—including convergence as the reset fraction vanishes, the full large-deviation principle, and strict comparison at every nonzero real displacement—are proved analytically in `RESULT.md`. A finite arithmetic test is not an asymptotic or universal certificate. For an independent re-derivation, start with the Brownian convolution and the independent exponential holding times, then recompute the cumulant-limit Riemann sum, verify the exponential-tilt LDP, and inspect the positive function \(G(z)=z^2-2z+2(1-e^{-z})\) used for strict ordering.

No independent audit has been performed. The publication-priority assessment is qualified by the possibility of a more general unpublished or unlocated large-deviation result.
