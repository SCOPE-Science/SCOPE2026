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

# Reproducible checks and scientific limits
Run `python3 verify.py` with Python 3 and only its standard library. The verifier recomputes all radius-one four-coordinate output balls by the five allowed swap-site patterns, enumerates all 43,023 potentially superoptimal fixed-composition subsets, checks the five explicit optimal local codes, and verifies explicit entire-alphabet constructions for sizes 2 through 6. Expected output: `VERIFY_OK; 43023 forbidden subsets; q=2..6 complete constructions`.

The all-alphabet theorem is proved mathematically in RESULT.md via the five canonical multiplicity classes and their count. The finite tests do not establish the theorem by themselves. No independent scientific audit has been performed; prior binary exact code size is credited.
