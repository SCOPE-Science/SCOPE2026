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

# Verification

The attached `CHECK.py` was executed against the actual mathematical formulas and produced `CHECK_OK`. It verifies symbolically the weighted divergence for an arbitrary differentiable activation \(h\), the one-sided divergences for the step activation, and the weighted normal jump at \(y=T_c\). It also checks sample parameters on both sides of the sufficient bound.

The analytical proof, which is not replaceable by finite computation, consists of the complete quadratic nonnegativity criterion, smooth Green flux cancellation, and the piecewise-domain boundary/interface flux contradiction in `RESULT.md`. At equality the weighted divergence can vanish on a single horizontal line but cannot have zero area integral over a nonempty Jordan interior. The no-cycle assertion is confined to positive classical trajectories and piecewise-regular Filippov cycles. Outside the sufficient inequality no assertion of existence or nonexistence is certified. The review is same-model only and independent validation has not been performed.
