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

# Verification record

Run `python3 check.py` from the directory containing `ANGLE_FORMULA.json`. The code uses only the Python standard library. Exact integer operations in the Tribonacci cubic field verify all 38 supporting faces, all edge incidences and five-cyclic vertex links, the complete 31-great-circle spherical subdivision, the sign-chamber counts, and all eighteen angle types and four coefficient vectors recorded in `ANGLE_FORMULA.json`. The independent 3,000-view planar hull comparison and floating-point evaluation of arccosine values are supplementary numerical checks. Neither finite random testing nor successful process termination alone is treated as a proof; the exhaustive exact sign-cell decomposition supplies the finite combinatorial proof for every generic normal. There is no external audit or independent validation.
