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

# Verification and scope

Run `python3 verify.py` alongside this file. It reconstructs the stated Lucas-cube graphs, their edge sets and distances, and exhaustively enumerates all shortest paths between all unordered pairs for \(5\le n\le9\). For each graph it verifies the constructed cardinality and the requirement that no geodesic contains three chosen edges.

Replayed observations:

- \(n=5\): 11 vertices, 15 edges, 7 chosen edges, 110 geodesics.
- \(n=6\): 18 vertices, 30 edges, 11 chosen edges, 558 geodesics.
- \(n=7\): 29 vertices, 56 edges, 18 chosen edges, 2534 geodesics.
- \(n=8\): 47 vertices, 104 edges, 29 chosen edges, 15224 geodesics.
- \(n=9\): 76 vertices, 189 edges, 47 chosen edges, 86742 geodesics.

The observed maximum of selected edges on any enumerated geodesic is two. The run ends `ALL_CHECKS_PASSED`.

The proof for every \(n\ge5\) uses the isometric bitflip property and the projection of selected edges onto the three spokes at state \(000\); the finite checks are supplementary. No claim of global optimality or independent mathematical audit is made.
