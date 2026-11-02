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

# Reproducibility and limits
The bundled `verify.py` is executable with Python 3 and standard-library dependencies only. Run `python3 verify.py` from a directory containing that file. It independently computes the binary-partition recurrence, checks the three-square obstruction by removing factors of four, verifies the exceptional-digit characterization, tests the four sixteen-site blocks, checks the eight transition types, and tallies all six gap counts. A successful run prints `VERIFY_OK` along with its tested ranges and integer tallies.

The finite calculations do not certify the limiting frequencies, an unlimited gap bound, or logarithmic error constants. The symbolic proof in `RESULT.md` derives those facts from the given recurrences; the checker serves as an exact-arithmetic consistency test. The quoted originality comparison is a bounded literature comparison, not an independent or exhaustive priority certification.
