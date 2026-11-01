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

# Verification and reproducibility

The self-contained analytic argument is in `RESULT.md`. Its critical steps are the exact finite lower-triangular singular-value identity, simultaneous upper and lower bounds after invertible diagonal multiplication, trace-class summability of the cross-slab part, and block-pinching lower bounds for nuclear norms.

Run `python verify_dirichlet_rhaly.py` with NumPy installed. The program was run from the packaged source and reported 482 successful finite checks: exact singular-value formulas for triangular finite sections, direct Hilbert–Schmidt sums, trace-norm lower checks, and diagonal-factor singular inequalities. These checks are finite and cannot validate the asymptotic claims by themselves.

The unbounded/compact boundary is established by a cited two-weight Hardy theorem. The nuclear endpoint and subunit quasi-Schatten obstruction are proved by explicit block decompositions, not inferred from the numerical experiments.

Independent mathematical review and independent validation have not been performed.
