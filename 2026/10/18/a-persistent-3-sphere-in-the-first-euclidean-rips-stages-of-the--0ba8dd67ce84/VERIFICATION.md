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

The supplied `verify.py` reconstructs the exact \(F_4\) root coordinates with integer arithmetic and independently enumerates the two clique complexes. The exact squared-distance spectrum for distinct roots, in coordinates multiplied by two, is \((4:240,8:168,12:384,16:84,20:144,24:96,32:12)\).

It verifies face vectors \((48,240,384,192)\) and \((48,408,1224,1560,840,168,24)\), respectively, and confirms that the \(24\) long-root neighbor sets correspond to six-vertex octahedral facets of the short-root \(24\)-cell. It then checks all \(1704\) listed pairs as free-face/coface pairs at their actual deletion stage. The final surviving subcomplex is *exactly* the radius-one complex. Free-face dimensions \(1,2,3,4,5\) occur \(168,672,696,144,24\) times.

The proof's identification of the radius-one complex with a facet-stellar subdivision of the boundary of a convex \(4\)-polytope uses its exact half-space description. The resulting sphere and Weyl orientation conclusions are mathematical deductions, not output that a finite checker alone can establish. No stage starting at \(\sqrt3\) is analyzed, and the verified collapse itself is not a group-equivariant matching. Independent scientific validation is not represented or claimed.
