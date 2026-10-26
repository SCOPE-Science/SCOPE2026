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

The exact rational checker `checks/verify.py` was executed with Python 3 and passed, using only the Python standard library. It verifies the moment equations, determinant factorization and universal velocity eigenvector over sampled stable rational parameters; it compares finite-lag propagation with the analytic exponential and the exact mean-square-displacement integral. The proofs of irreducible Metzler stability, existence of stationary stochastic convolution, and general-parameter monotonicity are contained in RESULT.md; finite tests alone do not certify any infinite-parameter theorem. At or beyond the second-moment threshold the claim is explicitly non-finiteness, not absence of stationary paths.
