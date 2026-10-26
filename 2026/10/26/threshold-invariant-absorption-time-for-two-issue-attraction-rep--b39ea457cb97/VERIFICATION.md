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

Run `python verify.py` with Python 3 standard library. The checker loops over all four-string population count compositions for population sizes 2 through 7, several rational weight/threshold choices away from ties, and computes focal/target/issue transitions from the source model rule. It checks exact birth/death rates and verifies the harmonic expectation recurrence for every nonabsorbing size 2 through 49. It also tests two-agent outcome-type differences and the neutral frozen boundary at similarity ties. These are finite regressions; the proof in RESULT.md establishes the general statement. No external audit or independent validation has occurred.
