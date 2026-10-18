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

## Reproducibility and checks
Run `python3 verify.py` with Python 3, NumPy and SciPy available. This checks exactly normalized generator-plane counts against an independent convex-hull/Euler computation for five concrete examples; for a specified affine-regular hexagonal base, it computes the polar vertices with rational arithmetic, verifies planar area \(12\), polar area \(3/4\), and three-dimensional prism product \(12\). It checks the positive constants numerically as auxiliary sanity tests.

## Proof checks independent of numerical sampling
The main mathematical validation is the four-part analytical proof in `RESULT.md`: exhaustive rank-three generator configurations and edge-count formula, the three-dimensional flag count, the known Blaschke–Santaló volume bound, and an exact polar-fiber calculation for the exceptional prism. No finite number of checked examples proves the general classification. The external volume-product inequalities are cited and their proof is not reproduced.

## Limits
The verified examples cover particular integer generators only. This artifact does not provide an independent mathematical audit, full historical novelty certification, or a sharp uniform deficit constant.
