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

Reproducibility: `python verification.py`, with dependencies in `requirements.txt`. The script builds the complete finite supporting-facet triangulations of the four-dimensional primal and polar polytopes at interior sample heights one and three. Their vertex positions, supporting facets, strict orientations, and interval-wide halfspace slacks are checked symbolically as rational functions in the height parameter. Volume expressions and exact positive-coefficient transformations of the Mahler gap are checked algebraically for both regimes and the shared transition. Random or sampled numerical volumes cannot alone prove this infinite-parameter claim; the interval-wide rational identities and boundary triangulation certificate supply the argument. The theorem covers exactly \(t>0\) in dimension four, not a larger convex-body class.
