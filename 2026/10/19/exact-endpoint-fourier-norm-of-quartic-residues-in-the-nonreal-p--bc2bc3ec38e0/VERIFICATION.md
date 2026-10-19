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
The supplied standalone `verify_quartic_projection.py` was run with `python verify_quartic_projection.py` using standard Python. It enumerated all 43 primes congruent to five modulo eight below 1001 and printed `VERIFY_OK primes 43 range 5 997`. For each it independently enumerated the multiplicative cosets, complex quartic Gaussian periods and Jacobi sum, verified the signed real Jacobi coordinate, compared squared period moduli and directly summed the convolution kernel to check the claimed sharp endpoint norm. Finite floating-point regression checks are not mathematical certificates for all primes; the analytic Gauss/Jacobi-sum argument establishes the theorem for every prime in the stated class. The norm-attainment classification is proved by equality in the finite triangle inequality.
