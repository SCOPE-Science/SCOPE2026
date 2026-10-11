---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The exact vertex-edge distances were reconstructed from the nested neighborhoods. Any transversal of \(P_r=\{a_r,b_{r+1}\}\) first separates unequal row indices and then unequal column indices. For the lower bound, landmarks on the ordered row-star edges act only as single-position markers or one-threshold markers, so \(k\) effective landmarks create at most \(k+1\) codes and at least \(p-1\) are required. Applying the same bound to prefix and suffix star subfamilies at equality excludes the ineffective endpoints and forces exactly one landmark in every \(P_r\). Independent exhaustive enumeration for \(2\le p\le8\) found no generator of size \(p-2\) and matched the transversal classification exactly.

## originality

PASS

The inspected edge-metric literature does not imply the half-graph all-bases theorem. The founding paper has no half/chain/Ferrers result, while the later connected-bipartite theorem characterizes only the different extremal value order minus two. Searches under half graph, chain graph, Ferrers graph, edge resolving set, and edge metric basis found no earlier statement giving the pair-transversal classification, \(p-1\) value, or \(2^{p-1}\) count.

## value

PASS

Half graphs are the canonical twin-free chain graphs. The result determines not only a scalar edge metric dimension but every minimum edge-resolving set and its exact count, exposing a rigid local pair-transversal structure. That is a natural complete classification rather than a routine example computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
