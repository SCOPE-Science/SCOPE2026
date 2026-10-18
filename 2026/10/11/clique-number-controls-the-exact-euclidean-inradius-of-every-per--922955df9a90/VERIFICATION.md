---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

PASS: Chvátal's perfect-graph description yields all halfspaces x_v≥0 and x(C)≤1 for maximal cliques. Both classes are facets: coordinate faces have affinely independent 0 and singletons except v; for maximal C, singleton e_c (c∈C) plus stable pair e_u+e_{c(u)} for each u∉C with c(u) nonadjacent to u yield |V| affinely independent on x(C)=1. A Euclidean radius-r ball at center c is contained exactly when c_v≥r and c(C)+r sqrt(|C|)≤1. A maximum clique and c_v≥r force r≤1/(ω+sqrt ω). Uniform c=r*1 attains all inequalities since k+sqrt k increases with k. At r*, these inequalities themselves give the complete incenter set. Every maximum clique forces c_v=r* on its vertices; hence unique iff all vertices are in max cliques, otherwise a vertex outside every maximum clique has finite positive slack and can be perturbed. At the uniform incenter every coordinate facet and only maximum clique facets touch. Algebraically invert r* to recover ω and, for perfect G, χ. The n=1 and edgeless graph boundaries satisfy the argument. Small independent instances corroborated, not proof.

## originality

PASS

PASS best-of-knowledge with a significant immediate-corollary caveat. Chvátal's perfect-graph H-description, quoted by Hu–Laurent, supplies the full defining inequalities; the metric formula and center set follow using generic Euclidean inscribed-ball optimization. Kohl–Olsen–Sanyal put stable-set polytopes in a broader anti-blocking geometry context, but no explicit same-metric radius, full optimal-center locus, max-clique cover uniqueness, or tangent facet census was identified. The related same-week Hansen polytope radius result concerns a different higher-dimensional centrally symmetric lift and does not imply this particular Euclidean result via isometry. No Resultary result available; unindexed Chebyshev-center folklore remains a real priority risk.

## value

PASS

PASS: Even though the calculation uses the known clique H-description and elementary distance-to-hyperplane geometry, it determines a natural canonical geometric optimization quantity for every perfect graph, its complete optimizer polytope, a sharp uniqueness criterion equivalent to maximum-clique coverage, and all tangent facets. These geometric equality data translate core clique/coloring information into an exact metric invariant, providing more than a one-off substitution or single tiny numeric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
