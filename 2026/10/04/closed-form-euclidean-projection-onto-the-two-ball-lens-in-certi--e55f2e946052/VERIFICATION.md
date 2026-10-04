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

The proof classifies the active set using uniqueness and normal-cone optimality for Euclidean projection onto a convex intersection. In the two-active branch, the intersection of the two boundary spheres is represented as a sphere in the radical hyperplane and projected onto directly.

`artifacts/verify_two_ball_projection.py` implements both the closed-form projector and an independent Dykstra iteration using only the Python standard library. It checks deterministic cases and random instances in several dimensions and compares the outputs to tight numerical tolerance.

The numerical replay is finite and does not prove the quantified result. The theorem assumes exact-real arithmetic and nonempty interior; finite-precision error analysis and intersections of three or more balls are outside scope.
