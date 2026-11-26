---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The stated bilinear group law gives (x,z)^2=(0,(x_u x_v)_e); thus x≠0 is impossible in the target even for a central target supported on isolated vertices. Nonzero edge labels force their endpoints nonzero, all other edges on those endpoints must also be nonzero, and their external neighbours are forced to zero. The free nonzero support is exactly an independent subset of the remaining induced graph. Comparing two solutions on a nonzero component gives ratios alternating between a and a⁻¹; an odd cycle forces a²=1, which has one solution since q−1 is odd. Root propagation tests existence, and the ratio calculation determines multiplicity whenever a solution exists. For the image, distinct feasible endpoint sets give disjoint strata, with empty endpoint set contributing one; the component product homomorphism gives the cardinality of each stratum. The zero-edge target is the independence-polynomial case and every fourth power is the identity. This argument covers q=2, empty and edgeless graphs, isolated vertices and mixed components. Inspected the supplied checker.py and recorded verification; its 24 cases enumerate vertex vectors and edge-label targets, use the uniform central-coordinate factor rather than an exhaustive full-group census in every case, and are not a proof for all graphs. No uploaded code was executed.

## originality

PASS

Pass for the full prescribed-square classification and assembled graph-uniform image formula, not for the group presentation, the fixed-support torus image calculation in isolation, or a separate originality claim for the element-order counts. The latter counts occur explicitly in another indexed record. The direct comparisons did not establish coverage of the complete prescribed-label theorem.

## value

PASS

A researcher investigating distributions of word maps on graphical groups can use the theorem to decide feasibility and count roots of a specified central target, not just determine which elements square to the identity. The decomposition makes a graph-uniform distinction between even-cycle constraints, odd-cycle determinacy and the independent-set contribution away from the forced support. This is an exact classification for a natural infinite family, even though some components are standard or separately known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
