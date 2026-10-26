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

# Reproducibility and mathematical limits

Run `python verify_taylor.py` with NumPy and SciPy installed. Its internal paths are self-contained and require no external data or prior results.

The executable independently checks the first clamped-beam root and its simple midpoint-even eigenfunction, the explicit sine–sinh critical profile, both clamped boundary conditions, odd/even orthogonality, Poiseuille energy \(12q^2\), the exact critical constants, and the supercritical two-branch identities. Polynomial Galerkin approximations with eight and twelve basis functions are checked for several subcritical and supercritical budgets, including randomized feasible competitors. Infinite-dimensional global optimality and exact optimizer multiplicity come from the analytic sharp clamped inequality and stationarity comparison identity, not finite tests.

The only scientific uncertainties left are absolute bibliographic priority, physical realizability of arbitrary optimized profiles by specific distributed forcing mechanisms, and extensions beyond a steady unit-width channel with reflecting solute boundaries and constant transverse diffusivity.
