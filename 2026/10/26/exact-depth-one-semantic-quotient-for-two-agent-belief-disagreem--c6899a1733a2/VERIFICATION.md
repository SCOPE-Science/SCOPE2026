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

# Verification of the depth-one disagreement theorem

`python3 checker.py` needs Python 3.10+ and the standard library only. The checker enumerates all ordered pairs of nonempty supports on \(m=1,2,3,4,8\) abstract valuations; for each pair it computes the complete Boolean event-test signature, compares it to the claimed null/disjoint-pair invariant, and checks the exact class count. It separately verifies the row criterion for KD45 in both two-world models and evaluates disagreement once and twice. On successful replay it prints `ALL_CHECKS_OK`.

**Logical scope of the checks:** The quantified theorem for every finite number of propositional variables and arbitrary (possibly infinite) KD45 models is proved in `RESULT.md` by the event-test lemma, explicit finite realization, and counting. Exhaustive enumeration at five valuation alphabet sizes does not prove an infinite statement. No independent audit or external validation has been performed.
