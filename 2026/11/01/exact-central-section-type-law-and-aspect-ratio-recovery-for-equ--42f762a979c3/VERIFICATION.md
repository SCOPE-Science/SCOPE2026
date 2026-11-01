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

# Verification of the exact central-section law

The mathematics is proved in `RESULT.md`. Reproduce auxiliary checks with `python proof/check_prism.py` (Python 3, NumPy, SciPy). The script constructs the six actual prism vertices, uses nine edges, samples isotropic normals, and counts sign-separated edges directly. For each of seven distinct aspect ratios it compares all three observed probabilities to the closed formula, and also compares the mean number of section sides. An independent one-dimensional integration of the *unreduced* spherical normal-cone formula matches the triangle probability. The single-statistic inverse and the unique-maximizer equation are also checked numerically.

Observed program output ends with `ROTATION_CONE_QUADRATURE_PASSED`, `UNIQUE_PENTAGON_MAXIMIZER_CHECK_PASSED`, `SHARP_ASPECT_RATIO_INVERSION_PASSED`, `DIRECT_EDGE_CROSSING_MONTE_CARLO_PASSED`, and `ALL_CHECKS_PASSED`.

The source-level proof does not depend on these finite checks. Historical novelty remains provisional because the complete manuscript of the most relevant random-affine-plane paper was not accessible. No independent mathematical audit has been performed.
