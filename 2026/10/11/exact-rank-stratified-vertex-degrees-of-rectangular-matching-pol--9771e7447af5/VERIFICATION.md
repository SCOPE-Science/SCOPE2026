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
# Reproduction checks
Run `python3 verify.py` from the directory containing the files. The verifier uses only the standard library and independently builds the one-skeleton from connected alternating symmetric differences. It tested ten rectangular parameters and 1,011 vertices by exhaustive pair comparison, and the inequality profile at 820 integer-parameter pairs. Exact comparison of all four alternating component classes and the recurrence is provided in RESULT.md. These finite checks do not establish the universal statement; that follows from the separate proof. The full text of the 2022 square-matrix face article was unavailable, so it was not used to assert noncoverage.
