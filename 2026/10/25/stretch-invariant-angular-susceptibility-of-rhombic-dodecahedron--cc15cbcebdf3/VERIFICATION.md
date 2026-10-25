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

# Verification of the central-section susceptibility result

Run `python checks/check_sections.py` with Python 3, NumPy and SciPy installed. The program is standalone relative to this directory and needs no external files. It reconstructs the polyhedral graph edges from the fourteen listed vertices, computes generic plane incidences independently of the analytical six-cone classification, uses one-dimensional spherical integration to check the cone probability, and verifies the trigonometric identity for unequal axis stretches. A separate Haar-geodesic experiment tests the first-order transition coefficient numerically for regular and anisotropic examples.

The numerical program finished with `ALL_RHOMBIC_DODECAHEDRON_SECTION_TESTS_OK`. Its checks do not certify universal quantifiers: the analytical proof in RESULT.md establishes the full all-positive-parameter theorem. Errors are bounded for each fixed positive triple as the geodesic perturbation tends to zero, not uniformly over degenerating triples. The discrete exceptional section planes are excluded from almost-sure assertions. No independent mathematical audit has been performed.
