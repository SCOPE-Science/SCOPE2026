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
The algebra was checked by deriving the affine projector and reflection, solving the zero-shrinkage phase exactly, and reconstructing the fixed point and identified-cell error matrix. The identity \(M^\top M=(a^2/(1+a^2))I\) gives the exact post-identification Euclidean contraction. The onset-error norm was simplified to a form strictly below \(b\), which, together with \(\gamma(1-a)\ge b\), supplies the invariant-cell proof.

The accompanying checker iterates the original nonlinear projector--reflection--soft-threshold map directly for multiple parameter choices. It verifies the exact first identified index, permanent cell membership, the fixed point, and the exact contraction ratio to numerical tolerance. Finite tests are supporting evidence only; the symbolic argument is the proof.

The source-side comparison used the full arXiv text of the primary basis-pursuit paper and the full arXiv text of the finite activity-identification paper at their relevant algorithm and theorem passages. Independent audit has not been performed.
