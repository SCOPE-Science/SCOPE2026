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

In K_{n_1,...,n_r}, distinct parts are adjacent and within-part pairs have distance 2, with every vertex of another part serving as middle. Therefore an omitted v in part i is on a geodesic between selected endpoints exactly when some j≠i contains at least two selected vertices. Writing H={i:s_i>=2}, all geodetic sets have at least two heavy parts; or exactly one heavy part fully selected; or no heavy part only when all parts are singletons and S=V. Counting no-heavy choices with A_i=1+n_ix and heavy with B_i=(1+x)^{n_i}-A_i yields g_G(x)=(1+x)^N-∏A_i-∑_i B_i∏_{j≠i}A_j+∑_{i:n_i>=2}x^{n_i}∏_{j≠i}A_j+1_{max n_i=1}x^N. Direct minimum is m if exactly one nonsingleton part, min(m,4) with at least two, and N for complete graphs. Exhaustive independent literal-shortest-path subset enumeration matched the criterion and polynomial for 102 part configurations (r=2..4, n_i=1..3, N<=9). This finite check is supplementary to the arbitrary-r exact structural argument.

## originality

PASS

The foundational geodetic-polynomial article defines the cardinality enumerator and treats unspecified specific graph families in its accessible abstract, while scalar geodetic-number algorithms and multipartite strong/edge/Steiner variants concern weaker or different invariants. The all-set ordinary-geodetic classification plus a closed polynomial for arbitrary multipartite part sizes was not recovered as prior full statement. The 2012 original article's full eight pages were inaccessible, so genuine older coverage remains a material risk; access failure alone is not treated as scientific failure.

## value

PASS

A complete cardinality enumerator for geodetic sets is a natural and potentially reusable refinement of the geodetic number, especially for multipartite graphs where every shortest path is length at most two. The all-part-size classification and exact coefficient polynomial supply information unavailable from the known scalar algorithms, not a recomputation of a known single minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
