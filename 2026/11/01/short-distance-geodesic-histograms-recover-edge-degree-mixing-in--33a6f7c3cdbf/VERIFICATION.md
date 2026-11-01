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

The embedded `verify.py` independently computes each unit-square probability as a union of four affine shortest-route sublevel sets, with exact rational polygon clipping and inclusion–exclusion. All tested graph/radius pairs agree exactly with the claimed quadratic spline. It explicitly verifies that the two witness graphs have invariants \((5,12,24)\) and \((5,12,23)\).

Finite verification does not prove a universal graph theorem: the written proof establishes route exhaustiveness up to \(3/2\) and the independent exact computations check its boundary and arithmetic. Independent scientific audit has not been performed.
