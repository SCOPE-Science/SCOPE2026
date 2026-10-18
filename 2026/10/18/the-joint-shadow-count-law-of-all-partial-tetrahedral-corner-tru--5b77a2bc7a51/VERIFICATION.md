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

# Verification details

The standalone source `verify.py` enumerates all sixteen truncation masks for four concrete tetrahedra. It uses rational coordinates, rational independent cut fractions, integer viewing directions and monotone-chain planar convex hulls computed exactly to test the predicted count for every mask, including complementary sums. It independently samples directions to compare the four unique-outlier cone probabilities with the spherical determinant formula for the interior solid angles. Running `python verify.py` prints the two `PARTIAL_TETRA_SHADOW_OK` and `ANGLE_MASS_MONTE_CARLO_OK` reports upon success.

These are finite numerical and rational diagnostics; the infinite theorem follows from the exact facet-pair argument and spherical area characterization given in `RESULT.md`. The external originality comparison remains incomplete, and no independent audit is claimed.
