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

Run `python verify.py` in a Python environment with NumPy, SciPy, and SymPy. The checker executes symbolic matrix/angle identities, exact finite-row relations, independent special-function quadrature, and direct Gaussian simulations for planar and five-dimensional examples. It evaluates sharp beta-exponent constants for six multiplicity configurations, finite-row heavy-tail coefficients, and numerical approaches to the limiting constants. Any Monte Carlo tolerance reflects finite sampling, not a rigorous enclosure.

The exact probability identity follows by independent chi-square geometry. The asymptotic limits, moment classifications, and the tail constant are proved by beta endpoint integration, Gaussian inverse-chi moments, and dominated-convergence arguments. They are not independently certified by this script or by sampling.

Scientific limits: two-level real symmetric matrices, an independent Haar trial vector, a Gaussian sketch, exact arithmetic, and fixed eigenvalue multiplicities in the large-sketch limit. No independent audit has been performed.
