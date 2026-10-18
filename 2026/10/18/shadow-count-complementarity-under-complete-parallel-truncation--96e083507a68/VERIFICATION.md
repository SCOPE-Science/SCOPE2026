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

The complete analytical argument is in `RESULT.md`: barycentric inequalities establish all 18 edges and paired normals; the contour normal-cone sign rule yields the pointwise equality for all admissible tetrahedra, depths and generic directions. The probability transfer invokes the known 2008 solid-angle theorem and is not based on sampling.

With Python 3, NumPy and SciPy, run `python verify.py`. This reconstructs planar projected convex hulls directly, independently of the contour-edge formula. Four tetrahedron geometries, three depth choices and 2300 quasi-uniform directions per shape passed. An independent exact-rational monotone-chain hull implementation checked 1016 nondegenerate integer directions with two tetrahedra and two unequal/equal cuts. The regular limiting constants were compared with exact spherical-angle expressions.

Observed terminal output contains `EXACT_RATIONAL_HULL_CHECKS_OK 1016` and `VERIFY_OK`. Rational finite tests do not replace the proof over all real parameters. Historical priority beyond the inspected sources remains open; independent audit has not been performed.
