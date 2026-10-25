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

# Verification protocol

The self-contained `verify.py` uses the Python standard library. Execute `python verify.py` in the directory containing the source. Expected terminal line:

`VERIFY_OK: rectangle, octahedron, all-dimensional orthotope Gram, even polygon tests`

Four independent diagnostic groups are included. In two dimensions, spherical arcs give exact rectangle-tail probabilities and their estimated slopes approach the closed-form coefficient for three different positive side pairs. In three dimensions, direct spherical polar integration of a regular octahedron's radial feasibility event approaches the coefficient \(3/(4\pi)\). In dimensions \(2,3,4,5,7\), Gram-determinant evaluations for orthotope tangent-section simplices agree with the predicted \((d-1)\)-volume. Exact regular even-polygon chord quantiles independently produce the same endpoint slopes.

The script checks finite values and floating-point agreement, not the general polyhedral remainder theorem. The analytic proof in `RESULT.md`, including tangential localization, finite facet perturbations and the spherical Jacobian, establishes the infinite quantifiers. Scientific originality comparisons remain subject to literature-access limitations. No independent audit has been performed.
