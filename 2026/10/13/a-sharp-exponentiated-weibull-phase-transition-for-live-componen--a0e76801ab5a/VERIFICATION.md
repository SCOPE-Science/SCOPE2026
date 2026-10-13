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

The proof was checked symbolically from the model definitions. The critical steps are: (1) exact conditioning on the survivor count; (2) uniform comparison of the residual maximum survival with the one-survivor excess survival; (3) a uniform EW tail expansion for all integration points beyond the threshold; and (4) the endpoint asymptotic for the resulting incomplete-gamma integral.

No numerical experiment is required for the theorem. The proof does not infer an infinite asymptotic from finite samples or plots. The result does not claim second-order terms, growing-system uniformity, or any statement for intermediate live order statistics.
