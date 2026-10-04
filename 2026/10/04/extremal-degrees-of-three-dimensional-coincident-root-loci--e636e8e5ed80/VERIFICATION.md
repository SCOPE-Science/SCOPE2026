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

The proof was replayed from Hilbert's degree formula for every three-part partition with \(3\le d\le500\) using exact integer arithmetic. For each \(d\), the checker forms all ordered representatives \(1\le a\le b\le c\), evaluates \(6abc/\prod_j e_j!\), and compares the exhaustive extrema with the theorem's closed forms.

The replay also verifies the four exceptional degrees and uniqueness of every claimed extremizer. No floating-point comparisons are used. The finite replay does not replace the uniform proof; it is a regression check on the formulas and case boundaries.

Limits: no higher-partition statement is checked or claimed, and no computation of dual or polar degrees is included.
