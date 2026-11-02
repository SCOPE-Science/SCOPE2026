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
Run `python3 checker.py` using Python 3 standard library only. The program enumerates all injective partial self-maps on labelled vertex sets of cardinalities zero through five, determines directed paths/cycles directly from the maps, and separately enumerates odd-order full permutations to compare against the claimed formula. Its one-vertex tests enumerate odd-order permutations of sizes one through five and verify every minimal one-point completion whose old set has size at most four. The distinguished-cycle recurrence is computed independently from the factorial and double-factorial expression for parameter pairs in the tested ranges.

The expected terminal output is `ALL_CHECKS_OK`. The checker tests finitely many instances; the theorem for arbitrary finite sets follows from the bijections in the proof. External audit is not included.
