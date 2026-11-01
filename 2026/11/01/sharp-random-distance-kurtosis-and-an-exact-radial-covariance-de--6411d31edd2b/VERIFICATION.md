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

# Verification scope

The all-dimensional mathematical argument is entirely explicit in `RESULT.md`: the independent-pair expansion (3), normalized polar moment identity (4)--(5), and centered covariance trace identity (7) imply the exact nonnegative decomposition (2). The equality case is a consequence of constant radial function. Finite tests provide diagnostics, not a proof in every dimension.

# Reproducible finite checks

Run `python3 verify.py` under Python 3, using only the standard library. In the actual scientific review, the program produced:

```
EXACT_BALL_CONSTANTS_D2_TO_D40_PASSED
RECTANGULAR_BOX_INDEPENDENT_MOMENTS_PASSED
RECTANGULAR_POLAR_INTEGRAL_PASSED
ANNULUS_CONVEXITY_BOUNDARY_PASSED
SEEDED_PAIR_SAMPLING_SANITY_PASSED
ALL_CHECKS_PASSED
```

`Fraction` arithmetic independently matches coordinate-wise fourth moments of independent differences on boxes with the moment-expansion formula. The distinct polar integral for a non-square rectangle tests the weighted radial integrations. The annulus is an exact counterexample once star-shapedness is removed. The random-pair simulation is seeded and is not an infinite certificate.

# Limits

Exact distributional reconstruction, noisy estimation, shape stability in Hausdorff or Banach--Mazur distance, and historical priority beyond inspected sources are not proved. Independent audit has not been performed.
