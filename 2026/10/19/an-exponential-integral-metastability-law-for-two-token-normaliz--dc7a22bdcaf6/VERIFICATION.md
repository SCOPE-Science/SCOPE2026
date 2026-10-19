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
# Reproducibility notes

Run `python3 checker.py` in a directory containing the enclosed standalone script. It performs 1,440 direct two-vector versus scalar-step comparisons across four ambient dimensions and checks invariance of the normalized sum direction. It also checks several first-passage times against the analytic fixed-correlation limit, computes a quadrature value for \(E_1(1)/2\), and tests monotone approach to that boundary-layer limit.

The checker is a finite numerical consistency test; it is not an exhaustive or independent certification of the theorem. Infinite-time convergence and both inverse-temperature limits rest on the exact recursions and integral estimates in `RESULT.md`. The result does not cover layer-varying or anisotropic attention, nor more than two tokens.
