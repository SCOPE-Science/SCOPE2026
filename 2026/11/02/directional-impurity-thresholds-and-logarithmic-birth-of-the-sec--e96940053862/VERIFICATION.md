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

The attached `verify_rectangular_two_impurity.py` is executable with Python 3, NumPy, and SciPy. Run `python verify_rectangular_two_impurity.py` and compare with `verify_rectangular_output.txt`. Six directional-threshold checks independently compare a one-dimensional integrated Green-function formula with a discrete two-dimensional Brillouin-zone quadrature away from the spectrum; all pass within \(2.8\times10^{-17}\). Three antisymmetric bound-state energies for \((t_x,t_y)=(3,1)\) agree with the second-largest eigenvalue of a \(41\times41\) open finite lattice to within \(1.3\times10^{-12}\). The critical nearest-neighbor values \(9\) and \(6\) are checked. Four finite-difference edge-slope tests show slow convergence toward the explicit analytic logarithmic coefficient. Numerical tests are finite corroboration only; the arbitrary-displacement and \(V\downarrow V_c\) statements follow from the proof's spectral and local integral arguments.

There has been no independent scientific audit or proof-assistant certification.
