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

# Verification record

The executable `verify_triangular_cylinder_neighborhood.py` is self-contained Python 3. It reconstructs all faces of the open-neighborhood complex of \(K_3\square C_n\) from the graph's neighbor generators for every \(5\le n\le14\). At each center it checks that the prescribed triangle is the unique free face of its tetrahedron, then checks that the opposite-layer edge is a free face of the remaining triangle, and removes both pairs. It compares the remaining faces to the predicted torus triangulation, checks that every edge belongs to two triangles with opposite induced orientations, checks connectivity and all vertex links, and verifies the Euler characteristic.

Actual execution returned `VERIFY_OK cases=10 total_elementary_pairs=570 integer_orientation=PASS vertex_links=PASS`. Reproducibility command: `python3 verify_triangular_cylinder_neighborhood.py`.

These bounded tests do not prove the infinite theorem; the proof is the local uniqueness and classification-of-surfaces argument in RESULT.md. Earlier cyclic instances overlap existing published work. No independent scientific audit has been performed.
