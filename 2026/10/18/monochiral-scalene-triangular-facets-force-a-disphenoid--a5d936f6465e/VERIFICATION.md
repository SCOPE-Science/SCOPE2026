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

# Mathematical verification

The proof in `RESULT.md` is analytic and self-contained. Reconstruct the oriented vertex link; because every facet has outward cyclic lengths in the same order, each transition advances the edge-length color by one position modulo three. The closure condition gives \(q\equiv0\pmod3\), and the angle sum equals \(q\pi/3\). Positive curvature at every extreme convex vertex forces \(q=3\). Euler and triangular facet incidences then yield \(V=F=4\), and opposite-edge equality plus the explicit disphenoid coordinate formula proves the precise acute boundary.

A separate finite consistency check labeled opposite tetrahedral edges by three distinct symbols and used an oriented boundary face list \((1,2,3),(0,3,2),(0,1,3),(0,2,1)\). The resulting cyclic words were \((c,a,b),(c,a,b),(a,b,c),(b,c,a)\), all cyclically equivalent; numerical side-length checks gave positive squared coordinates \((45/8,27/8,5/8)\) for \((4,5,6)\), zero for the right triple \((3,4,5)\), and a negative coordinate for \((4,4,7)\). Those finite checks confirm normalization and boundary behavior only.

Full-text material was read in the 2026 motivating preprint and in the author-hosted 2000 icosahedron paper. The theorem does not apply to mirror-mixed or isosceles/equilateral triangular facets, nor does it classify nonconvex surfaces. An independent audit has not yet been performed.
