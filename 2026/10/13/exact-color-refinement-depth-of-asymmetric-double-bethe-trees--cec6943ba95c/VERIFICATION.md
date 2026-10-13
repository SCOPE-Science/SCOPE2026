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
The attached `verify.py` independently implements the exact weighted quotient recurrence and, on a smaller range, constructs every graph explicitly and runs ordinary color refinement vertex by vertex.

It verifies every \(2\le d\le5\) and \(1\le a,b\le25\) in the quotient model, and every \(d\in\{2,3\}\), \(1\le a,b\le4\) as full graphs. The latter checks both depth and the predicted automorphism-orbit partition.

The checker returns:

`VERIFY_OK quotient_depth_checks=2500 full_graph_checks=32 orbit_checks=32 d=2..5 a,b=1..25; full d=2,3 a,b=1..4`

These finite checks are corroborative only. They do not replace the all-parameter weighted-path proof in `RESULT.md`.
