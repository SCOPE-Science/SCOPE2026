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

# Verification scope

The theorem in RESULT.md is established from the exact discrete second-moment map, the spectral radius of its nonnegative symmetric block, and a closed-form stationary linear system. Crucially, the boundary \(h=h_*\) and every supercritical step are treated with Perron eigenvector forcing, not inferred from numerical simulation. The complete correlated two-coordinate moment operator includes the off-diagonal mode, which is bounded by the diagonal Perron eigenvalue.

## Reproduction

Run `python verify.py` with Python 3, NumPy, and SymPy. The checker reconstructs the two-by-two forced moment map and the full three-dimensional symmetric covariance operator, verifies symbolic algebra and asymptotic substitutions, carries out 1,500 sampled full-operator comparisons, and solves four stationary examples with exact rational arithmetic. These are supplementary checks; they do not certify general-dimensional, nonlinear, or non-Euler integrators. No independent audit has been performed.
