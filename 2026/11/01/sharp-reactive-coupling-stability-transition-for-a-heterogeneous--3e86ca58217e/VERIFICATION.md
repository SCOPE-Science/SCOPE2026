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

The standalone exact-arithmetic script `verify.py` was executed successfully and printed `EXACT_CERTIFICATE_OK`.

The verification reconstructs the real Jacobian from its nonlinear differential equation, checks the zero-mean polygon and squared radii, derives the symbolic characteristic polynomial, and recomputes each Hurwitz determinant from its defining matrix. It checks exact endpoint signs for the uniquely positive cubic root and sample exact Routh signs on both sides.

The mathematical argument also proves monotonicity for the entire positive root range and invokes the Routh–Hurwitz theorem to count unstable eigenvalues for all reactive couplings, rather than extrapolating from a finite sampling grid. Approximate values are only explanatory. The local spectral theorem does not certify any nonlinear secondary branch, global attraction, or priority in the historical literature.
