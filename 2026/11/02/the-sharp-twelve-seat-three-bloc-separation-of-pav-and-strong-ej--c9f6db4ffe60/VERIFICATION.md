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

The result has a complete symbolic proof in `RESULT.md`. The exact-rational, standalone `check_family.py` verifies the PAV score differences and the strong-EJR+ coalition-payment formula for 810 small positive-integer parameter choices; all 55 necessary-inequality instances with committee size below 12; and unique PAV/strong-EJR+ separation for the explicitly constructed family at committee sizes 12 through 24. At twelve seats it checks all 1716 distinct coalition-type vectors, and obtains the strict deficit 1/984.

Reproduce with `python3 check_family.py` after extracting all files in this record to one directory. The analytic proof, not the finite tests, establishes the unbounded statements. The result is scoped to the specified three-bloc family and does not claim a global minimum. No independent audit has been performed.
