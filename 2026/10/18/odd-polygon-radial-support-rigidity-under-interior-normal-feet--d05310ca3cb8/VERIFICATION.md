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

## Analytical verification
The complete proof of the claimed odd-order uniqueness and local Jacobian nondegeneracy is in RESULT.md. The monotonic comparison uses the positive right-triangle angles supplied by a perpendicular foot **inside** each side; if a foot is outside, this argument must not be applied. The determinant of the sparse cyclic Jacobian consists of exactly two permutation products and is positive for odd order.

## Reproducible consistency checks
Run `python3 check_geometry.py` using Python's standard library. The program verifies the angle identity and positive Jacobian determinant numerically on 2,500 small perturbations of odd regular polygons, the exact coordinate-derived edge-support distances of a sample triangle, and an even-order family with identical measured data. These computations are not proof of global uniqueness and do not check possible literature priority.

## Review status
Self-review: passed. Independent audit: not yet performed.
