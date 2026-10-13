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

`artifacts/verify_csd_repeller.py` constructs the normalized three-mode projective map
\[
T_i(p)=
\frac{p_i(\mu-z_i)^4}
{\sum_\ell p_\ell(\mu-z_\ell)^4},
\qquad
z=(-1,0,1),
\]
in exact symbolic arithmetic. It verifies the two-cycle and computes the intrinsic two-dimensional Jacobians at both orbit points. Their products in both return orders are checked to equal
\[
-3I_2.
\]

The local repeller conclusion uses the smooth Taylor expansion of the return map and is not inferred from finite numerical simulation.
