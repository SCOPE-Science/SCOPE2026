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

The accompanying `verify_kp_first_defect.py` implements direct Heyting implication on all downsets of naturally labeled posets and separately checks the local set-inclusion failure criterion for posets through five points. It runs with unmodified standard Python 3 using `python3 verify_kp_first_defect.py`.

All natural-label posets of one through six points were enumerated (1, 2, 7, 40, 357, 4824 respectively), totaling 5231. The counts of posets with positive defect were (0, 0, 0, 1, 38, 1212). Each positive case had at least eight bad ordered triples. The only nine-element nonvalid algebra appearing on four points has exactly 24 failures, and the explicit constructed family at carrier orders 11 through 30 has exactly eight failures per case. The direct and local predicates agree on all posets of at most five points.

This finite computation does not certify universal propositions on its own; the proof in `RESULT.md` gives the uniform argument. Independent scientific audit has not been performed.
