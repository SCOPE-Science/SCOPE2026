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

`checker.py` requires Python 3 standard library only. Running `python checker.py` reconstructs paperfolding prefixes directly from their arithmetic definition, compares two rotation-sorting implementations on ranks two through nine, verifies the full explicit BWT formula and run count through rank fourteen, and checks the exact sixty-four macrotype/offset cases against all twenty-eight seven-factor classes. The expected last output line is `VERIFY_OK`.

The source certificate is the finite local classification in `SEVEN_GRAM_TABLE.md`. Completeness in all ranks follows from the infinite induction in `RESULT.md`, not from finite samples. The proof and checker both concern sentinel-free circular BWT only; no sentinel-terminated result or independent mathematical audit is claimed. The historical-priority comparison may be incomplete.
