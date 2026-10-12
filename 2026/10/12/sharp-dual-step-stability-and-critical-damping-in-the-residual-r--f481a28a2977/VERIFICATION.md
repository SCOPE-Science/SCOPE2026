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

The proof in `RESULT.md` is analytic.

`artifacts/verify_basadmm_scalar.py` reconstructs the scalar state matrix symbolically, verifies the characteristic trace and determinant, checks the three Jury expressions, verifies the critical-damping formulas, and derives the source-coupled discriminant.

It also evaluates representative parameter choices on both sides of the stability threshold and checks that the closed-form \(\sigma_\star\) minimizes the spectral radius on dense finite grids. Those finite grids are supporting checks only; uniqueness over the continuum follows from the discriminant and derivative argument in the proof.
