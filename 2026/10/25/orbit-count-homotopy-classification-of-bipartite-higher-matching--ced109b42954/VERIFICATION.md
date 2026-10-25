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

# Verification record

The self-contained `verify_rectangular_fixed.py` was executed using Python 3 standard-library functions. It enumerated all simplices of \(N_{a,b}\) for nine rectangles with \(2\le a,b\le4\), applied sequential greedy toggles, and found exactly one critical face of the predicted dimension in every case.

It separately compared orbit-expansion face conditions against rectangular quotient face conditions for 34 products of row and column cyclic actions on three- and four-point sets. All comparisons passed. The actual successful completion marker was:

`RECTANGULAR_FIXED_ORBIT_CHECKS_OK 9 34`

The code does not exhaust arbitrary subgroups or dimensions; the infinite homotopy assertion rests on the general barycentric-coordinate argument and matching proof in `RESULT.md`. Accompanying self-review is not an independent audit.
