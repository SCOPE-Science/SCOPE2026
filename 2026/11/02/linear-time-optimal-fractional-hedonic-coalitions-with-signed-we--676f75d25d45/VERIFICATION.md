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

# Verification and reproducibility

Run `python verify.py` using Python 3 standard library. This computes the proposed optimum and explicit witness on connected weighted paths and cycles as well as disconnected maximum-degree-two graphs; independently enumerates **all** unrestricted set partitions on the same small vertex sets; compares exact rational welfare values and actual witness welfare; and checks the two structural sharpness examples.

The run checked 2,209 connected path/cycle instances and 580 disconnected instances. Edge weights range over negative, zero, and positive rationals; for paths/cycles with at most six edges the ternary choices are exhaustive, and the remainder are seeded random instances. The code also implements the six-case cycle recurrence and has a separate path recurrence. The implementation accepts rational weights and represents all results exactly with `fractions.Fraction`.

The finite enumeration does not prove the universal statement. The proof's nonstandard step is the comparison of the original contribution \(2W/q\) with a positive-weight matching on a path, even cycle, or odd cycle. For odd cycles of length \(q\ge5\), \(q\) rotations give an average matching weight \((q-1)P/(2q)\), which dominates \(2W/q\) because \(P\ge W\) and \(q-1\ge4\). The remaining recurrence is an exhaustive enumeration of the permitted connected tiles.

The published literature comparison, uninspected material, and possible equivalent formulations are recorded in AUDIT.json. Independent validation or proof checking by an external party has not been performed.
