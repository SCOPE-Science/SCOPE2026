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

The arbitrary-order proof is a direct classification, not a finite inference. If no independent vertex is empty, feasibility is automatic unless a clique vertex is empty, in which case only the two monochromatic global label families fail. If an independent vertex is empty, both colors must occur on the clique, and that condition is also sufficient. These disjoint cases yield the closed polynomial by elementary inclusion-exclusion.

The standalone checker `verify.py` rebuilds the graph, tests the literal definition on every labeling, and compares the complete coefficient vector with an independently coded polynomial formula for all \(2\le r,n\le4\). It also checks the minimum coefficient and evaluation at \(x=1\). Replay output:

`VERIFY_OK r_range=2..4 n_range=2..4 labelings=112896 coefficient_checks=117 minimum_checks=9 total_checks=9 max_order=8`

The replay covers orders through \(8\) only. It is used to detect boundary and transcription errors; the proof supplies the quantification over all \(r,n\ge2\).
