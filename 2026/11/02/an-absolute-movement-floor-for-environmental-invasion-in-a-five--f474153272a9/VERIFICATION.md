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

The exact analytic verification uses the \(3\times3\) infection linearization, a strictly positive test vector, and the positive left Perron eigenvector of an irreducible Metzler matrix. The spectral-bound sign is therefore the sign of the scalar threshold polynomial; the unique-root and three-regime statements follow by direct inequalities. The verifier `verify.py` checks 729 exact rational matrix/determinant identities and additional exact examples and numerical limits. Finite tests are not substitutes for the proof.

Boundary \(H=0\): simple zero linear eigenvalue, nonlinear stability not assessed. The statement does not imply global persistence or finite-population outbreak probabilities. No independent audit has been performed.
