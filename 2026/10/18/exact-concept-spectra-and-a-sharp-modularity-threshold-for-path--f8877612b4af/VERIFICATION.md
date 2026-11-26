---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For nonempty attribute sets, the extreme columns determine the clipped intersection, and admissible intervals are recovered by columns b−k and a+k or a single column at a clipped endpoint. The end columns give bottom exactly when n≥2k+2; their intersection, when n≥k+2, has fewer than k+1 objects and cannot be a single column or top. In the sparse endpoint rectangle, each invalid triangular corner has binom(n−2k,2) pairs. The left endpoints of length-t intervals run from max(1,k+2−t) to min(n−k,n−t+1), giving the stated spectrum. At n=2k+2, the two missing extreme pairs can be replaced by bottom and top, preserving the product order. Beyond this boundary at positive k, the extents {k+1}, {k+3}, and [k+1,k+2] witness failure of modularity: joining the singletons produces [k+1,k+3], while {k+3} meets [k+1,k+2] in bottom. The height-two k=0 case is separate. The sparse census is a concave quadratic centered at (n−1)/3, and comparison with the first dense value and then the residues modulo 3 yields the unique optimizer and exact maximum, with n=2,3 separately checked.

## originality

PASS

The distinct contribution supported by this comparison is the explicit path-power spectrum, cutoff and radius optimization, not the general formal-concept representation by intersections. The closest overlap in neighborhood incidence counts rough pairs rather than concept extents; closely titled path-power biclique results use induced bicliques in a different graph.

## value

PASS

The band context is a natural reflexive neighborhood relation. The count by extent size and the precise change from a product of chains to a nonmodular lattice distinguish its enumeration from its order structure. The critical extra width retains distributivity by replacing the missing corners, and the independent optimization identifies the exact radius of highest concept count rather than just its growth rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
