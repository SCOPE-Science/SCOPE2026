---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

`verify.py` is a dependency-free exhaustive checker for the finite claim. It generates all binary words of length nine, filters bifix-free vertices, constructs the mutual cross-bifix compatibility graph, and enumerates every clique of cardinality fourteen by strictly increasing vertex index. The replay used for this result produced 148 vertices, 3,080 edges, 1,152 size-fourteen cliques, the minimum-distance histogram 1:1148 and 2:4, and one orbit of size four among the distance-two cases under complement and reversal.

The checker verifies only the new finite refinement. The fact that fourteen is the global cardinality optimum is also independently supplied by the cited primary source, whose Table I and accompanying maximum-clique paragraph were inspected. No claim is made for other lengths or alphabets.
