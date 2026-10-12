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

The analytic finding is proved in `RESULT.md` using a symmetric mutation generator, its positive edge-gradient semigroup, strict positivity of the pulse adjoint weight, and a Dirichlet-form differentiation identity. The reflecting continuum follows from Dirichlet gradient positivity and integration by parts. These steps establish strict inequalities for every admissible dimension and contact intensity, not merely a finite enumeration.

Run `python verify.py` with Python 3.9 or newer (standard library only). It checks 81 exact-rational instances of all three essential finite-dimensional algebraic identities (mutation-edge gradient intertwining, adjoint pulse forcing, and weighted Dirichlet integration by parts). It then evaluates the closed two-trait formula for a fully specified positive rational parameter choice and reports `VERIFY_OK`. The floating-point evaluation illustrates the exact symbolic formula; it is not used to prove positivity. The script does not test or validate the nonlinear susceptible-depletion model.

Self-review checked the formal domain, strictness, endpoint cases, recovery normalization, the time-reversal of the pulse adjoint and the limits of extrapolation. Independent audit and independent validation have not been performed.
