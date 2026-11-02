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

The accompanying `verify.py` independently enumerates every partial injection and directly tests adjacency preservation and reflection for graph sizes up to seven. This checked seven parameter configurations, including the exceptional complete-graph and star cases. All rank coefficients matched the closed formula; output ended in `VERIFY_OK`. Additional formula boundary checks covered 42 parameter pairs. Independent induced-subgraph grouping, performed separately, confirmed the predicted number of isomorphism types in four configurations, including ten-vertex windmills.

The proof of the all-parameter theorem is combinatorial. Exhaustive checks for small graphs do not prove the formula for unbounded parameters, and the external literature comparison does not establish independent priority or an independent audit.
