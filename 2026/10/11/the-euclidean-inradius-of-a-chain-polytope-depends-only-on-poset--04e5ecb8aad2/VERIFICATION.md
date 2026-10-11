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
The arbitrary-poset proof is given in `RESULT.md`.

Critical checks:
- the source chain polytope has coordinate nonnegativity facets and maximal-chain inequalities;
- a maximal chain with \(k\) elements has facet normal of Euclidean norm \(\sqrt k\);
- every radius-\(\rho\) inscribed ball has all coordinates at least \(\rho\);
- a longest chain forces \((h+\sqrt h)\rho\le1\);
- the point \(r\mathbf1\), \(r=(h+\sqrt h)^{-1}\), has clearance at least \(r\) from every maximal-chain facet;
- all optimal centers are exactly the points satisfying the displayed shrunk facet system;
- a longest-chain facet forces every coordinate on that chain to equal \(r\);
- if an element lies on no longest chain, every chain containing it has positive residual slack, so a small one-coordinate perturbation preserves optimality.

`verify.py` enumerates all naturally labeled posets on at most five elements, deduplicated after transitive closure. It computes all maximal chains, verifies the exact candidate clearances symbolically, checks the longest-chain coverage criterion, and constructs a positive perturbation in every nonunique case. Finite computation is corroborative only and does not assess originality.
