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

The verifier constructs every friendship graph \(F_r\) for
\[
2\le r\le8.
\]
It computes all-pairs vertex distances by breadth-first search and then forms the local edge-resolving neighborhood of every pair of adjacent edges directly from
\[
d(w,e)=\min\{d(w,x),d(w,y)\}.
\]

It checks symbolically that every two center edges \(cu,cv\) have local edge-resolving neighborhood exactly
\[
\{u,v\},
\]
and that the two remaining blade-pair neighborhoods match the formulas used in the proof.

The complete fractional linear program is then solved independently for each \(r\). Finally, every coordinate is minimized and maximized over the optimal face to verify uniqueness.

Recorded output:

```text
VERIFY_OK
friendship_parameters_checked = 2..8
adjacent_edge_pairs_checked = 441
lp_instances = 7
optimal_face_coordinate_checks = 77
all center-edge resolver neighborhoods were exactly the two outer endpoints
all blade-edge resolver neighborhoods matched the symbolic formulas
all LP optima equaled r
all optimum faces were the unique weighting: center 0, every outer vertex 1/2
```

The finite LP computation is corroborative only. The arbitrary-\(r\) value and uniqueness follow from the proof.
