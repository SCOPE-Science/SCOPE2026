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

# Mathematical verification
The finite checker `verify.py` is self-contained and requires only Python's standard library. The command `python verify.py` completed with `VERIFY_OK 8054` when run on the packaged candidate. It computes all bisubset cardinality distances for dimensions \(3\) through \(15\) and multiple weights on both sides of the proposed transition, checks tangent cardinality classes, and verifies the exact facet-slack identity with rational arithmetic. It also independently checks the product-permutohedron-plus-diagonal-simplex support-function optimization for dimensions \(3\) through \(6\).

The universal result is supported by a symbolic proof in `RESULT.md`: symmetrization fixes an optimal center; explicit projected normals reduce its facet distances to affine functions of the weight; an endpoint inequality establishes the lower envelope, and equality analysis gives all active facets. The center-locus inequalities are derived from all remaining facets, with a strict local-dimension argument. The finite checker does not certify the universal quantifiers or bibliographic uniqueness. No external independent mathematical review is represented.
