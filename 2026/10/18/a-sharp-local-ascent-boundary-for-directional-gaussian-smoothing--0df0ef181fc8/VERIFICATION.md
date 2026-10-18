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

# Reproducibility and limitations

Run `python3 verify_dgs.py` using Python 3 (standard library only). It must print `PASS 63 analytic and numerical checks` and show the explicit Jacobian threshold and one-step objective increases.

The script checks exact Gaussian-moment and smoothed-derivative identities against separate numerical integrations, differentiates the analytic objective and DGS formulas, independently reconstructs the symmetric rank-two eigenvalue, and verifies finite-step ascent for several small starting scales and four positive stepsizes. The reported representative objective increases from \(z=10^{-3}(-9.9,1)\) are about \(1.5254\cdot10^{-12}\), \(1.5302\cdot10^{-11}\), and \(1.5783\cdot10^{-10}\) at steps \(h=0.01\), \(h=0.1\), and \(h=1\), respectively.

For the infinite family of ridge functions and **all** positive fixed stepsizes, the required reasoning is analytic: rank-two spectral diagonalization, Gaussian moments, differentiability of the smoothed field, and an objective expansion at the minimizer. Finite arithmetic and quadrature do **not** prove the general statement. The equality case, implementation-level finite quadrature, and long-time convergence are outside scope.
