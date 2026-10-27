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
Execute `python3 verify_rank2.py` using standard-library Python 3. It enumerates 1,235 fan parameter triples and implements exact rational feasibility of anticanonical and canonical restriction polytopes at every divisor ray, plus exact integer determinants for all invariant curve walls. It prints `VERIFY_OK` and confirms the \(\mathbb F_2\) witness. The test is finite; the proof in `RESULT.md` establishes the statement for all integers.

Mathematical dependence: the established general invariant-orbit-closure criterion is applied to the two sections, four vertical surfaces, invariant curves, and the full variety. The product inequalities, strict negative-section wall, and exceptional zero-degree curve wall follow separately. Neither exhaustive infinite enumeration nor external certification was attempted. Historical priority outside the inspected sources remains uncertain.
