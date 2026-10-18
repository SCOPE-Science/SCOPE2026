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

# Reproducibility checks

Run `python verify.py` with Python 3, NumPy, and SciPy. The script computes the decaying modified-Bessel solution for a half-line diffusion with a quadratic reset intensity, integrates the exact one-dimensional mean-time formula, solves the analytic stationarity equation, and independently solves the finite-difference nonlocal generator with remote Neumann truncation.

For diffusion coefficient and reset location both equal to one, computed numerical values are \(\lambda_*\approx1.548485175665741\), \(\kappa_*\approx5.749475240578948\), and \(\mathbb E[\tau]_{\min}\approx0.9392900105291005\). Across five positive curvature choices, the mesh \(0.0125\) finite-difference values differ from the integral formula by at most \(2.21\times10^{-5}\); halving the coarser mesh reduces discrepancies by approximately a factor of four.

These floating-point values do not have certified interval enclosures; the continuum assertion of strict global uniqueness rests on the analytic proof. The distant reflecting boundary is only a numerical truncation device, not a boundary in the theorem. The two reference articles were compared scientifically; independent originality and correctness audits remain unperformed.
