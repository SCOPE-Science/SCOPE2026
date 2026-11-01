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

# Reproducible verification

Execute `python3 verify.py` with Python 3 and no nonstandard packages. The program works with `fractions.Fraction`, enumerates retained cube vertices and cut-edge crossings, constructs the explicit candidate directions, checks all strict active-facet inequalities, checks the disjoint lower-bound witness requirements, and independently enumerates polytope vertices from facet intersections for selected small dimensions.

Actual execution result:

`VERIFY_OK weighted cube-cap illumination: 354 exact parameter systems; 15035 checks`

The tests cover representative rational positive weight vectors in dimensions two through six, both exact subset-sum thresholds and interior thresholds. The independent full-vertex reconstruction covers selected instances in dimensions at most four. The equal-weight binomial formula was independently checked through dimension ten. These are finite consistency checks, not a proof for all dimensions or arbitrary real weights.

The universal proof in RESULT.md explicitly treats arbitrary positive real coefficients, threshold equality cases, the all-negative corner, and the conversion from vertex to full-boundary illumination. Mathematical correctness and original priority have not been externally certified.
