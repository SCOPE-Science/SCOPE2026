---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For each of the 16 switched K5 pentagonal facets, a_W.x<=6-q with min=-q; independent exact rational Walsh check found sum_W q=80, sum_W a_W=0 and A^T A=16I_10. Reflection constraints sum to 0<=16(s-5), so s>=5; equality forces all K5 coordinates half. Facet classification of edge-maximal K3,3-minor-free H (Chimani et al Thm3.3) has only switched triangle/pentagon constraints; half vector realizes factor5 (triangles have factor3), and every optimum center obeys exactly the written triangle halfspaces plus K5 pinning. Strict triangle slack at the half vector is 1/6, establishing affine dimension equal to number of non-K5 edges. For nonmaximal G, coordinate projection from an edge-maximal supergraph and onto K5 copies proves the claimed s=5 and center pinning, without claiming full center dimension for nonmaximal G.

## originality

PASS

Best-of-knowledge statement-and-implication assessment against published results, primary texts and published mathematical records; negative search is not priority certification.

## value

PASS

A complete optimal-center locus and exact affine-dimension/uniqueness transition for non-edge-transitive graphs is a geometrically motivated refinement of cut-polytope asymmetry. It identifies which graph edges rigidly constrain optimal centers and which remain free, beyond a value for K5 alone. Uses nontrivial facet theory and Walsh rigidity, not a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
