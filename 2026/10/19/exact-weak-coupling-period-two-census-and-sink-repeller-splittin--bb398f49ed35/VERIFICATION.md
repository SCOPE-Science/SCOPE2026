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

The accompanying standalone `verify.py` requires Python 3, SymPy and NumPy. Execute `python verify.py` in the same directory as the scientific result. It returned:

`PASS: 640 finite symbolic/numerical checks; analytical completeness and local stability are proved in RESULT.md`

The symbolic checks independently expand both one-step Jacobians and the product return characteristic polynomial. They verify the first derivative of the real Floquet multiplier and of the nonreal pair modulus at zero coupling. Finite cycle reconstructions cover rational couplings up to \(3/10\), all tested phase positions, and the sine wedge boundaries. Five small positive coupling values directly check the separate attracting and repelling spectra.

Completeness for all \(b>0\), \(0<k<1/3\), and hyperbolicity for every sufficiently small \(k>0\) are proved by the sign argument, monotonicity inequality, and analytic eigenvalue perturbation in `RESULT.md`. Finite computations cannot substitute for those infinite arguments or establish the sharpness of the sufficient monotonicity interval. Independent mathematical audit has not been performed.
