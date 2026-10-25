---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Strictly positive interior coefficients make every norm attaining vector have both endpoints of at least one edge equal +1 or equal -1. Convexity of the union of cube faces reduces the norm-attaining hull exactly to sign assignments with some monochromatic edge. Every maximizing sign vector either already lies in that hull, or is a proper 2-coloring and must flip a nonisolated coordinate; flipping the least |a_v| is feasible and optimal, proving the exact support L(a)-2 min_{v in V+}|a_v|. For nonbipartite graphs all signings are admitted, r=1. For bipartite graphs min≤L/k yields r≥1−2/k, while a proper coloring with active dual magnitudes 1/k realizes equality. Handles disconnectivity, ties, isolates, k=2 (r=0), and every interior weight. Independently enumerated 71 labeled graphs on 2–4 vertices and 40,204 exact integer dual comparisons; finite checks only corroborate the universal separation proof.

## originality

PASS

Kadets–Martín–Merí–Quero established the general quantitative generating-operator framework and finite-dimensional norm-attainment characterization; their open-access full article is not a theorem classifying edge-positive vertex-to-edge averages by graph bipartiteness with sharp radius 1−2/k. Known bipartite graph numerical indices concern other Banach spaces/invariants. The nonbipartite r=1 conclusion is largely a corollary of their criterion, but the support-function identity and bipartite exact quantitative branch survive.

## value

PASS

The formula is a precise universal and weight-independent quantitative norm-attainment invariant on a natural graph operator family, detects an extremal parity obstruction, and gives all cases including degeneracy k=2; it is more than a routine substitution in a general generating definition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
