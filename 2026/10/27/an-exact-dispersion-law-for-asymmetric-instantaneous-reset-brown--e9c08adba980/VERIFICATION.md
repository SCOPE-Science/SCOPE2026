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

# Computational verification

Run `python check.py` with NumPy and SciPy to reproduce **44 deterministic assertions**. The checker evaluates Gaussian Brownian step tails at fixed excursion durations, then independently integrates over exponential waiting times to recover step mean, step second moment, step-duration moment, drift and dispersion. It checks derivative sign changes at numerical roots of the optimal-current equation and the small/large-rate diffusion limits for representative parameter selections. The computations assume conventional floating-point quadrature and are not machine-verified proofs. The general proof, quantifiers, and sharp inequality arguments are given in `RESULT.md`.

There has been no independent audit or validation.
