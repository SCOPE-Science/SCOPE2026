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

Run `python verify.py` using only the Python standard library. The verifier uses `fractions.Fraction` to check the exact six-cycle, its preceding plateau orbit, images of both singular branches, 306 rational sixth-return samples, all 25 integer first-coordinate states of the invariant segment, rational scaling, and both inverse contraction factors. It reports `EXACT_RATIONAL_CHECKS_PASSED 1333`. Those checks were actually replayed from the embedded program prior to packaging.

The infinite Hausdorff-dimension statements are **not** certified by the finite tests. They follow from the full interval return formula published in [1], strong separation of two contracting inverse branches, the graph-entry and graph-visit propositions of [1], the rank-zero integer-grid argument, and the one-dimensional affine fiber argument in RESULT.md.

The only external mathematical dependency is the published graph-entry and itinerary description in [1]. The 2025 follow-up [2] supplies a comparison for measure-theoretic statements, not a proof premise. Historical priority is subject to the explicitly recorded residual risks. No independent external audit has been performed.
