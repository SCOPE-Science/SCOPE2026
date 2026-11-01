---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Every selected doubled subdivision incidence identifies one matching edge of the original graph, and different double-incidence vertices have disjoint original endpoints. After deleting these matched endpoints, selected single incidences have original centers C and opposite original endpoints in U, with no other restrictions. This is an invertible partition of all packings and proves the complete edge-size generating function for every finite simple G (empty/disconnected allowed). Maximizing selected incidences gives 2|M|+maxcut(G−V(M)); for K_n the endpoint maximum of f_n(k)=2k+floor((n−2k)^2/4) yields floor(n²/4) at n>=5 and balanced ordered cut extremizers, with separately evaluated n<=4 exceptions. A fresh conflict-graph subset enumerator checked each of 75 labelled simple graphs through 4 vertices and K5 coefficients (1,20,130,340,355,120,20), agreeing with the independently implemented matching/center formula. Enumeration supports, but is not a replacement for, the general bijection.

## originality

PASS

The induced-star structure and definition of edge-open packing are prior work; this result is assessed only for the canonical matching/center decomposition of arbitrary full one-subdivisions, the exact full generating function and matching-deletion max-cut formula, and the closed labelled K_n extremal count. Originality is best-of-knowledge, not a claim that the general induced-star observation is new.

## value

PASS

An exact full generating polynomial for all one-subdivisions of arbitrary finite simple graphs, plus a matching-deletion maximum-cut reduction, links two classical graph optimization structures. The sharp labelled complete-graph extremal census has natural combinatorial use beyond isolated small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
