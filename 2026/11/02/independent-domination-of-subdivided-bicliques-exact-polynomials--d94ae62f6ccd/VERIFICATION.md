---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Every maximal independent set I of S(G) is uniquely determined by U, the omitted original vertices: subdivision vertex s_uv is selected iff both u,v lie in U; every u in U is dominated iff G[U] has positive degree at u. Thus for all finite simple G the weight is |V|-|U|+|E(G[U])|. For K_ab nonempty admissible U meet both shores with sizes p,q and pq edges, giving the exact double binomial sum and its support a+b-1+(p-1)(q-1). The empty U term coincides with product 1 when a,b>=2; boundaries a=1 and n=2 are explicitly handled. Ford’s known multiplication-table order, not a new proof, yields sparse support; independent adjacency-based brute force checked five small bicliques including stars.

## originality

PASS

Best-of-knowledge original all-graph complete-subdivision transform and exact all-shore-size biclique polynomial with arithmetic support gaps. Known independent domination subdivision number and known multiplication-table estimates are acknowledged as distinct prior components.

## value

PASS

A natural complete transformation for independent-domination enumerators and a nontrivial full family with extensive structured missing cardinalities connect graph extremal enumeration to the multiplication-table problem; exact coefficients and support can inform further graph-polynomial classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
