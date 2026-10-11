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

The theorem is proved analytically in `RESULT.md`. The accompanying `verify.py` is an independent finite consistency check of the facet optimization.

For each unordered multipartition of \(n\) with at least three parts and \(3\le n\le8\), the checker constructs the complete multipartite graph, fixes one labeling value to zero, exhausts the finite labeling range forced by the graph diameter and edge-Lipschitz condition, keeps exactly those labelings whose tight-edge graph is connected, computes the projected-normal squared norm using exact rational arithmetic, and compares the maximum with the closed formula.

Expected replay output:

`VERIFY_OK complete-multipartite symmetric-edge inradius partitions=42 facet_labelings=5868 n=3..8`

The finite search does not prove the arbitrary-\(n\) theorem and is not presented as exhaustive literature evidence. The infinite proof depends on the published complete-multipartite facet classification and the elementary norm optimization in `RESULT.md`.
