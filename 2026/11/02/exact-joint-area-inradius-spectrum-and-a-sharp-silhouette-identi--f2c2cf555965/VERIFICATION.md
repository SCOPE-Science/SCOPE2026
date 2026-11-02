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

# Reproducibility checks

Run `python3 verify_octa_joint.py` in an environment with NumPy and SciPy. The script generates 2,500 independent unit directions, forms the planar orthogonal projections of all six vertices, and compares their convex hull areas, origin-centered inradii and vertex counts with separately derived formulas. It also checks 61 parameter levels of both complete fixed-radius fibers, verifies the unique interior maximizer and the exact gap-contact parameter, and stress-tests inclusion in the sharp feasible intervals for 200,000 more directions.

The final standalone program was executed and printed `OCTAHEDRON_JOINT_AREA_INRADIUS_CHECKS_PASSED`, including exact-value checks at the critical parameter. All exhaustive orientation claims rest on the two analytical one-dimensional parametrizations and algebraic inequalities in `RESULT.md`, not on random simulation. The code is diagnostic, not a formal machine-checked proof, not a proof of historical priority, and not an independent mathematical audit. Equivalences and exact normalization can be inspected directly from the supplied proof and code.
