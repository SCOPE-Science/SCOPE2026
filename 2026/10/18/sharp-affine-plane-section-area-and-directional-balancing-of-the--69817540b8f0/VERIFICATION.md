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

The exact symbolic checker verifies the rational central-area identity, its monotonicity derivative factorization, the endpoint inequality, and the body-diagonal parallel-section quadratic identity. It ran from the packaged source as:

```text
SYMBOLIC_SECTION_IDENTITIES_OK generic_area derivative_factors diagonal_profile
```

The independent-algorithm exact-rational checker constructs all twelve vertices, identifies the 24 edges, intersects them with 1,018 central planes with primitive integer normals, computes their convex hulls in rational projected coordinates, and checks the claimed formula. It also verifies 81 exact rational offsets along a body diagonal:

```text
CUBOCTAHEDRON_SECTION_FORMULA_OK cases=1018 vertices=12 edges=24
DIAGONAL_AFFINE_PROFILE_OK rational_offsets=81
```

Run `python symbolic_section_check.py` with SymPy installed and `python section_area_check.py` with the standard Python library. These checks validate the recorded algebraic identities and sampled geometric constructions. The full theorem relies on the analytic symmetry, Brunn concavity, and monotonicity proof. Exhaustive numerical testing over all real normals or an independent mathematical audit has not been performed.
