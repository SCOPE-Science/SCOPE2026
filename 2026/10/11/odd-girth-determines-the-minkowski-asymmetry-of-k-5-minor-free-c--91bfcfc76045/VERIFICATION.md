---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Cut vectors span every coordinate by the identity 2e_uv=delta(u)+delta(v)-delta({u,v}); uniform switching makes the center c*=1/2 feasible and optimal by convexity of the fixed-rho center set. Corollary 3.10 of Barahona--Mahjoub supplies ALL cycle inequalities and necessary edge bounds. At c*, odd cycle length l contributes ratio l/(l-2); even cycles and bounds contribute 1. Every shortest odd cycle is chordless. Hence global maximum gives the formula, including disconnected/bipartite cases. Inspected standard-library exact finite checker, which corroborates but does not prove arbitrary graph size.

## originality

PASS

The classical all-facets theorem and switching symmetry are prior ingredients. Their conjunction with the explicit facet-reflection minimax is an exact new odd-girth law not shown in the inspected source; no stronger matching result found in the targeted published search.

## value

PASS

The answer recovers a global affine-invariant convex-geometric quantity from one elementary graph statistic for the natural K5-minor-free class, with sharp triangle, long-odd-cycle and central-symmetry boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
