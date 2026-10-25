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

# Reproducibility and verification

Run `python3 verify_cube_section_perimeter.py` with Python 3 and NumPy. The program reconstructs every generic cube-section polygon from the intersections of its cutting plane with the 12 cube edges and compares its convex-hull perimeter and number of edges against the analytical face formulas on 650 random normals. It checks the exact local spherical-Jacobian identity and both first-order loss expansions down to deficits of order \(10^{-5}\). It also generates 3,200,000 independent Gaussian normal vectors and tests the quadratic Haar rare-event coefficient and near-equal frequency of the two polygon types at three deficit levels.

Expected final line: `ALL_NEAR_MAXIMUM_CUBE_SECTION_CHECKS_OK`. The finite sample estimates have simulation error and non-negligible higher-order corrections; the asymptotic laws are proved in RESULT.md by uniform expansion and normalized spherical integration, not by simulation. The proof of the sharp global maximum is credited to the specified primary geometric source.
