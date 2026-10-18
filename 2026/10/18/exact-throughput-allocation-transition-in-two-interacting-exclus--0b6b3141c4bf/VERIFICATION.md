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

The theorem is proved analytically in RESULT.md by reducing the two-density square to its diagonal and boundary through the exact affine-in-product identity. The exact cubic-root uniqueness and the completeness of global optimizer sets are proved, not inferred from a numerical scan. The two strict-local-stability thresholds follow from explicit derivatives, Hessians and concrete equality-threshold paths.

Run `python verify.py` using the supplied standalone Python 3 script. The program checks exact rational polynomial identities and non-exhaustive numerical diagnostics at multiple coupling strengths. It prints the assertion count and threshold approximations. Its finite tests are not treated as proofs of infinite-range statements.

Scientific limits: the optimized observable is summed *signed* stationary flux; independent density selection is an ensemble-comparison problem rather than a dynamical phase-selection assertion; the microscopic product-state flux is inherited from primary literature. No independent audit or external certification has been performed.
