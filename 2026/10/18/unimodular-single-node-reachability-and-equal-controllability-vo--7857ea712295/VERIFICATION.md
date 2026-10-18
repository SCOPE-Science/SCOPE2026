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

The analytical proof is given in `RESULT.md`. Run `python3 verify.py` using Python 3's standard library. The program uses fraction-free integer elimination for exact Kalman and finite discrete Gramian determinants; its continuous-time tests solve finite-dimensional Lyapunov equations over exact rational numbers. It uses no sampled eigenvectors or floating-point determinant threshold.

The expected verified output is:

`VERIFY_OK integer_krylov_cases=170 minimal_horizon_gramians=35 rational_lyapunov=9 affine_cases=132`

The finite tests check sizes \(2\le n\le18\) for all placements, plus small-size Gramian identities; they are not a substitute for the infinite-dimensional-size argument using eigenvector product identities. The review remains same-model only; independent audit is not yet performed.
