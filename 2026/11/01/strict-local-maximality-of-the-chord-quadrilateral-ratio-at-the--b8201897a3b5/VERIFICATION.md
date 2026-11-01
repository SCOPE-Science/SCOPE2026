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

The associated `verify.py` script recomputes the full eight-variable second-order interval jets and checks the precise rank and curvature certificates used in the proof. The calculation uses 45-digit outward-rounded `mpmath.iv` operations and makes no random or finite-sampling inference about general heptagons.

The six-by-six gradient minor is certified strictly negative, with approximate value \(-5.56537454546\cdot10^{-5}\). The mean Hessian restricted to the common two-dimensional kernel is certified negative definite by a strictly negative leading diagonal entry and strictly positive determinant (approximately \(0.0462806329214\)). The script also checks all 511 bounded four-normal choices for the regular reference heptagon and the three-sided incircle obstruction.

The identity that the seven gradients sum to zero is established by exact cyclic symmetry and affine invariance in the analytic proof. Its interval inclusion test is only a numerical cross-check. The qualitative local deficit follows from smooth Taylor expansion and a min-of-seven nonsmooth stability argument. No explicit neighborhood radius or optimal deficit coefficient is certified. Independent audit has not been performed.
