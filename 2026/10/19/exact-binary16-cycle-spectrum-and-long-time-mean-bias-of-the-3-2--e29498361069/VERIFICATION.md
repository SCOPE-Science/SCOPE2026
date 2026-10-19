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

# Reproducibility and evidence limits

The supplied `CHECKER.py` is a standalone standard-library program. Execute with `python3 CHECKER.py` to enumerate all \(15360\) finite binary16 states, reconstruct the successor function from integer midpoint rounding, perform a complete functional-graph decomposition, verify every period, basin and entry-time record, and check the exact successor-table hash. It also integrates Voronoi cell sizes in rational arithmetic to verify the uniform-real-initialization probabilities and computes the exact invariant Cesàro averages. For the real beta map it bounds the invariant mean by a \(120\)-term Parry-series enclosure, with an explicitly bounded tail, and tests the stated strict gap interval. The checker was run to completion with all assertions passing.

A distinct NumPy binary16 multiplication-and-subtraction evaluation matched the integer-defined transition at every state. This cross-check is supplementary; the standalone exact-integer checker is the complete enumeration proof.

The comparison is valid only for roundTiesToEven binary16 with retained subnormals, nearest rounding of multiplication, and subtraction of one after the rounded product. The exact finite-graph result does not establish statements about other precisions, stochastic arithmetic, other parameters, or independent external validation.
