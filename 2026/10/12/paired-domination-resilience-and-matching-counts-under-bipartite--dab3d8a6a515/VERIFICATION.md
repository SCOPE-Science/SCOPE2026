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

If selected set D admits an induced perfect matching in a bipartite graph, it has s vertices on each shore. For s>=2, every omitted vertex sees at least s-1 selected opposite vertices because deleted edges form a matching; Hall holds on D since a singleton has at least s-1 neighbors and any >=2 selected vertices jointly see all s opposite selected vertices. Thus every balanced D with s>=2 is paired dominating. For s=1, domination and a matching are simultaneous exactly when both chosen endpoints are untouched by deletion. Counting gives (m-t)(n-t)x^2+sum_{s>=2}C(m,s)C(n,s)x^(2s), total C(m+n,m)-1-t(m+n-t), and gamma 2 or 4 at the stated t boundary. Pairing-weighted coefficients for s>=2 count s-edge matchings avoiding t disjoint forbidden edges; inclusion-exclusion yields sum_j(-1)^j C(t,j)C(m-j,s-j)C(n-j,s-j)(s-j)!, with s=1 restricted to untouched endpoints. Direct independent subset and induced-perfect-matching enumeration for every 2<=m,n<=4 and each 0<=t<=min(m,n) verified all polynomial and weighted coefficients, including disconnected K_2,2-M_2.

## originality

PASS

Prior published complete-multipartite formula covers only t=0, the complete biclique. For t>=1 the missing edge means the graph is not complete multipartite; the published chain-graph theorem is also inapplicable for t>=2 because deleting two disjoint cross edges creates induced 2K2 (chain graphs are 2K2-free). The 2016 conference abstract is too sparse to infer noncoverage, but no checked full text proves all-t resilience and matching-witness polynomial. Best-of-knowledge original outside known t=0 and known crown minimum 4.

## value

PASS

The all-set coefficient invariance despite deleting any matching is a sharp fault-tolerance fact: pair feasibility changes only in two-vertex coefficient while the pairing-weighted enumerator still changes at higher degrees. This distinguishes preserved robust placements from lost backup pairings and fully classifies a natural entire edge-fault family, beyond scalar domination numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
