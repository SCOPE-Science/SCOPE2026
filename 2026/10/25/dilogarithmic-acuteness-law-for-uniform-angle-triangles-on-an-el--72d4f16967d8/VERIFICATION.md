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
# Verification of the affine-ellipse acuteness theorem

Run the standalone file with `python verify.py` in a Python environment with NumPy and SciPy. The analytical proof, not the numerical script, establishes the theorem for all positive axis ratios.

Successful execution of the embedded code produced:

```
DILOGARITHM_MATCHES_INDEPENDENT_SPHERICAL_ANGLE_QUADRATURE_OK
STRICT_ANISOTROPY_MONOTONICITY_SAMPLED_OK
NEAR_CIRCLE_AND_THIN_ELLIPSE_ASYMPTOTICS_OK
INDEPENDENT_CARTESIAN_THREE_VERTEX_MONTE_CARLO_OK_220000
ALL_AFFINE_ELLIPSE_ACUTENESS_CHECKS_OK
```

These checks independently compute Euclidean angles from Cartesian point differences at five aspect ratios, evaluate an integral before the dilogarithm reduction, and test two asymptotic regimes. Random sampling uses a fixed seed. Acceptance bounds are sampling and floating-point tolerances, not exact certificates.

The proof's nonstandard steps are the directed-chord uniform phase and triangular difference-density lemma; the piecewise arc-cosine conditional probability; the integration-by-parts change of variables; and the arcsine-square central-binomial expansion. All are explicit in the proof and can be checked symbolically without relying on the numerical tests.
