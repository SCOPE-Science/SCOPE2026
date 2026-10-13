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

The proof is analytic. A direct read-through checked the rank-two orthonormal residual decomposition, the independence of the probe coordinate, both angular integrals including differentiation conditions, the exact second moment, the sign of the palindromic quartic, the unique positive threshold, and the dominated-convergence conditions for nearby full-rank inputs.

Run `python3 verify.py` from the same directory. It needs the Python standard library only and should print `VERIFY_OK` with the number of checks and the threshold. Its finite rational tests, quadrature, and Monte Carlo sampling guard against transcription and implementation errors only; they cannot establish claims for every real spectrum or ambient dimension.

The exact scope is fixed three-query Gaussian estimators on a finite-dimensional rank-two positive-semidefinite matrix; it is not a claim of finite-precision reliability or globally optimal trace estimation. No independent audit has been performed.
