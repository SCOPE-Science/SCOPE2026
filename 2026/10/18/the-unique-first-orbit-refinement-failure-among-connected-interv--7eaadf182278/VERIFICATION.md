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

# Verification record

The three included executable scripts were run from their included source files with Python 3 and NetworkX 3.6.1. Their full standard output files are included. The two complete exhaustive enumeration implementations agree on 1,328 connected eight-vertex interval graphs and one non-refinable isomorphism type. The explicit witness checker derives the group order \(8\), cells \(2+6\), and three orbits \(2+2+4\) from actual adjacency data.

The proof of completeness requires the simplicial elimination property of interval graphs, the complete seven-vertex graph atlas, and the exactness of the finite graph predicates and GraphMatcher. This is an executable finite mathematical argument, not a proof about arbitrarily many vertices. Agreement with independently published connected interval-graph counts provides a consistency check; matching counts alone would not certify the exceptional-isomorphism uniqueness. No external audit was performed.
