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

The proof is analytic and applies to all \(c>0\), \(1/\sqrt3<u<1\), and nonnegative independent Itô noise intensities in the claimed strict region. It does not depend on finite sampling.

Run `python check_threshold.py` with Python, SymPy and NumPy installed. The script reconstructs the moment generator, checks all three characteristic-polynomial coefficients, symbolically checks the quadratic-generator identities, and tests 1260 parameter-grid cases of the exact frontier and constructive Lyapunov matrix. A successful run prints a `VERIFY_OK` line. Exact symbolic identities support the algebra; grid checks only test select parameters, not all parameters.

The deterministic Jacobian and the stochastic covariance equations are recovered directly from the equations reproduced in `RESULT.md`. Independent validation has not been carried out. No proof is given for the nonlinear stochastic system or for sample-path stability.
