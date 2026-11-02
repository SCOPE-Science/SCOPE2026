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

Run `python3 density_verify.py` using Python 3 standard library only. This independently compares the operator-word construction to direct nested partial-sum enumeration, and checks the exact binomial bound on all generated cases. All six test configurations printed `PASS` and the script ended with `VERIFY_OK` on the current source package. Finite tests are only consistency checks; the theorem follows from the word uniqueness and counting proof in RESULT.md. The threshold examples rely on standard real-logarithm comparisons; the theorem itself is an exact formula for an entropy exponent.
