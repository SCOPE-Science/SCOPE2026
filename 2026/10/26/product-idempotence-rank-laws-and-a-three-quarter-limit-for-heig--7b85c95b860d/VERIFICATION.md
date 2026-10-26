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

# Reproducible verification

Run `python verify.py` with Python 3 standard library. It constructs incidence-algebra matrices directly, enumerates idempotents over prime fields, counts products that are idempotent, and compares all three-rank coefficients with the closed weighted-label expression. Cases: a single edge over fields of size 2 and 3; a two-leaf star over 2 and 3; a three-leaf star over 2; a 2-by-2 complete bipartite poset over 2; disjoint edges over 2; a non-complete height-two fork over 2; and one edge plus isolated vertex over 3. Output ends in `VERIFY_OK`. Twenty symbolic integer evaluations of the star formula provide a separate arithmetic check. The theorem is proved for every prime-power field size and arbitrary finite height-two poset; enumeration checks do not prove this range, and field size four is used only in symbolic tests, not exhaustive finite-field matrix construction. No independent audit or certification is asserted.
