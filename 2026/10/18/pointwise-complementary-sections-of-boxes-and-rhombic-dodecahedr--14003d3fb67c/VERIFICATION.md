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

# Verification scope

Run `python check.py` with NumPy and SymPy. The checker verifies all 12 cube edges, 24 rhombic edges and 12 exact four-vertex rhombic facets, the three strict endpoint-sign possibilities for every paired edge, hundreds of nondegenerate exact-integer sample normals and four rational stretch choices, second-derivative algebra and 150,000 independent normals at each of four diagonal aspect ratios. The expected final output begins with four `GEOMETRY_CHECK` lines and ends with `CHECK_OK`.

The proof of the all-affine identity is the local per-edge sign bijection in `RESULT.md`. Random checks are only sanity checks. The Lagrange multiplier argument establishes all-positive-triple optimization; symbolic differentiation supports the Taylor coefficient. Neither a finite computation nor an inaccessible source was construed as exhaustive mathematical or bibliographic proof.
