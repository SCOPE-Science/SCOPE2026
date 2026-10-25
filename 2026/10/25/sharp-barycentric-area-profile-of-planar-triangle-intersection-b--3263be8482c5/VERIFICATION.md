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

# Reproducibility and verified scope

The analytic argument is fully written in `RESULT.md`. The standalone `verification.py` uses only Python's standard library. Run `python verification.py` in the same directory. It calculates the area of the star body by adaptive quadrature of a three-branch independent chord expression, checks the formula in seven nondegenerate affine normalizations, compares chord intersections using exact rational arithmetic over three test configurations, and tests 150 barycentric vectors against the claimed bound. Printed PASS means only those finite regressions succeeded.

The proof of the result for all nondegenerate triangles rests on the exact chord integrations and strict Schur-concavity argument, not on numerical samples. The boundary value concerns the continuous interior-center limit, and no physical measurement or external independent verification is claimed.
