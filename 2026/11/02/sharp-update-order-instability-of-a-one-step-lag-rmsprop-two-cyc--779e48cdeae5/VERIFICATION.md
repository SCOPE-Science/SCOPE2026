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

# Exact checks and limits

`verify.py` evaluates the stated lagged map using SymPy, differentiates both coordinates, and substitutes the exact two-cycle. It checks the spatial and memory updates, reflection covariance of the two local Jacobians, the two-step monodromy as a square, the trace/determinant polynomial, the discriminant and critical learning-rate substitutions, and 18 exact-rational sample combinations. Execute with `python verify.py` and a standard SymPy installation.

The proof of completeness of period-two orbits uses the displacement and memory identities directly; the linear stability classification uses strict Schur inequalities and discriminant signs for all real parameters. No finite sample proves parameter-uniform statements. At the critical unit-circle boundary, eigenvalues alone do not settle nonlinear attraction; this is explicitly unproved. Global basin dynamics and longer-period invariant sets are not classified. No independent audit has been performed.
