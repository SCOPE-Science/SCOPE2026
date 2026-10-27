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

# Reproducibility and checks

Execute `python verify.py` using Python 3, NumPy and SciPy. The code uses `scipy.special.kv`, `kve`, `iv` and Gamma functions, adaptive quadrature, and a bracketed scalar-root solver. Seven triples of positive sluggishness, reset rate and displaced reset point were tested, with **112 numerical assertions** passing. Both sides of the sharp right-peak pinning boundary were sampled. Numerically integrated stationary mass sums to one, the left-side mass agrees with the proposed first-passage transform, each weak stationarity residual is within tolerance, and the reset source has the correct derivative jump.

The published all-parameter proof is analytic: Bessel ODE, resolvent Wronskian and jump, monotone auxiliary energy, and integration of the backward hitting equation. Finite numerical checks are corroboration, not a proof for all parameters. The branch convention at the singular origin is the nonsticky natural-scale diffusion. The coupled problem is not claimed to have been independently audited.
