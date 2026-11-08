---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For the Paley graph on F13 with quadratic-residue difference set {1,3,4,9,10,12}, independent induced-component counting over all 8192 masks reproduces face totals Ind1=79, Ind2=313 and Ind3=677 including empty. Ind1 has (13 vertices,39 edges,26 triangles), each edge in two triangles and every vertex link is a hexagon; the pinned signed 26-triangle fundamental cycle has integral zero boundary, so the oriented connected chi=0 surface is T2. Independently read CERTIFICATE.json and recomputed that its 26 signed tetrahedra are Ind2 faces and have oriented boundary exactly the torus cycle, proving the inclusion kills H2. The audited source verifies an acyclic Morse matching with one 0-, one 2- and two 3-cells and signed d3=(0,0), yielding Ind2 homotopy S2 wedge two S3. From simply-connected target and the 2-dimensional torus obstruction class, zero induced H2 implies the full torus inclusion is nullhomotopic. Independently implemented and checked every one of the 182 actual free-face/coface collapses from Ind3 to exactly Ind2, not a homology-only comparison. The 78 pure tetrahedral facets of Ind2 plus nonzero H2 imply nonshellability.

## originality

PASS

This is a new finite filtration-and-inclusion calculation of higher-independence complexes for the specific 13-vertex Paley graph. The published Deshpande–Singh higher-independence theory covers complete multipartite, whiskered, cycle and rooted-tree families and does not include this nonchordal Paley graph; the literature describing a torus embedding of Paley13 does not determine subsequent Ind2/Ind3 topology or inclusion map. No Resultary same-object match surfaced. Retain unindexed-computation risk.

## value

PASS

A Paley strongly regular graph is a canonical symmetric finite object, and its induced-component-cutoff filtration is a natural topological sequence. Establishing a nullhomotopic inclusion between stages with nonzero H2 and a literal simple-homotopy plateau is a structural result about maps rather than isolated Betti-number recomputation. Its explicit finite chain witnesses support future persistence and equivariant explorations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
