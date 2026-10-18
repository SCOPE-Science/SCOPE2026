---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Read the full RESULT.md and verify.py at the assigned tree. Distinct duads are graph-distance 2 exactly if disjoint and 4 otherwise; distinct synthemes distance 2 iff they share a duad and 4 otherwise; every duad-syntheme pair has distance 1 or 3. Hence threshold3 graph has all 225 cross edges and the two internal factor graphs, giving an ACTUAL simplicial join, not a homology-only assertion. Independently enumerated all 15 duads and all 15 perfect matchings on six elements. Each factor has 15 vertices,45 edges,15 triangles, no 4-cliques, is connected, and every edge belongs to a unique triangle. Elementary collapse of one edge per triangle leaves 15v30e connected graph and hence wedge^16 S1; join-smash yields wedge^(16*16) S3. The supplied verifier additionally checks full 30-vertex threshold3 f-vector (30,315,1380,2475,1350,225) and GF2 Betti 256, but mod2 rank alone would be weaker than the structural homotopy proof. Integer-distance constancy justifies the entire interval 3<=r<4.

## originality

PASS

Searches with Tutte--Coxeter, Tutte 8-cage, Cremona--Richmond, GQ(2,2), duad--syntheme, generalized quadrangle and 256-sphere Rips aliases found no independent published coverage. The closest primary McCabe 2026 generalized-polygon paper proves girth-stability of graph-power clique complexes only for g>=3j+1: at g=8 and j=3 it is inapplicable. The Platonic-solid Rips paper concerns different metric sets and points toward buildings only as future direction. The structural join factorization is not implied by either theorem, though unindexed classical graph-power calculations remain a residual risk.

## value

PASS

The Tutte--Coxeter graph is the canonical smallest thick GQ(2,2) rank-two building incidence graph, and scale3 is the first beyond the available girth8 stability range. The natural exact invariant 256 independent three-spheres follows from explicit two-sided geometry, not a numerical log or an arbitrary parameter slice. The result is a complete natural finite-object homotopy classification useful in VR/genus and generalized-polygon comparisons; no general theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
