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

# Verification and reproducibility

The theorem follows analytically from the coherent-state integral formula, separated rank-two spectral projection, exact second-order cluster perturbation and a monotone positive Poisson-weight-ratio identity. The trace-class Taylor remainder controls all infinite-dimensional transitions. The supplied `check_two_mode.py` independently evaluates truncated matrices by regularized incomplete-gamma radial integration and discrete angular quadrature. At squared radii \(0.5,1,3\) it checks pure modes \(1,2,3,5\), mixed modes \(2,3\), exact quadrupole coefficient and finite monotonicity. It completed successfully with 24 assertions. The finite tests are not exhaustive and do not certify the infinite-dimensional proof.

Run with `python check_two_mode.py` after installing NumPy and SciPy. Only numerical tolerances printed in that file apply to numerical checks. No external audit, expert review, or independent verification is claimed.
