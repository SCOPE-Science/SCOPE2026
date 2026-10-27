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

The infinite coefficient-extraction proof and exact sign inequalities appear in `RESULT.md`. The independent finite enumerator `check.py` was executed with `python3 check.py` and returned `VERIFY_OK`. It checks six triples by two separate specifications: legal-word recursion and full-block concatenation, plus the bijection to actual recurrence intervals. Its rational certificates bracket the dominant roots for \((p,q)=(3,1),(20,1)\), while the golden-root identity handles \((2,1)\).

Finite enumeration is a consistency check rather than a proof of the limiting law. The limiting claim rests on the displayed rational word generating function, pole aperiodicity, and marked-block coefficient ratios. No independent external review or certification is claimed.
