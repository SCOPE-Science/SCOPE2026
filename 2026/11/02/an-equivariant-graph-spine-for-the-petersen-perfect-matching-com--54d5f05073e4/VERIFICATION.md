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

# Verification

Run `python3 verify_petersen_perfect_matching.py` from this directory using Python 3 with no third-party modules. Required success sentinel: `PETERSEN_PERFECT_MATCHING_EQUIVARIANT_CERTIFICATE_OK`.

The program constructs the Petersen graph as the disjoint-two-subset graph, enumerates all perfect matchings, verifies that every graph edge belongs to two perfect matchings and every distinct matching pair intersects in exactly one edge, builds every nonempty simplicial face, enumerates the complete 120-element automorphism action, tests the exterior-square homology character against \(\bigwedge^2 V\oplus (V\otimes\mathrm{sgn})\) for each group element, and counts quotient-graph cells for full, alternating and five-cycle subgroups.

**Exact observed output excerpt:** six matchings; fifteen graph edges; facet-derived face vector \((15,60,60,30,6)\); degree-one rank ten; traces \((10,-2,-2,1,1,0,0)\) on the conjugacy classes ordered as in the proof; quotient graph statistics \((2,1,0)\), \((2,1,0)\), and \((5,6,2)\), respectively (vertices, edges, cycle rank).

**Proof not outsourced to computation:** The second-largest-barycentric-coordinate formula explicitly defines a continuous equivariant strong deformation retraction of every facet onto a radial star, and its fixed intersection vertices ensure global gluing. The integral exterior-square homology formula follows from the graph-chain boundary. The finite exact checks substantiate the incidence and group-character calculations; no finite experiment is treated as proof of an unexamined infinite family.

Independent external audit or validation has not been performed.
