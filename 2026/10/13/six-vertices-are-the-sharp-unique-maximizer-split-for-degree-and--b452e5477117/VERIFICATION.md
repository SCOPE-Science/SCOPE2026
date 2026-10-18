---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For every connected simple undirected labeled graph through six vertices, reconstruct degree, closeness (n-1)/distance sum, and unnormalized Freeman betweenness (shortest-path shares over unordered endpoint pairs). An independent complete 2^(n choose 2) graph enumeration, exact-rational shortest-path counting and canonical isomorphism reduction obtains connected counts (1,1,4,38,728,26704), unique degree/betweenness leader disagreements (0,0,0,0,0,720), tie-level set differences 150 at order five, and a single asymmetric six-vertex class of orbit 720. Its edge representative {01,03,05,12,13,14,23,24} has unique degree/closeness leader vertex 1 and betweenness leader vertex 0. Complete finite enumeration proves the bounded claim, no assertion for n>6.

## originality

PASS

The familiar qualitative inequivalence of degree, closeness and betweenness is classical and not new. Independent comparison considers stronger family formulas and the exact graph-isomorphism boundary: Freeman defines the measures, and Unnithan et al. calculate betweenness in paths, stars, wheels, bipartite graphs and trees without a theorem classifying the least order of distinct unique maximizers. No dominating published exact 720/26704 first-layer classification was found; this is best-of-knowledge originality, not guaranteed novelty.

## value

PASS

The first graph order at which two canonical centrality notions choose different unambiguous leaders is a motivated structural threshold. Its unique isomorphism witness and exact orbit count tell network-centrality researchers how the divergence arises, and clarifying the order-five tie case prevents a misleading threshold statement. Finite classification is a substantive completed natural census, not an arbitrary numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
