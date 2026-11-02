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

# Verification
The executable `verify_rotated_dephasing.py` was run from the package contents with NumPy and SciPy installed. It independently forms the density-operator channel via its Kraus mixture and a two-qubit Choi state; it does not use the closed norm expression to compute Choi outputs. Numerical trials test the precise trace-norm identity and the sign of the least eigenvalue after partial transposition. Matrix-power simulations in the scaled window check convergence to the analytic critical root in multiple overdamped, defective, and oscillatory regimes. The program also checks the nilpotent exceptional-point matrix and Frobenius coefficient. Its recorded output was 619 passing assertions.

The proof of a limit is analytic and independent of these samples: matrix exponential convergence, Choi/PPT nuclear norm equivalence, strict contraction, and the trigonometric equality condition are detailed in `RESULT.md`. Floating-point agreement is not a certificate of all-parameter exactness, and no independent audit has been performed. Run `python verify_rotated_dephasing.py` with dependencies from `requirements.txt`.
