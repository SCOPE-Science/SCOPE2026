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
The proof reduces strong domination in a complete multipartite graph to the exact degree-order condition \(b\le a\) between the sizes of the dominator's part and the dominated vertex's part. The three resulting forms of \(\gamma_{st}\) are then applied after deletion.

The bundled checker independently enumerates candidate strong dominating sets and proper vertex-deletion sets for every noncomplete complete multipartite profile of order at most \(8\). It does not use the closed formulas to compute the direct values. The replay result is:

`ALL CHECKS PASSED; profiles=51; gamma_checks=51; stability_checks=51; order_range=2..8`

Finite verification is not used as an infinite proof. The arbitrary-order theorem is established by the analytic part-size argument in `RESULT.md`. The result does not cover complete graphs or strict-degree variants of strong domination.
